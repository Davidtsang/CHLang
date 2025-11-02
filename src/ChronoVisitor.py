# src/ChronoVisitor.py

from antlr4 import *
from parser.ChronoParser import ChronoParser
from parser.ChronoParserVisitor import ChronoParserVisitor as BaseChronoVisitor

INDENT = "    " 

class ChronoVisitor(BaseChronoVisitor):

    def __init__(self):
        super().__init__()
        self._in_class = False
        self._current_class_name = None

    # --- 辅助函数 ---
    def _chrono_to_cpp_type(self, chrono_type_name):
        if chrono_type_name == "int" or chrono_type_name == "i32":
            return "int32_t"
        if chrono_type_name == "i64":
            return "int64_t"
        if chrono_type_name == "String":
            return "ChronoString"
        if chrono_type_name == "Int":
            return "ChronoInt"
        return chrono_type_name

# [ 已修正 ]
    def visitProgram(self, ctx: ChronoParser.ProgramContext):
        
        # 1. 访问所有顶层语句 (imports, @cpp, class, func)
        #    ctx.topLevelStatement() 返回一个单一的、有序的列表
        #    这 100% 保证了 C++ 输出中的顺序
        all_code = "".join(self.visit(stmt) for stmt in ctx.topLevelStatement())
        
        # 2. 组装 main 包装器
        main_wrapper = (
            "\n// C++ 程序的标准入口\n"
            "int main() {\n"
            f"{INDENT}return Chrono_main();\n"
            "}\n"
        )
        
        # 3. 按正确顺序返回所有代码
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

    def visitClassDefinition(self, ctx: ChronoParser.ClassDefinitionContext):
        class_name = ctx.name.text
        base_name = ctx.base.text
        
        self._in_class = True
        self._current_class_name = class_name
        
        body_code = ""
        # [ 已修正 ] 遍历所有可能的子节点
        # (这比单独的 for 循环更健壮)
        for child in ctx.children:
            if isinstance(child, (ChronoParser.DeclarationContext,
                                ChronoParser.FunctionDefinitionContext,
                                ChronoParser.DeinitBlockContext,
                                ChronoParser.CppBlockContext)):
                body_code += self.visit(child)
            
        self._in_class = False
        self._current_class_name = None
        
        return (
            f"\nclass {class_name} : public {base_name} {{\n"
            "public:\n"
            f"{body_code}"
            "};\n"
        )
    
    def visitDeinitBlock(self, ctx: ChronoParser.DeinitBlockContext):
        body_code = "".join(self.visit(s) for s in ctx.statement())
        return (
            f"\n{INDENT}virtual ~{self._current_class_name}() {{\n"
            f"{INDENT}// --- Chrono Deinit Block ---\n"
            f"{body_code}"
            f"{INDENT}// --- Deinit End ---\n"
            f"{INDENT}}}\n"
        )

