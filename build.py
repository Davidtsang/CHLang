# build.py
# 位于 CH 项目的根目录 (与 src/, runtime/ 同级)

import os
import sys
import json
import subprocess
import argparse

# --- 配置 ---
CONFIG_FILE_NAME = "config.json"
PYTHON_EXE = "python3"  # 如果您的环境是 python，请改为 "python"
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def print_color(text, color_code):
    """在 Windows 终端打印彩色文本 (32=绿色, 31=红色, 33=黄色)"""
    print(f"\033[{color_code}m{text}\033[0m")


def load_config(project_dir):
    """
    加载并验证 config.json 配置文件。
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

    # [修改] 验证 build_rules 而不是单一的 src_dir
    if "build_rules" not in config:
        print_color(f"错误: {CONFIG_FILE_NAME} 格式过时或无效。", 31)
        print("  必须包含 'build_rules' 列表。")
        return None

    return config


def transpile_file(transpiler_path, input_path, output_path):
    """[新增] 调用 transpiler.py 处理单个文件的辅助函数"""

    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cmd = [PYTHON_EXE, transpiler_path, input_path, output_path]

    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        # 检查翻译器内部输出的错误标记
        if "NO OK!" in result.stdout or "NO OK!" in result.stderr:
            raise subprocess.CalledProcessError(1, cmd, result.stdout, result.stderr)

        return True, ""
    except subprocess.CalledProcessError as e:
        error_msg = f"STDOUT:\n{e.stdout}\nSTDERR:\n{e.stderr}"
        return False, error_msg


def run_build(config, project_dir):
    """
    [重构] 遍历 build_rules 并执行构建。
    """
    print_color("=== 开始构建 CH 项目 ===", 32)

    # 1. 定位转译器脚本
    raw_script_path = config.get("transpiler_script", "src/transpiler.py")
    transpiler_path = os.path.abspath(os.path.join(project_dir, raw_script_path))

    # 如果项目配置里的路径找不到，尝试相对于 build.py 的路径
    if not os.path.exists(transpiler_path):
        transpiler_path = os.path.join(SCRIPT_DIR, raw_script_path)

    if not os.path.exists(transpiler_path):
        print_color(f"错误: 找不到转译器脚本: {transpiler_path}", 31)
        return False

    total_success = 0
    total_failed = 0

    # 2. 遍历构建规则
    rules = config["build_rules"]
    for i, rule in enumerate(rules):
        src_root = rule.get("source_dir")
        out_root = rule.get("output_dir")
        note = rule.get("note", f"Rule #{i + 1}")

        if not src_root or not out_root:
            print_color(f"警告: 规则 '{note}' 缺少 source_dir 或 output_dir，跳过。", 33)
            continue

        # 转为绝对路径
        abs_src = os.path.join(project_dir, src_root)
        abs_out = os.path.join(project_dir, out_root)

        if not os.path.exists(abs_src):
            print_color(f"警告: 源码目录不存在: {abs_src} ({note})", 33)
            continue

        print(f"\n--- 执行规则: {note} ---")
        print(f"  输入: {src_root}")
        print(f"  输出: {out_root}")

        # 3. 递归扫描并转译
        for root, dirs, files in os.walk(abs_src):
            for file in files:
                # 只处理 .ch 文件
                if not file.endswith(".ch"):
                    continue

                in_file_path = os.path.join(root, file)

                # 计算相对路径，保持目录结构
                rel_path = os.path.relpath(in_file_path, abs_src)

                # 4. 后缀名映射策略
                out_file_name = file
                if file.endswith(".h.ch"):
                    out_file_name = file[:-3]  # remove .ch, keep .h
                elif file.endswith(".cpp.ch"):
                    out_file_name = file[:-3]  # remove .ch, keep .cpp
                elif file.endswith(".ch"):
                    out_file_name = file[:-3] + ".cpp"  # replace .ch with .cpp

                # 修正 rel_path 中的文件名部分
                out_rel_dir = os.path.dirname(rel_path)
                out_file_path = os.path.join(abs_out, out_rel_dir, out_file_name)

                # 执行转译
                print(f"  [转译] {rel_path} -> {out_file_name}")
                success, msg = transpile_file(transpiler_path, in_file_path, out_file_path)

                if success:
                    total_success += 1
                else:
                    total_failed += 1
                    print_color(f"  [失败] {file}:", 31)
                    print(msg)

    print("\n=== 构建统计 ===")
    if total_failed > 0:
        print_color(f"失败: {total_failed}", 31)
        print_color(f"成功: {total_success}", 32)
        return False
    else:
        print_color(f"全部成功 ({total_success} 个文件)", 32)
        return True


def main():
    parser = argparse.ArgumentParser(description="CH 构建脚本")
    subparsers = parser.add_subparsers(dest='command', required=True, help='构建命令')

    # 'transpile' 子命令
    transpile_parser = subparsers.add_parser(
        'transpile',
        help='翻译 CH 源码 (.ch) 到 C++ (.cpp/.h)'
    )
    transpile_parser.add_argument(
        '-d', '--directory',
        dest='project_dir',
        required=True,
        help=f"包含 '{CONFIG_FILE_NAME}' 的项目根目录"
    )

    args = parser.parse_args()

    # 2. 加载配置
    project_path = os.path.abspath(args.project_dir)
    config = load_config(project_path)
    if not config:
        sys.exit(1)

    # 3. 执行 'transpile' 命令
    if args.command == 'transpile':
        success = run_build(config, project_path)
        if not success:
            print_color("构建过程中有错误发生。", 31)
            sys.exit(1)

    # 这里不再打印输出目录，因为可能有多个输出目录


if __name__ == "__main__":
    main()