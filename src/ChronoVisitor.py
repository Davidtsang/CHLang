# src/ChronoVisitor.py
import os
from CompileContext import CompileContext

from parser.ChronoParser import ChronoParser
from parser.ChronoParserVisitor import ChronoParserVisitor as BaseChronoVisitor
from antlr4.tree.Tree import TerminalNodeImpl  # 导入 TerminalNodeImpl

INDENT = "    "


class ChronoVisitor(BaseChronoVisitor):

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
        self._class_sections = {"private": "", "public": ""}
        self._alias_to_namespace_map = {}
        # self._literal_alias_map = {} # <--- [删除] 改用 self.context
        self._scope_stack = [{}]
        self._namespace_is_open = False

        # 这个新状态用于跟踪我们是否在 'implement' 块中
        self._in_implementation_block = False
        self._current_namespace_str = ""  # 用于 C++ 作用域
        self._current_class_members = {}

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

    def visitTypeSpecifier(self, ctx: ChronoParser.TypeSpecifierContext):
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
            # 如果 base 已经包含 {NAME} (例如多维数组 [[i32; 2]; 3])
            # base 可能是 "int32_t {NAME}[2]"
            if "{NAME}" in base:
                # 对于多维数组，C++ 的顺序是 arr[Rows][Cols]
                # Chrono 是 [ [i32; Cols]; Rows ]
                # 我们需要把新的维度追加到 {NAME} 后面
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
            # ... (C-Style 函数指针处理逻辑保持不变，请保留原代码) ...
            # (为节省篇幅省略，确保保留之前的 RawAdder 修复逻辑)
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

        # [关键] 如果 core_type 已经包含 {NAME} (数组)，后缀应该放在类型前面吗？
        # int32_t {NAME}[3] 的指针 -> int32_t (*{NAME})[3] (太复杂了)
        # 暂时假设数组不会直接跟 * 后缀 (Chrono 语法目前 [Type; N]* 会被解析为 base 为数组)
        # 如果有 {NAME}，直接返回，暂不处理外部后缀叠加（除非你需要指向数组的指针）
        if "{NAME}" in core_type:
            return core_type

        return f"{core_type}{suffix_str}"

    def visitBaseType(self, ctx: ChronoParser.BaseTypeContext):
        raw_text = ctx.getText()

        # 2. 直接替换 :: (如果是新语法) 或者 . (如果是旧语法) 为 ::
        # 如果用户写 std::vector，raw_text 就是 std::vector
        # 如果用户写 std.vector，raw_text 就是 std.vector
        # 我们统一转换为 ::
        cpp_type = raw_text.replace('.', '::')

        # 处理别名 (例如 IO.cout -> IO::cout)
        parts = cpp_type.split('::')
        if parts[0] in self._alias_to_namespace_map:
            parts[0] = self._alias_to_namespace_map[parts[0]]

        final_type = "::".join(parts)
        return self._chrono_to_cpp_type(final_type)

    def visitNamespaceStatement(self, ctx: ChronoParser.NamespaceStatementContext):
        # [ [ [ 关键修复 ] ] ]
        # 'ctx.name' 是一个 ANTLR 规则上下文 (QualifiedIdentifierContext),
        # 不是一个 Token。我们必须使用 .getText() 方法来获取其完整文本。
        self._namespace_is_open = True
        namespace_name = ctx.name.getText()  # <--- 修复

        cpp_namespace = namespace_name.replace('.', '::')
        self._current_namespace_str = cpp_namespace + "::"

        # 1:1 翻译
        open_block = f"namespace {namespace_name.replace('.', ' { namespace ')} {{\n\n"
        # (我们必须在 visitProgram 中添加闭合 '}' )
        return open_block

    def visitEndNamespaceStatement(self, ctx: ChronoParser.EndNamespaceStatementContext):
        if not self._namespace_is_open:
            raise Exception(
                f"Chrono Translation Error (Line {ctx.start.line}): 'endnamespace;' called without a matching 'namespace' statement.")

        depth = self._current_namespace_str.count('::')
        closing_braces = "}" * depth
        comment_name = self._current_namespace_str.replace('::', '.')[:-1]

        self._namespace_is_open = False  # <-- [ [ [ 保留 ] ] ]
        self._current_namespace_str = ""

        return f"\n{closing_braces} // namespace {comment_name}\n\n"

    def visitImplementationBlock(self, ctx: ChronoParser.ImplementationBlockContext):
        # 1. 设置状态
        self._in_implementation_block = True
        self._current_class_name = ctx.name.text
        self._in_class = True  # (模拟在类中，以使 'this' 和方法解析正常工作)

        # 2. 访问所有实现体 (methodDefinition, initDefinition...)
        body_code = ""
        for child in ctx.children:
            if isinstance(child, (ChronoParser.MethodDefinitionContext,
                                  ChronoParser.InitDefinitionContext,
                                  ChronoParser.DeinitBlockContext)):
                body_code += self.visit(child)

        # 3. 重置状态
        self._in_implementation_block = False
        self._current_class_name = None
        self._in_class = False

        return body_code  # 返回所有 C++ 实现代码

    def visitMethodDefinition(self, ctx: ChronoParser.MethodDefinitionContext):

        line_comment = f"\n// Line {ctx.start.line} (method {ctx.name.text})\n"
        self._in_class_method = True
        self._enter_scope()

        # [ [ [ 修复 B-2: 加载 'this' 和所有成员到作用域 ] ] ]

        # 1. 确定 'this' 的访问器 (-> 或 .)
        accessor = "->"
        if self._in_struct:
            accessor = "."  # Struct 内部 'this.x' -> 'this.x'

        cpp_type = f"{self._current_class_name}*"

        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,  # ←-- 关键: '.' (struct) or '→' (class)
            "cpp_type": cpp_type
        })

        # 2. 将所有类/struct成员 (例如 's') 加载到当前作用域
        for member_name, metadata in self._current_class_members.items():
            self._add_variable(member_name, metadata)

        # [ [ [ 修复结束 ] ] ]

        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))
        return_type = self.visit(ctx.returnType) if ctx.returnType else "void"

        # [ [ [ 检查 'implement' 块 ] ] ]
        if self._in_implementation_block:

            # [ [ [ 修复 A-3: 移除 'implement' 块中的命名空间前缀 ] ] ]
            cpp_func_name = f"{self._current_class_name}::{func_name}"
            static_prefix = ""  # C++ .cpp 实现不重复 'static'

            func_def_code = (
                f"{line_comment}"
                f"\n{return_type} {cpp_func_name}({params_code}) {{\n"
                f"{body_code}"
                f"{INDENT}// --- Method End ---\n"
                f"{INDENT}}}\n"
            )
        else:
            # (内联模式)
            cpp_func_name = func_name
            is_static = getattr(ctx, '_chrono_static', False)
            access = getattr(ctx, '_chrono_access', 'private')
            if self._in_struct:
                access = getattr(ctx, '_chrono_access', 'public')

            static_prefix = "static " if is_static else ""
            virtual_prefix = "virtual " if not is_static else ""

            func_def_code = (
                f"{line_comment}"
                f"\n{INDENT}{virtual_prefix}{static_prefix}{return_type} {cpp_func_name}({params_code}) {{\n"
                f"{body_code}"
                f"{INDENT}\n"
                f"{INDENT}}}\n"
            )
            self._class_sections[access] += func_def_code

        self._exit_scope()
        self._in_class_method = False

        return func_def_code if self._in_implementation_block else ""

    def visitFunctionDefinition(self, ctx: ChronoParser.FunctionDefinitionContext):

        line_comment = f"\n// Line {ctx.start.line} (func {ctx.name.text})\n"
        # 这是一个全局函数 (不在类中或 implement 块中)
        self._enter_scope()

        func_name = ctx.name.text

        cpp_func_name = ""
        if func_name == "main":
            cpp_func_name = "main"  # 强制全局
        else:
            # [ [ [ 修复 A-2: 移除函数定义中的命名空间前缀 ] ] ]
            cpp_func_name = func_name

        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))
        return_type = self.visit(ctx.returnType) if ctx.returnType else "void"

        # [ [ [ 关键修复 ] ] ]
        # 正确检查 (STATIC)? 关键字
        # (ChronoParser.g4 中 functionDefinition 规则定义了 (STATIC)? )
        is_static = bool(ctx.STATIC())
        static_prefix = "static " if is_static else ""

        # [ [ [ 核心修复 ] ] ]
        # 直接构建并返回 C++ 代码字符串，不再委托给 visitMethodDefinition
        func_def_code = (
            f"{line_comment}"
            f"{static_prefix}{return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            f"{INDENT}// --- Function End ---\n"
            f"}}\n"
        )

        self._exit_scope()

        # [ [ [ 核心修复 ] ] ]
        return func_def_code  # <--- 返回生成的代码，而不是 ""

    def visitParameter(self, ctx: ChronoParser.ParameterContext):
        """
        [重构] 访问 'parameter' 规则。
        [ [ [ 关键修复 ] ] ] 移除了 '_' 前缀。
        """

        var_name = ctx.name.text
        key = var_name
        cpp_name = var_name  # 默认 C++ 名称 (无 '_')

        base_type_cpp = self.visit(ctx.typeName)
        cpp_final_type = base_type_cpp

        is_pointer = base_type_cpp.endswith('*')
        is_reference = base_type_cpp.endswith('&')
        is_c_array = False

        if not is_pointer and not is_reference and ';[' in base_type_cpp:
            is_c_array = True
            parts = base_type_cpp.split(';')
            base_only = parts[0]
            cpp_final_type = f"{base_only}*"
            is_pointer = True

        accessor = "."
        if is_c_array:
            accessor = "."
        elif is_pointer:
            accessor = "->"

        # [ [ [ 关键 ] ] ]
        # 移除了所有 'cpp_name = f"_{cpp_name}"' 逻辑

        self._add_variable(key, {
            "cpp_name": cpp_name,  # 始终使用原始名称
            "accessor": accessor,
            "cpp_type": base_type_cpp
        })

        return f"{cpp_final_type} {cpp_name}"

    def visitFunctionCallExpression(self, ctx: ChronoParser.FunctionCallExpressionContext):
        """
        [重构] 新增对 @move 的翻译
        """
        name_token = ctx.funcName

        if name_token.type == ChronoParser.AT_MOVE:
            cpp_func_name = "std::move"
        else:
            cpp_func_name = name_token.text

        args_list = []
        if ctx.expressionList():
            for arg_expr in ctx.expressionList().expression():
                arg_code = self.visit(arg_expr)
                args_list.append(arg_code)
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
                    f"Chrono Error (Line {ctx.start.line}): Declaration of '{var_name}' must have an explicit type or an initializer.")
            base_type_cpp = "auto"
            cpp_final_type = "auto"

        # --- 4. 验证 Const ---
        if is_const and not ctx.expression():
            raise Exception(
                f"Chrono Error (Line {ctx.start.line}): Constant declaration '{var_name}' must be initialized.")

        # --- 5. 确定是指针/引用/数组 ---
        is_pointer = False
        is_reference = False

        # 检查是否为 C-Style 函数指针 (特征：包含 (*{NAME}) )
        is_c_style_func_ptr = "(*{NAME})" in cpp_final_type

        # 检查是否为 C-Style 数组 (特征：包含 {NAME} 但不是函数指针)
        # 注意：visitTypeSpecifier 现在会为数组生成 int32_t {NAME}[3] 格式
        is_c_array = "{NAME}" in cpp_final_type and not is_c_style_func_ptr

        if base_type_cpp != "auto":
            # 判断是否为指针类型
            if base_type_cpp.endswith('*') or \
                    base_type_cpp.startswith("std::unique_ptr") or \
                    base_type_cpp.startswith("std::shared_ptr") or \
                    base_type_cpp.startswith("std::weak_ptr") or \
                    is_c_style_func_ptr:
                is_pointer = True

            is_reference = base_type_cpp.endswith('&')

        # [ auto 推导逻辑 ]
        if base_type_cpp == "auto" and ctx.expression():
            primary_node = None
            try:
                # 尝试获取表达式的第一个节点来推测是否是工厂调用
                # 这只是一个简单的启发式判断，用于设置默认访问器
                primary_node = ctx.expression().unaryExpression(0).simpleExpression().children[0]
            except Exception as e:
                pass

            is_factory_call = False
            if primary_node and isinstance(primary_node, ChronoParser.PrimaryContext):
                if primary_node.NEW():
                    is_factory_call = True
                elif primary_node.AT_MAKE_UNIQUE():
                    is_factory_call = True
                elif primary_node.AT_MAKE_SHARED():
                    is_factory_call = True

            if is_factory_call:
                is_pointer = True

        # --- 6. 确定访问器 ---
        accessor = "."
        if is_c_array:
            accessor = "."  # 数组名本身用 . 访问 (作为衰变后的指针或者对象)
        elif is_c_style_func_ptr:
            accessor = "."  # 函数指针通常直接调用，或者解引用
        elif is_pointer:
            accessor = "->"  # 指针默认用箭头

        # --- 7. 注册到作用域栈 ---
        # 将变量名及其属性注册到当前作用域，供后续表达式解析使用
        self._add_variable(key, {
            "cpp_name": cpp_name,
            "accessor": accessor,
            "cpp_type": base_type_cpp
        })

        # --- 8. 确定赋值 ---
        cpp_value = ""
        if ctx.expression():
            cpp_value = f" = {self.visit(ctx.expression())}"

        elif is_pointer and base_type_cpp != "auto":
            # [关键修复] 处理未初始化的指针
            # 1. 智能指针不需要显式 = nullptr (默认构造函数会处理)
            # 2. 裸指针 (*) 和 C-Style 函数指针 ((*)) 必须显式初始化为 nullptr，否则是野指针

            is_smart_ptr = (base_type_cpp.startswith("std::unique_ptr") or
                            base_type_cpp.startswith("std::shared_ptr") or
                            base_type_cpp.startswith("std::weak_ptr"))

            if not is_smart_ptr:
                cpp_value = " = nullptr"

        # --- 9. 确定是局部还是成员 ---
        is_member_variable = (self._in_class or self._in_struct) and not self._in_class_method
        access = getattr(ctx, '_chrono_access', 'private')

        # --- 10. 生成核心 C++ 代码 ---
        core_cpp = ""

        if "{NAME}" in cpp_final_type:
            # 这是一个带占位符的类型 (数组或函数指针)
            # e.g. "int32_t {NAME}[3]" -> "int32_t myArr[3]"
            # e.g. "int (*{NAME})(int)" -> "int (*myFunc)(int)"
            core_cpp = f"{const_prefix}{cpp_final_type.replace('{NAME}', cpp_name)}{cpp_value}"
        else:
            # 标准声明
            # e.g. "int32_t myVar"
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
        if token_type == ChronoParser.PLUS: return "+"
        if token_type == ChronoParser.MINUS: return "-"
        if token_type == ChronoParser.STAR: return "*"
        if token_type == ChronoParser.SLASH: return "/"
        if token_type == ChronoParser.MODULO: return "%"
        if token_type == ChronoParser.EQ: return "=="
        if token_type == ChronoParser.NEQ: return "!="
        if token_type == ChronoParser.LT: return "<"
        if token_type == ChronoParser.GT: return ">"
        if token_type == ChronoParser.LTE: return "<="
        if token_type == ChronoParser.GTE: return ">="
        if token_type == ChronoParser.AND_OP: return "&&"
        if token_type == ChronoParser.OR_OP: return "||"
        if token_type == ChronoParser.BIT_AND: return "&"
        if token_type == ChronoParser.BIT_OR: return "|"
        if token_type == ChronoParser.BIT_XOR: return "^"
        if token_type == ChronoParser.LSHIFT: return "<<"
        if token_type == ChronoParser.RSHIFT: return ">>"
        raise Exception(f"Unknown operator token type: {token_type}")

    def _add_variable(self, chrono_name, metadata):
        """在*当前*作用域中定义一个新变量 (使用 Chrono 名字 $s 或 s 作为 Key)"""
        self._scope_stack[-1][chrono_name] = metadata

    def _find_variable(self, chrono_name):
        """从当前作用域开始，向外(全局)查找一个变量 (使用 Chrono 名字 $s 或 s)"""
        for scope in reversed(self._scope_stack):
            if chrono_name in scope:
                return scope[chrono_name]
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

    def _chrono_to_cpp_type(self, chrono_type_name):
        """
        [重构] 新增智能指针关键字的翻译
        """
        if chrono_type_name == "bool":
            return "bool"
        if chrono_type_name == "unique":
            return "std::unique_ptr"
        if chrono_type_name == "shared":
            return "std::shared_ptr"
        if chrono_type_name == "weak":
            return "std::weak_ptr"
        if chrono_type_name == "i8":
            return "int8_t"
        if chrono_type_name == "u8":
            return "uint8_t"
        if chrono_type_name == "i16":
            return "int16_t"
        if chrono_type_name == "u16":
            return "uint16_t"
        if chrono_type_name == "int":
            return "int"
        if chrono_type_name == "i32":
            return "int32_t"
        if chrono_type_name == "u32":
            return "uint32_t"
        if chrono_type_name == "i64":
            return "int64_t"
        if chrono_type_name == "u64":
            return "uint64_t"
        if chrono_type_name == "f32" or chrono_type_name == "float":
            return "float"
        if chrono_type_name == "f64":
            return "double"
        return chrono_type_name

    def _get_access_level(self, ctx, default_level='private'):
        """检查上下文是否包含访问修饰符，返回 'public' 或指定的默认值。"""
        if hasattr(ctx, 'accessModifier') and ctx.accessModifier():
            return "public"
        elif hasattr(ctx, 'declaration') and hasattr(ctx.variableDeclaration(),
                                                     'accessModifier') and ctx.variableDeclaration().accessModifier():
            return "public"
        elif hasattr(ctx, 'methodDefinition') and hasattr(ctx.methodDefinition(),
                                                          'accessModifier') and ctx.methodDefinition().accessModifier():
            return "public"
        return default_level

    # --- 顶层规则 ---
    def visitProgram(self, ctx: ChronoParser.ProgramContext):

        # [ [ [ 修复：恢复“优雅”的顺序循环 ] ] ]
        all_code = ""

        # 1. 按顺序访问所有子节点 (Imports, Namespace, Code, EndNamespace)
        for child in ctx.children:

            # A. 处理顶层的 # 指令 (来自 topLevelImport)
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == ChronoParser.CPP_DIRECTIVE:
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
                "Chrono Translation Error: 'namespace' was declared, but 'endnamespace;' was missing before the end of the file.")

        return all_code.strip()

    def visitImportDirective(self, ctx: ChronoParser.ImportDirectiveContext):

        line_comment = f"\n// Line {ctx.start.line} \n"

        # --- [关键修复] 路径重建逻辑 ---
        # 因为我们从 Lexer 删除了 INCLUDE_PATH，现在需要在 Visitor 里还原路径字符串

        path_text = ""
        is_system_header = False

        if ctx.pathStr:
            # 情况 A: import "foo.ch"
            path_text = ctx.pathStr.text
        else:
            # 情况 B: import <vector> 或 import <sys/stat.h>
            # ANTLR 将其拆分为了 LT, IDENTIFIER(sys), SLASH, IDENTIFIER(stat), DOT, IDENTIFIER(h), GT
            # 我们需要获取 pathSeq 对应的完整原始文本
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

        base_name = os.path.basename(path_text.strip('\"<>'))
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

    def visitUsingAlias(self, ctx: ChronoParser.UsingAliasContext):
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

        # src/ChronoVisitor.py

    def visitParameters(self, ctx: ChronoParser.ParametersContext):
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
    def visitBaseInitializer(self, ctx: ChronoParser.BaseInitializerContext):
        """
        访问 'baseInitializer' 规则 (例如 : Window(args) )
        并将其翻译为 C++ 字符串 "Window(args)"
        """
        base_name = ctx.name.text
        args_code = self.visit(ctx.args) if ctx.args else ""
        return f"{base_name}({args_code})"

    def visitMethodSignature(self, ctx: ChronoParser.MethodSignatureContext):
        func_name = ctx.name.text
        cpp_func_name = func_name
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        if ctx.returnType:
            cpp_return_type = self.visit(ctx.returnType)
        else:
            cpp_return_type = "void"
        return f"{INDENT}virtual {cpp_return_type} {cpp_func_name}({params_code}) = 0;\n"

    def visitInterfaceDefinition(self, ctx: ChronoParser.InterfaceDefinitionContext):
        interface_name = ctx.name.text
        body_code = ""
        child_nodes = ctx.children[2:-1]
        for child in child_nodes:
            if isinstance(child, ChronoParser.MethodSignatureContext):
                body_code += self.visit(child)
            elif isinstance(child, ChronoParser.CppBlockContext):
                body_code += self.visit(child)
        code = f"\nclass {interface_name} {{\n"
        code += "public:\n"
        code += f"{INDENT}virtual ~{interface_name}() {{}} // Virtual destructor\n"
        code += body_code
        code += "};\n"
        return code

    def visitFunctionSignature(self, ctx: ChronoParser.FunctionSignatureContext):
        # is_static = (ctx.STATIC() is not None) # <-- [删除] 不再重新计算
        line_comment = f"\n// Line {ctx.start.line} \n"

        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        return_type = self.visit(ctx.returnType) if ctx.returnType else "void"

        if self._in_class or self._in_struct:
            default_access = 'public' if self._in_struct else 'private'
            access = getattr(ctx, '_chrono_access', default_access)

            # [ [ [ 关键修复 ] ] ]
            # 依赖从 visitClassBodyStatement 传递过来的 _chrono_static 标志
            is_static = getattr(ctx, '_chrono_static', False)

            static_prefix = "static " if is_static else ""
            virtual_prefix = "virtual " if not is_static else ""  # 保持：static 和 virtual 互斥

            decl = f"{line_comment}{INDENT}{virtual_prefix}{static_prefix}{return_type} {func_name}({params_code});\n"
            self._class_sections[access] += decl
            return ""
        else:
            # 全局函数签名 (不在类中)
            is_extern = bool(ctx.EXTERN())
            is_static = bool(ctx.STATIC())  # <--- [修正] 全局函数签名也需要正确检查
            static_prefix = "static " if is_static else ""
            extern_prefix = "extern " if is_extern else ""
            return f"{line_comment}{extern_prefix}{static_prefix}{return_type} {self._current_namespace_str}{func_name}({params_code});\n"

    def visitInitSignature(self, ctx: ChronoParser.InitSignatureContext):
        line_comment = f"\n// Line {ctx.start.line} \n"
        default_access = 'public' if self._in_struct else 'private'
        access = getattr(ctx, '_chrono_access', default_access)

        func_name = self._current_class_name
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        decl = f"{line_comment}{INDENT}{func_name}({params_code});\n"
        self._class_sections[access] += decl
        return ""

    def visitDeinitSignature(self, ctx: ChronoParser.DeinitSignatureContext):
        line_comment = f"\n// Line {ctx.start.line} \n"

        access = "public"  # Deinit 总是 public
        func_name = f"~{self._current_class_name}"

        decl = f"{line_comment}{INDENT}virtual {func_name}();\n"
        self._class_sections[access] += decl
        return ""

    def visitClassDefinition(self, ctx: ChronoParser.ClassDefinitionContext):
        # (调用  中的 visitClassDefinition 逻辑)
        # (它会访问 classBodyStatement，后者会填充 _class_sections)
        # (然后它会组装 C++ 类声明)
        self._current_class_members = {}  # <--- [ [ [ 新增 2/4 (a) ] ] ]
        self._in_class = True
        # --- 这是 .h.ch (HEADER) 模式 ---
        class_name = ctx.name.text
        inheritance_list = []
        if ctx.base:
            base_name = ctx.base.text
            inheritance_list.append(f"public {base_name}")
        if ctx.interfaces:
            interface_names_str = self.visit(ctx.interfaces)
            interfaces = [f"public {name.strip()}" for name in interface_names_str.split(',')]
            inheritance_list.extend(interfaces)
        inheritance_str = ""
        if inheritance_list:
            inheritance_str = " : " + ", ".join(inheritance_list)

        self._in_class = True
        self._in_struct = False
        self._current_class_name = class_name
        self._class_sections = {"private": "", "public": ""}  # 重置

        # 访问所有声明 (variableDeclaration, functionSignature, etc.)
        if hasattr(ctx, 'classBodyStatement'):
            for child in ctx.classBodyStatement():
                self.visit(child)

        self._in_class = False
        self._current_class_name = None

        final_class_body = ""
        if self._class_sections["public"]:
            final_class_body += "\npublic:\n" + self._class_sections["public"]

        if self._class_sections["private"]:
            final_class_body += "\nprivate:\n" + self._class_sections["private"]

        self._in_class = False
        self._current_class_name = None
        self._current_class_members = {}

        # [ [ [ 修复 A-1: 移除类定义中的命名空间前缀 ] ] ]
        return (
            f"\nclass {class_name}{inheritance_str} {{\n"
            f"{final_class_body.strip()}\n"
            "};\n"
        )

    def visitClassBodyStatement(self, ctx: ChronoParser.ClassBodyStatementContext):
        # [ [ [ 关键修复 ] ] ]
        # 修复了 static 关键字的检测。
        # G4 语法在 (classBody) 和 (functionSignature) 中都有 (STATIC)?，这有歧义。
        # 我们必须检查这两个地方，以确保捕捉到 'static'。

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
            ctx.variableDeclaration()._chrono_access = access
            # 传递 static 状态 (尽管 G4 不支持 static var)
            ctx.variableDeclaration()._chrono_static = is_static
            return self.visit(ctx.variableDeclaration())

            # [新增] 处理嵌套枚举
        elif ctx.enumDefinition():
            enum_code = self.visit(ctx.enumDefinition())
            # 枚举定义直接放入对应的访问区段
            self._class_sections[access] += enum_code
            return ""

        elif ctx.functionSignature():
            ctx.functionSignature()._chrono_access = access
            ctx.functionSignature()._chrono_static = is_static  # <--- 传递合并后的 'is_static' 状态
            return self.visit(ctx.functionSignature())

        elif ctx.initSignature():
            ctx.initSignature()._chrono_access = access
            return self.visit(ctx.initSignature())

        elif ctx.deinitSignature():
            # deinit 总是 public
            ctx.deinitSignature()._chrono_access = 'public'
            return self.visit(ctx.deinitSignature())


        elif ctx.cppBlock():
            return self.visit(ctx.cppBlock())

        return ""

    def visitInitDefinition(self, ctx: ChronoParser.InitDefinitionContext):

        line_comment = f"\n// Line {ctx.start.line} (init)\n"
        self._in_class_method = True
        self._enter_scope()

        # [ [ [ 修复 B-2: 加载 'this' 和所有成员到作用域 ] ] ]
        # ( ... 您现有的加载 'this' 和成员的代码 ... )
        accessor = "->"
        if self._in_struct:
            accessor = "."
        cpp_type = f"{self._current_class_name}*"
        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,
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
            # visit(ctx.baseInit) 将返回 "Window(L\"My Chrono GDI+ Window\", app)"
            base_init_code = f" : {self.visit(ctx.baseInit)}"
        # [ [ [ 新增结束 ] ] ]

        # [ [ [ 检查 'implement' 块 ] ] ]
        if self._in_implementation_block:
            # [修复 A-4]
            cpp_func_name = f"{self._current_class_name}::{self._current_class_name}"
        else:
            access = getattr(ctx, '_chrono_access', 'private')
            if self._in_struct:
                access = getattr(ctx, '_chrono_access', 'public')

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

    def _determine_initial_accessor(self, raw_primary_text, translated_primary_code):
        """
        [重构]
        [ [ [ 关键修复 ] ] ] 现在优先检查 typemap 代换
        """

        # 步骤 2: 检查 'var' 变量
        variable_info = self._find_variable(raw_primary_text)
        if variable_info:
            return translated_primary_code, variable_info["accessor"], variable_info["cpp_type"]

        # 步骤 3: 检查 'import as' 别名
        elif raw_primary_text in self._alias_to_namespace_map:
            return self._alias_to_namespace_map[raw_primary_text], "::", "namespace"

        # 步骤 4: 检查 'std'
        elif raw_primary_text == "std":
            return "std", "::", "namespace"

        # 步骤 5: 检查 C++ 类名 (大写)
        elif raw_primary_text and raw_primary_text.lstrip('$')[0].isupper():
            return self._chrono_to_cpp_type(raw_primary_text), "::", "class"

        # 步骤 6: 默认回退
        else:
            return translated_primary_code, ".", "literal"

    def _process_dot_chain_step(self, child_nodes, i, current_code, current_accessor, current_type, access_token_type):
        """
        [重构] 纯净版：不猜测，用户写什么就翻译什么。
        access_token_type: ChronoParser.DOT, ARROW, 或 COLON_COLON
        """
        i += 1
        if i >= len(child_nodes):
            return current_code, i, current_accessor, current_type

        ident_node = child_nodes[i]
        i += 1
        raw_ident_text = ident_node.getText()

        # 依然尝试查找变量名以获取正确的 C++ 名称 (e.g. map key to value)
        # 但不再用它来决定访问器
        member_info = self._find_variable(raw_ident_text)
        cpp_ident = member_info["cpp_name"] if member_info else raw_ident_text

        # [核心逻辑] 直接映射 Token 到 C++ 操作符
        accessor_str = ""
        if access_token_type == ChronoParser.DOT:
            accessor_str = "."
        elif access_token_type == ChronoParser.ARROW:
            accessor_str = "->"
        elif access_token_type == ChronoParser.COLON_COLON:
            accessor_str = "::"

        # 处理泛型 <T>
        template_args_str = ""
        if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.LT:
            i += 1  # skip <
            if i < len(child_nodes) and isinstance(child_nodes[i], ChronoParser.TypeListContext):
                template_args_str = self.visit(child_nodes[i])
                i += 1
            if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.GT:
                i += 1  # skip >

        if template_args_str:
            cpp_ident = f"{cpp_ident}<{template_args_str}>"

        # 处理函数调用 (...)
        if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.LPAREN:
            i += 1
            args = ""
            if i < len(child_nodes) and isinstance(child_nodes[i], ChronoParser.ExpressionListContext):
                args = self.visit(child_nodes[i])
                i += 1
            if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.RPAREN:
                i += 1
            # 生成代码
            new_code = f"{current_code}{accessor_str}{cpp_ident}({args})"
        else:
            # 生成代码
            new_code = f"{current_code}{accessor_str}{cpp_ident}"

        # 不需要再返回 next_accessor，因为我们不预测下一步，下一步完全取决于下一个 Token
        return new_code, i, None, "unknown"

    def _process_array_chain_step(self, child_nodes, i, current_code, current_accessor):
        i += 1
        if i >= len(child_nodes): return current_code, i, "."
        index_expr = self.visit(child_nodes[i])
        i += 1
        if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.RBRACK:
            i += 1
        new_code = f"{current_code}[{index_expr}]"
        new_accessor = current_accessor
        return new_code, i, new_accessor

    def visitDeinitBlock(self, ctx: ChronoParser.DeinitBlockContext):

        line_comment = f"\n// Line {ctx.start.line} (deinit)\n"

        self._in_class_method = True
        self._enter_scope()

        # [ [ [ 修复 B-2: 加载 'this' 和所有成员到作用域 ] ] ]

        # 1. 确定 'this' 的访问器 (-> 或 .)
        accessor = "->"
        if self._in_struct:
            accessor = "."  # Struct 内部 'this.x' -> 'this.x'

        cpp_type = f"{self._current_class_name}*"

        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,  # 关键: '.' (struct) or '→' (class)
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
                f"{INDENT}// --- Chrono Deinit Block ---\n"
                f"{body_code}"
                f"{INDENT}// --- Deinit End ---\n"
                f"{INDENT}}}\n"
            )
        else:
            access = "public"  # Deinit 总是 public
            deinit_code = (
                f"{line_comment}\n{INDENT}virtual {cpp_func_name}() {{\n"
                f"{INDENT}// --- Chrono Deinit Block ---\n"
                f"{body_code}"
                f"{INDENT}// --- Deinit End ---\n"
                f"{INDENT}}}\n"
            )
            self._class_sections[access] += deinit_code

        self._exit_scope()
        self._in_class_method = False

        return deinit_code if self._in_implementation_block else ""

    def visitTypeList(self, ctx: ChronoParser.TypeListContext):
        arg_list = [self.visit(t) for t in ctx.templateArgument()]
        return ", ".join(arg_list)

    def visitTemplateArgument(self, ctx: ChronoParser.TemplateArgumentContext):
        if ctx.typeSpecifier():
            return self.visit(ctx.typeSpecifier())
        if ctx.literal():
            return self.visit(ctx.literal())
        return ""

    def visitInitializerList(self, ctx: ChronoParser.InitializerListContext):
        args_code = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
        return f"{{{args_code}}}"

    def visitSimpleExpression(self, ctx: ChronoParser.SimpleExpressionContext):
        # 1. 初始部分 (同前)
        translated_primary = ""
        if ctx.primary():
            translated_primary = self.visit(ctx.primary())
        elif ctx.functionCallExpression():
            translated_primary = self.visit(ctx.functionCallExpression())
        else:
            return ""

        current_code = translated_primary

        # [修改] 初始访问器逻辑现在主要用于处理 import 别名等
        # _determine_initial_accessor 仍然有用 (例如将 'std' 映射为 'std')
        # 但在纯净模式下，primary 已经决定了第一部分。
        # 如果 primary 是 'std'，它返回 'std'，code 就是 'std'。

        child_nodes = ctx.children[1:]
        i = 0
        while i < len(child_nodes):
            token_type = child_nodes[i].getSymbol().type

            # [关键] 显式分发
            if token_type in [ChronoParser.DOT, ChronoParser.ARROW, ChronoParser.COLON_COLON]:
                current_code, i, _, _ = self._process_dot_chain_step(
                    child_nodes, i, current_code, None, None, token_type
                )

            elif token_type == ChronoParser.LBRACK:
                # 数组索引
                current_code, i, _ = self._process_array_chain_step(
                    child_nodes, i, current_code, None
                )
            else:
                i += 1

        return current_code

    def visitPrimary(self, ctx: ChronoParser.PrimaryContext):
        """
        [重构]
        [新增] 支持 static_cast[T](val), reinterpret_cast[T](val), const_cast[T](val)
        [修复] 确保 'typemap' 代换的常量 (e.g., C_COLOR_WINDOW) 在表达式中被正确识别
        """

        if ctx.NEW():
            class_name = self.visit(ctx.baseType())
            args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
            return f"new {class_name}({args})"

        # [ [ [ 关键：处理 Casts 和 @make ] ] ]
        #
        # 解析器 (g4) 匹配了 Chrono 语法 (使用方括号 LBRACK):
        # e.g., static_cast[C_HBRUSH](value)
        # e.g., @make[Resource](args)

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

        # [ [ [ 转换逻辑结束 ] ] ]

        if ctx.literal():
            return self.visit(ctx.literal())

        if ctx.initializerList():
            return self.visit(ctx.initializerList())

        if ctx.IDENTIFIER():
            primary_text = ctx.IDENTIFIER().getText()

            # 1. 优先查找变量 (局部变量、成员变量)
            variable_info = self._find_variable(primary_text)
            if variable_info:
                if '[' in variable_info["cpp_type"]:
                    return primary_text
                else:
                    return variable_info["cpp_name"]

            # 2. [关键修复] 查找 Import 别名 (Namespace Alias)
            # 如果 primary_text 是 "Math"，且在 map 中映射为 "MyMath"
            if primary_text in self._alias_to_namespace_map:
                return self._alias_to_namespace_map[primary_text]

            # 4. 最后的兜底 (原样输出)
            return primary_text

        if ctx.THIS():
            return "this"

        if ctx.LPAREN():
            return f"({self.visit(ctx.expression())})"

        return ""

    # [ [ [ 替换结束 ] ] ]

    def visitParameter(self, ctx: ChronoParser.ParameterContext):
        var_name = ctx.name.text
        key = var_name
        cpp_name = var_name

        base_type_cpp = self.visit(ctx.typeName)

        accessor = "."
        if base_type_cpp.endswith('*'):
            accessor = "->"

        # 注册变量
        self._add_variable(key, {
            "cpp_name": cpp_name,
            "accessor": accessor,
            "cpp_type": base_type_cpp
        })

        # [关键修改] 处理带 {NAME} 的类型 (数组/函数指针)
        if "{NAME}" in base_type_cpp:
            return base_type_cpp.replace("{NAME}", cpp_name)
        else:
            return f"{base_type_cpp} {cpp_name}"

    def visitStatement(self, ctx: ChronoParser.StatementContext):
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

    def visitReturnStatement(self, ctx: ChronoParser.ReturnStatementContext):
        line_comment = f"{INDENT}// Line {ctx.start.line}\n"
        if ctx.expression():  # [修复] return 可以是空的
            return_value = self.visit(ctx.expression())
            return f"{line_comment}{INDENT}return {return_value};\n"
        return f"{line_comment}{INDENT}return;\n"  # 空 return

    def visitCppBlock(self, ctx: ChronoParser.CppBlockContext):
        token_list = ctx.CPP_BODY()
        if token_list is None: token_list = []
        raw_cpp = "".join(token.getText() for token in token_list)
        return (
            f"\n{INDENT}// --- @cpp Block Start ---\n"
            f"{raw_cpp.strip()}\n"
            f"{INDENT}// --- @cpp Block End ---\n\n"
        )

    def visitAssignment(self, ctx: ChronoParser.AssignmentContext):
        line_comment = f"{INDENT}// Line {ctx.start.line}\n"
        target = self.visit(ctx.assignableExpression())
        value = self.visit(ctx.expression())
        op_str = self.visit(ctx.assignmentOperator())
        return f"{line_comment}{INDENT}{target} {op_str} {value};\n"

    def visitAssignableExpression(self, ctx: ChronoParser.AssignableExpressionContext):
        # ... (primary 处理同前) ...
        primary_ctx = ctx.assignablePrimary()
        current_code = self.visit(primary_ctx)

        child_nodes = ctx.children[1:]
        i = 0
        while i < len(child_nodes):
            token_type = child_nodes[i].getSymbol().type

            if token_type in [ChronoParser.DOT, ChronoParser.ARROW, ChronoParser.COLON_COLON]:
                i += 1  # Skip operator
                ident_node = child_nodes[i]
                i += 1
                raw_ident_text = ident_node.getText()

                # 简单的变量名映射 (s -> s, string -> string)
                member_info = self._find_variable(raw_ident_text)
                cpp_ident = member_info["cpp_name"] if member_info else raw_ident_text

                op_str = "."
                if token_type == ChronoParser.ARROW:
                    op_str = "->"
                elif token_type == ChronoParser.COLON_COLON:
                    op_str = "::"

                current_code = f"{current_code}{op_str}{cpp_ident}"

            elif token_type == ChronoParser.LBRACK:
                i += 1
                index_expr = self.visit(child_nodes[i])
                i += 2
                current_code = f"{current_code}[{index_expr}]"
            else:
                i += 1
        return current_code

    def visitForStatement(self, ctx: ChronoParser.ForStatementContext):
        self._enter_scope()
        init_code = ""
        if ctx.init:
            init_code = self.visit(ctx.init)
        cond_code = ""
        if ctx.cond:
            cond_code = self.visit(ctx.cond)
        incr_code = ""
        if ctx.incr:
            incr_code = self.visit(ctx.incr)
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        code = f"{INDENT}for ({init_code}; {cond_code}; {incr_code}) {{\n"
        code += body_code
        code += f"{INDENT}}}\n"
        return code

    def visitForInit(self, ctx: ChronoParser.ForInitContext):
        if ctx.variableDeclaration_no_semicolon():
            return self.visit(ctx.variableDeclaration_no_semicolon())
        if ctx.assignment_no_semicolon():
            return self.visit(ctx.assignment_no_semicolon())
        return ""

    def visitForIncrement(self, ctx: ChronoParser.ForIncrementContext):
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
            if isinstance(child, ChronoParser.StatementContext):
                body_code += self.visit(child)
        return body_code

    def visitAssignmentOperator(self, ctx: ChronoParser.AssignmentOperatorContext):
        if ctx.ASSIGN(): return "="
        if ctx.PLUS_ASSIGN(): return "+="
        if ctx.MINUS_ASSIGN(): return "-="
        if ctx.STAR_ASSIGN(): return "*="
        if ctx.SLASH_ASSIGN(): return "/="
        if ctx.MOD_ASSIGN(): return "%="
        return "="

    def visitIfStatement(self, ctx: ChronoParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        if_body = self.visit(ctx.if_block) if ctx.if_block else ""
        code = f"{INDENT}if ({condition}) {{\n{if_body}{INDENT}}}\n"
        if ctx.ELSE():
            if ctx.else_if:
                code += f"{INDENT}else {self.visit(ctx.else_if)}"
            elif ctx.else_block:
                else_body = self.visit(ctx.else_block)
                code += f"{INDENT}else {{\n{else_body}{INDENT}}}\n"
        return code

    def visitIfBlock(self, ctx: ChronoParser.IfBlockContext):
        self._enter_scope()
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        return body_code

    def visitElseBlock(self, ctx: ChronoParser.ElseBlockContext):
        self._enter_scope()
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        return body_code

    def visitWhileStatement(self, ctx: ChronoParser.WhileStatementContext):
        condition = self.visit(ctx.expression())
        self._enter_scope()
        body_statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in body_statements)
        self._exit_scope()
        code = f"{INDENT}while ({condition}) {{\n"
        code += body_code
        code += f"{INDENT}}}\n"
        return code

    def visitExpression(self, ctx: ChronoParser.ExpressionContext):
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

    def visitUnaryExpression(self, ctx: ChronoParser.UnaryExpressionContext):
        if ctx.simpleExpression():
            return self.visit(ctx.simpleExpression())
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

    def visitDeleteStatement(self, ctx: ChronoParser.DeleteStatementContext):
        target = self.visit(ctx.expression())
        return f"{INDENT}delete {target};\n"

    def visitAssignablePrimary(self, ctx: ChronoParser.AssignablePrimaryContext):
        if ctx.IDENTIFIER():
            primary_text = ctx.IDENTIFIER().getText()
            variable_info = self._find_variable(primary_text)
            if variable_info:
                if '[' in variable_info["cpp_type"]:
                    return primary_text
                else:
                    return variable_info["cpp_name"]  # [修复] 移除了 '_'
            else:
                return self._chrono_to_cpp_type(primary_text)
        if ctx.THIS():
            return "this"
        if ctx.STAR():
            return f"(*{self.visit(ctx.assignablePrimary())})"
        if ctx.BIT_AND():
            return f"(&{self.visit(ctx.assignablePrimary())})"
        if ctx.LPAREN():
            return f"({self.visit(ctx.assignableExpression())})"
        return ""

    def visitExpressionList(self, ctx: ChronoParser.ExpressionListContext):
        return ", ".join(self.visit(e) for e in ctx.expression())

    def visitLiteral(self, ctx: ChronoParser.LiteralContext):
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

    def visitAssignment_no_semicolon(self, ctx: ChronoParser.Assignment_no_semicolonContext):
        target = self.visit(ctx.assignableExpression())
        value = self.visit(ctx.expression())
        op_str = self.visit(ctx.assignmentOperator())
        return f"{target} {op_str} {value}"

    def visitStructBodyStatement(self, ctx: ChronoParser.StructBodyStatementContext):
        # struct 成员默认是 public
        access = self._get_access_level(ctx, default_level='public')

        if ctx.variableDeclaration():
            ctx.variableDeclaration()._chrono_access = access
            # (Structs 在 C++ 中通常不支持 static 成员变量)
            ctx.variableDeclaration()._chrono_static = False
            return self.visit(ctx.variableDeclaration())


        # 不再查找 ...Definition，而是查找 ...Signature
        elif ctx.functionSignature():
            ctx.functionSignature()._chrono_access = access
            ctx.functionSignature()._chrono_static = False  # Structs 不支持 static 方法
            return self.visit(ctx.functionSignature())

        elif ctx.initSignature():
            ctx.initSignature()._chrono_access = access
            return self.visit(ctx.initSignature())

        elif ctx.deinitSignature():
            ctx.deinitSignature()._chrono_access = 'public'
            return self.visit(ctx.deinitSignature())

        elif ctx.cppBlock():
            return self.visit(ctx.cppBlock())

        # elif ctx.rawCppDirective():
        #     return self.visit(ctx.rawCppDirective())

        return ""

    def visitStructDefinition(self, ctx: ChronoParser.StructDefinitionContext):
        struct_name = ctx.name.text
        # [ [ [ 修复 B-2: 添加 struct 的成员字典重置 ] ] ]
        self._current_class_members = {}
        self._in_class = False
        self._in_struct = True
        self._current_class_name = struct_name
        self._class_sections = {"private": "", "public": ""}
        if hasattr(ctx, 'structBodyStatement'):
            for child in ctx.structBodyStatement():
                self.visit(child)
        self._in_struct = False
        self._current_class_name = None
        # [ [ [ 修复 B-2: 添加 struct 的成员字典重置 ] ] ]
        self._current_class_members = {}
        final_struct_body = ""
        if self._class_sections["public"]:
            final_struct_body += "\npublic:\n"
            final_struct_body += self._class_sections["public"]
        if self._class_sections["private"]:
            final_struct_body += "\nprivate:\n"
            final_struct_body += self._class_sections["private"]
        return (
            f"\nstruct {struct_name} {{\n"
            f"{final_struct_body.strip()}\n"
            f"}};\n"
        )

    def visitVariableDeclaration(self, ctx: ChronoParser.VariableDeclarationContext):
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

    def visitVariableDeclaration_no_semicolon(self, ctx: ChronoParser.VariableDeclaration_no_semicolonContext):
        core_cpp, _, _, _, _ = self._translate_variable_declaration(ctx)
        return core_cpp

    def visitBlockStatement(self, ctx: ChronoParser.BlockStatementContext):
        self._enter_scope()
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        final_code = f"{INDENT}{{\n"
        final_code += body_code
        final_code += f"{INDENT}}}\n"
        return final_code

    def visitSwitchStatement(self, ctx: ChronoParser.SwitchStatementContext):
        """
        [新增] 访问 'switchStatement' 规则
        e.g., switch (val) { ... }
        """

        # 1. 翻译 switch (expr)
        expr = self.visit(ctx.expression())

        # 2. 翻译所有 case 块
        case_code = "".join(self.visit(cb) for cb in ctx.caseBlock())

        # 3. 翻译可选的 default 块
        default_code = self.visit(ctx.defaultBlock()) if ctx.defaultBlock() else ""

        # 4. 组装 C++
        code = f"{INDENT}switch ({expr}) {{\n"
        code += case_code
        code += default_code
        code += f"{INDENT}}}\n"
        return code

    def visitCaseBlock(self, ctx: ChronoParser.CaseBlockContext):
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

    def visitDefaultBlock(self, ctx: ChronoParser.DefaultBlockContext):
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
            if isinstance(statements[-1], ChronoParser.ReturnStatementContext):
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

        if node.getSymbol().type == ChronoParser.CPP_DIRECTIVE:
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

    def visitForwardDeclaration(self, ctx: ChronoParser.ForwardDeclarationContext):
        # 1. 获取名字
        name = ctx.name.text

        # 2. 获取种类 (class 或 struct)
        kind_keyword = ""
        if ctx.kind.type == ChronoParser.CLASS:
            kind_keyword = "class"
        elif ctx.kind.type == ChronoParser.STRUCT:
            kind_keyword = "struct"

        # 3. 生成 C++ 代码 (struct Child;)
        line_comment = f"\n// Line {ctx.start.line} (forward decl)\n"
        return f"{line_comment}{kind_keyword} {name};\n"

    # src/ChronoVisitor.py

    def visitEnumDefinition(self, ctx: ChronoParser.EnumDefinitionContext):
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

    def visitEnumItem(self, ctx: ChronoParser.EnumItemContext):
        name = ctx.name.text
        if ctx.expression():
            val = self.visit(ctx.expression())
            return f"{name} = {val}"
        return name