# src/ChronoVisitor.py

    # [ 已修正 ] 替换此方法
    def visitFunctionDefinition(self, ctx: ChronoParser.FunctionDefinitionContext):
            func_name = ctx.name.text
            params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""
            body_code = "".join(self.visit(s) for s in ctx.statement())
            
            cpp_return_type = ""
            cpp_func_name = ""
            
            # [ 新增 ] 检查 static 关键字
            is_static = True if ctx.STATIC() else False
            
            if ctx.returnType:
                return_type = ctx.returnType.text
                if func_name == "main" and return_type == "Int":
                    cpp_return_type = "int"
                    cpp_func_name = "Chrono_main"
                else:
                    if return_type in ("i32", "i64", "int"):
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
            
            indent = INDENT*2 if self._in_class else INDENT
            
            # [ 新增 ] 如果在类中且为 static, 添加 'static'
            static_prefix = "static " if (self._in_class and is_static) else ""

            if self._in_class:
                return (
                    f"\n{INDENT}{static_prefix}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
                    f"{body_code.replace(INDENT, indent)}"
                    f"{indent}// --- Method End ---\n"
                    f"{INDENT}}}\n"
                )
            else:
                return (
                    f"\n{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
                    f"{INDENT}// --- Chrono Function Body: {func_name} ---\n"
                    f"{body_code}"
                    f"{INDENT}// --- Function End ---\n"
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
        
        if type_name in ("i32", "i64", "int"):
            cpp_type = self._chrono_to_cpp_type(type_name)
            return f"{cpp_type} {name}"
        else:
            cpp_type = f"{self._chrono_to_cpp_type(type_name)}*"
            return f"{cpp_type} {name}"

    # --- 语句 ---
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
            
        return ""

# [ 已修正 ] 替换这个方法
    def visitDeclaration(self, ctx: ChronoParser.DeclarationContext):
        var_name = ctx.variableName.text
        type_name = ctx.typeName.text
        
        cpp_type = ""
        
        if type_name in ("i32", "i64", "int"):
            cpp_type = self._chrono_to_cpp_type(type_name)
            if self._in_class:
                return f"{INDENT}{cpp_type} {var_name};\n"
            else:
                cpp_value = "0"
                if ctx.expression():
                    cpp_value = self.visit(ctx.expression())
                return f"{INDENT}const {cpp_type} {var_name} = {cpp_value};\n"
        else:
            # --- 引用类型 (String, MyClass, etc.) ---
            cpp_class_name = self._chrono_to_cpp_type(type_name)
            cpp_type = f"{cpp_class_name}*"
            
            if self._in_class:
                return f"{INDENT}{cpp_type} {var_name};\n"
            else:
                cpp_value = "nullptr"
                if ctx.expression():
                    expression_code = self.visit(ctx.expression())
                    expression_node = ctx.expression()
                    
                    # [ 关键修复 ] 检查 'primary().literal()'
                    if expression_node.primary() and expression_node.primary().literal():
                        # 是字面量, 自动调用 .create()
                        cpp_value = f"{cpp_class_name}::create({expression_code})"
                    else:
                        # 是函数调用/变量/方法, 按原样使用
                        cpp_value = expression_code
                
                return f"{INDENT}{cpp_type} const {var_name} = {cpp_value};\n"

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
    
    # [ 已修正 ]
    # [ 已修正 ] 替换这个方法
    def visitAssignment(self, ctx: ChronoParser.AssignmentContext):
        # 左侧 (目标)
        target = self.visit(ctx.assignableExpression())
        # 右侧 (值)
        value = self.visit(ctx.expression())
        return f"{INDENT}{target} = {value};\n"

# [ 新增 ] 'visitAssignment' 需要这个方法
    def visitAssignableExpression(self, ctx: ChronoParser.AssignableExpressionContext):
        current_code = ""
        if ctx.THIS():
            current_code = "this"
        else:
            # 它是 'my_var' 或 'MyClass'
            current_code = ctx.IDENTIFIER(0).getText()
        
        is_first_ident = True
        for ident_node in ctx.IDENTIFIER():
            # 1. 跳过第一个 IDENTIFIER (如果不是 'this')
            if is_first_ident and not ctx.THIS():
                is_first_ident = False
                continue
            
            # 2. 处理 'this.member'
            if is_first_ident and ctx.THIS():
                current_code = f"this->{ident_node.getText()}"
                is_first_ident = False
                continue

            # 3. 处理链 (e.g., this.member.field)
            ident = ident_node.getText()
            current_code = f"{current_code}->{ident}"

        return current_code
    
    # [ 已修正 ] 替换这个方法
    def visitExpression(self, ctx: ChronoParser.ExpressionContext):
        if ctx.functionCallExpression():
            return self.visit(ctx.functionCallExpression())
        
        # 这处理 'primary ( DOT IDENTIFIER (LPAREN ...)? )*' 规则
        current_code = self.visit(ctx.primary())
        
        is_static = False
        # 检查 'primary' 是否是一个大写标识符 (例如 'String.create')
        if ctx.primary().IDENTIFIER():
                if ctx.primary().IDENTIFIER().getText()[0].isupper():
                    is_static = True

        # 遍历链式调用的其余部分 (DOT, IDENTIFIER, LPAREN, etc.)
        child_nodes = ctx.children[1:]
        
        i = 0
        while i < len(child_nodes):
            # child_nodes[i] 是 DOT, 我们跳过它
            i += 1 
            ident = child_nodes[i].getText()
            i += 1
            
            # 检查是否有 '('，判断是方法调用还是字段访问
            if i < len(child_nodes) and child_nodes[i].getSymbol().type == ChronoParser.LPAREN:
                # --- 是方法调用 (e.g., .method(args)) ---
                i += 1 # 跳过 LPAREN
                args = ""
                if i < len(child_nodes) and isinstance(child_nodes[i], ChronoParser.ExpressionListContext):
                    args = self.visit(child_nodes[i])
                    i += 1 # 跳过 ExpressionList
                i += 1 # 跳过 RPAREN
                
                if is_static:
                    current_code = f"{current_code}::{ident}({args})"
                else:
                    current_code = f"{current_code}->{ident}({args})"
                is_static = False # 调用后重置静态标志
            else:
                # --- 是字段访问 (e.g., .field) ---
                if is_static:
                    current_code = f"{current_code}::{ident}"
                else:
                    current_code = f"{current_code}->{ident}"
                
                # 检查这个新字段是否是一个静态类
                if ident[0].isupper():
                    is_static = True
        
        return current_code

# [ 已修正 ] 用这个版本替换
    def visitPrimary(self, ctx: ChronoParser.PrimaryContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        
        if ctx.IDENTIFIER():
            # [ 关键修复 ]
            # 我们必须翻译标识符, 以便 'String' 变为 'ChronoString'
            # 这对于 's' 这样的变量名也同样有效,
            # 因为 _chrono_to_cpp_type 会回退到返回 "s"
            chrono_name = ctx.IDENTIFIER().getText()
            return self._chrono_to_cpp_type(chrono_name)
            
        if ctx.THIS():
            return "this"
            
        if ctx.LPAREN():
            return f"({self.visit(ctx.expression())})"
            
        return "" # 不应发生
    

    def visitExpressionList(self, ctx: ChronoParser.ExpressionListContext):
        return ", ".join(self.visit(e) for e in ctx.expression())

    def visitLiteral(self, ctx: ChronoParser.LiteralContext):
        return ctx.getText()
        
# [ 已修正 ] 用这个功能更全的版本替换
    def visitFunctionCallExpression(self, ctx: ChronoParser.FunctionCallExpressionContext):
        func_name = ctx.name.text
        
        # [ 新逻辑 ] 我们必须迭代参数, 检查字面量
        args_list = []
        if ctx.expressionList():
            for arg_expr in ctx.expressionList().expression():
                # 1. 翻译参数
                arg_code = self.visit(arg_expr)
                
                # 2. 检查是否需要包装字面量
                #    (只为 'print' 和 大写构造器 调用)
                if func_name == "print" or func_name[0].isupper():
                    if arg_expr.primary() and arg_expr.primary().literal():
                        if arg_expr.primary().literal().STRING_LITERAL():
                            # Chrono: "Hello" -> C++: ChronoString::create("Hello")
                            args_list.append(f"ChronoString::create({arg_code})")
                        elif arg_expr.primary().literal().INTEGER_LITERAL():
                            if func_name == "print":
                                # Chrono: print(123) -> C++: Print(ChronoInt::create(123))
                                args_list.append(f"ChronoInt::create({arg_code})")
                            else:
                                # 构造器调用, 假定 123 是 i32
                                args_list.append(arg_code)
                        else:
                            args_list.append(arg_code) # 其他字面量
                    else:
                        args_list.append(arg_code) # 变量或方法调用
                else:
                    # 普通全局函数, 不包装
                    args_list.append(arg_code)

        args_code = ", ".join(args_list)

        # --- [ 新的 ] 3-Way 路由逻辑 ---
        if func_name == "print":
            # 1. 特殊情况: print
            return f"Print({args_code})"

        elif func_name[0].isupper():
            # 2. [ 关键修复 ] 构造器调用
            # Chrono: MemberTest(...) -> C++: new MemberTest(...)
            return f"new {func_name}({args_code})"

        else:
            # 3. 全局 C++ 函数 (小写)
            return f"{func_name}({args_code})"