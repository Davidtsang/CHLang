# src/ChronoVisitor.py

from antlr4 import *
from parser.ChronoParser import ChronoParser
from parser.ChronoParserVisitor import ChronoParserVisitor as BaseChronoVisitor

INDENT = "    " 

class ChronoVisitor(BaseChronoVisitor):

    # [ 新增 ] 
    # 这是一个辅助函数，用于将 Chrono 类型名映射到 C++ 类名
    def _chrono_to_cpp_type(self, chrono_type_name):
        if chrono_type_name == "String":
            return "ChronoString"
        if chrono_type_name == "Int":
            return "ChronoInt"
        # 默认回退（尽管在我们的示例中用不到）
        return chrono_type_name

# src/ChronoVisitor.py

    # [ 已修正 ]
    def visitProgram(self, ctx: ChronoParser.ProgramContext):
        
        # 1. [ 新 ] 访问所有全局语句 (imports 和 @cpp)
        #    ctx.globalStatement() 返回一个 *单一的、有序的* 列表
        #    这 100% 保证了它们在 C++ 输出中的顺序
        #    与它们在 .ch 源文件中的顺序一致。
        globals_code = "".join(self.visit(g) for g in ctx.globalStatement())
        
        # 2. 访问所有函数定义
        function_defs_code = "".join(self.visit(f) for f in ctx.functionDefinition())
        
        # 3. 组装 main 包装器
        main_wrapper = (
            "\n// C++ 程序的标准入口\n"
            "int main() {\n"
            f"{INDENT}return Chrono_main(); // 调用 Chrono 的入口函数\n"
            "}\n"
        )
        
        # 4. 按正确顺序返回所有代码
        return globals_code + function_defs_code + main_wrapper

    # [ 已修正 ] (修复 "引号没有剥离" 的问题)
    def visitImportDirective(self, ctx: ChronoParser.ImportDirectiveContext):
            # 提取原始路径 (例如: "<iostream>" 或 ""runtime/ChronoObject.h"")
            path_text = ctx.path.text
            
            if path_text.startswith('<'):
                # 这是一个系统路径, 例如 "<iostream>"
                # C++ 语法需要它原样保留尖括号
                return f"#include {path_text}\n"
            
            elif path_text.startswith('"'):
                # 这是一个本地路径, 例如 ""runtime/ChronoObject.h""
                # 我们需要剥离 "runtime/" 前缀, 并保留引号
                
                # 1. 剥离外部引号: "runtime/ChronoObject.h" -> runtime/ChronoObject.h
                path_content = path_text[1:-1] 
                
                # 2. 剥离 "runtime/" 前缀
                if path_content.startswith('runtime/'):
                    path_content = path_content.replace('runtime/', '') # -> ChronoObject.h
                
                # 3. 重新添加 C++ 风格的引号
                return f'#include "{path_content}"\n'
            
            # 不应该发生的回退
            return f"// ERROR: Invalid import path {path_text}\n"

