# src/ChronoVisitor.py

from antlr4 import *
from parser.ChronoParser import ChronoParser
from parser.ChronoParserVisitor import ChronoParserVisitor as BaseChronoVisitor
from antlr4.tree.Tree import TerminalNodeImpl  # 导入 TerminalNodeImpl

INDENT = "    "


class ChronoVisitor(BaseChronoVisitor):

    def __init__(self):
        super().__init__()
        self._in_class_method = False
        self._in_class = False
        self._current_class_name = None
        # [新增] Class Assembler 状态
        self._class_sections = {"private": "", "public": ""}

    # ... (在 __init__ 之后) ...

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
        if chrono_type_name == "int" or chrono_type_name == "i32":
            return "int32_t"
        if chrono_type_name == "i64":
            return "int64_t"
        if chrono_type_name == "String":
            return "ChronoString"
        if chrono_type_name == "Int":
            return "ChronoInt"
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
        main_wrapper = (
            "\n// C++ 程序的标准入口\n"
            "int main() {\n"
            f"{INDENT}return Chrono_main();\n"
            "}\n"
        )
        return all_code + main_wrapper

    def visitImportDirective(self, ctx: ChronoParser.ImportDirectiveContext):
        path_text = ctx.path.text
        if path_text.startswith('<'):
            return f"#include {path_text}\n"
        elif path_text.startswith('"'):
            path_content = path_text[1:-1]
            if path_content.startswith('runtime/'):
                path_content = path_content.replace('runtime/', '')
            return f'#include "{path_content}"\n'
        return f"// ERROR: Invalid import path {path_text}\n"

    # 替换 [visitClassDefinition] (移除重复的 行)
    def visitClassDefinition(self, ctx: ChronoParser.ClassDefinitionContext):
        class_name = ctx.name.text
        base_name = ctx.base.text

        self._in_class = True
        self._current_class_name = class_name
        self._class_sections = {"private": "", "public": ""}

        # 遍历 classBodyStatement 规则
        if hasattr(ctx, 'classBodyStatement'):
            for child in ctx.classBodyStatement():
                self.visit(child)  # <--- 这将调用 visitClassBodyStatement

        self._in_class = False
        self._current_class_name = None

        # [修复] 组装 C++ 类体 (移除了重复代码 )
        final_class_body = ""

        # 1. 输出 private (默认)
        if self._class_sections["private"]:
            final_class_body += "\nprivate:\n"
            final_class_body += self._class_sections["private"]

        # 2. 输出 public
        if self._class_sections["public"]:
            final_class_body += "\npublic:\n"
            final_class_body += self._class_sections["public"]

        return (
            f"\nclass {class_name} : public {base_name} {{\n"
            f"{final_class_body.strip()}\n"  # <-- 现在只包含正确的代码
            "};\n"
        )

    # [新增] visitClassBodyStatement (用于传递修饰符)
    def visitClassBodyStatement(self, ctx: ChronoParser.ClassBodyStatementContext):
        # 1. 确定修饰符
        is_static = hasattr(ctx, 'STATIC') and ctx.STATIC()
        access = self._get_access_level(ctx)

        print("===>", type(ctx))
        child_type_name = type(ctx).__name__
        print(child_type_name)
        print("child text: ", ctx.getText())

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

    def visitMethodDefinition(self, ctx: ChronoParser.MethodDefinitionContext):
        self._in_class_method = True
        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        is_static = getattr(ctx, '_chrono_static', False)
        access = getattr(ctx, '_chrono_access', 'private')

        # --- (签名逻辑...) ---
        if ctx.returnType:
            return_type = ctx.returnType.text
            if return_type in ("i32", "i64", "int", "bool"):
                cpp_return_type = self._chrono_to_cpp_type(return_type)
            else:
                cpp_return_type = f"{self._chrono_to_cpp_type(return_type)}*"
            cpp_func_name = func_name
        else:
            cpp_return_type = "void"
            cpp_func_name = func_name

        # --- [ 关键移除 ] ---
        # 'if func_name == "init":' 这一段特殊逻辑已被删除
        # --- (签名逻辑结束) ---

        static_prefix = "static " if is_static else ""

        func_def_code = (
            f"\n{INDENT}{static_prefix}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            f"{INDENT}// --- Method End ---\n"
            f"{INDENT}}}\n"
        )

        self._class_sections[access] += func_def_code
        self._in_class_method = False
        return ""

    def visitInitDefinition(self, ctx: ChronoParser.InitDefinitionContext):
        self._in_class_method = True

        # C++ 构造函数没有返回类型
        cpp_return_type = ""
        # 构造函数名称就是类名
        cpp_func_name = self._current_class_name

        # 1. 读取访问修饰符 (构造函数可以是 private/public)
        access = getattr(ctx, '_chrono_access', 'private')

        # 2. 访问参数和函数体
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        # 3. 组装 C++ 构造函数
        init_code = (
            f"\n{INDENT}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            f"{INDENT}}}\n"
        )

        # 4. 追加到 Class Assembler
        self._class_sections[access] += init_code

        self._in_class_method = False
        return ""

    # 你的 ChronoVisitor.py 文件
    def visitDeinitBlock(self, ctx: ChronoParser.DeinitBlockContext):
        # [关键修复] 使用安全迭代
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        # [修复] 组装析构函数代码
        deinit_code = (
            f"\n{INDENT}virtual ~{self._current_class_name}() {{\n"
            f"{INDENT}// --- Chrono Deinit Block ---\n"
            f"{body_code}"  # clang-format 会处理缩进
            f"{INDENT}// --- Deinit End ---\n"
            f"{INDENT}}}\n"
        )

        # [修复] 析构函数必须是 public 才能被 'delete' 调用
        # 将其追加到 Class Assembler，而不是 return
        self._class_sections["public"] += deinit_code

        return ""  # 返回空字符串，因为代码已被追加

    def visitDeclaration(self, ctx: ChronoParser.DeclarationContext):
        var_name = ctx.variableName.text
        type_name = ctx.typeName.text
        cpp_type = self._chrono_to_cpp_type(type_name)
        cpp_class_name = cpp_type
        cpp_value = ""

        # I. 局部变量
        if not self._in_class or self._in_class_method:
            if type_name in ("i32", "i64", "int", "bool"):
                cpp_value = "false" if type_name == "bool" else "0"
                if ctx.expression():
                    cpp_value = self.visit(ctx.expression())
                return f"{INDENT}{cpp_type} {var_name} = {cpp_value};\n"
            else:
                cpp_type = f"{cpp_type}*"
                cpp_value = "nullptr"
                if ctx.expression():
                    expression_code = self.visit(ctx.expression())
                    expression_node = ctx.expression()
                    if (expression_node.simpleExpression(0) and
                            not expression_node.simpleExpression(1) and
                            expression_node.simpleExpression(0).primary() and
                            expression_node.simpleExpression(0).primary().literal()):
                        cpp_value = f"{cpp_class_name}::create({expression_code})"
                    else:
                        cpp_value = expression_code
                return f"{INDENT}{cpp_type}  {var_name} = {cpp_value};\n"

        # II. 类成员
        else:
            # [修复] 从父级注入的属性中读取修饰符
            access = getattr(ctx, '_chrono_access', 'private')

            if type_name in ("i32", "i64", "int", "bool"):
                declaration_line = f"{INDENT}{cpp_type} {var_name};\n"
            else:
                cpp_type = f"{cpp_type}*"
                declaration_line = f"{INDENT}{cpp_type} {var_name};\n"

            self._class_sections[access] += declaration_line
            return ""

    def visitFunctionDefinition(self, ctx: ChronoParser.FunctionDefinitionContext):
        func_name = ctx.name.text
        params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

        # [修复 1: 解决 NoneType 错误]
        statements = self._safe_iterate_statements(ctx.statement())
        body_code = "".join(self.visit(s) for s in statements)

        is_static = False
        if hasattr(ctx, 'STATIC') and ctx.STATIC():
            is_static = True

        # --- (其余逻辑保持不变) ---
        if ctx.returnType:
            return_type = ctx.returnType.text
            if func_name == "main" and return_type == "Int":
                cpp_return_type = "int"
                cpp_func_name = "Chrono_main"
            else:
                if return_type in ("i32", "i64", "int", "bool"):
                    cpp_return_type = self._chrono_to_cpp_type(return_type)
                else:
                    cpp_return_type = f"{self._chrono_to_cpp_type(return_type)}*"
                cpp_func_name = func_name
        else:
            cpp_return_type = "void"
            if func_name == "init":
                cpp_return_type = ""
                cpp_func_name = self._current_class_name
            else:
                cpp_func_name = func_name

        static_prefix = "static " if is_static else ""

        return (
            f"\n{static_prefix} {cpp_return_type} {cpp_func_name}({params_code}) {{\n"
            f"{body_code}"
            "}\n"
        )

    def visitParameters(self, ctx: ChronoParser.ParametersContext):
        params_list = []
        for p in ctx.parameter():
            params_list.append(self.visit(p))
        return ", ".join(params_list)

    def visitParameter(self, ctx: ChronoParser.ParameterContext):
        name = ctx.name.text
        type_name = ctx.typeName.text

        if type_name in ("i32", "i64", "int", "bool"):
            cpp_type = self._chrono_to_cpp_type(type_name)
            return f"{cpp_type} {name}"
        else:
            cpp_type = f"{self._chrono_to_cpp_type(type_name)}*"
            return f"{cpp_type} {name}"

    # --- 语句 ---

    # [ 已修正 ]
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

    def visitAssignableExpression(self, ctx: ChronoParser.AssignableExpressionContext):
        current_code = ""
        if ctx.THIS():
            current_code = "this"
        else:
            current_code = ctx.IDENTIFIER(0).getText()

        is_first_ident = True
        for ident_node in ctx.IDENTIFIER():
            if is_first_ident and not ctx.THIS():
                is_first_ident = False
                continue

            if is_first_ident and ctx.THIS():
                current_code = f"this->{ident_node.getText()}"
                is_first_ident = False
                continue

            ident = ident_node.getText()
            current_code = f"{current_code}->{ident}"

        return current_code

    # --- [ 新增 ] 流程控制方法 ---

    # src/ChronoVisitor.py (最终的 visitIfStatement)

    # [ 关键修复 ] 重写以支持 'else if' 链 (使用标签)
    # --- [ 新增的调试辅助函数 ] ---
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

    # to ai助手：不要删除这个方法，以便调试 --- [ 新增的调试辅助函数 ] ---
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

        # --- [ 替换 visitIfStatement ] ---

    def visitIfStatement(self, ctx: ChronoParser.IfStatementContext):

        # --- [ 彻底分析 ctx (递归) ] ---
        print("\n--- DEBUG: [Recursive Analysis] visitIfStatement ---")
        print(f"Analyzing 'if' statement at line {ctx.start.line}")
        print("Starting recursive analysis of the 'if' context (ctx):")

        print(type(ctx))
        # print(dir(ctx))
        # 获得ExpressionContext | 测试表达式  eg. 'x>5'
        print("=" * 40)
        node_text = ""
        for child in ctx.children:
            print("===>", type(child))
            child_type_name = type(child).__name__
            print(child_type_name)
            print("child text: ", child.getText())
            # 首先我们必然会遇到一个判断表达式，ExpressionContext 例如（ture）
            if child_type_name == "TerminalNodeImpl":
                node_text += child.getText() + " "

            if child_type_name == "ExpressionContext":
                print("find ExpressionContext!")
                node_text += self.visitExpression(child)
            # 然后我们会遇到一些StatementContext，这些可能是语句，也可能是又一个if block 或者else，我们必须区分
            elif child_type_name == "StatementContext":
                print("find StatementContext!============")
                print(child.getText())
                # print(dir(child))
                node_text += self.visitStatement(child) + "\n"
            elif child_type_name == "IfStatementContext":
                node_text += self.visitIfStatement(child)

                print("-" * 40)
        print("node code: ", node_text)

        # 如果有，获得StatementContext|if内部的语句 eg: 'print("ok");'
        return node_text
        # 启动递归分析
        self._recursive_analyze(ctx)

        print("\n--- DEBUG: Analysis Complete. Exiting. ---")
        import sys
        sys.exit(1)  # 强制退出程序

    def visitWhileStatement(self, ctx: ChronoParser.WhileStatementContext):
        condition = self.visit(ctx.expression())

        indent = INDENT * 2 if self._in_class else INDENT

        # [ 关键修复 ] While 块只有一组语句，直接使用 children 过滤
        body_code = self._process_block_children(ctx.children)
        body_code_indented = body_code.replace(INDENT, indent)

        code = f"{INDENT}while ({condition}) {{\n"
        code += body_code_indented
        code += f"{INDENT}}}\n"
        return code

    # 'visitExpression' 现在是新的顶层, 处理比较
    def visitExpression(self, ctx: ChronoParser.ExpressionContext):
        lhs = self.visit(ctx.simpleExpression(0))
        if ctx.simpleExpression(1):
            rhs = self.visit(ctx.simpleExpression(1))
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

    # [ 已重命名/修正 ] 这是我们旧的 'visitExpression'
    # 它现在处理链式调用和全局函数调用
    def visitSimpleExpression(self, ctx: ChronoParser.SimpleExpressionContext):
        if ctx.functionCallExpression():
            return self.visit(ctx.functionCallExpression())

        # 这处理 'primary ( DOT IDENTIFIER (LPAREN ...)? )*' 规则
        current_code = self.visit(ctx.primary())

        is_static = False
        if ctx.primary().IDENTIFIER():
            if ctx.primary().IDENTIFIER().getText()[0].isupper():
                is_static = True

        child_nodes = ctx.children[1:]

        i = 0
        while i < len(child_nodes):
            i += 1
            ident = child_nodes[i].getText()
            i += 1

            if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.LPAREN:
                i += 1
                args = ""
                if i < len(child_nodes) and isinstance(child_nodes[i], ChronoParser.ExpressionListContext):
                    args = self.visit(child_nodes[i])
                    i += 1
                i += 1

                if is_static:
                    current_code = f"{current_code}::{ident}({args})"
                else:
                    current_code = f"{current_code}->{ident}({args})"
                is_static = False
            else:
                if is_static:
                    current_code = f"{current_code}::{ident}"
                else:
                    current_code = f"{current_code}->{ident}"

                if ident[0].isupper():
                    is_static = True

        return current_code

    def visitPrimary(self, ctx: ChronoParser.PrimaryContext):
        if ctx.literal():
            return self.visit(ctx.literal())

        if ctx.IDENTIFIER():
            # 必须翻译 'String' -> 'ChronoString'
            chrono_name = ctx.IDENTIFIER().getText()
            return self._chrono_to_cpp_type(chrono_name)

        if ctx.THIS():
            return "this"

        if ctx.LPAREN():
            return f"({self.visit(ctx.expression())})"

        return ""

    def visitExpressionList(self, ctx: ChronoParser.ExpressionListContext):
        return ", ".join(self.visit(e) for e in ctx.expression())

    # [ 已修正 ]
    def visitLiteral(self, ctx: ChronoParser.LiteralContext):
        if ctx.BOOL_LITERAL():
            return ctx.BOOL_LITERAL().getText()
        return ctx.getText()

    # [ 已修正 ]
    def visitFunctionCallExpression(self, ctx: ChronoParser.FunctionCallExpressionContext):
        func_name = ctx.name.text

        args_list = []
        if ctx.expressionList():
            for arg_expr in ctx.expressionList().expression():
                arg_code = self.visit(arg_expr)

                if func_name == "print" or func_name[0].isupper():
                    # [ 关键修复 ] 必须检查新的 'simpleExpression' 结构
                    if (arg_expr.simpleExpression(0) and
                            not arg_expr.simpleExpression(1) and  # 确保它不是一个比较
                            arg_expr.simpleExpression(0).primary() and
                            arg_expr.simpleExpression(0).primary().literal()):

                        literal_node = arg_expr.simpleExpression(0).primary().literal()

                        if literal_node.STRING_LITERAL():
                            args_list.append(f"ChronoString::create({arg_code})")
                        elif literal_node.INTEGER_LITERAL():
                            if func_name == "print":
                                args_list.append(f"ChronoInt::create({arg_code})")
                            else:
                                args_list.append(arg_code)  # 构造器, 假定 i32
                        elif literal_node.BOOL_LITERAL():
                            args_list.append(arg_code)  # bool, 按原样传递
                        else:
                            args_list.append(arg_code)
                    else:
                        args_list.append(arg_code)  # 变量或方法调用
                else:
                    args_list.append(arg_code)  # 普通全局函数

        args_code = ", ".join(args_list)

        if func_name == "print":
            return f"Print({args_code})"
        elif func_name[0].isupper():
            return f"new {func_name}({args_code})"
        else:
            return f"{func_name}({args_code})"
