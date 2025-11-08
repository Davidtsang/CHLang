# src/ChronoVisitor.py
import os
from antlr4 import *
from parser.ChronoParser import ChronoParser
from parser.ChronoParserVisitor import ChronoParserVisitor as BaseChronoVisitor
from antlr4.tree.Tree import TerminalNodeImpl  # 导入 TerminalNodeImpl

INDENT = "    "

# [ [ 1. 新增：我们的“例外列表” ] ]
# 规则 3：这些是“身为值，却用 ->”的反常规类型
# （我们使用 set 以便快速查找）
_ACCESSOR_EXCEPTION_LIST = {
    "std::shared_ptr",
    "std::unique_ptr",
    "std::optional",
    # "iterator" 我们将通过名称后缀 "::iterator" 来特殊处理
}


class ChronoVisitor(BaseChronoVisitor):

    # [ 替换 ] __init__
    def __init__(self):
        super().__init__()
        self._in_class_method = False
        self._in_class = False
        self._current_class_name = None
        self._class_sections = {"private": "", "public": ""}
        self._alias_to_namespace_map = {}

        # [ [ 2. 新增：我们的“作用域栈” ] ]
        # 这是一个字典的列表。
        # 栈顶 (self._scope_stack[-1]) 代表当前作用域。
        # 字典格式: { "var_name_in_chrono": { "accessor": "->", "cpp_name": "_var" } }
        self._scope_stack = [{}]  # 初始化一个“全局作用域”

    # [ [ 3. 新增：作用域栈的辅助方法 ] ]

    def _enter_scope(self):
        """进入一个新的作用域 (例如函数体或 if 块)"""
        self._scope_stack.append({})

    def _exit_scope(self):
        """退出当前作用域"""
        if len(self._scope_stack) > 1:
            self._scope_stack.pop()

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
        if chrono_type_name == "bool":
            return "bool"
            # --- [新增] 完整的整数类型映射 ---
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
        # --- [新增] 浮点类型映射 ---
        if chrono_type_name == "f32" or chrono_type_name == "float":
            return "float"
        if chrono_type_name == "f64":
            return "double"
        # --- [新增结束] ---
        return chrono_type_name

    def _get_access_level(self, ctx):
        """检查上下文是否包含访问修饰符，返回 'public' 或默认 'private'。"""
        # [修复] 检查 'ctx' 本身是否有 'accessModifier'
        if hasattr(ctx, 'accessModifier') and ctx.accessModifier():
            # 检查 accessModifier 规则的文本，我们假设只有 PUBLIC
            return "public"
        # [修复] 检查 'declaration' 或 'methodDefinition' (如果它们是父级)
        elif hasattr(ctx, 'declaration') and hasattr(ctx.declaration(),
                                                     'accessModifier') and ctx.declaration().accessModifier():
            return "public"
        elif hasattr(ctx, 'methodDefinition') and hasattr(ctx.methodDefinition(),
                                                          'accessModifier') and ctx.methodDefinition().accessModifier():
            return "public"

        return "private"  # 默认是 private (Rust/Swift 哲学)

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

    # 替换 [visitClassDefinition] (移除重复的 行)

    def visitClassDefinition(self, ctx: ChronoParser.ClassDefinitionContext):
        class_name = ctx.name.text

        # [ 关键修复 ] 检查 base class 是否存在
        base_name_str = ""
        if ctx.base:
            # 如果存在基类 (e.g., : ChronoObject)
            base_name = ctx.base.text
            base_name_str = f" : public {base_name}"  # 假设所有继承都是 public

        # --- (Class Assembler 逻辑保持不变) ---
        self._in_class = True
        self._current_class_name = class_name
        self._class_sections = {"private": "", "public": ""}

        if hasattr(ctx, 'classBodyStatement'):
            for child in ctx.classBodyStatement():
                self.visit(child)  # <--- 这将调用 visitClassBodyStatement

        self._in_class = False
        self._current_class_name = None

        final_class_body = ""

        # 1. 输出 private (默认)
        if self._class_sections["private"]:
            final_class_body += "\nprivate:\n"
            final_class_body += self._class_sections["private"]
        if self._class_sections["public"]:
            final_class_body += "\npublic:\n"
            final_class_body += self._class_sections["public"]
        # --- (Class Assembler 逻辑结束) ---

        # [ 关键修复 ] 使用 base_name_str 变量
        return (
            f"\nclass {class_name}{base_name_str} {{\n"  # <-- 动态添加继承
            f"{final_class_body.strip()}\n"
            "};\n"
        )

    # [新增] visitClassBodyStatement (用于传递修饰符)
    def visitClassBodyStatement(self, ctx: ChronoParser.ClassBodyStatementContext):
        # 1. 确定修饰符
        is_static = hasattr(ctx, 'STATIC') and ctx.STATIC()
        access = self._get_access_level(ctx)

        # 2. 将修饰符 "注入" 到子上下文中
        if ctx.declaration():
            ctx.declaration()._chrono_access = access
            return self.visit(ctx.declaration())

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

    def visitMethodDefinition(self, ctx: ChronoParser.MethodDefinitionContext):
        self._in_class_method = True
        self._enter_scope()

        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": "->",
            "cpp_type": f"{self._current_class_name}*"
        })

        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        is_static = getattr(ctx, '_chrono_static', False)
        access = getattr(ctx, '_chrono_access', 'private')

        if ctx.returnType:
            # [ [ 修复 ] ]
            # 我们不再手动剥离 $，而是依赖 visitTypeSpecifier
            # visitTypeSpecifier 将返回 "String*" 或 "int32_t"
            cpp_return_type = self.visit(ctx.returnType)
            # [ [ 修复结束 ] ]

            # --- [ 关键修复 ] ---
            cpp_func_name = func_name.lstrip('$')  # 剥离 $
            # --- [ 修复结束 ] ---

        else:
            cpp_return_type = "void"

            # --- [ 关键修复 ] ---
            cpp_func_name = func_name.lstrip('$')  # 剥离 $
            # --- [ 修复结束 ] ---

        static_prefix = "static " if is_static else ""

        func_def_code = (
            f"\n{INDENT}{static_prefix}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            f"{INDENT}// --- Method End ---\n"
            f"{INDENT}}}\n"
        )

        self._class_sections[access] += func_def_code

        self._exit_scope()
        self._in_class_method = False
        return ""

    def visitInitDefinition(self, ctx: ChronoParser.InitDefinitionContext):
        self._in_class_method = True
        self._enter_scope()  # <-- [新增]

        # [新增] 注册 'this'
        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": "->",
            "cpp_type": f"{self._current_class_name}*"
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

    # 你的 ChronoVisitor.py 文件
    # src/ChronoVisitor.py

    def visitDeinitBlock(self, ctx: ChronoParser.DeinitBlockContext):
        self._enter_scope()

        # --- [ 新增修复 ] ---
        # 必须像 init/method 一样注册 'this'，否则 deinit 内部无法访问成员
        self._add_variable("this", {
            "cpp_name": "this",
            "accessor": "->",
            "cpp_type": f"{self._current_class_name}*"
        })
        # --- [ 修复结束 ] ---

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
        return ""


        # src/ChronoVisitor.py

    def visitTypeSpecifier(self, ctx: ChronoParser.TypeSpecifierContext):
        """
        [修改] 访问 'typeSpecifier' 规则。
        处理:
        1. 泛型: std.vector[i32] -> std::vector<int32_t>
        2. 数组: [char; 20] -> char[20]
        """

        # [ [ 关键修复 ] ]
        # 我们必须首先检查数组路径。
        # 路径 A = baseType [...]
        # 路径 B = [baseType; ...]
        # 检查 LBRACK 和 SEMIC_TOKEN 是区分它们的唯一可靠方法。

        if ctx.LBRACK() and ctx.SEMIC_TOKEN():
            # --- 路径 B: C-Style 数组 (例如 [char; 20]) ---

            # 1. 翻译基础类型 (例如 "char")
            base = self.visit(ctx.baseType())

            # 2. 翻译数组大小 (例如 "20")
            size_expr = self.visit(ctx.expression())

            # 3. 组合 (例如 "char[20]")
            return f"{base}[{size_expr}]"

        elif ctx.baseType():
            # --- 路径 A: 泛型 (例如 std.vector[i32] 或 基础类型 i32) ---

            # 1. 翻译基础类型 (例如 "std.vector" -> "std::vector")
            base = self.visit(ctx.baseType())

            # 2. 如果有泛型参数 (LBRACK typeList RBRACK)
            if ctx.typeList():
                # 3. 翻译参数列表 (例如 "i32, 5" -> "int32_t, 5")
                args = self.visit(ctx.typeList())
                # 4. 组合 (例如 "std::vector<int32_t>")
                return f"{base}<{args}>"
            else:
                return base  # (例如 "i32")

        return ""  # 不太可能
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
        # 处理 primary 或 functionCallExpression
        if ctx.primary():
            primary_ctx = ctx.primary()
            translated_primary = self.visit(primary_ctx)
            raw_primary_text = primary_ctx.getText()
        elif ctx.functionCallExpression():
            translated_primary = self.visit(ctx.functionCallExpression())
            raw_primary_text = ctx.functionCallExpression().getText()
        else:
            return ""

        current_code = translated_primary

        # 决定初始访问器
        variable_info = self._find_variable(raw_primary_text)
        if variable_info:
            current_accessor = variable_info["accessor"]
        elif raw_primary_text in self._alias_to_namespace_map:
            current_code = self._alias_to_namespace_map[raw_primary_text]
            current_accessor = "::"
        elif raw_primary_text and raw_primary_text.lstrip('$')[0].isupper():
            current_accessor = "::"
        else:
            current_accessor = "."

        # 遍历链条
        child_nodes = ctx.children[1:]
        i = 0
        while i < len(child_nodes):
            if child_nodes[i].getSymbol().type == ChronoParser.DOT:
                i += 1
                if i >= len(child_nodes):
                    break
                ident_node = child_nodes[i]
                i += 1
                raw_ident_text = ident_node.getText()
                cpp_ident = f"_{raw_ident_text.lstrip('$')}" if raw_ident_text.startswith('$') else raw_ident_text
                if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.LPAREN:
                    i += 1
                    args = ""
                    if i < len(child_nodes) and isinstance(child_nodes[i], ChronoParser.ExpressionListContext):
                        args = self.visit(child_nodes[i])
                        i += 1
                    if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.RPAREN:
                        i += 1
                    current_code = f"{current_code}{current_accessor}{cpp_ident}({args})"
                else:
                    current_code = f"{current_code}{current_accessor}{cpp_ident}"
                current_accessor = "::" if cpp_ident and cpp_ident[0].isupper() else "->"
            elif child_nodes[i].getSymbol().type == ChronoParser.LBRACK:
                i += 1
                if i >= len(child_nodes):
                    break
                index_expr = self.visit(child_nodes[i])
                i += 1
                if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.RBRACK:
                    i += 1
                current_code = f"{current_code}[{index_expr}]"
                current_accessor = "."
            else:
                i += 1  # 跳过意外节点

        return current_code

    def visitBaseType(self, ctx: ChronoParser.BaseTypeContext):
        """
        [新增] 访问 'baseType' 规则。
        处理:
        1. 命名空间: "std.string" -> "std::string"
        2. 别名: "Math.Type" -> "MyMath::Type"
        3. $类型: "$String" -> "String*"
        4. 基础类型: "i32" -> "int32_t"
        """
        raw_text = ctx.getText()  # (例如 "std.string", "$String", "i32")

        parts = raw_text.split('.')
        first_part = parts[0]

        # 1. 检查别名
        if first_part in self._alias_to_namespace_map:
            parts[0] = self._alias_to_namespace_map[first_part]

        cpp_namespace_type = "::".join(parts)  # (例如 "std::string", "$String")

        # 2. 检查 $ 标记 (用于泛型参数)
        if cpp_namespace_type.startswith('$'):
            base = cpp_namespace_type.lstrip('$')
            return f"{self._chrono_to_cpp_type(base)}*"  # (例如 "String*")

        # 3. 检查基础类型
        return self._chrono_to_cpp_type(cpp_namespace_type)  # (例如 "std::string", "int32_t")

    def visitDeclaration(self, ctx: ChronoParser.DeclarationContext):
        var_name = ctx.variableName.text
        key = var_name
        cpp_name = var_name

        # --- [ 升级 ] ---
        # 之前的: base_type_cpp = self._translate_type_string(...)
        # 现在的: 我们访问新的 'typeSpecifier' 规则
        base_type_cpp = self.visit(ctx.typeName)
        # (例如 "std::vector<int32_t>" 或 "std::string" 或 "int32_t[5]")
        # --- [ 升级结束 ] ---

        accessor = "."
        is_pointer = False

        if var_name.startswith('$'):
            accessor = "->"
            is_pointer = True
            cpp_name = f"_{var_name.lstrip('$')}"
        else:
            accessor = "."
            is_pointer = False
            if base_type_cpp in _ACCESSOR_EXCEPTION_LIST or "::iterator" in base_type_cpp:
                accessor = "->"

        cpp_final_type = f"{base_type_cpp}*" if is_pointer else base_type_cpp

        # [ [ 关键修复：数组 ] ]
        # 如果类型是数组 (例如 "int32_t[5]")，我们需要将名称放在类型和方括号之间
        # "int32_t[5]" (base_type_cpp) + "numbers" (cpp_name)
        # 变为: "int32_t numbers[5]"

        is_c_array = False
        if not is_pointer and '[' in base_type_cpp and base_type_cpp.endswith(']'):
            is_c_array = True
            parts = base_type_cpp.split('[')
            base_only = parts[0]  # "int32_t"
            array_part = '[' + parts[1]  # "[5]"

            # C++ 最终类型现在是 "int32_t"
            cpp_final_type = base_only
            # C++ 名称现在是 "numbers[5]"
            cpp_name = f"{cpp_name}{array_part}"

            # (访问器保持为 '.')

        self._add_variable(key, {
            "cpp_name": cpp_name if not is_c_array else ctx.variableName.text,  # 作用域栈使用 'numbers'
            "accessor": accessor,
            "cpp_type": cpp_final_type if not is_c_array else base_type_cpp  # 作用域栈使用 'int32_t[5]'
        })

        # ... (I. 局部变量 和 II. 类成员 逻辑) ...
        # I. 局部变量
        if not self._in_class or self._in_class_method:
            cpp_value = ""

            # [修改] 数组不需要 ' = nullptr' 或 ' = 0'
            if not is_c_array:
                if is_pointer:
                    cpp_value = " = nullptr"
                elif base_type_cpp == "bool":
                    cpp_value = " = false"
                elif base_type_cpp in ("int32_t", "int64_t"):
                    cpp_value = " = 0"
                # (std::string 和 std::vector 会被默认构造, 这是正确的)

            if ctx.expression():
                cpp_value = f" = {self.visit(ctx.expression())}"

            return f"{INDENT}{cpp_final_type} {cpp_name}{cpp_value};\n"

        # II. 类成员
        else:
            access = getattr(ctx, '_chrono_access', 'private')
            # [修改] C-Style 数组在类中也需要特殊处理
            if is_c_array:
                declaration_line = f"{INDENT}{cpp_final_type} {cpp_name};\n"
            else:
                declaration_line = f"{INDENT}{cpp_final_type} {cpp_name};\n"

            self._class_sections[access] += declaration_line
            return ""

    def visitParameter(self, ctx: ChronoParser.ParameterContext):
        var_name = ctx.name.text
        key = var_name
        cpp_name = var_name

        # --- [ 升级 ] ---
        # 现在的: 我们访问新的 'typeSpecifier' 规则
        base_type_cpp = self.visit(ctx.typeName)
        # --- [ 升级结束 ] ---

        accessor = "."
        is_pointer = False

        if var_name.startswith('$'):
            accessor = "->"
            is_pointer = True
            cpp_name = f"_{var_name.lstrip('$')}"
        elif base_type_cpp in _ACCESSOR_EXCEPTION_LIST or "::iterator" in base_type_cpp:
            accessor = "->"
            is_pointer = False

        cpp_final_type = f"{base_type_cpp}*" if is_pointer else base_type_cpp

        # [ [ 新增：处理 C-Style 数组参数 ] ]
        # C++ 不允许值传递 C-Style 数组，它们会衰变为指针。
        # [i32; 5] 必须翻译为 int32_t*
        # (我们在此处不支持 C++20 的 std::array)
        is_c_array = False
        if not is_pointer and '[' in base_type_cpp and base_type_cpp.endswith(']'):
            is_c_array = True
            parts = base_type_cpp.split('[')
            base_only = parts[0]  # "int32_t"

            # 将 'int32_t[5]' 衰变为 'int32_t*'
            cpp_final_type = f"{base_only}*"
            # 访问器应为 '->' (虽然我们不能索引它)
            accessor = "->"

        self._add_variable(key, {
            "cpp_name": cpp_name,
            "accessor": accessor,
            "cpp_type": cpp_final_type
        })

        return f"{cpp_final_type} {cpp_name}"

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
            # --- [ 升级 ] ---
            cpp_return_type = self.visit(ctx.returnType)
            # --- [ 升级结束 ] ---

            if func_name == "main":  # 'main' 必须返回 'int'
                cpp_return_type = "int"
                cpp_func_name = "main"
            else:
                # [ [ 修复 ] ]
                # 我们不再检查类型，因为 visitTypeSpecifier
                # 已经返回了 "String*" 或 "int32_t"
                cpp_func_name = func_name.lstrip('$')
        else:
            cpp_return_type = "void"
            cpp_func_name = func_name.lstrip('$')

        static_prefix = "static " if is_static else ""
        self._exit_scope()
        return (
            f"\n{static_prefix} {cpp_return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            "}\n"
        )

    def visitPrimary(self, ctx: ChronoParser.PrimaryContext):
        if ctx.NEW():
            # --- [ 升级 ] ---
            # 之前的: class_name = self._chrono_to_cpp_type(ctx.IDENTIFIER().getText())
            # 现在的: 访问 'baseType' 规则
            class_name = self.visit(ctx.baseType())
            # (注意: 'new' 不支持泛型参数, 'new std.vector[i32]()' 语法无效)
            # (我们的语法 只支持 'new baseType()')
            # --- [ 升级结束 ] ---

            args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
            return f"new {class_name}({args})"

        if ctx.literal():
            return self.visit(ctx.literal())

        # [ [ 新增 ] ]
        if ctx.initializerList():
            return self.visit(ctx.initializerList())

        if ctx.IDENTIFIER():
            primary_text = ctx.IDENTIFIER().getText()
            variable_info = self._find_variable(primary_text)
            if variable_info:
                # [ [ 关键修复：数组 ] ]
                # 如果我们访问 'numbers' (一个 C 数组)
                # 我们必须返回它的 C++ 名称 ("numbers")
                # 而不是它的 (可能被修改的) "cpp_name" ("numbers[5]")
                if '[' in variable_info["cpp_type"]:
                    return ctx.IDENTIFIER().getText().lstrip('$')

                return variable_info["cpp_name"]
            else:
                # (处理 "String.create()" 中的 "String")
                return self._chrono_to_cpp_type(primary_text.lstrip('$'))

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
        if ctx.declaration():
            return self.visit(ctx.declaration())
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
        return f"{INDENT}{target} = {value};\n"

        # [ 替换 ] visitAssignableExpression
        # src/ChronoVisitor.py

    def visitAssignableExpression(self, ctx: ChronoParser.AssignableExpressionContext):
        """
        [修改] 访问 'assignableExpression' 规则。
        处理:
        1. 链式调用: .foo
        2. 数组索引: [i]
        """
        # 1. 访问第一个环节 (例如 "$s", "this", "numbers")
        if ctx.THIS():
            primary_text = "this"
        else:
            primary_text = ctx.IDENTIFIER(0).getText()

        # 2. 决定“第一个”访问器
        current_accessor = None
        variable_info = self._find_variable(primary_text)

        if variable_info:
            # 案例 A: 这是一个已知的变量 (s, p, this)

            # [ [ 关键修复：数组 ] ]
            # 如果我们访问 'numbers' (一个 C 数组)
            # 我们必须返回它的 C++ 名称 ("numbers")
            if '[' in variable_info["cpp_type"]:
                current_code = ctx.IDENTIFIER(0).getText().lstrip('$')
            else:
                current_code = variable_info["cpp_name"]  # (例如 "_s" 或 "s")

            current_accessor = variable_info["accessor"]
        else:
            # 后备情况 (例如静态访问)
            current_code = self._chrono_to_cpp_type(primary_text)
            current_accessor = "::"

        # 3. 遍历链条 (DOT IDENTIFIER | LBRACK ...)*
        child_nodes = ctx.children[1:]  # 获取第一个 IDENTIFIER/THIS 之后的所有内容
        i = 0
        while i < len(child_nodes):

            if child_nodes[i].getSymbol().type == ChronoParser.DOT:
                # --- 路径 A: 成员访问 (.foo) ---
                i += 1  # 跳过 DOT
                ident_node = child_nodes[i]
                i += 1

                raw_ident_text = ident_node.getText()
                cpp_ident = f"_{raw_ident_text.lstrip('$')}" if raw_ident_text.startswith('$') else raw_ident_text

                current_code = f"{current_code}{current_accessor}{cpp_ident}"

                # 更新下一次访问的访问器 (启发式)
                current_accessor = "->"
                if cpp_ident and cpp_ident[0].isupper():
                    current_accessor = "::"

            elif child_nodes[i].getSymbol().type == ChronoParser.LBRACK:
                # --- 路径 B: 数组索引 ([i]) ---
                i += 1  # 跳过 [
                index_expr = self.visit(child_nodes[i])  # 访问 'expression'
                i += 2  # 跳过 'expression' 和 ']'

                current_code = f"{current_code}[{index_expr}]"

                # C++ 中数组索引后, 访问器必须是 '.' 或 '->'
                current_accessor = "."  # 假定值类型

            else:
                # (不应该发生)
                i += 1

        return current_code

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
        # [修改] 现在调用 unaryExpression
        lhs = self.visit(ctx.unaryExpression(0))

        if ctx.unaryExpression(1):
            rhs = self.visit(ctx.unaryExpression(1))
            # [修改结束]
            op = ""
            if ctx.EQ():
                op = "=="
            elif ctx.NEQ():
                op = "!="
            elif ctx.LT():
                op = "<"
            elif ctx.GT():
                op = ">"
            elif ctx.LTE():
                op = "<="
            elif ctx.GTE():
                op = ">="
            # [新增] 算术翻译 (使用 hasattr 防御性检查)
            elif hasattr(ctx, 'PLUS') and ctx.PLUS():
                op = "+"
            elif hasattr(ctx, 'MINUS') and ctx.MINUS():
                op = "-"
            elif hasattr(ctx, 'STAR') and ctx.STAR():
                op = "*"
            elif hasattr(ctx, 'SLASH') and ctx.SLASH():
                op = "/"
            else:
                raise Exception("Unknown comparison operator")
            return f"{lhs} {op} {rhs}"
        else:
            return lhs

        # src/ChronoVisitor.py (在 visitExpression 下方添加)

    def visitUnaryExpression(self, ctx: ChronoParser.UnaryExpressionContext):
        """
        [新增] 访问新的一元表达式规则 (处理 -8)
        """
        if ctx.simpleExpression():
            # 路径 A: 这是一个没有一元运算符的常规表达式 (例如 "8")
            return self.visit(ctx.simpleExpression())

        # 路径 B: 这是一个带一元运算符的表达式 (例如 "-8")
        op = ""
        if ctx.MINUS():
            op = "-"
        elif ctx.PLUS():
            op = "+"

        # 递归访问操作数
        operand = self.visit(ctx.unaryExpression())

        # C++ 原生支持一元 + 和 -
        return f"{op}{operand}"  # (例如: "-8" 或 "+10")

    # [新增] 访问 delete 语句
    def visitDeleteStatement(self, ctx: ChronoParser.DeleteStatementContext):
        target = self.visit(ctx.expression())
        return f"{INDENT}delete {target};\n"

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

    def visitFunctionCallExpression(self, ctx: ChronoParser.FunctionCallExpressionContext):
        # --- [ 关键修复 ] ---
        func_name = ctx.name.text
        cpp_func_name = func_name.lstrip('$')  # 剥离 $
        # --- [ 修复结束 ] ---

        args_list = []
        if ctx.expressionList():
            for arg_expr in ctx.expressionList().expression():
                arg_code = self.visit(arg_expr)

                args_list.append(arg_code)

        args_code = ", ".join(args_list)

        return f"{cpp_func_name}({args_code})"  # 使用剥离 $ 后的名称
        # --- [ 修复结束 ] ---