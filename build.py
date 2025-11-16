# build.py
# 位于 Chrono 项目的根目录 (与 src/, runtime/ 同级)

import os
import sys
import json
import subprocess
import argparse  # <-- [新增] 用于解析命令行参数

# --- 配置 ---
CONFIG_FILE_NAME = "chrono.json"
PYTHON_EXE = "python3"
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def print_color(text, color_code):
    """在 Windows 终端打印彩色文本 (32=绿色, 31=红色)"""
    print(f"\033[{color_code}m{text}\033[0m")


def load_config(project_dir):
    """
    加载并验证 chrono.json 配置文件。
    """
    config_path = os.path.join(project_dir, CONFIG_FILE_NAME)
    if not os.path.exists(config_path):
        print_color(f"错误: 找不到配置文件: {config_path}", 31)
        return None

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        print_color(f"错误: 配置文件 {config_path} 格式无效: {e}", 31)
        return None

    # 验证基本键 (简化版)
    required_keys = ["src_dir", "out_dir", "transpiler_script"]
    if not all(key in config for key in required_keys):
        print_color(f"错误: {config_path} 缺失必要的键。", 31)
        print("  必须包含: src_dir, out_dir, transpiler_script")
        return None

    return config


def run_transpile(config, project_dir):
    """
    递归扫描 src_dir 并翻译所有 .ch 文件。
    """
    print_color("--- [Chrono] 翻译阶段 (.ch -> .cpp/.h) ---", 32)

    # 1. 解析路径
    src_dir = os.path.join(project_dir, config["src_dir"])
    out_dir = os.path.join(project_dir, config["out_dir"])

    # 找到 transpiler.py (相对于 build.py)
    transpiler_path = os.path.realpath(
        os.path.join(SCRIPT_DIR, config["transpiler_script"])
    )

    if not os.path.exists(src_dir):
        print_color(f"错误: 源码目录不存在: {src_dir}", 31)
        return False
    if not os.path.exists(transpiler_path):
        print_color(f"错误: 翻译器脚本不存在: {transpiler_path}", 31)
        return False

    transpiled_count = 0

    # 2. 递归扫描 (os.walk)
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            in_file_path = os.path.join(root, file)

            # 计算相对路径 (例如: "MyWindow.h.ch" 或 "framework/Window.ch")
            relative_path = os.path.relpath(in_file_path, src_dir)

            # 3. 后缀名映射
            out_file_path = None
            if file.endswith(".h.ch"):
                out_file_path = os.path.join(out_dir, relative_path.replace(".h.ch", ".h"))
            elif file.endswith(".cpp.ch"):
                out_file_path = os.path.join(out_dir, relative_path.replace(".cpp.ch", ".cpp"))
            elif file.endswith(".ch"):
                out_file_path = os.path.join(out_dir, relative_path.replace(".ch", ".cpp"))
            else:
                continue  # 忽略非 .ch 文件

            # 4. 确保输出目录存在
            os.makedirs(os.path.dirname(out_file_path), exist_ok=True)

            # 5. 执行翻译
            print(f"  [翻译] {relative_path} -> {os.path.relpath(out_file_path, project_dir)}")
            transpile_cmd = [PYTHON_EXE, transpiler_path, in_file_path, out_file_path]

            try:
                # 运行翻译器
                result = subprocess.run(
                    transpile_cmd,
                    check=True,
                    capture_output=True,
                    text=True,
                    encoding='utf-8'
                )

                # 检查翻译器本身的输出 (OK! vs NO OK!)
                if "NO OK!" in result.stdout or "NO OK!" in result.stderr:
                    raise subprocess.CalledProcessError(1, transpile_cmd, result.stdout, result.stderr)

                transpiled_count += 1

            except subprocess.CalledProcessError as e:
                print_color(f"  [失败] 翻译 {file} 失败:", 31)
                print("  --- 翻译器 STDOUT ---\n", e.stdout)
                print("  --- 翻译器 STDERR ---\n", e.stderr)
                return False  # 翻译失败，停止

    print_color(f"翻译阶段完成。 成功翻译 {transpiled_count} 个文件。", 32)
    return True


def main():
    # 1. 设置命令行解析 (满足您的 'build.py transpile -d <dir>' 需求)
    parser = argparse.ArgumentParser(description="Chrono 构建脚本")

    # 'transpile' 是一个子命令
    subparsers = parser.add_subparsers(dest='command', required=True, help='构建命令')

    # 'transpile' 子命令的参数
    transpile_parser = subparsers.add_parser(
        'transpile',
        help='翻译 Chrono 源码 (.ch) 到 C++ (.cpp/.h)'
    )
    transpile_parser.add_argument(
        '-d', '--directory',
        dest='project_dir',
        required=True,
        help=f"包含 '{CONFIG_FILE_NAME}' 的项目根目录"
    )

    args = parser.parse_args()

    # 2. 加载配置
    project_path = args.project_dir
    config = load_config(project_path)
    if not config:
        sys.exit(1)

    print_color(f"=== 正在翻译 Chrono 项目 ===", 32)

    # 3. 执行 'transpile' 命令
    if args.command == 'transpile':
        success = run_transpile(config, project_path)
        if not success:
            print_color("翻译失败。", 31)
            sys.exit(1)

    print_color(f"=== 翻译完成。输出目录: {config['out_dir']} ===", 32)
    print("下一步：您可以运行 CMake 来编译生成的 C++ 源码。")


if __name__ == "__main__":
    main()