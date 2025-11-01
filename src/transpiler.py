# src/transpiler.py

import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from parser.ChronoLexer import ChronoLexer
from parser.ChronoParser import ChronoParser
from ChronoVisitor import ChronoVisitor 

# --- 新增：自定义错误监听器 ---
class ChronoErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # 抛出一个 Python 异常，这将立即停止脚本
        raise Exception(f"❌ ANTLR Parse Error at Line {line}:{column} - {msg}")

def translate(input_file, output_file):
    try:
        # --- 修正：使用 Python 手动读取文件 ---
        # 1. 'encoding="utf-8-sig"' 会自动检测并处理(跳过) UTF-8 BOM
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            data = f.read()
        
        # 2. 将读取的字符串传递给 ANTLR 的 InputStream
        input_stream = InputStream(data)
        
        # --- 正常的 ANTLR 流程 ---
        lexer = ChronoLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ChronoParser(stream)
        
        # --- 新增：附加我们的自定义错误监听器 ---
        parser.removeErrorListeners() # 移除默认的控制台打印监听器
        parser.addErrorListener(ChronoErrorListener()) # 添加我们严格的监听器
        
        tree = parser.program() 

        # --- 正常的 Visitor 流程 ---
        visitor = ChronoVisitor()
        final_cpp_code = visitor.visit(tree)
        
        with open(output_file, "w", encoding='utf-8-sig') as f:
            f.write(final_cpp_code)
        
        print(f"OK! Translation successful. C++ code written to {output_file}")
    
    except Exception as e:
        print(f"NO OK! Translation failed.")
        print(f"Error Details: {e}")
        sys.exit(1) # 失败时退出

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python src/transpiler.py <input.ch> [output.cpp]")
        sys.exit(1)
        
    in_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else "build/main.cpp"
    
    translate(in_file, out_file)