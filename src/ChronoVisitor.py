# src/ChronoVisitor.py
import os
from antlr4 import *

from parser.ChronoParser import ChronoParser
from parser.ChronoParserVisitor import ChronoParserVisitor as BaseChronoVisitor
from antlr4.tree.Tree import TerminalNodeImpl  # 导入 TerminalNodeImpl

INDENT = "    "


class ChronoVisitor(BaseChronoVisitor):

    # [ 替换 ] __init__
    def __init__(self):
        super().__init__()
        self._in_class_method = False
        self._in_class = False
        self._in_struct = False  # <-- [新增]
        self._current_class_name = None
        self._class_sections = {"private": "", "public": ""}
        self._alias_to_namespace_map = {}

        # [ [ 2. 新增：我们的“作用域栈” ] ]
        # 这是一个字典的列表。
        # 栈顶 (self._scope_stack[-1]) 代表当前作用域。
        # 字典格式: { "var_name_in_chrono": { "accessor": "->", "cpp_name": "_var" } }
        self._scope_stack = [{}]  # 初始化一个“全局作用域”

    def visitTypeSpecifier(self, ctx: ChronoParser.TypeSpecifierContext):
        """
        [重构] 访问 'typeSpecifier' 规则。
        [最终方案]
        1. (typeList?) -> R 语法总是先被构建为 std::function。
        2. 如果 (1) 的后缀是 '*'，则将其转换为 C-Style 指针模式。
        3. 括号 () 语法 (Path D) 被正确处理。
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

                # [ [ [ 关键变更 ] ] ]
                # 我们现在访问 'params' (一个 typeList 节点)
                # 'visitTypeList' 返回一个 "i32, std::string" 字符串
                params_str = self.visit(ctx.params) if ctx.params else ""
                return_str = self.visit(ctx.returnType)

                # 总是先构建 std::function
                core_type = f"std::function<{return_str}({params_str})>"

            # 选项 2: 这是一个带括号的类型 (Path D)
            elif ctx.nested:
                core_type = self.visit(ctx.nested)
                # 检查内层类型是否是函数
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

        # 检查是否需要 C-Style 转换
        if suffixes and suffixes[0].getText() == '*' and is_function_type:
            # 它是一个指针 (*) 并且它附加到一个函数类型上

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
        [重构] 访问 'baseType' 规则。
        处理:
        1. 命名空间: "std.string" -> "std::string"
        2. 别名: "Math.Type" -> "MyMath::Type"
        3. 基础类型: "i32" -> "int32_t"

        [移除] 不再需要处理 $
        """
        raw_text = ctx.getText()  # (例如 "std.string", "String", "i32")

        parts = raw_text.split('.')
        first_part = parts[0]

        # 1. 检查别名
        if first_part in self._alias_to_namespace_map:
            parts[0] = self._alias_to_namespace_map[first_part]

        cpp_namespace_type = "::".join(parts)  # (例如 "std::string", "String")

        # 2. [关键简化]
        #    我们不再检查 $。
        #    我们只翻译基础类型 (i32 -> int32_t)
        return self._chrono_to_cpp_type(cpp_namespace_type)

    def visitMethodDefinition(self, ctx: ChronoParser.MethodDefinitionContext):
        self._in_class_method = True
        self._enter_scope()

        # 'this' 永远是一个指针, 无论在 class 还是 struct 中
        accessor = "->"
        cpp_type = f"{self._current_class_name}*"

        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,
            "cpp_type": cpp_type
        })

        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        is_static = getattr(ctx, '_chrono_static', False)
        access = getattr(ctx, '_chrono_access', 'private')

        if ctx.returnType:
            cpp_return_type = self.visit(ctx.returnType)
            cpp_func_name = func_name
        else:
            cpp_return_type = "void"
            cpp_func_name = func_name

        static_prefix = "static " if is_static else ""

        func_def_code = (
            f"\n{INDENT}{static_prefix}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            f"{INDENT}// --- Method End ---\n"
            # [ [ 关键修复 ] ]
            # 之前是: f"{INDENT}}}}\n" (4个括号, 错误地输出 '}}')
            # 或者是 (如你的日志所示) 3个括号 (语法错误)
            # 正确的: f"{INDENT}}}\n" (2个括号, 输出 '}')
            f"{INDENT}}}\n"
        )

        self._class_sections[access] += func_def_code

        self._exit_scope()
        self._in_class_method = False
        return ""

    def visitFunctionDefinition(self, ctx: ChronoParser.FunctionDefinitionContext):
        self._enter_scope()

        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        is_static = False
        if hasattr(ctx, 'STATIC') and ctx.STATIC():
            is_static = True

        if ctx.returnType:
            cpp_return_type = self.visit(ctx.returnType)

            if func_name == "main":  # 'main' 必须返回 'int'
                cpp_return_type = "int"
                cpp_func_name = "main"
            else:
                cpp_func_name = func_name
        else:
            cpp_return_type = "void"
            cpp_func_name = func_name

        static_prefix = "static " if is_static else ""
        self._exit_scope()
        return (
            f"\n{static_prefix}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            # [ [ 关键修复 ] ]
            # 之前可能是 f"}}\n" (2个括号, 输出 '}')
            # (这个之前可能是对的，但为了保持一致性，我们确保它是 2 个)
            f"}}\n"
        )

    # [ [ 5. 替换 ] ]
    # 'visitParameter' 必须被完全重写，以使用类型信息
    #
    def visitParameter(self, ctx: ChronoParser.ParameterContext):
        """
        [重构] 访问 'parameter' 规则。
        e.g., (s: String*) or (count: i32) or (arr: [i32; 3])
        """

        # --- 1. 获取名称 (现在没有 $) ---
        var_name = ctx.name.text
        key = var_name
        cpp_name = var_name  # 默认 C++ 名称

        # --- 2. 获取 C++ 类型 ---
        # (e.g., "String*", "int32_t", "int32_t;[3]")
        base_type_cpp = self.visit(ctx.typeName)
        cpp_final_type = base_type_cpp  # 最终的 C++ 参数类型 (e.g., "String*" 或 "int32_t*")

        # --- 3. 确定是指针/引用/数组 ---
        is_pointer = base_type_cpp.endswith('*')
        is_reference = base_type_cpp.endswith('&')
        is_c_array = False  # (在参数中，数组会衰变为指针)

        # --- 4. 数组逻辑 (衰变为指针) ---
        if not is_pointer and not is_reference and ';[' in base_type_cpp:
            is_c_array = True
            parts = base_type_cpp.split(';')
            base_only = parts[0]
            # e.g., "int32_t" -> "int32_t*"
            cpp_final_type = f"{base_only}*"
            is_pointer = True  # 衰变的数组是 C++ 指针

        # --- 5. 决定访问器 (Accessor) ---
        accessor = "."  # 默认 (值类型, 引用类型)
        if is_c_array:
            accessor = "."  # 访问衰变的数组 (arr[0]) 仍然使用 .
        elif is_pointer:
            accessor = "->"  # C++ 指针
        # (引用 & 使用 .)

        # --- 6. [约定] 为指针添加 '_' 前缀 ---
        if is_pointer and not is_c_array:
            cpp_name = f"_{cpp_name}"

        # --- 7. 添加到作用域栈 ---
        self._add_variable(key, {
            "cpp_name": cpp_name,
            "accessor": accessor,  # "->" 或 "."
            "cpp_type": base_type_cpp  # e.g., "String*" 或 "int32_t"
        })

        # --- 8. 返回 C++ 参数字符串 ---
        # (e.g., "String* _s" or "int32_t count" or "int32_t* arr")
        return f"{cpp_final_type} {cpp_name}"

    # [ [ 6. 替换 ] ]
    # 'visitFunctionCallExpression' 必须移除 lstrip('$')
    #

    # [ [ 1. 替换 ] ]
    def visitFunctionCallExpression(self, ctx: ChronoParser.FunctionCallExpressionContext):
        """
        [重构] 新增对 @move 的翻译
        """
        # 1. 获取函数名 Token 和文本
        name_token = ctx.funcName  # 使用我们新的 funcName 标签

        if name_token.type == ChronoParser.AT_MOVE:
            cpp_func_name = "std::move"  # [新增] Chrono @move -> C++ std::move
        else:
            # [ [ 关键修复 ] ]
            # CommonToken 使用 .text, 而不是 .getText()
            cpp_func_name = name_token.text  # 默认 IDENTIFIER

        # (参数列表逻辑不变)
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
                 移除了 '_' 前缀。
                 修复了 'nullptr' 初始化逻辑 (包括拼写错误)。
        """

        # --- 1. 确定 Const / Var ---
        is_const = bool(ctx.CONST())
        const_prefix = "const " if is_const else ""

        # --- 2. 确定名称 ---
        var_name = ctx.name.text
        key = var_name
        cpp_name = var_name

        # --- 3. 确定类型 ---
        base_type_cpp = ""
        cpp_final_type = ""

        if ctx.typeName:
            base_type_cpp = self.visit(ctx.typeName)  # e.g., "std::function<...>" or "int (*{NAME})(...)"
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
                    is_c_style_func_ptr:  # C-Style 指针也是指针
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
        accessor = "."  # 默认

        if is_c_array:
            accessor = "."
        elif is_c_style_func_ptr:
            accessor = "."  # C-Style 指针调用是 p(..), 算作 "."
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

                # --- 9. 注册到作用域栈 ---
        self._add_variable(key, {
            "cpp_name": cpp_name_for_scope,
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

    def _collect_suffixes(self, ctx):
        """
        [新增辅助函数] 收集并按源代码顺序排序类型后缀 (* 和 &)。
        """
        suffixes = []
        if ctx.STAR():
            suffixes.extend(ctx.STAR())
        if ctx.BIT_AND():
            suffixes.extend(ctx.BIT_AND())

        # 按它们在源代码中出现的顺序排序
        suffixes.sort(key=lambda x: x.getSymbol().tokenIndex)
        return suffixes

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
        if token_type == ChronoParser.MODULO: return "%"  # <-- [新增]
        if token_type == ChronoParser.EQ: return "=="
        if token_type == ChronoParser.NEQ: return "!="
        if token_type == ChronoParser.LT: return "<"
        if token_type == ChronoParser.GT: return ">"
        if token_type == ChronoParser.LTE: return "<="
        if token_type == ChronoParser.GTE: return ">="
        if token_type == ChronoParser.AND_OP: return "&&"  # <-- [新增]
        if token_type == ChronoParser.OR_OP: return "||"  # <-- [新增]

        # [ [ 新增 ] ]
        if token_type == ChronoParser.BIT_AND: return "&"
        if token_type == ChronoParser.BIT_OR: return "|"
        if token_type == ChronoParser.BIT_XOR: return "^"
        if token_type == ChronoParser.LSHIFT: return "<<"
        if token_type == ChronoParser.RSHIFT: return ">>"

        raise Exception(f"Unknown operator token type: {token_type}")

    def _add_variable(self, chrono_name, metadata):
        """在*当前*作用域中定义一个新变量 (使用 Chrono 名字 $s 或 s 作为 Key)"""
        # metadata 示例: {"accessor": ".", "cpp_name": "s"}
        self._scope_stack[-1][chrono_name] = metadata

    def _find_variable(self, chrono_name):
        """从当前作用域开始，向外(全局)查找一个变量 (使用 Chrono 名字 $s 或 s)"""
        # 从后向前遍历 (LIFO)
        for scope in reversed(self._scope_stack):
            if chrono_name in scope:
                return scope[chrono_name]
        return None  # 未找到

    # --- [ 替换 _safe_process_statements_from_label ] ---
    def _safe_iterate_statements(self, statement_ctx_or_list):
        """
        [全局辅助函数]
        安全地处理 ANTLR 返回的:
        1. None (0 语句)
        2. 单个 StatementContext/TopLevelStatement 对象 (1 语句)
        3. 列表 (0 或 2+ 语句)
        """
        if not statement_ctx_or_list:
            return []  # Case 1: 0 语句, 返回空列表

        if isinstance(statement_ctx_or_list, list):
            return statement_ctx_or_list  # Case 3: 2+ 语句, 返回列表
        else:
            # Case 2: 1 语句, 包装成列表
            return [statement_ctx_or_list]

    # --- 辅助函数 ---
    def _chrono_to_cpp_type(self, chrono_type_name):
        """
        [重构] 新增智能指针关键字的翻译
        """
        if chrono_type_name == "bool":
            return "bool"

        # [ [ 新增 ] ] 智能指针关键字
        if chrono_type_name == "unique":
            return "std::unique_ptr"
        if chrono_type_name == "shared":
            return "std::shared_ptr"
        if chrono_type_name == "weak":
            return "std::weak_ptr"
        # [ [ 新增结束 ] ]

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
        # [修复] 检查 'ctx' 本身是否有 'accessModifier'
        if hasattr(ctx, 'accessModifier') and ctx.accessModifier():
            # 检查 accessModifier 规则的文本，我们假设只有 PUBLIC
            return "public"
        # [修复] 检查 'declaration' 或 'methodDefinition' (如果它们是父级)
        elif hasattr(ctx, 'declaration') and hasattr(ctx.variableDeclaration(),
                                                     'accessModifier') and ctx.variableDeclaration().accessModifier():
            return "public"
        elif hasattr(ctx, 'methodDefinition') and hasattr(ctx.methodDefinition(),
                                                          'accessModifier') and ctx.methodDefinition().accessModifier():
            return "public"

        return default_level  # <-- [修改] 返回 'private' 或 'public'

    # --- 顶层规则 ---
    def visitProgram(self, ctx: ChronoParser.ProgramContext):
        all_code = "".join(self.visit(stmt) for stmt in ctx.topLevelStatement())
        return all_code

        # (确保在 ChronoVisitor.py 顶部添加 'import os')

        # [ 替换 ] visitImportDirective

    def visitImportDirective(self, ctx: ChronoParser.ImportDirectiveContext):
        path_text = ctx.path.text

        # 1. [ 关键 ] 推断 C++ 真实命名空间 (基于文件名)
        # (这仍然是我们的“脆弱推断”，但现在它是正确的逻辑)
        base_name = os.path.basename(path_text.strip('\"<>'))
        true_namespace, _ = os.path.splitext(base_name)

        alias_name = ""

        # 2. 确定别名
        if ctx.alias:
            # 场景 A: 自定义别名 (import "MyMath.h" as Math)
            alias_name = ctx.alias.text
        else:
            # 场景 B: 自动别名 (import "MyMath.h")
            alias_name = true_namespace

        # 3. 注册映射：Chrono 别名 -> C++ 命名空间
        if alias_name and true_namespace:
            self._alias_to_namespace_map[alias_name] = true_namespace

        # 4. 翻译为 C++ #include (逻辑不变)
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
        [新增] 访问 'usingAlias' 规则。
        e.g., using MyInt = i32;
        e.g., using RawAdder = ((i32) -> i32)*;
        """

        # 1. 获取别名 (e.g., "MyInt" or "RawAdder")
        chrono_name = ctx.name.text

        # 2. 访问类型。这可能会返回:
        #    - "int32_t"
        #    - "std::function<...>"
        #    - "int32_t (*{NAME})(int32_t)" (特殊 C-Style 模式)
        cpp_type_pattern = self.visit(ctx.typeName)

        cpp_type = ""

        # 3. [ [ 关键处理 ] ]
        #    我们必须转换 C-Style 指针的模式
        if "(*{NAME})" in cpp_type_pattern:
            # 模式: "int32_t (*{NAME})(int32_t)"
            # C++ 别名语法需要: "int32_t (*)(int32_t)"
            # 我们用 "(*)" 替换 "(*{NAME})"
            cpp_type = cpp_type_pattern.replace("(*{NAME})", "(*)")
        else:
            # 标准类型 (i32, std::function<...>, std.vector[...])
            cpp_type = cpp_type_pattern

        # 4. 返回 C++ using 语句
        return f"using {chrono_name} = {cpp_type};\n"


    def visitMethodSignature(self, ctx: ChronoParser.MethodSignatureContext):
        # 将 Chrono 方法签名翻译为 C++ 纯虚函数

        func_name = ctx.name.text
        cpp_func_name = func_name.lstrip('$')

        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        if ctx.returnType:
            cpp_return_type = self.visit(ctx.returnType)
        else:
            cpp_return_type = "void"

        # C++ 语法: virtual <type> <name>(<params>) = 0;
        return f"{INDENT}virtual {cpp_return_type} {cpp_func_name}({params_code}) = 0;\n"

    # [ [ 新增：粘贴此方法 ] ]
    def visitInterfaceDefinition(self, ctx: ChronoParser.InterfaceDefinitionContext):
        interface_name = ctx.name.text

        body_code = ""

        # 迭代接口体内的所有节点
        child_nodes = ctx.children[2:-1]  # 跳过 'INTERFACE', 'NAME', '{' 和 '}'
        for child in child_nodes:
            if isinstance(child, ChronoParser.MethodSignatureContext):
                body_code += self.visit(child)
            elif isinstance(child, ChronoParser.CppBlockContext):
                body_code += self.visit(child)

        # 构建 C++ 抽象类
        code = f"\nclass {interface_name} {{\n"
        code += "public:\n"  # 接口方法在 C++ 中是 public

        # [关键] 添加一个虚析构函数，这是 C++ 接口的最佳实践
        code += f"{INDENT}virtual ~{interface_name}() {{}} // Virtual destructor\n"

        code += body_code
        code += "};\n"
        return code

    # 确保您的 visitClassDefinition 仍然包含 'impl' 逻辑
    def visitClassDefinition(self, ctx: ChronoParser.ClassDefinitionContext):
        class_name = ctx.name.text

        # [ [ 关键重构：继承列表 ] ]
        inheritance_list = []

        # 1. 添加基类 (例如: public ChronoObject)
        if ctx.base:
            base_name = ctx.base.text
            inheritance_list.append(f"public {base_name}")

        # 2. 添加所有接口 (例如: public IPrintable, public ISerializable)
        if ctx.interfaces:
            # self.visit(ctx.interfaces) 会返回一个 "IPrintable, ISerializable" 字符串
            interface_names_str = self.visit(ctx.interfaces)

            # 我们需要 split -> 'public ...' -> join
            interfaces = [f"public {name.strip()}" for name in interface_names_str.split(',')]
            inheritance_list.extend(interfaces)

        inheritance_str = ""
        if inheritance_list:
            # 组合成: " : public ChronoObject, public IPrintable"
            inheritance_str = " : " + ", ".join(inheritance_list)
        # [ [ 重构结束 ] ]

        # --- (Class Assembler 逻辑保持不变) ---
        self._in_class = True
        self._in_struct = False  # <-- [新增]
        self._current_class_name = class_name
        self._class_sections = {"private": "", "public": ""}

        if hasattr(ctx, 'classBodyStatement'):
            for child in ctx.classBodyStatement():
                self.visit(child)

        self._in_class = False
        self._current_class_name = None

        final_class_body = ""

        if self._class_sections["private"]:
            final_class_body += "\nprivate:\n"
            final_class_body += self._class_sections["private"]
        if self._class_sections["public"]:
            final_class_body += "\npublic:\n"
            final_class_body += self._class_sections["public"]
        # --- (Class Assembler 逻辑结束) ---

        # [修改] 使用新的 inheritance_str
        return (
            f"\nclass {class_name}{inheritance_str} {{\n"  # <-- 动态添加所有继承
            f"{final_class_body.strip()}\n"
            "};\n"
        )

    # [新增] visitClassBodyStatement (用于传递修饰符)
    def visitClassBodyStatement(self, ctx: ChronoParser.ClassBodyStatementContext):
        # 1. 确定修饰符
        is_static = hasattr(ctx, 'STATIC') and ctx.STATIC()
        access = self._get_access_level(ctx, default_level='private')

        # 2. 将修饰符 "注入" 到子上下文中
        if ctx.variableDeclaration():
            ctx.variableDeclaration()._chrono_access = access
            return self.visit(ctx.variableDeclaration())

        elif ctx.methodDefinition():
            ctx.methodDefinition()._chrono_access = access
            ctx.methodDefinition()._chrono_static = is_static
            return self.visit(ctx.methodDefinition())

        # --- [ 新增分支 ] ---
        elif ctx.initDefinition():
            # 将 access 注入
            ctx.initDefinition()._chrono_access = access
            return self.visit(ctx.initDefinition())
        # --- [ 新增结束 ] ---

        elif ctx.deinitBlock():
            return self.visit(ctx.deinitBlock())

        elif ctx.cppBlock():
            return self.visit(ctx.cppBlock())

        return ""

        # src/ChronoVisitor.py

    def visitInitDefinition(self, ctx: ChronoParser.InitDefinitionContext):
        self._in_class_method = True
        self._enter_scope()  # <-- [新增]

        # 'this' 永远是一个指针, 无论在 class 还是 struct 中
        accessor = "->"
        cpp_type = f"{self._current_class_name}*"

        # [新增] 注册 'this'
        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,  # <-- [修改]
            "cpp_type": cpp_type  # <-- [修改]
        })

        cpp_return_type = ""
        cpp_func_name = self._current_class_name
        access = getattr(ctx, '_chrono_access', 'private')
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        init_code = (
            f"\n{INDENT}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            f"{INDENT}}}\n"
        )
        self._class_sections[access] += init_code

        self._exit_scope()  # <-- [新增]
        self._in_class_method = False
        return ""

    def _determine_initial_accessor(self, raw_primary_text, translated_primary_code):
        """
        [重构] 根据 'raw_primary_text' (e.g., '$p', 'std', 'String')
        决定正确的 C++ 起始代码和第一个访问器 (., ->, ::)。

        返回: (初始 C++ 代码, 初始访问器, 变量类型)
        """
        variable_info = self._find_variable(raw_primary_text)

        if variable_info:
            # 案例 A: 变量 (e.g., $p, myStruct)
            # [ [ 改进 ] ] 返回 cpp_type 以供智能指针决策
            return translated_primary_code, variable_info["accessor"], variable_info["cpp_type"]

        elif raw_primary_text in self._alias_to_namespace_map:
            # 案例 B: 别名 (e.g., Chrono.log)
            return self._alias_to_namespace_map[raw_primary_text], "::", "namespace"

        elif raw_primary_text == "std":
            # 案例 C: 'std' 命名空间
            return "std", "::", "namespace"

        elif raw_primary_text and raw_primary_text.lstrip('$')[0].isupper():
            # 案例 D: 静态类名 (e.g., String.create)
            return self._chrono_to_cpp_type(raw_primary_text), "::", "class"

        else:
            # 案例 E: 默认回退 (e.g., 10.foo() 或 functionCall.foo())
            return translated_primary_code, ".", "literal"

    def _process_dot_chain_step(self, child_nodes, i, current_code, current_accessor, current_type, access_token_type):
        """
        [ [ 关键重构：翻转 . 和 -> ] ]
        [ [ BUG 修复：不再检查 current_type 字符串，而是信任传入的 current_accessor ] ]
        """

        # --- 1. IDENTIFIER (方法/成员名) ---
        i += 1  # 跳过 . 或 ->
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

        # [ [
        #
        #
        #
        #
        #  "翻转" 逻辑 (已修复) ] ]
        accessor_to_use = "."  # 默认

        if access_token_type == ChronoParser.DOT:
            # Chrono '.' (99% 用例)
            # [修复] 使用从 scope/determine_accessor 传入的 accessor
            # (它知道 's' 是 '->', 'p4' 是 '.')
            accessor_to_use = current_accessor

        elif access_token_type == ChronoParser.ARROW:
            # Chrono '->' (1% 用例)
            accessor_to_use = "."  # 强制 C++ '.' (访问指针/智能指针本身)

        # [ [ 逻辑结束 ] ]

        # --- 2. 泛型/模板块 [T] ---
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

        # --- 3. 函数调用块 () ---
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

        # --- 4. 更新下一次访问的访问器 (启发式) ---
        new_accessor = "->"
        if cpp_ident and cpp_ident[0].isupper():
            new_accessor = "::"

        return new_code, i, new_accessor, "unknown"

    def _process_array_chain_step(self, child_nodes, i, current_code, current_accessor):
        """
        [重构] 处理链条中从 LBRACK 开始的步骤: [expression]
        返回: (新的代码片段, 更新的索引 i, 更新的访问器)
        """
        i += 1  # 跳过 [
        if i >= len(child_nodes): return current_code, i, "."

        index_expr = self.visit(child_nodes[i])
        i += 1  # 跳过 expression

        if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.RBRACK:
            i += 1  # 跳过 ]

        new_code = f"{current_code}[{index_expr}]"

        # [ [ 关键修复 ] ]
        # 数组索引后, 访问器 *不* 改变。
        # 如果我们访问的是 $String[0] (指针数组), 下一个访问器仍然是 '->'
        new_accessor = current_accessor  # <-- [修改] 返回传入的访问器

        return new_code, i, new_accessor

    def visitDeinitBlock(self, ctx: ChronoParser.DeinitBlockContext):
        self._in_class_method = True  # <-- [新增] 必须设置此标志
        self._enter_scope()

        # 'this' 永远是一个指针, 无论在 class 还是 struct 中
        accessor = "->"
        cpp_type = f"{self._current_class_name}*"

        # --- [ 新增修复 ] ---
        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": accessor,  # <-- [修改]
            "cpp_type": cpp_type  # <-- [修改]
        })

        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)
        deinit_code = (
            f"\n{INDENT}virtual ~{self._current_class_name}() {{\n"
            f"{INDENT}// --- Chrono Deinit Block ---\n"
            f"{body_code}"
            f"{INDENT}// --- Deinit End ---\n"
            f"{INDENT}}}\n"
        )
        self._class_sections["public"] += deinit_code

        self._exit_scope()
        self._in_class_method = False  # <-- [新增] 必须重置此标志
        return ""

        # src/ChronoVisitor.py

    # [替换] visitTypeList
    def visitTypeList(self, ctx: ChronoParser.TypeListContext):
        """
        [修改] 访问 'typeList' 规则。
        现在访问 'templateArgument' 列表。
        """
        arg_list = [self.visit(t) for t in ctx.templateArgument()]
        return ", ".join(arg_list)

    # [新增]
    def visitTemplateArgument(self, ctx: ChronoParser.TemplateArgumentContext):
        """
        [新增] 访问 'templateArgument' 规则。
        它可能是 'typeSpecifier' (i32) 或 'literal' (5)。
        """
        if ctx.typeSpecifier():
            return self.visit(ctx.typeSpecifier())
        if ctx.literal():
            return self.visit(ctx.literal())
        return ""  # 不太可能

        # ... (在 visitLiteral 之后) ...

        # [新增]

    def visitInitializerList(self, ctx: ChronoParser.InitializerListContext):
        """
        [新增] 访问 '{ ... }' 聚合初始化。
        将 Chrono {1, 2} 翻译为 C++ {1, 2}。
        """
        # 访问内部的 'expressionList'
        args_code = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
        return f"{{{args_code}}}"

    def visitSimpleExpression(self, ctx: ChronoParser.SimpleExpressionContext):
        """
        [重构] 实现了 "翻转" 的 . 和 -> 逻辑。
        """
        # 1. 确定初始部分
        if ctx.primary():
            primary_ctx = ctx.primary()
            translated_primary = self.visit(primary_ctx)
            raw_primary_text = primary_ctx.getText()
        elif ctx.functionCallExpression():
            translated_primary = self.visit(ctx.functionCallExpression())
            raw_primary_text = ctx.functionCallExpression().getText()
        else:
            return ""

        # 2. 确定初始访问器 (和类型)
        current_code, current_accessor, current_type = self._determine_initial_accessor(
            raw_primary_text, translated_primary
        )

        # 3. 遍历链条
        child_nodes = ctx.children[1:]
        i = 0
        while i < len(child_nodes):

            token_type = child_nodes[i].getSymbol().type

            if token_type == ChronoParser.DOT:
                # 3a. 处理点访问
                current_code, i, current_accessor, current_type = self._process_dot_chain_step(
                    child_nodes, i, current_code, current_accessor, current_type, ChronoParser.DOT
                )

            elif token_type == ChronoParser.LBRACK:
                # 3b. 处理数组索引 ([i])
                current_code, i, current_accessor = self._process_array_chain_step(
                    child_nodes, i, current_code, current_accessor
                )
                current_type = "unknown"  # (我们不知道数组元素的类型)

            elif token_type == ChronoParser.ARROW:
                # 3c. 处理箭头访问
                current_code, i, current_accessor, current_type = self._process_dot_chain_step(
                    child_nodes, i, current_code, current_accessor, current_type, ChronoParser.ARROW
                )

            else:
                i += 1

        return current_code

    def visitPrimary(self, ctx: ChronoParser.PrimaryContext):
        """
        [重构] 新增对 @make 和 @make_shared 的翻译
        """
        if ctx.NEW():
            class_name = self.visit(ctx.baseType())
            args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
            return f"new {class_name}({args})"

        # [ [ 关键新增 ] ] 处理 @make[Type](args)
        if ctx.AT_MAKE_UNIQUE():
            target_type = self.visit(ctx.typeSpecifier())
            args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
            # C++ 格式: std::make_unique<Type>(args)
            return f"std::make_unique<{target_type}>({args})"

        if ctx.AT_MAKE_SHARED():
            target_type = self.visit(ctx.typeSpecifier())
            args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
            # C++ 格式: std::make_shared<Type>(args)
            return f"std::make_shared<{target_type}>({args})"
        # [ [ 新增结束 ] ]

        if ctx.literal():
            return self.visit(ctx.literal())

        if ctx.initializerList():
            return self.visit(ctx.initializerList())

        if ctx.IDENTIFIER():
            primary_text = ctx.IDENTIFIER().getText()
            variable_info = self._find_variable(primary_text)

            if variable_info:
                if '[' in variable_info["cpp_type"]:
                    return ctx.IDENTIFIER().getText().lstrip('$')
                return variable_info["cpp_name"]
            else:
                return primary_text

        if ctx.THIS():
            return "this"

        if ctx.LPAREN():
            return f"({self.visit(ctx.expression())})"

        return ""

    def visitParameters(self, ctx: ChronoParser.ParametersContext):
        params_list = []
        for p in ctx.parameter():
            params_list.append(self.visit(p))
        return ", ".join(params_list)

    def visitStatement(self, ctx: ChronoParser.StatementContext):
        if ctx.variableDeclaration():  # <-- [修改]
            return self.visit(ctx.variableDeclaration())  # <-- [修改]
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        if ctx.cppBlock():
            return self.visit(ctx.cppBlock())
        if ctx.expression():
            expr_code = self.visit(ctx.expression())
            return f"{INDENT}{expr_code};\n"
        # [ 新增 ]
        if ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        if ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        # [ 关键 ] 确保此行存在
        if ctx.deleteStatement():
            return self.visit(ctx.deleteStatement())
        if ctx.forStatement():
            return self.visit(ctx.forStatement())
        # [ [ 关键修复：添加此检查 ] ]
        if ctx.blockStatement():
            return self.visit(ctx.blockStatement())
        return ""

    # [ 已修正 ]

    def visitReturnStatement(self, ctx: ChronoParser.ReturnStatementContext):
        return_value = self.visit(ctx.expression())
        return f"{INDENT}return {return_value};\n"

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

        # [ 修改 ] 不再硬编码 "="
        # 而是访问 assignmentOperator 规则
        op_str = self.visit(ctx.assignmentOperator())

        return f"{INDENT}{target} {op_str} {value};\n"

    def visitAssignableExpression(self, ctx: ChronoParser.AssignableExpressionContext):
        """
        [重构] 访问 'assignableExpression' 规则。
        [更新] 实现了 "翻转" 的 . 和 -> 逻辑。
        [BUG 修复] 信任 'current_accessor'，而不是检查 'current_type'。
        """

        # 1. 访问第一个环节 (e.g., "(*_s)", "this", "i")
        primary_ctx = ctx.assignablePrimary()
        current_code = self.visit(primary_ctx)

        # 2. 决定“第一个”访问器 (启发式)
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

        current_accessor = "."  # 默认 C++ 访问器
        current_type = "value"  # 默认类型

        if base_ident_text:
            variable_info = self._find_variable(base_ident_text)
            if variable_info:
                current_type = variable_info["cpp_type"]
                current_accessor = variable_info["accessor"]  # [关键] 获取初始访问器
            elif base_ident_text == "std" or base_ident_text in self._alias_to_namespace_map:
                current_accessor = "::"
                current_type = "namespace"

        # 3. 遍历链条 (DOT IDENTIFIER | LBRACK ... | ARROW ...)*
        child_nodes = ctx.children[1:]  # 跳过 assignablePrimary
        i = 0
        while i < len(child_nodes):

            token_type = child_nodes[i].getSymbol().type
            accessor_to_use = current_accessor

            # [ [
            #
            #
            #
            #
            #  "翻转" 逻辑 (已修复) ] ]
            if token_type == ChronoParser.DOT:
                # Chrono '.' (99% 用例)
                # [修复] 使用从 scope 传入的 accessor
                accessor_to_use = current_accessor

            elif token_type == ChronoParser.ARROW:
                # Chrono '->' (1% 用例)
                accessor_to_use = "."  # 强制 C++ '.'

            # [ [ 逻辑结束 ] ]

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

                # 更新下一次迭代的状态
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
            init_code = self.visit(ctx.init)  # 调用 visitForInit

        cond_code = ""
        if ctx.cond:
            cond_code = self.visit(ctx.cond)  # 调用 visitExpression

        incr_code = ""
        if ctx.incr:
            incr_code = self.visit(ctx.incr)  # [修改] 现在调用 visitForIncrement

        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        self._exit_scope()

        code = f"{INDENT}for ({init_code}; {cond_code}; {incr_code}) {{\n"
        code += body_code
        code += f"{INDENT}}}\n"
        return code

    # [ [ 新增 ] ]
    def visitForInit(self, ctx: ChronoParser.ForInitContext):
        # 这个辅助方法会访问 'declaration_no_semicolon'
        # 或 'assignment_no_semicolon'
        if ctx.variableDeclaration_no_semicolon():  # <-- [修改]
            return self.visit(ctx.variableDeclaration_no_semicolon())  # <-- [修改]
        if ctx.assignment_no_semicolon():
            return self.visit(ctx.assignment_no_semicolon())
        return ""

    # [ [ 新增 ] ]
    def visitForIncrement(self, ctx: ChronoParser.ForIncrementContext):
        # 访问它唯一的子节点，无论是赋值还是表达式
        if ctx.assignment_no_semicolon():
            return self.visit(ctx.assignment_no_semicolon())
        if ctx.expression():
            return self.visit(ctx.expression())
        return ""

    # [ [ 新增 ] ]

    def _recursive_analyze(self, node, indent_level=0):
        """
        递归地打印出 ANTLR 树中一个节点及其所有子节点的结构。
        """
        indent = "  " * indent_level

        # 1. 获取节点类型名
        node_type = type(node).__name__

        # 2. 获取节点文本
        node_text_repr = repr(node.getText())

        # 3. 打印当前节点信息
        print(f"{indent}Type: {node_type.ljust(30)} | Text: {node_text_repr}")

        # 4. 递归 (只对 'Context' 对象，不对 'Terminal' 词元)
        # 我们检查 'children' 属性是否存在且不为空
        if hasattr(node, 'children') and node.children:
            indent_level += 1
            for child in node.children:
                self._recursive_analyze(child, indent_level)

    def _process_block_children(self, children):
        """
        通用辅助函数：遍历 children 列表，只收集 StatementContext 节点。
        """
        body_code = ""
        for child in children:
            if isinstance(child, ChronoParser.StatementContext):
                body_code += self.visit(child)
        return body_code

        # src/ChronoVisitor.py (添加一个辅助函数，并替换 visitIfStatement)

        # src/ChronoVisitor.py

    def visitAssignmentOperator(self, ctx: ChronoParser.AssignmentOperatorContext):
        """将赋值操作符词元翻译为 C++ 字符串"""
        if ctx.ASSIGN(): return "="
        if ctx.PLUS_ASSIGN(): return "+="
        if ctx.MINUS_ASSIGN(): return "-="
        if ctx.STAR_ASSIGN(): return "*="
        if ctx.SLASH_ASSIGN(): return "/="
        if ctx.MOD_ASSIGN(): return "%="
        # 不太可能的回退
        return "="

    def visitIfStatement(self, ctx: ChronoParser.IfStatementContext):
        condition = self.visit(ctx.expression())

        # [修改] 调用 self.visit(ctx.if_block)
        # (如果 ctx.if_block 存在, 否则返回 "")
        if_body = self.visit(ctx.if_block) if ctx.if_block else ""

        # [修改] 作用域已在 visitIfBlock 内部处理
        code = f"{INDENT}if ({condition}) {{\n{if_body}{INDENT}}}\n"

        if ctx.ELSE():
            if ctx.else_if:
                # 递归调用 'else if' (这部分不变)
                code += f"{INDENT}else {self.visit(ctx.else_if)}"

            elif ctx.else_block:
                # [修改] 调用 self.visit(ctx.else_block)
                else_body = self.visit(ctx.else_block)
                # [修改] 作用域已在 visitElseBlock 内部处理
                code += f"{INDENT}else {{\n{else_body}{INDENT}}}\n"
        return code

    def visitIfBlock(self, ctx: ChronoParser.IfBlockContext):
        """[新增] 处理 if (...) { ... } 块"""
        self._enter_scope()

        # [关键修复]
        # 使用默认的 ctx.statement() 访问器,
        # 它被证明可以正确返回*所有*语句的列表。
        statements = self._safe_iterate_statements(ctx.statement())

        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        return body_code

    def visitElseBlock(self, ctx: ChronoParser.ElseBlockContext):
        """[新增] 处理 else { ... } 块"""
        self._enter_scope()

        # [关键修复]
        # 使用默认的 ctx.statement() 访问器
        statements = self._safe_iterate_statements(ctx.statement())

        body_code = "".join(self.visit(s) for s in statements)
        self._exit_scope()
        return body_code

    def visitWhileStatement(self, ctx: ChronoParser.WhileStatementContext):
        condition = self.visit(ctx.expression())

        self._enter_scope()

        # --- [ 关键修复 ] ---
        #
        # 之前的 (错误的):
        # body_statements = self._safe_iterate_statements(ctx.statements)
        #
        # 现在的 (正确的):
        # 我们必须使用默认的 ctx.statement() 访问器,
        # 这与 visitFunctionDefinition (可以工作的) 中使用的模式一致。
        #
        body_statements = self._safe_iterate_statements(ctx.statement())
        # --- [ 修复结束 ] ---

        body_code = "".join(self.visit(s) for s in body_statements)
        self._exit_scope()

        code = f"{INDENT}while ({condition}) {{\n"
        code += body_code
        code += f"{INDENT}}}\n"
        return code

    # 'visitExpression' 现在是新的顶层, 处理比较
    def visitExpression(self, ctx: ChronoParser.ExpressionContext):
        """
        [修改] 访问 'expression' 规则。
        现在支持链式操作 (A + B + C)，但*不支持*优先级。
        """

        # 1. 获取所有操作数 (例如 [arr[0], arr[1], arr[2]])
        operand_nodes = ctx.unaryExpression()

        # 2. 访问第一个操作数 (LHS)
        current_code = self.visit(operand_nodes[0])

        # 3. 检查是否有任何操作符
        if len(operand_nodes) == 1:
            return current_code  # 只有一个操作数 (例如 "arr[0]")

        # 4. [新循环逻辑]
        #    构建一个包含所有操作符的列表
        all_ops = []
        if ctx.PLUS(): all_ops.extend(ctx.PLUS())
        if ctx.MINUS(): all_ops.extend(ctx.MINUS())
        if ctx.STAR(): all_ops.extend(ctx.STAR())
        if ctx.SLASH(): all_ops.extend(ctx.SLASH())
        if ctx.MODULO(): all_ops.extend(ctx.MODULO())  # <-- [新增]
        if ctx.EQ(): all_ops.extend(ctx.EQ())
        if ctx.NEQ(): all_ops.extend(ctx.NEQ())
        if ctx.LT(): all_ops.extend(ctx.LT())
        if ctx.GT(): all_ops.extend(ctx.GT())
        if ctx.LTE(): all_ops.extend(ctx.LTE())
        if ctx.GTE(): all_ops.extend(ctx.GTE())
        if ctx.AND_OP(): all_ops.extend(ctx.AND_OP())  # <-- [新增]
        if ctx.OR_OP(): all_ops.extend(ctx.OR_OP())  # <-- [新增]

        # [ [ 新增 ] ]
        if ctx.BIT_AND(): all_ops.extend(ctx.BIT_AND())
        if ctx.BIT_OR(): all_ops.extend(ctx.BIT_OR())
        if ctx.BIT_XOR(): all_ops.extend(ctx.BIT_XOR())
        if ctx.LSHIFT(): all_ops.extend(ctx.LSHIFT())
        if ctx.RSHIFT(): all_ops.extend(ctx.RSHIFT())

        # 5. [关键] 按它们在源代码中出现的顺序对操作符进行排序
        #    (因为 ctx.PLUS() 等只返回一种类型的列表)
        all_ops.sort(key=lambda x: x.getSymbol().tokenIndex)

        # 6. 遍历操作符，构建 C++ 字符串
        for i in range(len(all_ops)):
            # 获取操作符 (例如 "+")
            op_node = all_ops[i]
            op_str = self._get_op_string_from_token_type(op_node.getSymbol().type)

            # 获取右侧操作数 (RHS)
            rhs_code = self.visit(operand_nodes[i + 1])

            # C++ 支持左结合 (left-associativity)
            current_code = f"{current_code} {op_str} {rhs_code}"

        return current_code

        # (在 src/ChronoVisitor.py 中替换 visitUnaryExpression)

    def visitUnaryExpression(self, ctx: ChronoParser.UnaryExpressionContext):
        """
        [修改] 访问一元表达式规则，处理 & (取地址) 和 * (解引用)
        """
        if ctx.simpleExpression():
            return self.visit(ctx.simpleExpression())

        op = ""

        # [ [ 关键新增 ] ] 处理 BIT_AND (& 取地址)
        if ctx.BIT_AND():
            op = "&"  # Chrono & -> C++ & (取地址操作符)

        # [ [ 关键新增 ] ] 处理 STAR (* 解引用)
        elif ctx.STAR():
            op = "*"  # Chrono * -> C++ * (解引用操作符)

        elif ctx.MINUS():
            op = "-"
        elif ctx.PLUS():
            op = "+"
        elif ctx.NOT_OP():
            op = "!"
        elif ctx.BIT_NOT():  # 假设 BIT_NOT 仍然是 ~
            op = "~"

        # 递归访问操作数
        operand = self.visit(ctx.unaryExpression())

        if op == "*" or op == "&":
            # 无论是取地址还是解引用，使用括号 () 封装能确保优先级
            return f"{op}{operand}"
        else:
            return f"{op}{operand}"

    # [新增] 访问 delete 语句
    def visitDeleteStatement(self, ctx: ChronoParser.DeleteStatementContext):
        target = self.visit(ctx.expression())
        return f"{INDENT}delete {target};\n"

    # (在 ChronoVisitor.py 中新增此方法，例如放在 visitAssignableExpression 附近)
    def visitAssignablePrimary(self, ctx: ChronoParser.AssignablePrimaryContext):
        """
        [新增] 访问 assignablePrimary 规则，处理 * 和 & 作为左值。
        """
        if ctx.IDENTIFIER():
            # 查找变量的 C++ 名称 (s -> s, _s, data[3], etc.)
            primary_text = ctx.IDENTIFIER().getText()
            variable_info = self._find_variable(primary_text)

            # 沿用 visitAssignableExpression 的逻辑来决定是返回原始名还是 C++ 名
            if variable_info:
                if '[' in variable_info["cpp_type"]:
                    return primary_text  # 数组使用原始名称
                else:
                    return variable_info["cpp_name"]  # 例如: "_s"
            else:
                return self._chrono_to_cpp_type(primary_text)  # Fallback

        if ctx.THIS():
            return "this"

        # [关键] 处理一元操作符 * (STAR) 和 & (BIT_AND)
        if ctx.STAR():
            # 递归访问右侧，并添加 *
            return f"(*{self.visit(ctx.assignablePrimary())})"

        if ctx.BIT_AND():
            # 递归访问右侧，并添加 &
            return f"(&{self.visit(ctx.assignablePrimary())})"

        if ctx.LPAREN():
            return f"({self.visit(ctx.assignableExpression())})"

        return ""

    def visitExpressionList(self, ctx: ChronoParser.ExpressionListContext):
        return ", ".join(self.visit(e) for e in ctx.expression())

    # [ 已修正 ]
    def visitLiteral(self, ctx: ChronoParser.LiteralContext):
        if ctx.BOOL_LITERAL():
            return ctx.BOOL_LITERAL().getText()
        if ctx.CHAR_LITERAL():  # <-- [新增]
            return ctx.CHAR_LITERAL().getText()  # 原样返回 (例如 's')

        # --- [新增] 翻译 Byte 字面量 ---
        if ctx.BYTE_LITERAL():
            raw_text = ctx.BYTE_LITERAL().getText()  # (例如: "b'A'")
            char_part = raw_text[1:]  # (提取: "'A'")

            # 翻译为 C++ (uint8_t)'A'
            # 我们必须包含 stdint.h (Chrono.h 已经包含了)
            return f"(uint8_t){char_part}"
        # 现在的:
        if ctx.OCTAL_LITERAL():
            raw_text = ctx.OCTAL_LITERAL().getText()  # (例如: "0o52")
            # 将 "0o52" 翻译为 "052" (C++ 经典语法)
            return f"0{raw_text[2:]}"
        # C++ 原生支持 3.14, 所以我们只返回文本
        if ctx.FLOAT_LITERAL():
            return ctx.FLOAT_LITERAL().getText()
        return ctx.getText()

    def visitAssignment_no_semicolon(self, ctx: ChronoParser.Assignment_no_semicolonContext):
        # 这就像 visitAssignment，但没有分号
        target = self.visit(ctx.assignableExpression())
        value = self.visit(ctx.expression())

        # [ 修改 ] 不再硬编码 "="
        # 而是访问 assignmentOperator 规则
        op_str = self.visit(ctx.assignmentOperator())

        # [关键] 返回 C++ 代码时 *不带* 分号
        return f"{target} {op_str} {value}"

    def visitStructBodyStatement(self, ctx: ChronoParser.StructBodyStatementContext):
        """
        [新增] 访问 struct 体内的语句。
        与 classBodyStatement 类似, 但
        1. 默认是 'public'
        2. 不支持 'static' (已在 Parser 中禁止)
        """
        # 1. 确定修饰符
        # [ 关键 ] struct 默认是 'public'
        access = self._get_access_level(ctx, default_level='public')

        # 2. 将修饰符 "注入" 到子上下文中
        if ctx.variableDeclaration():
            ctx.variableDeclaration()._chrono_access = access
            return self.visit(ctx.variableDeclaration())

        elif ctx.methodDefinition():
            ctx.methodDefinition()._chrono_access = access
            ctx.methodDefinition()._chrono_static = False  # struct 不支持 static
            return self.visit(ctx.methodDefinition())

        elif ctx.initDefinition():
            ctx.initDefinition()._chrono_access = access
            return self.visit(ctx.initDefinition())

        elif ctx.deinitBlock():
            # deinit 总是 public (由 visitDeinitBlock 内部处理)
            return self.visit(ctx.deinitBlock())

        elif ctx.cppBlock():
            return self.visit(ctx.cppBlock())

        return ""

    # [ [ 新增 ] ]
    def visitStructDefinition(self, ctx: ChronoParser.StructDefinitionContext):
        """
        [新增] 访问 struct 定义
        """
        struct_name = ctx.name.text

        # 1. [ 关键 ] 设置标志
        #    self._in_class (引用类型) = False
        #    self._in_struct (值类型) = True
        self._in_class = False
        self._in_struct = True
        self._current_class_name = struct_name  # (重用此标志)

        # 重置 sections
        self._class_sections = {"private": "", "public": ""}

        # 2. 遍历所有 'structBodyStatement'
        if hasattr(ctx, 'structBodyStatement'):
            for child in ctx.structBodyStatement():
                self.visit(child)  # -> 调用 visitStructBodyStatement

        # 3. 重置标志
        self._in_struct = False
        self._current_class_name = None

        # 4. 组装 C++ struct
        final_struct_body = ""

        # [ 关键 ] C++ struct 默认是 public,
        # 所以我们先输出 public, 再输出 private

        if self._class_sections["public"]:
            final_struct_body += "\npublic:\n"
            final_struct_body += self._class_sections["public"]

        if self._class_sections["private"]:
            final_struct_body += "\nprivate:\n"
            final_struct_body += self._class_sections["private"]

        # 5. 返回最终代码
        return (
            f"\nstruct {struct_name} {{\n"  # 翻译为 C++ 'struct'
            f"{final_struct_body.strip()}\n"
            f"}};\n"
        )

    # [ [ 新增 ] ]
    def visitVariableDeclaration(self, ctx: ChronoParser.VariableDeclarationContext):
        """
        [新增] 访问新的 'variableDeclaration' 规则。
        处理: const/var, 显式/推导 ($)
        """

        # 1. 调用核心翻译逻辑
        # (它返回 C++ 代码片段，*不带*分号)
        core_cpp, is_member_variable, access, cpp_final_type, cpp_name = self._translate_variable_declaration(ctx)

        # 2. 根据是“成员”还是“局部”来组装
        if is_member_variable:
            # [ 成员变量 ] -> 添加到 class/struct sections
            declaration_line = f"{INDENT}{core_cpp};\n"
            self._class_sections[access] += declaration_line
            return ""
        else:
            # [ 局部变量 ] -> 返回完整的 C++ 语句
            return f"{INDENT}{core_cpp};\n"

    # [ [ 新增 ] ]
    def visitVariableDeclaration_no_semicolon(self, ctx: ChronoParser.VariableDeclaration_no_semicolonContext):
        """
        [新增] 访问 'for' 循环的 'variableDeclaration_no_semicolon'。
        """

        # 1. 调用核心翻译逻辑 (它返回 C++ 代码片段，*不带*分号)
        core_cpp, _, _, _, _ = self._translate_variable_declaration(ctx)

        # 2. 直接返回核心 C++ (不带分号)
        return core_cpp

    # [ [ 新增 ] ]

    # [ [ 新增：用于处理 { ... } 块 ] ]
    def visitBlockStatement(self, ctx: ChronoParser.BlockStatementContext):
        """
        [新增] 访问一个独立的块语句 { ... }
        这在 C++ 中创建了一个新的作用域。
        """
        self._enter_scope()

        # [关键] 使用 _safe_iterate_statements 访问所有子语句
        # (这与 visitFunctionDefinition, visitIfBlock 等使用的方法一致)
        statements = self._safe_iterate_statements(ctx.statement())

        body_code = "".join(self.visit(s) for s in statements)

        self._exit_scope()

        # 返回块的完整 C++ 代码
        # 注意：我们不在 Visitor 中添加 { 和 }，因为
        # C++ 语句 (如 if/while) 已经添加了它们。
        #
        # [ [ 关键修改 ] ]
        # 经过重新思考，独立的 { ... } 块 *必须* 返回大括号。
        # 否则 `func main() { { ... } }` 会变成 `int main() { ... }` (缺少了内部的 { } )

        final_code = f"{INDENT}{{\n"
        final_code += body_code
        final_code += f"{INDENT}}}\n"

        return final_code
