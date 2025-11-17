# src/transpiler.py
import sys
import os
import subprocess
import traceback
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# 导入生成的 Parser/Lexer
from parser.ChronoLexer import ChronoLexer
from parser.ChronoParser import ChronoParser

# 导入我们的新组件
from ChronoVisitor import ChronoVisitor
from TypemapScanner import TypemapScanner
from CompileContext import CompileContext

# 全局上下文 (在单次 transpiler 运行期间保持活跃)
# 注意：如果 build.py 多次调用 transpiler.py (作为子进程)，
# 这个 context 每次都会重置。
# 如果想要跨文件共享，build.py 应该传递信息，或者 transpiler.py 需要能处理整个项目。
# 目前的设计假设 transpiler.py 处理单个文件，
# 但我们会通过递归扫描 import 来重建必要的上下文。
global_context = CompileContext()


class ChronoErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"NO OK! ANTLR Parse Error at Line {line}:{column} - {msg}")


def scan_file_for_typemaps(file_path):
    """
    解析文件并提取 typemap，但不生成代码。
    """
    # 规范化路径以避免重复 (e.g., ./A.ch vs A.ch)
    abs_path = os.path.abspath(file_path)

    if global_context.is_scanned(abs_path):
        return

    if not os.path.exists(abs_path):
        # 可能是系统文件或路径错误，忽略
        # print(f"  [Scanner] 跳过 (未找到): {file_path}")
        return

    # print(f"  [Scanner] 正在扫描头文件: {os.path.basename(file_path)}")

    try:
        with open(abs_path, 'r', encoding='utf-8-sig') as f:
            data = f.read()

        input_stream = InputStream(data)
        lexer = ChronoLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ChronoParser(stream)

        # 使用静默监听器，避免扫描时的语法错误干扰主流程
        # (或者我们希望头文件必须语法正确？这里假设必须正确)
        parser.removeErrorListeners()
        parser.addErrorListener(ChronoErrorListener())

        tree = parser.program()

        # 运行扫描器
        scanner = TypemapScanner(global_context)
        scanner.visit(tree)

        global_context.mark_as_scanned(abs_path)

    except Exception as e:
        print(f"  [警告] 扫描导入文件失败 {os.path.basename(file_path)}: {e}")


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

        scan_file_for_typemaps(found_path)
    else:
        # 找不到文件，可能是 C++ 系统头文件 (<windows.h>)，忽略
        pass


def translate(input_file, output_file):
    try:
        # 1. 读取主文件
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            data = f.read()

        input_stream = InputStream(data)
        lexer = ChronoLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ChronoParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ChronoErrorListener())

        tree = parser.program()

        # 2. 准备 Import 回调
        current_dir = os.path.dirname(os.path.abspath(input_file))

        def import_callback(path):
            resolve_and_load_import(path, current_dir)

        # 3. 运行主 Visitor
        # 传入 global_context (可能已包含之前扫描的内容) 和 回调
        visitor = ChronoVisitor(global_context, import_callback)
        final_cpp_code = visitor.visit(tree)

        # 4. 输出
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        with open(output_file, "w", encoding='utf-8-sig') as f:
            f.write(final_cpp_code)

        # 5. 格式化 (可选)
        try:
            style_override = "{BasedOnStyle: LLVM, SortIncludes: false}"
            format_cmd = ["clang-format", "-i", f"-style={style_override}", output_file]
            subprocess.run(format_cmd, check=True, capture_output=True, text=True)
            print(f"OK! Transpiled: {input_file}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"OK! Transpiled (unformatted): {input_file}")

    except Exception as e:
        print(f"NO OK! Translation failed for {input_file}")
        print(f"Error Details: {e}")
        # traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python src/transpiler.py <input.ch> [output.cpp]")
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else "build/main.cpp"

    translate(in_file, out_file)