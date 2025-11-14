# src/transpiler.py

import sys
import os  # <-- [新增] 导入 os
import subprocess  # <-- [新增] 导入 subprocess
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from parser.ChronoLexer import ChronoLexer
from parser.ChronoParser import ChronoParser
from ChronoVisitor import ChronoVisitor
import traceback


# --- 新增：自定义错误监听器 ---
class ChronoErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # 抛出一个 Python 异常，这将立即停止脚本
        raise Exception(f"NO OK! ANTLR Parse Error at Line {line}:{column} - {msg}")


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
        parser.removeErrorListeners()  # 移除默认的控制台打印监听器
        parser.addErrorListener(ChronoErrorListener())  # 添加我们严格的监听器

        tree = parser.program()

        # --- 正常的 Visitor 流程 ---
        # (这里假设你使用的是我们之前简化的、移除嵌套缩进的 Visitor)
        visitor = ChronoVisitor()
        final_cpp_code = visitor.visit(tree)

        # --- [新增] 确保输出目录存在 ---
        output_dir = os.path.dirname(output_file)
        if output_dir:  # 检查是否为空字符串 (例如，输出到当前目录)
            os.makedirs(output_dir, exist_ok=True)

        # --- 写入未格式化的 C++ 代码 ---
        with open(output_file, "w", encoding='utf-8-sig') as f:
            f.write(final_cpp_code)

        # --- [ 新增：调用 clang-format ] ---
        try:
            # -i (in-place) 原地修改文件
            # -style=LLVM (一个常见的默认风格，如果 .clang-format 文件不存在)
            #   (或者使用 -style=file 来自动查找 .clang-format 配置文件)
            #format_cmd = ["clang-format", "-i", "-style=LLVM", output_file]
            style_override = "{BasedOnStyle: LLVM, SortIncludes: false}"
            format_cmd = ["clang-format", "-i", f"-style={style_override}", output_file]

            # check=True 会在 clang-format 失败时抛出异常
            subprocess.run(format_cmd, check=True, capture_output=True, text=True)

            # [修改] 更新成功消息
            print(f"OK! Translation successful. C++ code formatted and saved to {output_file}")

        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            # 如果 clang-format 未安装或失败，我们只打印一个警告
            # C++ 文件仍然存在，只是未格式化
            print(f"OK! Translation successful (but formatting failed). C++ code saved to {output_file}")
            print(f"  [WARN] clang-format failed or not found. C++ code is unformatted.")
            if isinstance(e, subprocess.CalledProcessError):
                print(f"  [WARN] clang-format stderr: {e.stderr}")
        # --- [ 格式化结束 ] ---

    except Exception as e:
        print(f"NO OK! Translation failed.")
        print(f"Error Details: {e}")
        traceback.print_exc()
        sys.exit(1)  # 失败时退出


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python src/transpiler.py <input.ch> [output.cpp]")
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else "build/main.cpp"

    translate(in_file, out_file)