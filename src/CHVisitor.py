# src/CHVisitor.py
import os
from CompileContext import CompileContext

from parser.CHParser import CHParser
from parser.CHParserVisitor import CHParserVisitor as BaseCHVisitor
from antlr4.tree.Tree import TerminalNodeImpl  # 导入 TerminalNodeImpl

INDENT = "    "


class CHVisitor(BaseCHVisitor):

    def __init__(self, context: CompileContext = None, import_loader_callback=None):
        super().__init__()

        # 上下文与回调 (用于智能导入)
        self.context = context if context else CompileContext()
        self.import_loader_callback = import_loader_callback

        # (我们回到了您最初的简单 Visitor)
        self._in_class_method = False
        self._in_class = False
        self._in_struct = False
        self._current_class_name = None
        self._class_sections = {"private": "", "public": "", "protected": ""}
        self._alias_to_namespace_map = {}
        self._scope_stack = [{}]
        self._namespace_is_open = False

        # 这个新状态用于跟踪我们是否在 'implement' 块中
        self._in_implementation_block = False
        self._current_namespace_str = ""  # 用于 C++ 作用域
        self._current_class_members = {}

        # [新增] 控制流深度 (0=线性/顶层, >0=条件或循环内)
        self._control_flow_depth = 0

        self._current_impl_methods = []  # [新增]用于存储当前 implement 块中的方法信息

        self._current_base_name = None  # [新增]

        # [新增] 记录继承关系: {"Dog": "Animal", "Cat": "Animal"}
        self._inheritance_map = {}

    def _collect_suffixes(self, ctx):
        """
        [辅助函数] 收集并按源代码顺序排序类型后缀 (* 和 &)。
        """
        suffixes = []
        if ctx.STAR():
            suffixes.extend(ctx.STAR())
        if ctx.BIT_AND():
            suffixes.extend(ctx.BIT_AND())

        # 按它们在源代码中出现的顺序排序
        suffixes.sort(key=lambda x: x.getSymbol().tokenIndex)
        return suffixes

    def visitTypeSpecifier(self, ctx: CHParser.TypeSpecifierContext):
        """
        [重构] 访问 'typeSpecifier' 规则。
        处理泛型 < >，C++函数类型 Ret(Args)，以及 C-Style 数组/指针转换。
        """
        core_type = ""
        is_function_type = False
        suffixes = self._collect_suffixes(ctx)

        # --- 路径 A: C-Style 数组 [type; size] ---
        if ctx.LBRACK() and ctx.SEMIC_TOKEN():
            # e.g. [i32; 3]
            base = self.visit(ctx.typeSpecifier())  # i32 -> "int32_t"
            size_expr = self.visit(ctx.expression())  # 3 -> "3"

            # [关键修复] 使用 {NAME} 占位符构建 C++ 数组声明语法
            if "{NAME}" in base:
                # 对于多维数组，C++ 的顺序是 arr[Rows][Cols]
                core_type = base.replace("{NAME}", f"{{NAME}}[{size_expr}]")
            else:
                # 基础情况: int32_t {NAME}[3]
                core_type = f"{base} {{NAME}}[{size_expr}]"

        # ... (路径 C/D 保持不变) ...
        elif ctx.LPAREN() and ctx.RPAREN() and not getattr(ctx, 'baseType', lambda: None)():
            if ctx.ARROW():
                is_function_type = True
                params_str = self.visit(ctx.params) if ctx.params else ""
                return_str = self.visit(ctx.returnType)
                core_type = f"std::function<{return_str}({params_str})>"
            elif ctx.nested:
                core_type = self.visit(ctx.nested)
                if core_type.startswith("std::function<"):
                    is_function_type = True
            else:
                core_type = ""

        # ... (路径 B 保持不变) ...
        elif ctx.baseType():
            base = self.visit(ctx.baseType())
            core_type = base
            if ctx.LT():
                generic_args = self.visit(ctx.typeList(0))
                core_type = f"{core_type}<{generic_args}>"
            if ctx.LPAREN():
                type_list_idx = 1 if ctx.LT() else 0
                func_args = ""
                if len(ctx.typeList()) > type_list_idx:
                    func_args = self.visit(ctx.typeList(type_list_idx))
                core_type = f"{core_type}({func_args})"
        else:
            return ""

        # --- 后缀处理 ---
        # 如果是函数指针模式
        if is_function_type and suffixes and suffixes[0].getText() == '*':
            inner_sig = core_type[14:-1]
            first_paren_index = inner_sig.find('(')
            if first_paren_index != -1:
                ret_type = inner_sig[:first_paren_index].strip()
                args_part = inner_sig[first_paren_index:]
                remaining_suffixes = suffixes[1:]
                remaining_suffix_str = "".join(s.getText() for s in remaining_suffixes)
                return f"{ret_type} (*{{NAME}}){args_part}{remaining_suffix_str}"
            pass

        # --- 普通类型后缀 ---
        suffix_str = "".join(s.getText() for s in suffixes)

        if "{NAME}" in core_type:
            return core_type

        return f"{core_type}{suffix_str}"

    def visitBaseType(self, ctx: CHParser.BaseTypeContext):
        raw_text = ctx.getText()

        # 2. 直接替换 :: (如果是新语法) 或者 . (如果是旧语法) 为 ::
        cpp_type = raw_text.replace('.', '::')

        # 处理别名 (例如 IO.cout -> IO::cout)
        parts = cpp_type.split('::')
        if parts[0] in self._alias_to_namespace_map:
            parts[0] = self._alias_to_namespace_map[parts[0]]

        final_type = "::".join(parts)
        return self._CH_to_cpp_type(final_type)

    def visitNamespaceStatement(self, ctx: CHParser.NamespaceStatementContext):
        self._namespace_is_open = True
        namespace_name = ctx.name.getText()

        cpp_namespace = namespace_name.replace('.', '::')
        self._current_namespace_str = cpp_namespace + "::"

        # 1:1 翻译
        open_block = f"namespace {namespace_name.replace('.', ' { namespace ')} {{\n\n"
        return open_block

    def visitEndNamespaceStatement(self, ctx: CHParser.EndNamespaceStatementContext):
        if not self._namespace_is_open:
            raise Exception(
                f"CH Translation Error (Line {ctx.start.line}): 'endnamespace;' called without a matching 'namespace' statement.")

        depth = self._current_namespace_str.count('::')
        closing_braces = "}" * depth
        comment_name = self._current_namespace_str.replace('::', '.')[:-1]

        self._namespace_is_open = False
        self._current_namespace_str = ""

        return f"\n{closing_braces} // namespace {comment_name}\n\n"

    def visitImplementationBlock(self, ctx: CHParser.ImplementationBlockContext):
        self._in_implementation_block = True
        self._current_class_name = ctx.name.text
        self._in_class = True

        # [新增] 清空方法列表
        self._current_impl_methods = []

        # [新增] 检查是否标记为 @dynamic
        is_dynamic = bool(ctx.AT_DYNAMIC())

        body_code = ""
        for child in ctx.children:
            if isinstance(child, (CHParser.MethodDefinitionContext,
                                  CHParser.InitDefinitionContext,
                                  CHParser.DeinitBlockContext)):
                body_code += self.visit(child)

        # [核心逻辑] 如果是动态类，自动生成反射胶水代码
        if is_dynamic:
            glue_code = self._generate_dynamic_glue_code()
            body_code += glue_code

        self._in_implementation_block = False
        self._current_class_name = None
        self._in_class = False
        self._current_impl_methods = []  # 清理

        return body_code

    def visitMethodDefinition(self, ctx: CHParser.MethodDefinitionContext):
        self._in_class_method = True
        self._enter_scope()
        self._add_variable("this", {"cpp_name": "this", "cpp_type": f"{self._current_class_name}*"})

        # [新增] 获取返回类型
        return_type = "void"
        if ctx.returnType:
            return_type = self.visit(ctx.returnType)  # e.g., "int32_t", "std::string"

        # [关键] 收集方法信息
        if self._in_implementation_block:
            func_name = ctx.name.text
            params = []
            if ctx.parameters():
                for p in ctx.parameters().parameter():
                    p_type = self.visit(p.typeName)
                    params.append(p_type)

            # [修改] 存入三元组: (函数名, 参数列表, 返回类型)
            self._current_impl_methods.append((func_name, params, return_type))

        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))

        # 注意：这里的 return_type 变量上面已经计算过了

        self._exit_scope()
        self._in_class_method = False

        if self._in_implementation_block:
            return f"\n{return_type} {self._current_class_name}::{func_name}({params_code}) {{\n{body_code}{INDENT}}}\n"
        else:
            # 内联
            access = getattr(ctx, '_CH_access', 'public')
            self._class_sections[
                access] += f"\n{INDENT}{return_type} {func_name}({params_code}) {{\n{body_code}{INDENT}}}\n"
            return ""

    def _generate_dynamic_glue_code(self):
        class_name = self._current_class_name
        code = f"\n// --- CH Runtime Glue Code for {class_name} ---\n"
        code += f"CHObject::MethodTrampoline {class_name}::findMethodImpl(SelectorID sel) {{\n"

        for func_name, param_types, ret_type in self._current_impl_methods:
            code += f"{INDENT}if (sel == _SEL(\"{func_name}\")) {{\n"
            code += f"{INDENT}{INDENT}return [this](void* inst, std::vector<std::any>& args) -> std::any {{\n"
            code += f"{INDENT}{INDENT}{INDENT}{class_name}* self = static_cast<{class_name}*>(inst);\n"

            # 检查参数数量 (可选，这里暂时注释掉以防变参数)
            # code += f"{INDENT}{INDENT}{INDENT}if (args.size() < {len(param_types)}) return {{}};\n"

            call_args = []
            for i, p_type in enumerate(param_types):
                call_args.append(f"std::any_cast<{p_type}>(args[{i}])")

            call_args_str = ", ".join(call_args)
            call_expr = f"self->{func_name}({call_args_str})"

            if ret_type == "void":
                code += f"{INDENT}{INDENT}{INDENT}{call_expr};\n"
                code += f"{INDENT}{INDENT}{INDENT}return {{}};\n"
            else:
                code += f"{INDENT}{INDENT}{INDENT}return {call_expr};\n"

            code += f"{INDENT}{INDENT}}};\n"
            code += f"{INDENT}}}\n"

        # [修复 2/2] 使用记录的基类，而不是硬编码 CHObject
        parent_class = self._inheritance_map.get(class_name, "CHObject")
        code += f"{INDENT}return {parent_class}::findMethodImpl(sel);\n"
        code += "}\n"
        return code

    def visitFunctionDefinition(self, ctx: CHParser.FunctionDefinitionContext):

        line_comment = f"\n// Line {ctx.start.line} (func {ctx.name.text})\n"
        # 这是一个全局函数 (不在类中或 implement 块中)
        self._enter_scope()

        func_name = ctx.name.text

        cpp_func_name = ""
        if func_name == "main":
            cpp_func_name = "main"  # 强制全局
        else:
            cpp_func_name = func_name

        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))
        return_type = self.visit(ctx.returnType) if ctx.returnType else "void"

        is_static = bool(ctx.STATIC())
        static_prefix = "static " if is_static else ""

        func_def_code = (
            f"{line_comment}"
            f"{static_prefix}{return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            f"{INDENT}// --- Function End ---\n"
            f"}}\n"
        )

        self._exit_scope()
        return func_def_code

    def visitParameter(self, ctx: CHParser.ParameterContext):
        """
        [重构] 访问 'parameter' 规则。
        [修复] 正确处理带 {NAME} 占位符的数组/函数指针类型。
        """

        var_name = ctx.name.text
        key = var_name
        cpp_name = var_name

        base_type_cpp = self.visit(ctx.typeName)

        # 注册变量
        self._add_variable(key, {
            "cpp_name": cpp_name,
            "cpp_type": base_type_cpp
        })

        # [关键修复] 检查类型字符串是否包含 {NAME} 占位符
        # 数组类型 (e.g. [i32; 3]) 会被翻译为 "int32_t {NAME}[3]"
        # 我们必须将 {NAME} 替换为实际的参数名 "arr"，生成 "int32_t arr[3]"
        if "{NAME}" in base_type_cpp:
            return base_type_cpp.replace("{NAME}", cpp_name)

        # 普通类型处理
        cpp_final_type = base_type_cpp

        # (旧逻辑兼容: 如果 base_type_cpp 包含 ';[' 则转为指针)
        is_pointer = base_type_cpp.endswith('*')
        is_reference = base_type_cpp.endswith('&')

        if not is_pointer and not is_reference and ';[' in base_type_cpp:
            parts = base_type_cpp.split(';')
            base_only = parts[0]
            cpp_final_type = f"{base_only}*"

        return f"{cpp_final_type} {cpp_name}"


    def visitFunctionCallExpression(self, ctx: CHParser.FunctionCallExpressionContext):
        name_token = ctx.funcName

        # @move 检查
        is_safe_move = (name_token.type == CHParser.AT_MOVE)
        is_unsafe_move = False
        if hasattr(CHParser, 'AT_UNSAFE_MOVE'):
            is_unsafe_move = (name_token.type == CHParser.AT_UNSAFE_MOVE)

        if is_safe_move or is_unsafe_move:
            var_name = ""
            if ctx.expressionList() and ctx.expressionList().expression():
                arg_node = ctx.expressionList().expression()[0]
                var_name = arg_node.getText()
            var_info = self._find_variable(var_name)
            if var_info:
                if var_info.get('state') == 'Moved':
                    raise Exception(f"\n[CH Borrow Error] Variable '{var_name}' ALREADY moved!")
                var_depth = var_info.get('def_depth', 0)
                current_depth = self._control_flow_depth
                if is_safe_move and (current_depth > var_depth):
                    raise Exception(f"\n[CH Safety Error] Cannot safely @move('{var_name}') inside loop.")
                var_info['state'] = 'Moved'
                return f"std::move({var_name})"

        # 普通函数调用
        raw_name = name_token.text

        # [新增] 类型映射，支持构造函数简写 (e.g. string() -> std::string())
        cpp_func_name = "std::move" if name_token.type == CHParser.AT_MOVE else self._CH_to_cpp_type(raw_name)

        args_list = []
        if ctx.expressionList():
            for arg_expr in ctx.expressionList().expression():
                args_list.append(self.visit(arg_expr))
        args_code = ", ".join(args_list)
        return f"{cpp_func_name}({args_code})"


    def _translate_variable_declaration(self, ctx):
        """
        [重构 - 完整版]
        处理变量声明，包含以下特性支持：
        1. Const/Var 区分。
        2. 自动类型推导 (auto)。
        3. 智能指针识别 (std::unique_ptr 等)。
        4. C-Style 数组声明 (int arr[3])，通过 {NAME} 占位符处理。
        5. C-Style 函数指针声明 (int (*p)(int))，通过 {NAME} 占位符处理。
        6. 强制未初始化的裸指针为 nullptr。
        """

        # --- 1. 确定 Const / Var ---
        is_const = bool(ctx.CONST())
        const_prefix = "const " if is_const else ""

        # --- 2. 确定名称 ---
        var_name = ctx.name.text
        key = var_name
        cpp_name = var_name  # 始终使用原始名称

        # --- 3. 确定类型 ---
        base_type_cpp = ""
        cpp_final_type = ""

        if ctx.typeName:
            base_type_cpp = self.visit(ctx.typeName)
            cpp_final_type = base_type_cpp
        else:
            if not ctx.expression():
                raise Exception(
                    f"CH Error (Line {ctx.start.line}): Declaration of '{var_name}' must have an explicit type or an initializer.")
            base_type_cpp = "auto"
            cpp_final_type = "auto"

        # --- 4. 验证 Const ---
        if is_const and not ctx.expression():
            raise Exception(
                f"CH Error (Line {ctx.start.line}): Constant declaration '{var_name}' must be initialized.")

        # --- 5. 确定是指针/引用/数组 ---
        is_pointer = False

        # 检查是否为 C-Style 函数指针 (特征：包含 (*{NAME}) )
        is_c_style_func_ptr = "(*{NAME})" in cpp_final_type

        if base_type_cpp != "auto":
            # 判断是否为指针类型
            if base_type_cpp.endswith('*') or \
                    base_type_cpp.startswith("std::unique_ptr") or \
                    base_type_cpp.startswith("std::shared_ptr") or \
                    base_type_cpp.startswith("std::weak_ptr") or \
                    is_c_style_func_ptr:
                is_pointer = True

        # [ auto 推导逻辑 ]
        if base_type_cpp == "auto" and ctx.expression():
            primary_node = None
            try:
                # 尝试获取表达式的第一个节点来推测是否是工厂调用
                primary_node = ctx.expression().unaryExpression(0).simpleExpression().children[0]
            except Exception as e:
                pass

            is_factory_call = False
            if primary_node and isinstance(primary_node, CHParser.PrimaryContext):
                if primary_node.NEW():
                    is_factory_call = True
                elif primary_node.AT_MAKE_UNIQUE():
                    is_factory_call = True
                elif primary_node.AT_MAKE_SHARED():
                    is_factory_call = True

            if is_factory_call:
                is_pointer = True

        # [清理] 移除了步骤 6 (确定访问器)

        # --- 7. 注册到作用域栈 ---
        # [清理] 不再存储 accessor
        self._add_variable(key, {
            "cpp_name": cpp_name,
            "cpp_type": base_type_cpp
        })

        # --- 8. 确定赋值 ---
        cpp_value = ""
        if ctx.expression():
            cpp_value = f" = {self.visit(ctx.expression())}"

        elif is_pointer and base_type_cpp != "auto":
            # [关键修复] 处理未初始化的指针
            is_smart_ptr = (base_type_cpp.startswith("std::unique_ptr") or
                            base_type_cpp.startswith("std::shared_ptr") or
                            base_type_cpp.startswith("std::weak_ptr"))

            if not is_smart_ptr:
                cpp_value = " = nullptr"

        # --- 9. 确定是局部还是成员 ---
        is_member_variable = (self._in_class or self._in_struct) and not self._in_class_method
        access = getattr(ctx, '_CH_access', 'private')

        # --- 10. 生成核心 C++ 代码 ---
        core_cpp = ""

        if "{NAME}" in cpp_final_type:
            # 这是一个带占位符的类型 (数组或函数指针)
            core_cpp = f"{const_prefix}{cpp_final_type.replace('{NAME}', cpp_name)}{cpp_value}"
        else:
            # 标准声明
            core_cpp = f"{const_prefix}{cpp_final_type} {cpp_name}{cpp_value}"

        # 返回元组
        return (core_cpp, is_member_variable, access, cpp_final_type, cpp_name)

    def _enter_scope(self):
        """进入一个新的作用域 (例如函数体或 if 块)"""
        self._scope_stack.append({})

    def _exit_scope(self):
        """退出当前作用域"""
        if len(self._scope_stack) > 1:
            self._scope_stack.pop()

    def _get_op_string_from_token_type(self, token_type):
        """根据 ANTLR 词元类型返回操作符的 C++ 字符串"""
        if token_type == CHParser.PLUS: return "+"
        if token_type == CHParser.MINUS: return "-"
        if token_type == CHParser.STAR: return "*"
        if token_type == CHParser.SLASH: return "/"
        if token_type == CHParser.MODULO: return "%"
        if token_type == CHParser.EQ: return "=="
        if token_type == CHParser.NEQ: return "!="
        if token_type == CHParser.LT: return "<"
        if token_type == CHParser.GT: return ">"
        if token_type == CHParser.LTE: return "<="
        if token_type == CHParser.GTE: return ">="
        if token_type == CHParser.AND_OP: return "&&"
        if token_type == CHParser.OR_OP: return "||"
        if token_type == CHParser.BIT_AND: return "&"
        if token_type == CHParser.BIT_OR: return "|"
        if token_type == CHParser.BIT_XOR: return "^"
        if token_type == CHParser.LSHIFT: return "<<"
        if token_type == CHParser.RSHIFT: return ">>"
        raise Exception(f"Unknown operator token type: {token_type}")

    def _add_variable(self, CH_name, metadata):
        """在*当前*作用域中定义一个新变量 (使用 CH 名字 $s 或 s 作为 Key)"""
        # [新增] 初始化借用状态元数据
        metadata['state'] = 'Alive'  # 状态: Alive / Moved
        metadata['def_depth'] = self._control_flow_depth  # 出生时的深度

        self._scope_stack[-1][CH_name] = metadata

    def _find_variable(self, CH_name):
        """从当前作用域开始，向外(全局)查找一个变量 (使用 CH 名字 $s 或 s)"""
        for scope in reversed(self._scope_stack):
            if CH_name in scope:
                return scope[CH_name]
        return None  # 未找到

    def _safe_iterate_statements(self, statement_ctx_or_list):
        """
        [全局辅助函数]
        安全地处理 ANTLR 返回的:
        1. None (0 语句)
        2. 单个 StatementContext/TopLevelStatement 对象 (1 语句)
        3. 列表 (0 或 2+ 语句)
        """
        if not statement_ctx_or_list:
            return []
        if isinstance(statement_ctx_or_list, list):
            return statement_ctx_or_list
        else:
            return [statement_ctx_or_list]

    def _CH_to_cpp_type(self, CH_type_name):
        """
        [重构] 新增智能指针关键字的翻译
        """
        if CH_type_name == "bool":
            return "bool"
        if CH_type_name == "unique":
            return "std::unique_ptr"
        if CH_type_name == "shared":
            return "std::shared_ptr"
        if CH_type_name == "weak":
            return "std::weak_ptr"
        if CH_type_name == "i8":
            return "int8_t"
        if CH_type_name == "u8":
            return "uint8_t"
        if CH_type_name == "i16":
            return "int16_t"
        if CH_type_name == "u16":
            return "uint16_t"
        if CH_type_name == "int":
            return "int"
        if CH_type_name == "i32":
            return "int32_t"
        if CH_type_name == "u32":
            return "uint32_t"
        if CH_type_name == "i64":
            return "int64_t"
        if CH_type_name == "u64":
            return "uint64_t"
        if CH_type_name == "f32" or CH_type_name == "float":
            return "float"
        if CH_type_name == "f64":
            return "double"
        # [新增] 动态类型映射
        if CH_type_name == "dyn":
            return "dyn"

        return CH_type_name

    def _get_access_level(self, ctx, default_level='private'):
        """检查上下文是否包含访问修饰符，返回 'public', 'protected' 或默认值。"""

        # 辅助函数：从具体的 AccessModifierContext 解析字符串
        def resolve_modifier(mod_ctx):
            if not mod_ctx: return None
            if mod_ctx.PROTECTED(): return "protected"
            if mod_ctx.PUBLIC(): return "public"
            return None

        # 1. 直接检查当前节点 (如 classBodyStatement)
        if hasattr(ctx, 'accessModifier') and ctx.accessModifier():
            return resolve_modifier(ctx.accessModifier())

        # 2. 检查嵌套声明 (如 variableDeclaration)
        # 有些规则可能是 declaration -> variableDeclaration -> accessModifier
        elif hasattr(ctx, 'variableDeclaration') and ctx.variableDeclaration():
            var_decl = ctx.variableDeclaration()
            if hasattr(var_decl, 'accessModifier') and var_decl.accessModifier():
                return resolve_modifier(var_decl.accessModifier())

        elif hasattr(ctx, 'methodDefinition') and hasattr(ctx.methodDefinition(), 'accessModifier'):
            # 注意：methodDefinition 在 .g4 中可能没有直接挂 accessModifier，通常由 classBodyStatement 处理
            # 如果您的语法树结构里 methodDefinition 自带修饰符，则取消注释
            pass

        return default_level

    # --- 顶层规则 ---
    def visitProgram(self, ctx: CHParser.ProgramContext):

        # [ [ [ 修复：恢复“优雅”的顺序循环 ] ] ]
        all_code = ""

        # 1. 按顺序访问所有子节点 (Imports, Namespace, Code, EndNamespace)
        for child in ctx.children:

            # A. 处理顶层的 # 指令 (来自 topLevelImport)
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == CHParser.CPP_DIRECTIVE:
                    all_code += self.visit(child)
                continue  # (忽略其他终端节点，如 EOF)

            # B. 访问所有其他规则 (Import, Namespace, Statement, EndNamespace)
            elif child:
                all_code += self.visit(child)

        # 2. [ [ [ 关键的强制检查 ] ] ]
        #    在文件末尾，检查 namespace 是否“被遗忘了”
        #    如果 'visitEndNamespaceStatement' 没被调用, self._namespace_is_open 将是 True
        if self._namespace_is_open:
            # 抛出一个硬错误，而不是自动闭合
            raise Exception(
                "CH Translation Error: 'namespace' was declared, but 'endnamespace;' was missing before the end of the file.")

        return all_code.strip()

    def visitImportDirective(self, ctx: CHParser.ImportDirectiveContext):

        line_comment = f"\n// Line {ctx.start.line} \n"

        # --- [关键修复] 路径重建逻辑 ---
        path_text = ""
        is_system_header = False

        if ctx.pathStr:
            # 情况 A: import "foo.ch"
            path_text = ctx.pathStr.text
        else:
            # 情况 B: import <vector> 或 import <sys/stat.h>
            raw_seq = ctx.pathSeq.getText()  # getText() 会自动拼接子节点文本
            path_text = f"<{raw_seq}>"
            is_system_header = True

        # --- 智能导入逻辑 ---
        # 如果是用户导入 ("...")，尝试加载它以获取 typemaps
        if not is_system_header and self.import_loader_callback:
            raw_path = path_text[1:-1]  # 去除引号
            # 触发回调，扫描目标文件
            self.import_loader_callback(raw_path)
        # --------------------

        base_name = os.path.basename(path_text.strip('\\\"<>'))
        true_namespace, _ = os.path.splitext(base_name)

        if ctx.alias:
            alias_name = ctx.alias.text
        else:
            alias_name = true_namespace
        if alias_name and true_namespace:
            self._alias_to_namespace_map[alias_name] = true_namespace

        if is_system_header:
            return f"#include {path_text}\n"
        else:
            # 用户头文件
            path_content = path_text[1:-1]  # 去引号

            # 1. 处理 runtime 路径修正 (保留现有逻辑)
            if path_content.startswith('runtime/'):
                path_content = path_content.replace('runtime/', '')

            # 2. [ [ [ 修复 ] ] ] 自动追加 .h 后缀
            root, ext = os.path.splitext(path_content)
            if not ext:
                path_content += ".h"

            return f'{line_comment}#include "{path_content}"\n'

        return f"// ERROR: Invalid import path {path_text}\n"

    def visitUsingAlias(self, ctx: CHParser.UsingAliasContext):
        line_comment = f"\n// Line {ctx.start.line} \n"
        name = ctx.name.text
        cpp_type_pattern = self.visit(ctx.typeName)

        cpp_type = ""
        # [关键修改]
        if "{NAME}" in cpp_type_pattern:
            # C-Style 函数指针: int (*{NAME})(int) -> int (*)(int)
            # C-Style 数组: int32_t {NAME}[3] -> int32_t[3] (在 using 中合法)
            if "(*{NAME})" in cpp_type_pattern:
                cpp_type = cpp_type_pattern.replace("(*{NAME})", "(*)")
            else:
                # 数组情况：直接去掉 {NAME}
                cpp_type = cpp_type_pattern.replace("{NAME}", "")
        else:
            cpp_type = cpp_type_pattern

        return f"{line_comment}using {name} = {cpp_type};\n"

    def visitParameters(self, ctx: CHParser.ParametersContext):
        """
        [恢复] 处理参数列表 (p1, p2, p3)
        防止无参数时返回 None
        """
        params_list = []
        for p in ctx.parameter():
            code = self.visit(p)
            params_list.append(code)
        return ", ".join(params_list)

    # [ [ [ 新增：访问基类初始化器 ] ] ]
    def visitBaseInitializer(self, ctx: CHParser.BaseInitializerContext):
        """
        访问 'baseInitializer' 规则 (例如 : Window(args) )
        并将其翻译为 C++ 字符串 "Window(args)"
        """
        base_name = ctx.name.text
        args_code = self.visit(ctx.args) if ctx.args else ""
        return f"{base_name}({args_code})"

    def visitMethodSignature(self, ctx: CHParser.MethodSignatureContext):
        func_name = ctx.name.text
        cpp_func_name = func_name
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        if ctx.returnType:
            cpp_return_type = self.visit(ctx.returnType)
        else:
            cpp_return_type = "void"
        return f"{INDENT}virtual {cpp_return_type} {cpp_func_name}({params_code}) = 0;\n"

    def visitInterfaceDefinition(self, ctx: CHParser.InterfaceDefinitionContext):
        interface_name = ctx.name.text
        body_code = ""

        # 遍历子节点
        for child in ctx.children:
            if isinstance(child, CHParser.MethodSignatureContext):
                # [核心逻辑] 检查是否有 @optional
                is_optional = bool(child.AT_OPTIONAL())

                if is_optional:
                    # 如果是可选的，生成注释，或者完全不生成 C++ 代码
                    # 这样 C++ 编译器就不会因为没实现它而报错
                    func_name = child.name.text
                    body_code += f"{INDENT}// virtual void {func_name}(...) // @optional in CH\n"
                else:
                    # 必须实现的，生成纯虚函数
                    body_code += self.visit(child)

        code = f"\nclass {interface_name} {{\n"
        code += "public:\n"
        code += f"{INDENT}virtual ~{interface_name}() {{}} \n"
        code += body_code
        code += "};\n"
        return code

    def visitFunctionSignature(self, ctx: CHParser.FunctionSignatureContext):
        line_comment = f"\n// Line {ctx.start.line} \n"

        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        return_type = self.visit(ctx.returnType) if ctx.returnType else "void"

        if self._in_class or self._in_struct:
            default_access = 'public' if self._in_struct else 'private'
            access = getattr(ctx, '_CH_access', default_access)

            # 1. 获取修饰符状态
            # (STATIC)? 来自 Parser
            is_static = bool(ctx.STATIC())
            # (VIRTUAL)? 来自 Parser [新增]
            is_virtual = bool(ctx.VIRTUAL()) if hasattr(ctx, 'VIRTUAL') and ctx.VIRTUAL() else False
            # (OVERRIDE)? 来自 Parser [新增]
            is_override = bool(ctx.OVERRIDE()) if hasattr(ctx, 'OVERRIDE') and ctx.OVERRIDE() else False

            # 如果是从 classBodyStatement 传下来的 static 标志 (兼容旧逻辑)
            if getattr(ctx, '_CH_static', False):
                is_static = True

            # 2. 构建前缀/后缀
            static_prefix = "static " if is_static else ""

            # [核心修改] 不再自动 virtual，必须显式指定
            virtual_prefix = "virtual " if is_virtual else ""

            override_suffix = " override" if is_override else ""

            # 3. 互斥检查 (C++ 不允许 static virtual)
            if is_static and (is_virtual or is_override):
                raise Exception(
                    f"Error (Line {ctx.start.line}): Function '{func_name}' cannot be both static and virtual/override.")

            decl = f"{line_comment}{INDENT}{virtual_prefix}{static_prefix}{return_type} {func_name}({params_code}){override_suffix};\n"
            self._class_sections[access] += decl
            return ""
        else:
            # 全局函数... (保持不变)
            is_extern = bool(ctx.EXTERN())
            is_static = bool(ctx.STATIC())
            static_prefix = "static " if is_static else ""
            extern_prefix = "extern " if is_extern else ""
            return f"{line_comment}{extern_prefix}{static_prefix}{return_type} {self._current_namespace_str}{func_name}({params_code});\n"

    def visitInitSignature(self, ctx: CHParser.InitSignatureContext):
        line_comment = f"\n// Line {ctx.start.line} \n"
        default_access = 'public' if self._in_struct else 'private'
        access = getattr(ctx, '_CH_access', default_access)

        func_name = self._current_class_name
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        decl = f"{line_comment}{INDENT}{func_name}({params_code});\n"
        self._class_sections[access] += decl
        return ""

    def visitDeinitSignature(self, ctx: CHParser.DeinitSignatureContext):
        line_comment = f"\n// Line {ctx.start.line} \n"

        access = "public"  # Deinit 总是 public
        func_name = f"~{self._current_class_name}"

        decl = f"{line_comment}{INDENT}virtual {func_name}();\n"
        self._class_sections[access] += decl
        return ""

    def visitCastExpression(self, ctx: CHParser.CastExpressionContext):
        # 1. 获取左侧表达式 (simpleExpression)
        code = self.visit(ctx.simpleExpression())

        # 2. 如果没有 AS 关键字，直接返回左侧代码 (透传)
        if not ctx.AS():
            return code

        # 3. 处理 AS 转换
        # 遍历所有的 typeSpecifier (处理 obj as A as B 的情况)
        for type_ctx in ctx.typeSpecifier():
            target_type = self.visit(type_ctx)

            # [智能修正]
            # 如果用户写 "as Button"，生成 "dynamic_cast<Button*>"
            # 如果用户写 "as Button*"，生成 "dynamic_cast<Button*>"
            # 我们默认 CH 的类转换都是指针转换
            if not target_type.endswith('*'):
                target_type += "*"

            # 生成 C++ dynamic_cast
            code = f"dynamic_cast<{target_type}>({code})"

        return code


    def visitClassDefinition(self, ctx: CHParser.ClassDefinitionContext):
        self._current_class_members = {}
        self._in_class = True
        self._in_struct = False
        class_name = ctx.name.text

        # [修复 1/2] 记录继承关系
        base_name = "CHObject"
        if ctx.base:
            base_name = ctx.base.text
        self._inheritance_map[class_name] = base_name

        inheritance_list = []
        if ctx.base: inheritance_list.append(f"public {ctx.base.text}")
        if ctx.interfaces:
            for name in self.visit(ctx.interfaces).split(','):
                inheritance_list.append(f"public {name.strip()}")
        inheritance_str = (" : " + ", ".join(inheritance_list)) if inheritance_list else ""

        self._current_class_name = class_name
        self._class_sections = {"private": "", "public": "", "protected": ""}
        is_dynamic = bool(ctx.AT_DYNAMIC())

        if hasattr(ctx, 'classBodyStatement'):
            for child in ctx.classBodyStatement():
                self.visit(child)

        if is_dynamic:
            self._class_sections[
                "public"] += f"{INDENT}virtual MethodTrampoline findMethodImpl(SelectorID sel) override;\n"

        final_body = ""
        # [修改] 按 C++ 习惯顺序组装: public -> protected -> private
        if self._class_sections["public"]:
            final_body += f"\npublic:\n{self._class_sections['public']}"

        # [新增] 插入 protected 块
        if self._class_sections["protected"]:
            final_body += f"\nprotected:\n{self._class_sections['protected']}"

        if self._class_sections["private"]:
            final_body += f"\nprivate:\n{self._class_sections['private']}"

        self._in_class = False
        self._current_class_name = None
        return f"\nclass {class_name}{inheritance_str} {{\n{final_body.strip()}\n}};\n"



    def visitClassBodyStatement(self, ctx: CHParser.ClassBodyStatementContext):
        # [ [ [ 关键修复 ] ] ]
        # 修复了 static 关键字的检测。
        is_static = False
        if ctx.functionSignature():
            # 检查 classBodyStatement 级别的 (STATIC)?
            is_static = bool(ctx.STATIC())
            if not is_static:
                # 检查 functionSignature 级别的 (STATIC)?
                is_static = bool(ctx.functionSignature().STATIC())
        else:
            # (处理 static var, G4 当前不支持, 但保持逻辑完整)
            is_static = bool(ctx.STATIC())

        access = self._get_access_level(ctx, default_level='private')

        if ctx.variableDeclaration():
            ctx.variableDeclaration()._CH_access = access
            # 传递 static 状态 (尽管 G4 不支持 static var)
            ctx.variableDeclaration()._CH_static = is_static
            return self.visit(ctx.variableDeclaration())

            # [新增] 处理嵌套枚举
        elif ctx.enumDefinition():
            enum_code = self.visit(ctx.enumDefinition())
            # 枚举定义直接放入对应的访问区段
            self._class_sections[access] += enum_code
            return ""

        elif ctx.functionSignature():
            ctx.functionSignature()._CH_access = access
            ctx.functionSignature()._CH_static = is_static  # <--- 传递合并后的 'is_static' 状态
            return self.visit(ctx.functionSignature())

        elif ctx.initSignature():
            ctx.initSignature()._CH_access = access
            return self.visit(ctx.initSignature())

        elif ctx.deinitSignature():
            # deinit 总是 public
            ctx.deinitSignature()._CH_access = 'public'
            return self.visit(ctx.deinitSignature())


        elif ctx.cppBlock():
            return self.visit(ctx.cppBlock())

        return ""

    def visitInitDefinition(self, ctx: CHParser.InitDefinitionContext):

        line_comment = f"\n// Line {ctx.start.line} (init)\n"
        self._in_class_method = True
        self._enter_scope()

        # [ [ [ 修复 B-2: 加载 'this' 和所有成员到作用域 ] ] ]
        # [清理] 移除 accessor 相关逻辑
        cpp_type = f"{self._current_class_name}*"
        self._add_variable("this", {
            "cpp_name": "this",
            "cpp_type": cpp_type
        })
        for member_name, metadata in self._current_class_members.items():
            self._add_variable(member_name, metadata)
        # [ [ [ 修复结束 ] ] ]

        cpp_func_name = self._current_class_name

        # [ [ [ 新增：处理基类初始化 ] ] ]
        base_init_code = ""
        if ctx.baseInit:
            # ctx.baseInit 是 BaseInitializerContext
            # visit(ctx.baseInit) 将返回 "Window(L\"My CH GDI+ Window\", app)"
            base_init_code = f" : {self.visit(ctx.baseInit)}"
        # [ [ [ 新增结束 ] ] ]

        # [ [ [ 检查 'implement' 块 ] ] ]
        if self._in_implementation_block:
            # [修复 A-4]
            cpp_func_name = f"{self._current_class_name}::{self._current_class_name}"
        else:
            access = getattr(ctx, '_CH_access', 'private')
            if self._in_struct:
                access = getattr(ctx, '_CH_access', 'public')

        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))

        init_code = (
            f"{line_comment}\n{INDENT if not self._in_implementation_block else ''}"
            # [ [ [ 修改：插入 base_init_code ] ] ]
            f"{cpp_func_name}({params_code}){base_init_code} {{\n"
            f"{body_code}"
            f"{INDENT if not self._in_implementation_block else ''}}}\n"
        )

        if not self._in_implementation_block:
            self._class_sections[access] += init_code

        self._exit_scope()
        self._in_class_method = False

        return init_code if self._in_implementation_block else ""

    def visitDeinitBlock(self, ctx: CHParser.DeinitBlockContext):

        line_comment = f"\n// Line {ctx.start.line} (deinit)\n"

        self._in_class_method = True
        self._enter_scope()

        # [ [ [ 修复 B-2: 加载 'this' 和所有成员到作用域 ] ] ]
        # [清理] 移除 accessor 相关逻辑
        cpp_type = f"{self._current_class_name}*"

        self._add_variable("this", {
            "cpp_name": "this",
            "cpp_type": cpp_type
        })

        # 2. 将所有类/struct成员 (例如 's') 加载到当前作用域
        for member_name, metadata in self._current_class_members.items():
            self._add_variable(member_name, metadata)

        # [ [ [ 修复结束 ] ] ]

        cpp_func_name = f"~{self._current_class_name}"
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))

        # [ [ [ 检查 'implement' 块 ] ] ]
        if self._in_implementation_block:
            # [ [ [ 修复 A-5: 移除 'implement' 块中的命名空间前缀 ] ] ]
            cpp_func_name = f"{self._current_class_name}::{cpp_func_name}"
            deinit_code = (
                f"{line_comment}\n{cpp_func_name}() {{\n"
                f"{INDENT}// --- CH Deinit Block ---\n"
                f"{body_code}"
                f"{INDENT}// --- Deinit End ---\n"
                f"{INDENT}}}\n"
            )
        else:
            access = "public"  # Deinit 总是 public
            deinit_code = (
                f"{line_comment}\n{INDENT}virtual {cpp_func_name}() {{\n"
                f"{INDENT}// --- CH Deinit Block ---\n"
                f"{body_code}"
                f"{INDENT}// --- Deinit End ---\n"
                f"{INDENT}}}\n"
            )
            self._class_sections[access] += deinit_code

        self._exit_scope()
        self._in_class_method = False

        return deinit_code if self._in_implementation_block else ""

    def visitTypeList(self, ctx: CHParser.TypeListContext):
        arg_list = [self.visit(t) for t in ctx.templateArgument()]
        return ", ".join(arg_list)

    def visitTemplateArgument(self, ctx: CHParser.TemplateArgumentContext):
        if ctx.typeSpecifier():
            return self.visit(ctx.typeSpecifier())
        if ctx.literal():
            return self.visit(ctx.literal())
        return ""

    def visitInitializerList(self, ctx: CHParser.InitializerListContext):
        args_code = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
        return f"{{{args_code}}}"

    def visitSimpleExpression(self, ctx: CHParser.SimpleExpressionContext):
        """
        [重构] 支持 . / -> / :: / [] / ~>
        """
        # 1. Primary
        current_code = ""
        if ctx.primary():
            current_code = self.visit(ctx.primary())
        elif ctx.functionCallExpression():
            current_code = self.visit(ctx.functionCallExpression())
        else:
            return ""

        # 2. Suffixes
        child_nodes = ctx.children
        i = 1
        while i < len(child_nodes):
            node = child_nodes[i]
            token_type = node.getSymbol().type

            # A. 访问符 (., ->, ::)
            if token_type in [CHParser.DOT, CHParser.ARROW, CHParser.COLON_COLON]:
                op = node.getText()  # ., ->, ::
                i += 1
                ident = child_nodes[i].getText()

                # 变量名映射
                var_info = self._find_variable(ident)
                if var_info:
                    ident = var_info["cpp_name"]
                else:
                    ident = self._CH_to_cpp_type(ident)  # 类型映射 (支持 string::npos)

                current_code += f"{op}{ident}"
                i += 1

                # Template <T>
                if i < len(child_nodes) and child_nodes[i].getSymbol().type == CHParser.LT:
                    i += 1  # <
                    if i < len(child_nodes) and isinstance(child_nodes[i], CHParser.TypeListContext):
                        current_code += f"<{self.visit(child_nodes[i])}>"
                        i += 1
                    i += 1  # >

                # Call (...)
                if i < len(child_nodes) and child_nodes[i].getSymbol().type == CHParser.LPAREN:
                    i += 1  # (
                    args = ""
                    if i < len(child_nodes) and isinstance(child_nodes[i], CHParser.ExpressionListContext):
                        args = self.visit(child_nodes[i])
                        i += 1
                    i += 1  # )
                    current_code += f"({args})"

            # B. 数组索引 [ ]
            elif token_type == CHParser.LBRACK:
                i += 1
                idx = self.visit(child_nodes[i])
                i += 2
                current_code += f"[{idx}]"

            # C. [新增] 动态调用 ~>
            elif token_type == CHParser.TILDE_ARROW:
                i += 1  # skip ~>

                method_name = child_nodes[i].getText()
                i += 1

                args_code = ""
                if i < len(child_nodes) and child_nodes[i].getSymbol().type == CHParser.LPAREN:
                    i += 1  # (
                    if i < len(child_nodes) and isinstance(child_nodes[i], CHParser.ExpressionListContext):
                        # 特殊处理：参数装箱
                        boxed_args = []
                        for expr in child_nodes[i].expression():
                            val = self.visit(expr)
                            # 字符串字面量处理: "abc" -> std::string("abc")
                            # 否则 std::any 会存 const char*，导致解包 std::string 失败
                            if val.startswith('"') and val.endswith('"'):
                                val = f"std::string({val})"
                            boxed_args.append(val)
                        args_code = ", ".join(boxed_args)
                        i += 1
                    i += 1  # )

                # 生成 msgSend 代码
                current_code = f"{current_code}->msgSend(_SEL(\"{method_name}\"), {{ {args_code} }})"

            else:
                i += 1

        return current_code

    def visitPrimary(self, ctx: CHParser.PrimaryContext):
        if ctx.NEW():
            type_name = self.visit(ctx.baseType())
            args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
            return f"new {type_name}({args})"

        # @make 等处理
        if ctx.LT():
            cpp_func_name = ""
            if ctx.AT_MAKE_UNIQUE():
                cpp_func_name = "std::make_unique"
            elif ctx.AT_MAKE_SHARED():
                cpp_func_name = "std::make_shared"
            elif ctx.STATIC_CAST():
                cpp_func_name = "static_cast"
            elif ctx.REINTERPRET_CAST():
                cpp_func_name = "reinterpret_cast"
            elif ctx.CONST_CAST():
                cpp_func_name = "const_cast"

            target_type = self.visit(ctx.typeSpecifier())
            args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
            return f"{cpp_func_name}<{target_type}>({args})"

        if ctx.literal(): return self.visit(ctx.literal())
        if ctx.initializerList(): return self.visit(ctx.initializerList())

        if ctx.IDENTIFIER():
            text = ctx.IDENTIFIER().getText()
            var = self._find_variable(text)
            if var:
                if var.get('state') == 'Moved':
                    raise Exception(f"Use of moved variable '{text}'.")
                if '[' in var["cpp_type"]: return text
                return var["cpp_name"]

            if text in self._alias_to_namespace_map:
                return self._alias_to_namespace_map[text]

            # [新增] 类型映射 (e.g. string::npos -> std::string::npos)
            mapped = self._CH_to_cpp_type(text)
            return mapped

        if ctx.THIS(): return "this"
        if ctx.LPAREN(): return f"({self.visit(ctx.expression())})"
        return ""
    def visitStatement(self, ctx: CHParser.StatementContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        if ctx.cppBlock():
            return self.visit(ctx.cppBlock())
        if ctx.expression():
            line_comment = f"{INDENT}// Line {ctx.start.line}\n"  # <-- [新增]
            expr_code = self.visit(ctx.expression())
            return f"{line_comment}{INDENT}{expr_code};\n"
        if ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        if ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        if ctx.deleteStatement():
            return self.visit(ctx.deleteStatement())
        if ctx.forStatement():
            return self.visit(ctx.forStatement())
        if ctx.switchStatement():
            return self.visit(ctx.switchStatement())
        if ctx.blockStatement():
            return self.visit(ctx.blockStatement())
        return ""

    def visitReturnStatement(self, ctx: CHParser.ReturnStatementContext):
        line_comment = f"{INDENT}// Line {ctx.start.line}\n"
        if ctx.expression():  # [修复] return 可以是空的
            return_value = self.visit(ctx.expression())
            return f"{line_comment}{INDENT}return {return_value};\n"
        return f"{line_comment}{INDENT}return;\n"  # 空 return

    def visitCppBlock(self, ctx: CHParser.CppBlockContext):
        token_list = ctx.CPP_BODY()
        if token_list is None: token_list = []
        raw_cpp = "".join(token.getText() for token in token_list)
        return (
            f"\n{INDENT}// --- @cpp Block Start ---\n"
            f"{raw_cpp.strip()}\n"
            f"{INDENT}// --- @cpp Block End ---\n\n"
        )

    def visitAssignment(self, ctx: CHParser.AssignmentContext):
        line_comment = f"{INDENT}// Line {ctx.start.line}\n"

        # [修改] 移除了“复活逻辑”
        # 我们不再检查是否是纯赋值，也不再将状态重置为 'Alive'。

        # 直接生成目标代码。
        # 关键点：self.visit(ctx.assignableExpression()) 会调用 visitAssignablePrimary。
        # 如果该变量的状态是 'Moved'，visitAssignablePrimary 会直接抛出 Safety Error。
        # 这意味着：禁止对已移动的变量进行任何操作（包括赋值）。
        target = self.visit(ctx.assignableExpression())

        value = self.visit(ctx.expression())
        op_str = self.visit(ctx.assignmentOperator())
        return f"{line_comment}{INDENT}{target} {op_str} {value};\n"

    def visitAssignableExpression(self, ctx: CHParser.AssignableExpressionContext):
        """
        [重构 - 纯净模式]
        赋值左值处理。完全遵照用户输入的访问符。
        """
        # 1. 处理头部
        current_code = self.visit(ctx.assignablePrimary())

        # 2. 遍历后缀链
        child_nodes = ctx.children
        i = 1
        while i < len(child_nodes):
            node = child_nodes[i]
            token_type = node.getSymbol().type

            # --- 情况 A: 访问符 ---
            if token_type in [CHParser.DOT, CHParser.ARROW, CHParser.COLON_COLON]:
                # 1. 映射
                op_str = ""
                if token_type == CHParser.DOT:
                    op_str = "."
                elif token_type == CHParser.ARROW:
                    op_str = "->"
                elif token_type == CHParser.COLON_COLON:
                    op_str = "::"

                # 2. 标识符
                i += 1
                ident_node = child_nodes[i]
                raw_ident = ident_node.getText()

                # 名字映射 (保留)
                var_info = self._find_variable(raw_ident)
                cpp_ident = var_info["cpp_name"] if var_info else raw_ident

                current_code = f"{current_code}{op_str}{cpp_ident}"
                i += 1

            # --- 情况 B: 数组索引 ---
            elif token_type == CHParser.LBRACK:
                i += 1  # [
                index_expr = self.visit(child_nodes[i])
                i += 1  # expr
                if i < len(child_nodes) and child_nodes[i].getSymbol().type == CHParser.RBRACK:
                    i += 1  # ]
                current_code = f"{current_code}[{index_expr}]"

            else:
                i += 1

        return current_code

    def visitForStatement(self, ctx: CHParser.ForStatementContext):
        self._enter_scope()
        init_code = self.visit(ctx.init) if ctx.init else ""

        # 进入循环体 (包含条件和增量部分) -> 深度 +1
        self._control_flow_depth += 1

        cond_code = self.visit(ctx.cond) if ctx.cond else ""
        incr_code = self.visit(ctx.incr) if ctx.incr else ""

        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        self._control_flow_depth -= 1
        self._exit_scope()

        code = f"{INDENT}for ({init_code}; {cond_code}; {incr_code}) {{\n"
        code += body_code
        code += f"{INDENT}}}\n"
        return code

    def visitForInit(self, ctx: CHParser.ForInitContext):
        if ctx.variableDeclaration_no_semicolon():
            return self.visit(ctx.variableDeclaration_no_semicolon())
        if ctx.assignment_no_semicolon():
            return self.visit(ctx.assignment_no_semicolon())
        return ""

    def visitForIncrement(self, ctx: CHParser.ForIncrementContext):
        if ctx.assignment_no_semicolon():
            return self.visit(ctx.assignment_no_semicolon())
        if ctx.expression():
            return self.visit(ctx.expression())
        return ""

    def _recursive_analyze(self, node, indent_level=0):
        indent = "  " * indent_level
        node_type = type(node).__name__
        node_text_repr = repr(node.getText())
        print(f"{indent}Type: {node_type.ljust(30)} | Text: {node_text_repr}")
        if hasattr(node, 'children') and node.children:
            indent_level += 1
            for child in node.children:
                self._recursive_analyze(child, indent_level)

    def _process_block_children(self, children):
        body_code = ""
        for child in children:
            if isinstance(child, CHParser.StatementContext):
                body_code += self.visit(child)
        return body_code

    def visitAssignmentOperator(self, ctx: CHParser.AssignmentOperatorContext):
        if ctx.ASSIGN(): return "="
        if ctx.PLUS_ASSIGN(): return "+="
        if ctx.MINUS_ASSIGN(): return "-="
        if ctx.STAR_ASSIGN(): return "*="
        if ctx.SLASH_ASSIGN(): return "/="
        if ctx.MOD_ASSIGN(): return "%="
        return "="

    def visitIfStatement(self, ctx: CHParser.IfStatementContext):
        condition = self.visit(ctx.expression())

        # 进入 IF 块 -> 深度 +1
        self._control_flow_depth += 1
        if_body = self.visit(ctx.if_block) if ctx.if_block else ""
        self._control_flow_depth -= 1

        code = f"{INDENT}if ({condition}) {{\n{if_body}{INDENT}}}\n"

        if ctx.ELSE():
            if ctx.else_if:
                code += f"{INDENT}else {self.visit(ctx.else_if)}"
            elif ctx.else_block:
                # 进入 ELSE 块 -> 深度 +1
                self._control_flow_depth += 1
                else_body = self.visit(ctx.else_block)
                self._control_flow_depth -= 1

                code += f"{INDENT}else {{\n{else_body}{INDENT}}}\n"
        return code

    def visitIfBlock(self, ctx: CHParser.IfBlockContext):
        self._enter_scope()
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        return body_code

    def visitElseBlock(self, ctx: CHParser.ElseBlockContext):
        self._enter_scope()
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        return body_code

    def visitWhileStatement(self, ctx: CHParser.WhileStatementContext):
        # While 也算控制流
        self._control_flow_depth += 1
        condition = self.visit(ctx.expression())

        self._enter_scope()
        body_statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in body_statements)
        self._exit_scope()

        self._control_flow_depth -= 1

        code = f"{INDENT}while ({condition}) {{\n"
        code += body_code
        code += f"{INDENT}}}\n"
        return code

    def visitExpression(self, ctx: CHParser.ExpressionContext):
        operand_nodes = ctx.unaryExpression()
        current_code = self.visit(operand_nodes[0])

        if len(operand_nodes) == 1:
            return current_code
        all_ops = []
        if ctx.PLUS(): all_ops.extend(ctx.PLUS())
        if ctx.MINUS(): all_ops.extend(ctx.MINUS())
        if ctx.STAR(): all_ops.extend(ctx.STAR())
        if ctx.SLASH(): all_ops.extend(ctx.SLASH())
        if ctx.MODULO(): all_ops.extend(ctx.MODULO())
        if ctx.EQ(): all_ops.extend(ctx.EQ())
        if ctx.NEQ(): all_ops.extend(ctx.NEQ())
        if ctx.LT(): all_ops.extend(ctx.LT())
        if ctx.GT(): all_ops.extend(ctx.GT())
        if ctx.LTE(): all_ops.extend(ctx.LTE())
        if ctx.GTE(): all_ops.extend(ctx.GTE())
        if ctx.AND_OP(): all_ops.extend(ctx.AND_OP())
        if ctx.OR_OP(): all_ops.extend(ctx.OR_OP())
        if ctx.BIT_AND(): all_ops.extend(ctx.BIT_AND())
        if ctx.BIT_OR(): all_ops.extend(ctx.BIT_OR())
        if ctx.BIT_XOR(): all_ops.extend(ctx.BIT_XOR())
        if ctx.LSHIFT(): all_ops.extend(ctx.LSHIFT())
        if ctx.RSHIFT(): all_ops.extend(ctx.RSHIFT())
        all_ops.sort(key=lambda x: x.getSymbol().tokenIndex)
        for i in range(len(all_ops)):
            op_node = all_ops[i]
            op_str = self._get_op_string_from_token_type(op_node.getSymbol().type)
            rhs_code = self.visit(operand_nodes[i + 1])
            current_code = f"{current_code} {op_str} {rhs_code}"
        # print(current_code)
        return current_code

    def visitUnaryExpression(self, ctx: CHParser.UnaryExpressionContext):
        if ctx.castExpression():
            return self.visit(ctx.castExpression())
        op = ""
        if ctx.BIT_AND():
            op = "&"
        elif ctx.STAR():
            op = "*"
        elif ctx.MINUS():
            op = "-"
        elif ctx.PLUS():
            op = "+"
        elif ctx.NOT_OP():
            op = "!"
        elif ctx.BIT_NOT():
            op = "~"
        operand = self.visit(ctx.unaryExpression())
        if op == "*" or op == "&":
            return f"{op}{operand}"
        else:
            return f"{op}{operand}"

    def visitDeleteStatement(self, ctx: CHParser.DeleteStatementContext):
        target = self.visit(ctx.expression())
        return f"{INDENT}delete {target};\n"

    def visitAssignablePrimary(self, ctx: CHParser.AssignablePrimaryContext):
        if ctx.IDENTIFIER():
            primary_text = ctx.IDENTIFIER().getText()
            variable_info = self._find_variable(primary_text)

            if variable_info:
                # [新增] 检查是否访问了“尸体” (左值访问)
                # 即使是赋值操作 (a->id = 200)，如果 a 已经 Moved，也是非法的！
                if variable_info.get('state') == 'Moved':
                    raise Exception(
                        f"\n[CH Safety Error] Line {ctx.start.line}: Use of moved variable '{primary_text}'.\n"
                        f"Hint: Ownership was transferred via @move/@unsafe_move. This variable is now invalid (null).\n"

                    )

                if '[' in variable_info["cpp_type"]:
                    return primary_text
                else:
                    return variable_info["cpp_name"]  # [修复] 移除了 '_'
            else:
                return self._CH_to_cpp_type(primary_text)

        if ctx.THIS():
            return "this"
        if ctx.STAR():
            return f"(*{self.visit(ctx.assignablePrimary())})"
        if ctx.BIT_AND():
            return f"(&{self.visit(ctx.assignablePrimary())})"
        if ctx.LPAREN():
            return f"({self.visit(ctx.assignableExpression())})"
        return ""

    def visitExpressionList(self, ctx: CHParser.ExpressionListContext):
        return ", ".join(self.visit(e) for e in ctx.expression())

    def visitLiteral(self, ctx: CHParser.LiteralContext):
        if ctx.BOOL_LITERAL():
            return ctx.BOOL_LITERAL().getText()
        if ctx.CHAR_LITERAL():
            return ctx.CHAR_LITERAL().getText()
        if ctx.BYTE_LITERAL():
            raw_text = ctx.BYTE_LITERAL().getText()
            char_part = raw_text[1:]
            return f"(uint8_t){char_part}"
        if ctx.OCTAL_LITERAL():
            raw_text = ctx.OCTAL_LITERAL().getText()
            return f"0{raw_text[2:]}"

        # [ [ [ 新增：处理所有 C++ 前缀字符串 ] ] ]
        if ctx.U8_STRING_LITERAL():
            return ctx.U8_STRING_LITERAL().getText()
        if ctx.U_STRING_LITERAL():
            return ctx.U_STRING_LITERAL().getText()
        if ctx.U_STRING_LITERAL_CAP():
            return ctx.U_STRING_LITERAL_CAP().getText()
        if ctx.L_STRING_LITERAL_CAP():
            return ctx.L_STRING_LITERAL_CAP().getText()
        # [ [ [ 新增结束 ] ] ]

        if ctx.FLOAT_LITERAL():
            return ctx.FLOAT_LITERAL().getText()
        return ctx.getText()

    def visitAssignment_no_semicolon(self, ctx: CHParser.Assignment_no_semicolonContext):
        target = self.visit(ctx.assignableExpression())
        value = self.visit(ctx.expression())
        op_str = self.visit(ctx.assignmentOperator())
        return f"{target} {op_str} {value}"

    def visitStructBodyStatement(self, ctx: CHParser.StructBodyStatementContext):
        # struct 成员默认是 public
        access = self._get_access_level(ctx, default_level='public')

        if ctx.variableDeclaration():
            ctx.variableDeclaration()._CH_access = access
            # (Structs 在 C++ 中通常不支持 static 成员变量)
            ctx.variableDeclaration()._CH_static = False
            return self.visit(ctx.variableDeclaration())


        # 不再查找 ...Definition，而是查找 ...Signature
        elif ctx.functionSignature():
            ctx.functionSignature()._CH_access = access
            # [修复] 允许 struct 拥有静态方法
            is_static = bool(ctx.functionSignature().STATIC())
            ctx.functionSignature()._CH_static = is_static
            return self.visit(ctx.functionSignature())

        elif ctx.initSignature():
            ctx.initSignature()._CH_access = access
            return self.visit(ctx.initSignature())

        elif ctx.deinitSignature():
            ctx.deinitSignature()._CH_access = 'public'
            return self.visit(ctx.deinitSignature())

        elif ctx.cppBlock():
            return self.visit(ctx.cppBlock())

        # elif ctx.rawCppDirective():
        #     return self.visit(ctx.rawCppDirective())

        return ""

    def visitStructDefinition(self, ctx: CHParser.StructDefinitionContext):
        struct_name = ctx.name.text
        # [ [ [ 修复 B-2: 添加 struct 的成员字典重置 ] ] ]
        self._current_class_members = {}
        self._in_class = False
        self._in_struct = True
        self._current_class_name = struct_name
        self._class_sections = {"private": "", "public": "", "protected": ""}

        if hasattr(ctx, 'structBodyStatement'):
            for child in ctx.structBodyStatement():
                self.visit(child)
        self._in_struct = False
        self._current_class_name = None
        # [ [ [ 修复 B-2: 添加 struct 的成员字典重置 ] ] ]
        self._current_class_members = {}
        final_struct_body = ""

        if self._class_sections["public"]:
            final_struct_body += f"\npublic:\n{self._class_sections['public']}"

        # [新增]
        if self._class_sections["protected"]:
            final_struct_body += f"\nprotected:\n{self._class_sections['protected']}"

        if self._class_sections["private"]:
            final_struct_body += f"\nprivate:\n{self._class_sections['private']}"

        return (
            f"\nstruct {struct_name} {{\n"
            f"{final_struct_body.strip()}\n"
            f"}};\n"
        )

    def visitVariableDeclaration(self, ctx: CHParser.VariableDeclarationContext):
        line_comment = f"{INDENT}// Line {ctx.start.line}\n"

        is_extern = bool(ctx.EXTERN())
        extern_prefix = "extern " if is_extern else ""

        core_cpp, is_member_variable, access, cpp_final_type, cpp_name = self._translate_variable_declaration(ctx)

        if is_member_variable:
            # [ [ [ 修复 B-2: 记住成员变量及其访问器 ] ] ]
            # (在 _translate_variable_declaration 中, 'cpp_name' 已被添加到
            #  当前的 scope_stack[-1] 中。我们现在将其复制到
            #  _current_class_members 字典中，以便稍后加载到方法作用域中)
            var_info = self._find_variable(cpp_name)
            if var_info:
                self._current_class_members[cpp_name] = var_info

            declaration_line = f"{line_comment}{INDENT}{core_cpp};\n"
            self._class_sections[access] += declaration_line
            return ""
        else:
            return f"{line_comment}{INDENT}{extern_prefix}{core_cpp};\n"

    def visitVariableDeclaration_no_semicolon(self, ctx: CHParser.VariableDeclaration_no_semicolonContext):
        core_cpp, _, _, _, _ = self._translate_variable_declaration(ctx)
        return core_cpp

    def visitBlockStatement(self, ctx: CHParser.BlockStatementContext):
        self._enter_scope()
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        final_code = f"{INDENT}{{\n"
        final_code += body_code
        final_code += f"{INDENT}}}\n"
        return final_code

    def visitSwitchStatement(self, ctx: CHParser.SwitchStatementContext):
        self._control_flow_depth += 1

        expr = self.visit(ctx.expression())
        case_code = "".join(self.visit(cb) for cb in ctx.caseBlock())
        default_code = self.visit(ctx.defaultBlock()) if ctx.defaultBlock() else ""

        self._control_flow_depth -= 1

        code = f"{INDENT}switch ({expr}) {{\n"
        code += case_code
        code += default_code
        code += f"{INDENT}}}\n"
        return code

    def visitCaseBlock(self, ctx: CHParser.CaseBlockContext):
        """
        [新增] 访问 'caseBlock' 规则
        e.g., case 1 { ... }
        [ [ [ 关键修复 ] ] ]
        如果块的最后一条语句是 'return', 则不再自动添加 'break;'
        """

        # 1. 翻译 case expr:
        case_expr = self.visit(ctx.expression())

        # 2. 翻译 { ... } 内部的语句 (带作用域)
        self._enter_scope()
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()

        # 3. [ [ 修复 ] ] 检查最后一条语句
        ends_with_return = False
        if statements:  # 确保语句列表不为空

            if statements[-1].returnStatement():
                ends_with_return = True

        # 4. 组装 C++
        code = f"{INDENT}case {case_expr}:\n"
        code += f"{INDENT}{{\n"
        code += body_code
        if not ends_with_return:
            code += f"{INDENT}break;\n"  # <-- [修复] 只有在需要时才添加
        code += f"{INDENT}}}\n"
        return code

    def visitDefaultBlock(self, ctx: CHParser.DefaultBlockContext):
        """
        [新增] 访问 'defaultBlock' 规则
        e.g., default { ... }
        [ [ [ 关键修复 ] ] ]
        如果块的最后一条语句是 'return', 则不再自动添加 'break;'
        """

        # 1. 翻译 'default:'

        # 2. 翻译 { ... } 内部的语句 (带作用域)
        self._enter_scope()
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()

        # 3. [ [ 修复 ] ] 检查最后一条语句
        ends_with_return = False
        if statements:  # 确保语句列表不为空
            if isinstance(statements[-1], CHParser.ReturnStatementContext):
                ends_with_return = True

        # 4. 组装 C++
        code = f"{INDENT}default:\n"
        code += f"{INDENT}{{\n"
        code += body_code
        if not ends_with_return:
            code += f"{INDENT}break;\n"  # <-- [修复] 只有在需要时才添加
        code += f"{INDENT}}}\n"
        return code

    def visitTerminal(self, node: TerminalNodeImpl):
        """
        [新增] 访问一个终端节点 (Token)。

        我们重写这个方法，专门用于捕获在语法树中
        作为 '叶子' 出现的 CPP_DIRECTIVE 词元。

        这之所以能工作，是因为 CPP_DIRECTIVE 被直接添加到了
        'topLevelStatement', 'statement', 'classBodyStatement' 等规则中。
        """

        if node.getSymbol().type == CHParser.CPP_DIRECTIVE:
            # 1:1 翻译，原样输出

            # 确定是否需要缩进 (在方法/类/struct内部)
            indent = ""

            # [修复] 只有在函数/方法 *内部* 才需要缩进。
            # 类/Struct 内部 (非方法) 和顶层不需要缩进，
            # 因为 #pragma 和 #define 通常必须在第 1 列。
            if self._in_class_method:
                indent = INDENT

            # [关键] 必须在末尾添加换行符，因为 Lexer 消耗了它
            return indent + node.getText() + "\n"

        # (重要) 返回一个空字符串，而不是 node.getText()，
        # 否则我们可能会意外地打印出 'EOF' 或其他词元。
        return ""

    def visitForwardDeclaration(self, ctx: CHParser.ForwardDeclarationContext):
        # 1. 获取名字
        name = ctx.name.text

        # 2. 获取种类 (class 或 struct)
        kind_keyword = ""
        if ctx.kind.type == CHParser.CLASS:
            kind_keyword = "class"
        elif ctx.kind.type == CHParser.STRUCT:
            kind_keyword = "struct"

        # 3. 生成 C++ 代码 (struct Child;)
        line_comment = f"\n// Line {ctx.start.line} (forward decl)\n"
        return f"{line_comment}{kind_keyword} {name};\n"

    # src/CHVisitor.py

    def visitEnumDefinition(self, ctx: CHParser.EnumDefinitionContext):
        line_comment = f"\n// Line {ctx.start.line} (enum)\n"

        # 1. 确定是 enum 还是 enum class
        is_scoped = bool(ctx.CLASS())
        keyword = "enum class" if is_scoped else "enum"

        name = ctx.name.text

        # 2. 处理底层类型 (e.g. : u8 -> : uint8_t)
        underlying_type = ""
        if ctx.typeSpecifier():
            cpp_type = self.visit(ctx.typeSpecifier())
            underlying_type = f" : {cpp_type}"

        # 3. 处理枚举体
        body_code = ""
        if ctx.enumBody():
            # 手动遍历 item，确保格式整洁
            items = ctx.enumBody().enumItem()
            formatted_items = []
            for item in items:
                item_code = self.visit(item)
                formatted_items.append(f"{INDENT}{item_code}")

            body_code = ",\n".join(formatted_items)
            if body_code:
                body_code = f"\n{body_code}\n"

        # 4. 组装 C++
        # 检查是否有访问修饰符 (用于类内部定义)
        # 但这个是在父级 (classBodyStatement) 处理的，这里只返回定义本身

        code = (
            f"{line_comment}"
            f"{keyword} {name}{underlying_type} {{\n"
            f"{body_code}"
            f"}};\n"
        )
        return code

    def visitEnumItem(self, ctx: CHParser.EnumItemContext):
        name = ctx.name.text
        if ctx.expression():
            val = self.visit(ctx.expression())
            return f"{name} = {val}"
        return name