# [ 已修正 ]
    def visitFunctionDefinition(self, ctx: ChronoParser.FunctionDefinitionContext):
        func_name = ctx.name.text
        return_type = ctx.returnType.text
        body_code = "".join(self.visit(s) for s in ctx.statement())
        
        cpp_return_type = ""
        cpp_func_name = ""
        
        if func_name == "main" and return_type == "Int":
            cpp_return_type = "int"
            cpp_func_name = "Chrono_main"
        else:
            # 检查是值类型还是引用类型
            if return_type in ("i32", "i64", "int"):
                cpp_return_type = self._chrono_to_cpp_type(return_type)
            else:
                # [ 关键修正 ] 
                # 返回类型现在是 T* (原始指针)
                cpp_return_type = f"{self._chrono_to_cpp_type(return_type)}*"
            cpp_func_name = func_name
        
        return (
            f"\n{cpp_return_type} {cpp_func_name}() {{\n"
            f"{INDENT}// --- Chrono Function Body: {func_name} ---\n"
            f"{body_code}"
            f"{INDENT}// --- Function End ---\n"
            "}\n"
        )

 # --- 语句 ---
    # [ 已修正 ]
    def visitDeclaration(self, ctx: ChronoParser.DeclarationContext):
        var_name = ctx.variableName.text
        type_name = ctx.typeName.text
        expression_code = self.visit(ctx.expression())
        
        # 检查是值类型还是引用类型
        if type_name in ("i32", "i64", "int"):
            # --- 值类型 (Value Type) ---
            cpp_type = f"const {self._chrono_to_cpp_type(type_name)}"
            cpp_value = expression_code
            
        else:
            # --- 引用类型 (Reference Type) ---
            cpp_class_name = self._chrono_to_cpp_type(type_name)
            
            # [ 关键修正 ]
            # 不再使用 Ref<T>，而是使用 T*
            cpp_type = f"{cpp_class_name}* const" # const T* (指针本身不可变)
            
            cpp_value = ""
            expression_node = ctx.expression()
            
            if expression_node.methodCallExpression():
                cpp_value = expression_code # 方法调用已返回 T*
            elif expression_node.literal():
                # T::create() 返回 T*
                cpp_value = f"{cpp_class_name}::create({expression_code})"
            elif expression_node.IDENTIFIER():
                cpp_value = expression_code # 变量赋值 (T* 被复制)
        
        return f"{INDENT}{cpp_type} {var_name} = {cpp_value};\n"
 
    def visitReturnStatement(self, ctx: ChronoParser.ReturnStatementContext):
        return_value = self.visit(ctx.expression())
        return f"{INDENT}return {return_value};\n"

    def visitMethodCall(self, ctx: ChronoParser.MethodCallContext):
        expression_code = self.visit(ctx.methodCallExpression())
        return f"{INDENT}{expression_code};\n"

    def visitCppBlock(self, ctx: ChronoParser.CppBlockContext):
        token_list = ctx.CPP_BODY()
        if token_list is None:
            token_list = []
        raw_cpp = "".join(token.getText() for token in token_list)
        return (
            f"\n{INDENT}// --- @cpp Block Start ---\n"
            f"{raw_cpp.strip()}\n" 
            f"{INDENT}// --- @cpp Block End ---\n\n"
        )

    # --- 表达式 ---
    def visitExpression(self, ctx: ChronoParser.ExpressionContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        if ctx.methodCallExpression():
            return self.visit(ctx.methodCallExpression())
        raise Exception(f"Unknown expression type at line {ctx.start.line}")

    def visitMethodCallExpression(self, ctx: ChronoParser.MethodCallExpressionContext):
        receiver = ctx.receiver.text
        method = ctx.methodName.text
        args = ""
        if ctx.expressionList():
            args = self.visit(ctx.expressionList())
        return f"{receiver}->{method}({args})"

    def visitExpressionList(self, ctx: ChronoParser.ExpressionListContext):
        return ", ".join(self.visit(e) for e in ctx.expression())

    def visitLiteral(self, ctx: ChronoParser.LiteralContext):
        return ctx.getText()
    
    # --- [ 新方法 ] ---
    # visitFunctionCall 用于处理 'print(x);' 这样的语句
    def visitFunctionCall(self, ctx: ChronoParser.FunctionCallContext):
        # 只是访问表达式并添加分号
        call_code = self.visit(ctx.functionCallExpression())
        return f"{INDENT}{call_code};\n"

# [ 已修正 ]
    # (此方法现在是 'visitFunctionCallExpression' 的一部分)
    def visitFunctionCallExpression(self, ctx: ChronoParser.FunctionCallExpressionContext):
        func_name = ctx.name.text
        
        args_code = ""
        if ctx.expressionList():
            args_code = self.visit(ctx.expressionList())

        if func_name == "print":
            # [ 关键修正 ]
            # print("literal") 会创建对象，但它会泄漏！
            # 这是 MRC 的预期行为。程序员必须自己管理。
            arg_expression = ctx.expressionList().expression(0)
            arg_code = self.visit(arg_expression)
            
            cpp_value = ""
            if arg_expression.literal():
                if arg_expression.literal().STRING_LITERAL():
                    cpp_value = f"ChronoString::create({arg_code})"
                elif arg_expression.literal().INTEGER_LITERAL():
                    cpp_value = f"ChronoInt::create({arg_code})"
            else:
                cpp_value = arg_code # 已经是 T* 或 i32
            
            return f"Print({cpp_value})"

        else:
            # C++ 宏或全局函数
            return f"{func_name}({args_code})"