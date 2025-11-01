# run_tests.py
import os
import glob
import subprocess
import filecmp
import sys

# --- 配置 ---
PYTHON_EXE = "python3"
TRANSPILER_SCRIPT = os.path.join("src", "transpiler.py")
TEST_DIR = "test"
BUILD_DIR = "build"
RUNTIME_DIR = "runtime"

# 编译命令 (作为列表)
# 我们使用与你手动编译时相同的、成功的命令
CPP_COMPILE_COMMAND = [
    "cl",
    "/std:c++17",
    "/EHsc",
    f"/I{RUNTIME_DIR}", # /I 和 "runtime" 之间没有空格
    "/nologo",
    os.path.join(RUNTIME_DIR, "ChronoString.cpp")
]
CPP_LINK_COMMAND = [
    "/link",
    "/SUBSYSTEM:CONSOLE"
]
# --- 结束配置 ---

def print_color(text, color_code):
    """在 Windows 终端打印彩色文本"""
    # 32 = 绿色 (PASS), 31 = 红色 (FAIL)
    print(f"\033[{color_code}m{text}\033[0m")

def run_test(test_file_path):
    """运行一个单独的 Chrono 测试文件"""
    
    test_name = os.path.basename(test_file_path).replace(".ch", "")
    print(f"[TEST] Running: {test_name}")
    
    # 1. 定义所有路径
    cpp_output = os.path.join(BUILD_DIR, f"{test_name}.cpp")
    exe_output = os.path.join(BUILD_DIR, f"{test_name}.exe")
    actual_output = os.path.join(BUILD_DIR, f"{test_name}.actual.txt")
    expected_output = os.path.join(TEST_DIR, f"{test_name}.expected.txt")

    try:
        # --- 步骤 1: 翻译 (Python -> C++) ---
        # check=True: 如果翻译器失败，立即抛出异常
        transpile_cmd = [PYTHON_EXE, TRANSPILER_SCRIPT, test_file_path, cpp_output]
        print(f"  [Transpile] {' '.join(transpile_cmd)}")
        subprocess.run(transpile_cmd, check=True, capture_output=True)

        # --- 步骤 2: 编译 (C++ -> EXE) ---
        compile_cmd = CPP_COMPILE_COMMAND + [cpp_output, "/Fe:" + exe_output] + CPP_LINK_COMMAND
        print(f"  [Compile] {' '.join(compile_cmd)}")
        
        # check=True: 如果 cl.exe 或 link.exe 失败，立即抛出异常
        # 这解决了 "静默链接器失败" 的问题
        subprocess.run(compile_cmd, check=True, capture_output=True)

        # --- 步骤 3: 运行 (EXE -> Output) ---
        print(f"  [Run] {exe_output}")
        # text=True: 将输出解码为文本
        run_result = subprocess.run([exe_output], check=True, capture_output=True, text=True)
        
        # 将实际输出写入文件 (清理 \r\n 为 \n 以便比较)
        actual_content = run_result.stdout.strip().replace('\r\n', '\n')
        with open(actual_output, 'w') as f:
            f.write(actual_content)

        # --- 步骤 4: 比较 (Output vs Expected) ---
        with open(expected_output, 'r') as f:
            expected_content = f.read().strip().replace('\r\n', '\n')
        
        if actual_content == expected_content:
            print_color("  [PASS]", 32)
            return True
        else:
            print_color(f"  [FAIL] Output mismatch.", 31)
            print("  --- Expected ---")
            print(expected_content)
            print("  --- Actual ---")
            print(actual_content)
            return False

    except subprocess.CalledProcessError as e:
        # 捕获翻译或编译失败
        print_color(f"  [FAIL] Process failed with return code {e.returncode}", 31)
        # 打印编译器或翻译器的错误信息
        print("  --- STDOUT ---")
        print(e.stdout.decode(errors='ignore'))
        print("  --- STDERR ---")
        print(e.stderr.decode(errors='ignore'))
        return False
    except FileNotFoundError as e:
        print_color(f"  [FAIL] File not found: {e.filename}", 31)
        return False
    except Exception as e:
        print_color(f"  [FAIL] An unexpected error occurred: {e}", 31)
        return False

def main():
    print("===================================")
    print("= Chrono Language Test Suite (Python)")
    print("===================================")
    
    # 确保 build 目录存在
    os.makedirs(BUILD_DIR, exist_ok=True)
    
    test_files = glob.glob(os.path.join(TEST_DIR, "*.ch"))
    if not test_files:
        print_color(f"No test files found in {TEST_DIR}/", 31)
        sys.exit(1)
        
    fail_count = 0
    for test_file in test_files:
        if not run_test(test_file):
            fail_count += 1
        print("-" * 30)

    print("===================================")
    if fail_count > 0:
        print_color(f"Summary: FAILED ({fail_count} / {len(test_files)} tests failed)", 31)
    else:
        print_color(f"Summary: SUCCESS (All {len(test_files)} tests passed)", 32)
    print("===================================")

if __name__ == "__main__":
    main()