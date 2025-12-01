# src/transpiler.py
import sys
import os
import subprocess
import argparse
import traceback
import json
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from parser.CHLexer import CHLexer
from parser.CHParser import CHParser
from CHVisitor import CHVisitor
from CompileContext import CompileContext

# 全局上下文
global_context = CompileContext()


class CHErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"NO OK! ANTLR Parse Error at Line {line}:{column} - {msg}")


def resolve_and_load_import(import_path, current_file_dir):
    # (保留此函数的空实现或旧逻辑，此处省略以节省篇幅，保持原样即可)
    pass


# [修改] 增加了 project_root 参数
def translate(input_file, output_file, dep_file, current_symbol_path=None, dep_symbol_paths=None, project_root=None):
    try:
        # 1. 初始化全局编译上下文
        # [修改] 将 project_root 传给 Context
        ctx = CompileContext(current_symbol_path, dep_symbol_paths, project_root)

        # 设置当前正在处理的文件名
        try:
            ctx.set_current_file(os.path.relpath(input_file))
        except:
            ctx.set_current_file(input_file)

        # 2. 读取源代码
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            data = f.read()

        input_stream = InputStream(data)
        lexer = CHLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CHParser(stream)

        parser.removeErrorListeners()
        parser.addErrorListener(CHErrorListener())

        tree = parser.program()

        dependency_list = []

        def import_callback(path):
            dependency_list.append(path)

        # 3. 运行 Visitor
        visitor = CHVisitor(ctx, import_callback)
        final_cpp_code = visitor.visit(tree)

        # 4. 智能写入 (Smart Write)
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        should_write = True
        if os.path.exists(output_file):
            try:
                with open(output_file, "r", encoding='utf-8-sig') as f:
                    old_content = f.read()
                if old_content == final_cpp_code:
                    should_write = False
            except:
                pass

        if should_write:
            with open(output_file, "w", encoding='utf-8-sig') as f:
                f.write(final_cpp_code)
        else:
            pass

        # 5. 写入依赖文件
        if dep_file:
            dep_data = {
                "source": input_file,
                "imports": dependency_list
            }
            with open(dep_file, "w", encoding='utf-8') as f:
                json.dump(dep_data, f, indent=4)

        # 6. 调用 clang-format
        if should_write:
            try:
                style_override = "{BasedOnStyle: LLVM, SortIncludes: false, ColumnLimit: 0}"
                format_cmd = ["clang-format", "-i", f"-style={style_override}", output_file]
                subprocess.run(format_cmd, check=True, capture_output=True, text=True)
                print(f"OK! Transpiled: {input_file}")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"OK! Transpiled (unformatted): {input_file}")

    except Exception as e:
        print(f"NO OK! Translation failed for {input_file}")
        print(f"Error Details: {e}")
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chrono Transpiler")

    parser.add_argument("input", help="Input .ch source file")
    parser.add_argument("output", help="Output .cpp file")
    parser.add_argument("dep_file", help="Output dependency json file")

    parser.add_argument("--symbols", help="Path to current project's symbols.json", default=None)
    parser.add_argument("--deps", help="Paths to dependency symbol files", nargs='*', default=[])

    # [新增] 接收项目根目录参数
    parser.add_argument("--project-root", help="Root directory of the user project", default=None)

    args = parser.parse_args()

    # [修改] 传递 project_root
    translate(args.input, args.output, args.dep_file, args.symbols, args.deps, args.project_root)