# run_tests.py
import os
import glob
import subprocess
import sys
import time
import re

# --- 配置 ---
PYTHON_EXE = "python3"
TRANSPILER_SCRIPT = os.path.join("src", "transpiler.py")
TEST_DIR = "test"
BUILD_DIR = "build"
RUNTIME_DIR = "runtime"

# 编译命令
CPP_COMPILE_COMMAND = [
    "cl", "/std:c++17", "/EHsc", f"/I{RUNTIME_DIR}", "/nologo",
    os.path.join(RUNTIME_DIR, "CHString.cpp")
]
CPP_LINK_COMMAND = ["/link", "/SUBSYSTEM:CONSOLE"]


def print_color(text, color_code):
    """32=Green, 31=Red, 33=Yellow, 36=Cyan"""
    print(f"\033[{color_code}m{text}\033[0m")


def smart_compare(actual, expected):
    a_lines = actual.strip().splitlines()
    e_lines = expected.strip().splitlines()

    if len(a_lines) != len(e_lines):
        print(f"      [Diff] Line count mismatch: Actual {len(a_lines)}, Expected {len(e_lines)}")
        return False

    for i, (a_line, e_line) in enumerate(zip(a_lines, e_lines)):
        # 1. 如果预期行包含 {{HASH}} 占位符
        if "{{HASH}}" in e_line:
            # 将 {{HASH}} 替换为匹配数字的正则 \d+
            # 注意：先 escape 掉行里的其他特殊字符（如 [ ] ( )）
            pattern_str = re.escape(e_line).replace(r"\{\{HASH\}\}", r"\d+")

            # 使用正则进行全匹配
            if not re.fullmatch(pattern_str, a_line):
                print(f"      [Diff Line {i + 1}] Pattern mismatch.")
                print(f"        Exp: {e_line}")
                print(f"        Act: {a_line}")
                return False

        # 2. 否则，普通字符串比较
        elif a_line != e_line:
            print(f"      [Diff Line {i + 1}] Content mismatch.")
            print(f"        Exp: {e_line}")
            print(f"        Act: {a_line}")
            return False

    return True

def run_test(test_file_path):
    test_name = os.path.basename(test_file_path).replace(".ch", "")
    print(f"[TEST] Running: {test_name} ... ", end="", flush=True)

    cpp_output = os.path.join(BUILD_DIR, f"{test_name}.cpp")
    exe_output = os.path.join(BUILD_DIR, f"{test_name}.exe")
    dep_output = os.path.join(BUILD_DIR, f"{test_name}.dep.json")

    # [关键] 设置 project_root 为 test 目录
    project_root = os.path.abspath(TEST_DIR)

    try:
        # --- 步骤 1: 翻译 (Python -> C++) ---
        transpile_cmd = [
            PYTHON_EXE, TRANSPILER_SCRIPT,
            test_file_path,
            cpp_output,
            dep_output,
            "--project-root", project_root
        ]

        subprocess.run(transpile_cmd, check=True, capture_output=True)

        # --- 步骤 2: 编译 (C++ -> EXE) ---
        compile_cmd = CPP_COMPILE_COMMAND + [cpp_output, "/Fe:" + exe_output] + CPP_LINK_COMMAND
        subprocess.run(compile_cmd, check=True, capture_output=True)

        # --- 步骤 3: 运行 ---
        run_result = subprocess.run(
            [exe_output],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8'
        )

        actual_content = run_result.stdout.strip().replace('\r\n', '\n')

        # 检查预期文件
        expected_output = os.path.join(TEST_DIR, f"{test_name}.expected.txt")
        if not os.path.exists(expected_output):
            print_color("[PASS] (No expected file)", 33)  # Yellow
            # print(f"      Output: {actual_content}")
            return True

        # 比较
        with open(expected_output, 'r', encoding='utf-8') as f:
            expected_content = f.read().strip().replace('\r\n', '\n')

        if smart_compare(actual_content, expected_content):
            print_color("[PASS]", 32)  # Green
            return True
        else:
            print_color("[FAIL] Output mismatch", 31)  # Red
            print("  --- Expected ---")
            print(expected_content)
            print("  --- Actual ---")
            print(actual_content)
            return False

    except subprocess.CalledProcessError as e:
        print_color("[FAIL] Process Error", 31)
        if e.stdout: print(e.stdout.decode('utf-8', errors='ignore'))
        if e.stderr: print(e.stderr.decode('utf-8', errors='ignore'))
        return False
    except Exception as e:
        print_color(f"[FAIL] Exception: {e}", 31)
        return False


def main():
    # 确保构建目录存在
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)

    # 获取测试文件列表
    targets = sys.argv[1:] if len(sys.argv) > 1 else glob.glob(os.path.join(TEST_DIR, "*.ch"))

    if not targets:
        print_color(f"No test files found in {TEST_DIR}", 33)
        return

    print("========================================")
    print(f"Starting Test Suite ({len(targets)} files)")
    print("========================================")

    passed_count = 0
    failed_count = 0
    start_time = time.time()

    # 执行循环
    for t in targets:
        if run_test(t):
            passed_count += 1
        else:
            failed_count += 1

    end_time = time.time()
    duration = end_time - start_time

    # 打印摘要
    print("\n========================================")
    print("TEST SUMMARY")
    print("========================================")
    print(f"Total Tests: {len(targets)}")
    print_color(f"Passed:      {passed_count}", 32)

    if failed_count > 0:
        print_color(f"Failed:      {failed_count}", 31)
    else:
        print(f"Failed:      0")

    print(f"Time Taken:  {duration:.2f}s")
    print("========================================")

    # 如果有失败，返回非 0 状态码
    if failed_count > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()