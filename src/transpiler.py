# src/transpiler.py
import sys
import os
import subprocess
import argparse
import traceback
import json  # [新增] 用于写入依赖文件
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# 导入生成的 Parser/Lexer
from parser.CHLexer import CHLexer
from parser.CHParser import CHParser

# 导入核心组件
from CHVisitor import CHVisitor
from CompileContext import CompileContext

# 全局上下文
global_context = CompileContext()


class CHErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"NO OK! ANTLR Parse Error at Line {line}:{column} - {msg}")


def resolve_and_load_import(import_path, current_file_dir):
    """
    解析导入路径 (支持省略后缀) 并触发扫描。
    (保留此函数以兼容旧逻辑，但在当前的构建系统中，依赖由 build.py 管理)
    """
    cwd = os.getcwd()
    candidates_dirs = [
        current_file_dir,
        cwd,
        os.path.join(cwd, "src")
    ]

    search_paths = []
    has_ext = import_path.endswith('.ch')

    for d in candidates_dirs:
        base = os.path.join(d, import_path)
        if has_ext:
            search_paths.append(base)
        else:
            search_paths.append(base + ".ch")
            search_paths.append(base + ".h.ch")

    found_path = None
    for test_path in search_paths:
        if os.path.isfile(test_path):
            found_path = test_path
            break

    if found_path:
        pass
    else:
        pass


# [修改] 增加了 dep_file 参数
def translate(input_file, output_file, dep_file, current_symbol_path=None, dep_symbol_paths=None):
    try:
        # 1. 初始化全局编译上下文
        ctx = CompileContext(current_symbol_path, dep_symbol_paths)

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

        # [新增] 收集依赖列表
        dependency_list = []

        def import_callback(path):
            # path 是 import 语句中的原始字符串 (例如 "runtime/CH.h")
            dependency_list.append(path)

        # 3. 运行 Visitor
        visitor = CHVisitor(ctx, import_callback)
        final_cpp_code = visitor.visit(tree)

        # ==========================================
        # 4. [核心逻辑] 智能写入 (Smart Write)
        # ==========================================
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        should_write = True

        # 如果目标文件已存在，读取旧内容进行对比
        if os.path.exists(output_file):
            try:
                with open(output_file, "r", encoding='utf-8-sig') as f:
                    old_content = f.read()

                # 如果新旧内容完全一致，则跳过写入
                # 这样文件的时间戳就不会改变，CMake 就会跳过编译
                if old_content == final_cpp_code:
                    should_write = False
            except:
                pass  # 读取错误则强制覆盖

        if should_write:
            with open(output_file, "w", encoding='utf-8-sig') as f:
                f.write(final_cpp_code)
            # 只有真正写入了才打印 Update，方便调试
            # print(f"  [Updated] {output_file}")
        else:
            # print(f"  [Cached] {output_file}")
            pass

        # 5. [新增] 写入依赖文件 (.dep.json)
        # 无论 C++ 是否更新，依赖关系文件最好总是刷新，或者至少保证它存在
        if dep_file:
            dep_data = {
                "source": input_file,
                "imports": dependency_list
            }
            # 写入依赖文件
            with open(dep_file, "w", encoding='utf-8') as f:
                json.dump(dep_data, f, indent=4)

        # 6. 调用 clang-format
        # 只有当文件确实被写入(更新)了，才需要运行 format，节省时间
        # 或者为了保险起见，每次都跑也行，但通常 should_write 为 False 时不需要
        if should_write:
            try:
                style_override = "{BasedOnStyle: LLVM, SortIncludes: false, ColumnLimit: 0}"
                format_cmd = ["clang-format", "-i", f"-style={style_override}", output_file]
                subprocess.run(format_cmd, check=True, capture_output=True, text=True)
                print(f"OK! Transpiled: {input_file}")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"OK! Transpiled (unformatted): {input_file}")
        else:
            # 如果没写入，也可以打印一个提示，或者保持静默
            # print(f"OK! Up-to-date: {input_file}")
            pass

    except Exception as e:
        print(f"NO OK! Translation failed for {input_file}")
        print(f"Error Details: {e}")
        # traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chrono Transpiler")

    # 必选参数
    parser.add_argument("input", help="Input .ch source file")
    parser.add_argument("output", help="Output .cpp file")

    # [新增] 依赖描述输出文件 (build.py 会传入)
    parser.add_argument("dep_file", help="Output dependency json file")

    # 可选参数
    parser.add_argument("--symbols", help="Path to current project's symbols.json", default=None)
    parser.add_argument("--deps", help="Paths to dependency symbol files", nargs='*', default=[])

    args = parser.parse_args()

    # 执行转换
    translate(args.input, args.output, args.dep_file, args.symbols, args.deps)