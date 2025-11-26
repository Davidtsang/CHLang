# src/transpiler.py
import sys
import os
import subprocess
import argparse
import traceback
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# 导入生成的 Parser/Lexer
from parser.CHLexer import CHLexer
from parser.CHParser import CHParser

# 导入核心组件
from CHVisitor import CHVisitor
from CompileContext import CompileContext

# 全局上下文 (在单次 transpiler 运行期间保持活跃)
# 注意：如果 build.py 多次调用 transpiler.py (作为子进程)，
# 这个 context 每次都会重置。
# 如果想要跨文件共享，build.py 应该传递信息，或者 transpiler.py 需要能处理整个项目。
# 目前的设计假设 transpiler.py 处理单个文件，
# 但我们会通过递归扫描 import 来重建必要的上下文。
global_context = CompileContext()


class CHErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"NO OK! ANTLR Parse Error at Line {line}:{column} - {msg}")


def resolve_and_load_import(import_path, current_file_dir):
    """
    解析导入路径 (支持省略后缀) 并触发扫描。
    """
    # 1. 确定搜索的基础路径
    # 我们搜索两个位置：
    # A. 相对于当前文件的目录
    # B. 相对于工作目录 (通常是项目根目录)

    cwd = os.getcwd()

    candidates_dirs = [
        current_file_dir,
        cwd,
        os.path.join(cwd, "src")  # 尝试 src/ 目录
    ]

    # 2. 后缀尝试列表
    # 用户写 'framework/Window' -> 尝试 .ch, .h.ch
    # 用户写 'framework/Window.h' -> 尝试 .ch (作为容错), .h.ch (虽然 .h 不是 ch 后缀)
    # 正确的逻辑：如果路径已经有后缀，优先用它。如果没有，尝试添加。

    search_paths = []

    has_ext = import_path.endswith('.ch')

    for d in candidates_dirs:
        base = os.path.join(d, import_path)
        if has_ext:
            search_paths.append(base)
        else:
            search_paths.append(base + ".ch")
            search_paths.append(base + ".h.ch")
            # search_paths.append(base) # 也可以尝试无后缀 (虽然不太可能)

    found_path = None
    for test_path in search_paths:
        if os.path.isfile(test_path):
            found_path = test_path
            break

    if found_path:
        # 递归扫描找到的文件
        # 这里的递归意味着：如果 Window.h.ch 导入了 Application.h.ch，
        # 扫描 Window.h.ch 的 Visitor (TypemapScanner) 不会触发新的 import。
        # TypemapScanner 目前只看 typemap 定义。
        # *改进*: 如果需要深层递归 typemap，TypemapScanner 也需要处理 import。
        # 目前我们假设只有一层或用户显式导入。

        #scan_file_for_typemaps(found_path)
        pass
    else:
        # 找不到文件，可能是 C++ 系统头文件 (<windows.h>)，忽略
        pass


def translate(input_file, output_file, current_symbol_path=None, dep_symbol_paths=None):
    try:
        # 1. 初始化全局编译上下文
        # current_symbol_path: 当前项目要写入/更新的符号表路径
        # dep_symbol_paths: 依赖项目的符号表路径列表 (只读)
        ctx = CompileContext(current_symbol_path, dep_symbol_paths)

        # 设置当前正在处理的文件名 (用于 ClassInfo.file 字段)
        # 转换为相对路径以保持整洁，如果失败则使用绝对路径
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

        # 注册错误监听器
        parser.removeErrorListeners()
        parser.addErrorListener(CHErrorListener())

        # 解析语法树
        tree = parser.program()

        # Import 回调 (预留给未来递归扫描 import 语句用，目前由 build.py 处理依赖)
        def import_callback(path):
            pass

        # 3. 运行 Visitor (传入上下文)
        visitor = CHVisitor(ctx, import_callback)
        final_cpp_code = visitor.visit(tree)

        # 4. 写入输出文件
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        with open(output_file, "w", encoding='utf-8-sig') as f:
            f.write(final_cpp_code)

        # 5. 调用 clang-format 进行格式化 (如果系统中有)
        try:
            style_override = "{BasedOnStyle: LLVM, SortIncludes: false, ColumnLimit: 0}"
            format_cmd = ["clang-format", "-i", f"-style={style_override}", output_file]
            subprocess.run(format_cmd, check=True, capture_output=True, text=True)
            print(f"OK! Transpiled: {input_file}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            # 如果没有 clang-format，也不报错，只是不格式化
            print(f"OK! Transpiled (unformatted): {input_file}")

    except Exception as e:
        print(f"NO OK! Translation failed for {input_file}")
        print(f"Error Details: {e}")
        # traceback.print_exc() # 调试时可取消注释
        sys.exit(1)


if __name__ == '__main__':
    # 使用 argparse 处理命令行参数
    parser = argparse.ArgumentParser(description="Chrono Transpiler")

    # 必选参数
    parser.add_argument("input", help="Input .ch source file")
    parser.add_argument("output", help="Output .cpp file")

    # 可选参数：当前项目的符号表路径 (读+写)
    parser.add_argument("--symbols", help="Path to current project's symbols.json", default=None)

    # 可选参数：依赖项目的符号表路径列表 (只读)
    parser.add_argument("--deps", help="Paths to dependency symbol files", nargs='*', default=[])

    args = parser.parse_args()

    # 执行转换
    translate(args.input, args.output, args.symbols, args.deps)
