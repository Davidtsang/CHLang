# src/ChronoVisitor.py
import os
from antlr4 import *

from parser.ChronoParser import ChronoParser
from parser.ChronoParserVisitor import ChronoParserVisitor as BaseChronoVisitor
from antlr4.tree.Tree import TerminalNodeImpl  # 导入 TerminalNodeImpl

INDENT = "    "


class ChronoVisitor(BaseChronoVisitor):

    def __init__(self):
        super().__init__()

        # [ [ [ 恢复为简单状态 ] ] ]
        # (我们回到了您最初  的简单 Visitor)
        self._in_class_method = False
        self._in_class = False
        self._in_struct = False
        self._current_class_name = None
        self._class_sections = {"private": "", "public": ""}
        self._alias_to_namespace_map = {}
        self._literal_alias_map = {}
        self._scope_stack = [{}]

        # [ [ [ 新增 ] ] ]
        # 这个新状态用于跟踪我们是否在 'implement' 块中
        self._in_implementation_block = False
        self._current_namespace_str = ""  # 用于 C++ 作用域

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
        [最终方案]
        1. (typeList?) -> R 语法总是先被构建为 std::function。
        2. 如果 (1) 的后缀是 '*'，则将其转换为 C-Style 指针模式。
        3. 括号 () 语法 (Path D) 被正确处理。
        4. [重要] 此规则 *不* 接受 STRING_LITERAL (保持纯净)
        """

        core_type = ""
        is_function_type = False  # 标志位

        # 收集后缀
        suffixes = self._collect_suffixes(ctx)

        # --- 路径 A: C-Style 数组 ---
        if ctx.LBRACK() and ctx.SEMIC_TOKEN():
            base = self.visit(ctx.typeSpecifier())
            size_expr = self.visit(ctx.expression())
            core_type = f"{base};[{size_expr}]"

        # --- [ [ [ 路径 C/D (LPAREN) ] ] ] ---
        elif ctx.LPAREN() and ctx.RPAREN():

            # 选项 1: 这是一个函数类型 (Path C)
            if ctx.ARROW():
                is_function_type = True  # 标记
                params_str = self.visit(ctx.params) if ctx.params else ""
                return_str = self.visit(ctx.returnType)
                core_type = f"std::function<{return_str}({params_str})>"

            # 选项 2: 这是一个带括号的类型 (Path D)
            elif ctx.nested:
                core_type = self.visit(ctx.nested)
                if core_type.startswith("std::function<"):
                    is_function_type = True

            else:
                core_type = ""  # 不太可能

        # --- 路径 B: 基础/泛型类型 ---
        elif ctx.baseType():
            base = self.visit(ctx.baseType())
            if ctx.typeList():
                args = self.visit(ctx.typeList())
                core_type = f"{base}<{args}>"
            else:
                core_type = base

        else:
            return ""  # 兜底

        # --- [ [ [ 最终处理：C-Style 转换和后缀组合 ] ] ] ---
        if suffixes and suffixes[0].getText() == '*' and is_function_type:
            # --- 是 C-Style 函数指针 ---
            func_sig = core_type[len("std::function<"):-1]
            parts = func_sig.split('(', 1)
            return_str = parts[0].strip()
            params_str = parts[1].rsplit(')', 1)[0].strip()

            remaining_suffixes = suffixes[1:]
            remaining_suffix_str = "".join(s.getText() for s in remaining_suffixes)

            # 返回 C-Style 模式
            return f"{return_str} (*{{NAME}})({params_str}){remaining_suffix_str}"

        # --- 不是 C-Style 函数指针 ---
        suffix_str = "".join(s.getText() for s in suffixes)

        if (ctx.LPAREN() and ctx.nested):
            core_type = f"({core_type})"

        return f"{core_type}{suffix_str}"

    def visitBaseType(self, ctx: ChronoParser.BaseTypeContext):
        """
        [重构]
        [ [ [ 关键修复 ] ] ]
        确保此方法优先检查 'self._literal_alias_map'
        """
        raw_text = ctx.getText()  # (例如 "C_INT_WINAPI", "std.string", "i32")

        # 步骤 1: 检查 'typemap' 字面量代换
        if raw_text in self._literal_alias_map:
            # [修复] 必须返回此字典中的值
            return self._literal_alias_map[raw_text]

        # --- (以下是现有逻辑) ---
        parts = raw_text.split('.')
        first_part = parts[0]
        if first_part in self._alias_to_namespace_map:
            parts[0] = self._alias_to_namespace_map[first_part]

        cpp_namespace_type = "::".join(parts)
        return self._chrono_to_cpp_type(cpp_namespace_type)

    def visitNamespaceStatement(self, ctx: ChronoParser.NamespaceStatementContext):
        namespace_name = ctx.name.text
        cpp_namespace = namespace_name.replace('.', '::')
        self._current_namespace_str = cpp_namespace + "::"

        # 1:1 翻译
        open_block = f"namespace {namespace_name.replace('.', ' { namespace ')} {{\n\n"
        # (我们必须在 visitProgram 中添加闭合 '}' )
        return open_block

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
        self._in_class_method = True
        self._enter_scope()

        # [ [ [ 关键修正：'this' 始终是 '->' ] ] ]
        accessor = "->"
        cpp_type = f"{self._current_class_name}*"
        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,
            "cpp_type": cpp_type
        })

        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))
        return_type = self.visit(ctx.returnType) if ctx.returnType else "void"

        # [ [ [ 检查 'implement' 块 ] ] ]
        if self._in_implementation_block:
            cpp_func_name = f"{self._current_namespace_str}{self._current_class_name}::{func_name}"
            static_prefix = ""  # C++ .cpp 实现不重复 'static'

            func_def_code = (
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
                f"\n{INDENT}{virtual_prefix}{static_prefix}{return_type} {cpp_func_name}({params_code}) {{\n"
                f"{body_code}"
                f"{INDENT}// --- Method End ---\n"
                f"{INDENT}}}\n"
            )
            self._class_sections[access] += func_def_code

        self._exit_scope()
        self._in_class_method = False

        return func_def_code if self._in_implementation_block else ""

    def visitFunctionDefinition(self, ctx: ChronoParser.FunctionDefinitionContext):
        # 这是一个全局函数 (不在类中或 implement 块中)
        self._enter_scope()

        func_name = ctx.name.text

        # [ [ [ 关键修复 ] ] ]
        # 正确处理命名空间 (如果存在)
        cpp_func_name = f"{self._current_namespace_str}{func_name}"

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
            f"\n{static_prefix}{return_type} {cpp_func_name}({params_code}) {{\n"
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
        [重构]
        [最终方案] 识别 C-Style 函数指针模式 '(*{NAME})'。
                 [ [ 关键 ] ] 移除了 '_' 前缀。
                 修复了 'nullptr' 初始化逻辑。
        """

        # --- 1. 确定 Const / Var ---
        is_const = bool(ctx.CONST())
        const_prefix = "const " if is_const else ""

        # --- 2. 确定名称 ---
        var_name = ctx.name.text
        key = var_name
        cpp_name = var_name  # [ [ 关键 ] ] 始终使用原始名称

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
        is_c_array = False

        is_c_style_func_ptr = "(*{NAME})" in cpp_final_type

        if base_type_cpp != "auto":
            if base_type_cpp.endswith('*') or \
                    base_type_cpp.startswith("std::unique_ptr") or \
                    base_type_cpp.startswith("std::shared_ptr") or \
                    base_type_cpp.startswith("std::weak_ptr") or \
                    is_c_style_func_ptr:
                is_pointer = True

            is_reference = base_type_cpp.endswith('&')

            if not is_pointer and not is_reference and ';[' in base_type_cpp:
                is_c_array = True

        # --- 6. 组合数组类型 ---
        cpp_name_for_declaration = cpp_name
        cpp_name_for_scope = cpp_name

        if is_c_array:
            parts = cpp_final_type.split(';')
            base_only = parts[0]
            dim_parts = parts[1:]
            dim_parts.reverse()
            dims_str = "".join(dim_parts)

            cpp_final_type = base_only
            cpp_name_for_declaration = f"{cpp_name}{dims_str}"

        # --- 7. 确定访问器 ---
        accessor = "."

        if is_c_array:
            accessor = "."
        elif is_c_style_func_ptr:
            accessor = "."
        elif is_pointer:
            accessor = "->"

        # [ auto 推导逻辑 ]
        if base_type_cpp == "auto" and ctx.expression():
            primary_node = None
            try:
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
                accessor = "->"

        # --- 8. [ [ [ 关键 ] ] ] 移除了 '_' 前缀逻辑 ---

        # --- 9. 注册到作用域栈 ---
        self._add_variable(key, {
            "cpp_name": cpp_name_for_scope,  # 始终使用原始名称
            "accessor": accessor,
            "cpp_type": base_type_cpp
        })

        # --- 10. 确定赋值 ---
        cpp_value = ""
        if ctx.expression():
            cpp_value = f" = {self.visit(ctx.expression())}"
        elif is_pointer and base_type_cpp != "auto":

            # [关键修复] 确保智能指针不被错误地赋予 '= nullptr'
            if not (base_type_cpp.startswith("std::unique_ptr") or
                    base_type_cpp.startswith("std::shared_ptr") or
                    base_type_cpp.startswith("std::weak_ptr")):
                # C-Style Ptr, MRC Ptr 等, 都会被初始化为 nullptr
                cpp_value = " = nullptr"

        # --- 11. 确定是局部还是成员 ---
        is_member_variable = (self._in_class or self._in_struct) and not self._in_class_method
        access = getattr(ctx, '_chrono_access', 'private')

        # --- 12. 返回 C++ 代码片段 ---
        core_cpp = ""

        if is_c_style_func_ptr:
            # 特殊 C-Style 格式化
            cpp_type_with_name = cpp_final_type.replace("(*{NAME})", f"(*{cpp_name_for_declaration})")
            core_cpp = f"{const_prefix}{cpp_type_with_name}{cpp_value}"
        else:
            # 标准格式化
            core_cpp = f"{const_prefix}{cpp_final_type} {cpp_name_for_declaration}{cpp_value}"

        return (core_cpp, is_member_variable, access, cpp_final_type, cpp_name_for_scope)

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
        if chrono_type_name == "int" or chrono_type_name == "i32":
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
        # (调用  中的 visitProgram 逻辑)
        all_code = ""
        for child in ctx.children:
            if not isinstance(child, TerminalNodeImpl):
                all_code += self.visit(child)

        # 添加命名空间闭合符
        if self._current_namespace_str:
            all_code += f"\n}} // namespace {self._current_namespace_str.replace('::', '.')[:-1]}\n"

        return all_code

    def visitImportDirective(self, ctx: ChronoParser.ImportDirectiveContext):
        path_text = ctx.path.text

        base_name = os.path.basename(path_text.strip('\"<>'))
        true_namespace, _ = os.path.splitext(base_name)

        if ctx.alias:
            alias_name = ctx.alias.text
        else:
            alias_name = true_namespace
        if alias_name and true_namespace:
            self._alias_to_namespace_map[alias_name] = true_namespace
        if path_text.startswith('<'):
            return f"#include {path_text}\n"
        elif path_text.startswith('\"'):
            path_content = path_text[1:-1]
            if path_content.startswith('runtime/'):
                path_content = path_content.replace('runtime/', '')
            return f'#include "{path_content}"\n'
        return f"// ERROR: Invalid import path {path_text}\n"

    def visitUsingAlias(self, ctx: ChronoParser.UsingAliasContext):
        """
        [还原] 访问 'usingAlias' 规则。
        这 *只* 处理类型安全的别名，并 *总是* 生成 C++ 'using'。
        """
        name = ctx.name.text
        cpp_type_pattern = self.visit(ctx.typeName)
        cpp_type = ""
        if "(*{NAME})" in cpp_type_pattern:
            cpp_type = cpp_type_pattern.replace("(*{NAME})", "(*)")
        else:
            cpp_type = cpp_type_pattern
        return f"using {name} = {cpp_type};\n"

    # [ [ [ 新增 ] ] ]
    def visitTypemapDefinition(self, ctx: ChronoParser.TypemapDefinitionContext):
        """
        [新增] 访问 'typemap' 规则。
        e.g., typemap C_INT_WINAPI : i32 = "int WINAPI";

        这 *不* 会生成 C++ 代码，而是将 "C_INT_WINAPI" -> "int WINAPI"
        注册到翻译器的内部代换映射 (_literal_alias_map) 中。

        ': i32' (ctx.hint) 部分被翻译器完全忽略。
        """
        name = ctx.name.text
        value = ctx.value.text[1:-1]  # [修复] 使用 .text
        self._literal_alias_map[name] = value
        return ""
        # [ [ [ 新增结束 ] ] ]

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

            decl = f"{INDENT}{virtual_prefix}{static_prefix}{return_type} {func_name}({params_code});\n"
            self._class_sections[access] += decl
            return ""
        else:
            # 全局函数签名 (不在类中)
            is_static = bool(ctx.STATIC())  # <--- [修正] 全局函数签名也需要正确检查
            static_prefix = "static " if is_static else ""
            return f"\n{static_prefix}{return_type} {self._current_namespace_str}{func_name}({params_code});\n"

    def visitInitSignature(self, ctx: ChronoParser.InitSignatureContext):

        default_access = 'public' if self._in_struct else 'private'
        access = getattr(ctx, '_chrono_access', default_access)

        func_name = self._current_class_name
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        decl = f"{INDENT}{func_name}({params_code});\n"
        self._class_sections[access] += decl
        return ""

    def visitDeinitSignature(self, ctx: ChronoParser.DeinitSignatureContext):
        access = "public"  # Deinit 总是 public
        func_name = f"~{self._current_class_name}"

        decl = f"{INDENT}virtual {func_name}();\n"
        self._class_sections[access] += decl
        return ""

    def visitClassDefinition(self, ctx: ChronoParser.ClassDefinitionContext):
        # (调用  中的 visitClassDefinition 逻辑)
        # (它会访问 classBodyStatement，后者会填充 _class_sections)
        # (然后它会组装 C++ 类声明)

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
        if self._class_sections["private"]:
            final_class_body += "\nprivate:\n" + self._class_sections["private"]
        if self._class_sections["public"]:
            final_class_body += "\npublic:\n" + self._class_sections["public"]

        return (
            f"\nclass {self._current_namespace_str}{class_name}{inheritance_str} {{\n"
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
        self._in_class_method = True
        self._enter_scope()

        # [ [ [ 关键修正：'this' 始终是 '->' ] ] ]
        accessor = "->"
        cpp_type = f"{self._current_class_name}*"
        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,
            "cpp_type": cpp_type
        })

        cpp_func_name = self._current_class_name

        # [ [ [ 检查 'implement' 块 ] ] ]
        if self._in_implementation_block:
            cpp_func_name = f"{self._current_namespace_str}{self._current_class_name}::{self._current_class_name}"
        else:
            access = getattr(ctx, '_chrono_access', 'private')
            if self._in_struct:
                access = getattr(ctx, '_chrono_access', 'public')

        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))

        init_code = (
            f"\n{INDENT if not self._in_implementation_block else ''}"
            f"{cpp_func_name}({params_code}) {{\n"
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

        # 步骤 1: 检查 'typemap' 字面量代换
        if raw_primary_text in self._literal_alias_map:
            # 这是一个原始文本代换 (e.g., "COLOR_WINDOW")
            # 它没有访问器，所以我们返回它自己，accessor 为 "."
            return self._literal_alias_map[raw_primary_text], ".", "literal"

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
        i += 1
        if i >= len(child_nodes):
            return current_code, i, current_accessor, current_type
        ident_node = child_nodes[i]
        i += 1
        raw_ident_text = ident_node.getText()
        member_info = self._find_variable(raw_ident_text)
        if member_info:
            cpp_ident = member_info["cpp_name"]
        else:
            cpp_ident = raw_ident_text
        accessor_to_use = "."
        if access_token_type == ChronoParser.DOT:
            accessor_to_use = current_accessor
        elif access_token_type == ChronoParser.ARROW:
            accessor_to_use = "."
        template_args_str = ""
        if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.LBRACK:
            i += 1
            if i < len(child_nodes) and isinstance(child_nodes[i], ChronoParser.TypeListContext):
                template_args_str = self.visit(child_nodes[i])
                i += 1
            if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.RBRACK:
                i += 1
        if template_args_str:
            cpp_ident = f"{cpp_ident}<{template_args_str}>"
        if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.LPAREN:
            i += 1
            args = ""
            if i < len(child_nodes) and isinstance(child_nodes[i], ChronoParser.ExpressionListContext):
                args = self.visit(child_nodes[i])
                i += 1
            if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.RPAREN:
                i += 1
            new_code = f"{current_code}{accessor_to_use}{cpp_ident}({args})"
        else:
            new_code = f"{current_code}{accessor_to_use}{cpp_ident}"
        new_accessor = "->"
        if cpp_ident and cpp_ident[0].isupper():
            new_accessor = "::"
        return new_code, i, new_accessor, "unknown"

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
        self._in_class_method = True
        self._enter_scope()

        # [ [ [ 关键修正：'this' 始终是 '->' ] ] ]
        accessor = "->"
        cpp_type = f"{self._current_class_name}*"
        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,
            "cpp_type": cpp_type
        })

        cpp_func_name = f"~{self._current_class_name}"
        body_code = "".join(self.visit(s) for s in self._safe_iterate_statements(ctx.statement()))

        # [ [ [ 检查 'implement' 块 ] ] ]
        if self._in_implementation_block:
            cpp_func_name = f"{self._current_namespace_str}{self._current_class_name}::{cpp_func_name}"
            deinit_code = (
                f"\n{cpp_func_name}() {{\n"
                f"{INDENT}// --- Chrono Deinit Block ---\n"
                f"{body_code}"
                f"{INDENT}// --- Deinit End ---\n"
                f"{INDENT}}}\n"
            )
        else:
            access = "public"  # Deinit 总是 public
            deinit_code = (
                f"\n{INDENT}virtual {cpp_func_name}() {{\n"
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
        """
        [重构]
        [ [ [ 关键修复 ] ] ]
        不再调用 primary_ctx.getText()。
        而是将 'translated_primary' 同时用作 "raw_text" 和 "translated_code"
        传递给 _determine_initial_accessor。
        """

        # 1. 确定初始部分
        translated_primary = ""

        if ctx.primary():
            primary_ctx = ctx.primary()
            # [修复] 这是唯一一次我们调用 visit(primary)
            translated_primary = self.visit(primary_ctx)
            # [修复] 删除了 'raw_primary_text = primary_ctx.getText()'

        elif ctx.functionCallExpression():
            translated_primary = self.visit(ctx.functionCallExpression())
        else:
            return ""

        # 2. 确定初始访问器 (和类型)
        # [ [ [ 关键修复 ] ] ]
        # 我们现在将 "已翻译的" 值 (e.g., "COLOR_WINDOW")
        # 作为 'raw_primary_text' 传递，以便 _determine_initial_accessor
        # (即使是旧版本) 也能正确处理它。
        # (我们新的 _determine_initial_accessor 也会正确处理它)
        current_code, current_accessor, current_type = self._determine_initial_accessor(
            translated_primary, translated_primary
        )

        # 3. 遍历链条 (此逻辑不变)
        child_nodes = ctx.children[1:]
        i = 0
        while i < len(child_nodes):
            token_type = child_nodes[i].getSymbol().type
            if token_type == ChronoParser.DOT:
                current_code, i, current_accessor, current_type = self._process_dot_chain_step(
                    child_nodes, i, current_code, current_accessor, current_type, ChronoParser.DOT
                )
            elif token_type == ChronoParser.LBRACK:
                current_code, i, current_accessor = self._process_array_chain_step(
                    child_nodes, i, current_code, current_accessor
                )
                current_type = "unknown"
            elif token_type == ChronoParser.ARROW:
                current_code, i, current_accessor, current_type = self._process_dot_chain_step(
                    child_nodes, i, current_code, current_accessor, current_type, ChronoParser.ARROW
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

        if ctx.LBRACK():  # 检查是否是 'func[Type](args)' 结构

            # 1. 确定 C++ 中的函数名
            cpp_func_name = ""
            if ctx.AT_MAKE_UNIQUE():
                cpp_func_name = "std::make_unique"
            elif ctx.AT_MAKE_SHARED():
                cpp_func_name = "std::make_shared"
            elif ctx.STATIC_CAST():
                cpp_func_name = "static_cast"
                print(ctx.expressionList())


            elif ctx.REINTERPRET_CAST():
                cpp_func_name = "reinterpret_cast"
            elif ctx.CONST_CAST():
                cpp_func_name = "const_cast"

            # 2. 访问 Chrono 的 [Type] (e.g., "C_HBRUSH")
            target_type = self.visit(ctx.typeSpecifier())

            # 3. 访问 Chrono 的 (args) (e.g., "C_COLOR_WINDOW + 1")

            args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""

            # 4. 组装 *C++* 语法 (使用 C++ 的 <...>)
            return f"{cpp_func_name}<{target_type}>({args})"

        # [ [ [ 转换逻辑结束 ] ] ]

        if ctx.literal():
            return self.visit(ctx.literal())

        if ctx.initializerList():
            return self.visit(ctx.initializerList())

        if ctx.IDENTIFIER():
            primary_text = ctx.IDENTIFIER().getText()
            variable_info = self._find_variable(primary_text)

            # [ [ [ 关键修复：C_COLOR_WINDOW 问题的修复点 ] ] ]
            #
            # 如果 'IDENTIFIER' 不是一个已知变量 (e.g., "myVar")
            if not variable_info:
                # 检查它是否是 'typemap' 定义的常量 (e.g., "C_COLOR_WINDOW")

                if primary_text in self._literal_alias_map:
                    # print("im here!")
                    val_ = self._literal_alias_map[primary_text]
                    return val_
            # [ [ [ 修复结束 ] ] ]

            if variable_info:
                # [修复] 移除了旧的 .lstrip('$') 逻辑
                if '[' in variable_info["cpp_type"]:
                    return primary_text  # 数组
                return variable_info["cpp_name"]
            else:
                # 最后的兜底
                return primary_text

        if ctx.THIS():
            return "this"

        if ctx.LPAREN():
            return f"({self.visit(ctx.expression())})"

        return ""

    # [ [ [ 替换结束 ] ] ]

    def visitParameters(self, ctx: ChronoParser.ParametersContext):
        params_list = []
        for p in ctx.parameter():
            params_list.append(self.visit(p))
        return ", ".join(params_list)

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
            expr_code = self.visit(ctx.expression())
            return f"{INDENT}{expr_code};\n"
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
        if ctx.expression():  # [修复] return 可以是空的
            return_value = self.visit(ctx.expression())
            return f"{INDENT}return {return_value};\n"
        return f"{INDENT}return;\n"  # 空 return

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
        target = self.visit(ctx.assignableExpression())
        value = self.visit(ctx.expression())
        op_str = self.visit(ctx.assignmentOperator())
        return f"{INDENT}{target} {op_str} {value};\n"

    def visitAssignableExpression(self, ctx: ChronoParser.AssignableExpressionContext):
        primary_ctx = ctx.assignablePrimary()
        current_code = self.visit(primary_ctx)
        base_ident_text = None
        temp_node = primary_ctx
        while True:
            if temp_node.IDENTIFIER():
                base_ident_text = temp_node.IDENTIFIER().getText()
                break
            if temp_node.THIS():
                base_ident_text = "this"
                break
            if hasattr(temp_node, 'assignablePrimary') and temp_node.assignablePrimary():
                temp_node = temp_node.assignablePrimary()
            elif hasattr(temp_node, 'assignableExpression') and temp_node.assignableExpression():
                temp_node = temp_node.assignableExpression().assignablePrimary()
            else:
                break
        current_accessor = "."
        current_type = "value"
        if base_ident_text:
            variable_info = self._find_variable(base_ident_text)
            if variable_info:
                current_type = variable_info["cpp_type"]
                current_accessor = variable_info["accessor"]
            elif base_ident_text == "std" or base_ident_text in self._alias_to_namespace_map:
                current_accessor = "::"
                current_type = "namespace"
        child_nodes = ctx.children[1:]
        i = 0
        while i < len(child_nodes):
            token_type = child_nodes[i].getSymbol().type
            accessor_to_use = current_accessor
            if token_type == ChronoParser.DOT:
                accessor_to_use = current_accessor
            elif token_type == ChronoParser.ARROW:
                accessor_to_use = "."
            if token_type == ChronoParser.DOT or token_type == ChronoParser.ARROW:
                i += 1
                ident_node = child_nodes[i]
                i += 1
                raw_ident_text = ident_node.getText()
                member_info = self._find_variable(raw_ident_text)
                if member_info:
                    cpp_ident = member_info["cpp_name"]
                else:
                    cpp_ident = raw_ident_text
                current_code = f"{current_code}{accessor_to_use}{cpp_ident}"
                current_accessor = "->"
                if cpp_ident and cpp_ident[0].isupper():
                    current_accessor = "::"
                current_type = "unknown"
            elif token_type == ChronoParser.LBRACK:
                i += 1
                index_expr = self.visit(child_nodes[i])
                i += 2
                current_code = f"{current_code}[{index_expr}]"
                pass
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
        self._in_class = False
        self._in_struct = True
        self._current_class_name = struct_name
        self._class_sections = {"private": "", "public": ""}
        if hasattr(ctx, 'structBodyStatement'):
            for child in ctx.structBodyStatement():
                self.visit(child)
        self._in_struct = False
        self._current_class_name = None
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
        core_cpp, is_member_variable, access, cpp_final_type, cpp_name = self._translate_variable_declaration(ctx)
        if is_member_variable:
            declaration_line = f"{INDENT}{core_cpp};\n"
            self._class_sections[access] += declaration_line
            return ""
        else:
            return f"{INDENT}{core_cpp};\n"

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
