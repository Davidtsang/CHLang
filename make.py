# make.py - 通用 CMake 构建助手
# 使用: python make.py [target_dir] [option]
# 示例: python make.py examples/MyGdiApp --run
# 示例: python make.py examples/MyGdiApp --clean --vs (生成 VS 工程)

import os
import sys
import shutil
import subprocess
import argparse


def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def run_command(cmd, cwd=None):
    print_color(f"cmd> {cmd}", 36)  # Cyan
    ret = subprocess.call(cmd, shell=True, cwd=cwd)
    if ret != 0:
        print_color("Error: Command failed.", 31)
        sys.exit(ret)


def main():
    parser = argparse.ArgumentParser(description="Chrono CMake 构建助手")
    parser.add_argument('target', help='目标目录 (例如 libs/jsonp 或 examples/MyGdiApp)')
    parser.add_argument('--clean', action='store_true', help='清理构建目录')
    parser.add_argument('--vs', action='store_true', help='使用 Visual Studio 生成器 (默认 Ninja)')
    parser.add_argument('--run', action='store_true', help='构建成功后运行 .exe')
    parser.add_argument('--config', default='Debug', help='构建配置 (Debug/Release)')

    args = parser.parse_args()

    root_dir = os.getcwd()
    target_dir = os.path.abspath(args.target)
    build_dir = os.path.join(target_dir, "build_cmake")

    # 1. 自动触发转译 (Dependencies aware)
    # 我们调用 build.py 来确保 C++ 代码是最新的
    print_color(f"=== [1] Transpiling {args.target} ===", 32)
    run_command(f"python build.py transpile -d {args.target}", cwd=root_dir)

    # 2. 清理
    if args.clean and os.path.exists(build_dir):
        print_color(f"=== [Clean] Removing {build_dir} ===", 33)
        shutil.rmtree(build_dir)

    # 3. 创建目录
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    # 4. CMake Configure
    # 只有当没有缓存文件时才运行 configure，或者强制 clean 时
    if not os.path.exists(os.path.join(build_dir, "CMakeCache.txt")):
        print_color(f"=== [2] Configuring CMake ===", 32)
        generator = "" if args.vs else "-G Ninja"
        run_command(f"cmake {generator} ..", cwd=build_dir)

    # 5. CMake Build
    print_color(f"=== [3] Building ({args.config}) ===", 32)
    run_command(f"cmake --build . --config {args.config}", cwd=build_dir)

    # 6. Run
    if args.run:
        print_color(f"=== [4] Running Application ===", 32)

        # 寻找 exe
        exe_name = os.path.basename(target_dir)  # 假设 exe 名字和目录名一致 (MyGdiApp)
        # 还要处理可能的后缀 _test_runner

        # 简单的查找逻辑
        exe_path = os.path.join(build_dir, f"{exe_name}.exe")
        if not os.path.exists(exe_path):
            exe_path = os.path.join(build_dir, "Debug", f"{exe_name}.exe")  # VS 默认路径

        if not os.path.exists(exe_path):
            # 尝试找 libs 的 test_runner
            # 假设目录是 libs/jsonp -> jsonp_test_runner.exe
            lib_name = os.path.basename(target_dir)
            exe_path = os.path.join(build_dir, f"{lib_name}_test_runner.exe")

        if os.path.exists(exe_path):
            # [关键] 复制资源文件 (layout.json) 到 exe 目录
            src_layout = os.path.join(target_dir, "layout.json")
            if os.path.exists(src_layout):
                dst_layout = os.path.join(os.path.dirname(exe_path), "layout.json")
                shutil.copy(src_layout, dst_layout)
                print(f"  (Copied layout.json to {os.path.dirname(exe_path)})")

            run_command(f"\"{exe_path}\"", cwd=os.path.dirname(exe_path))
        else:
            print_color("Error: Could not find executable to run.", 31)


if __name__ == "__main__":
    main()