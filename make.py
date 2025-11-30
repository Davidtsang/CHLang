# make.py - 通用 CMake 构建助手 (支持资源拷贝)
import os
import sys
import shutil
import subprocess
import argparse
import json

CONFIG_FILE_NAME = "config.json"


def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def run_command(cmd, cwd=None):
    print_color(f"cmd> {cmd}", 36)  # Cyan
    ret = subprocess.call(cmd, shell=True, cwd=cwd)
    if ret != 0:
        print_color("Error: Command failed.", 31)
        sys.exit(ret)


def load_config(project_dir):
    path = os.path.join(project_dir, CONFIG_FILE_NAME)
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None


def copy_resources(project_dir, output_dir, config):
    """
    根据 config.json 中的 resources 规则拷贝文件
    """
    resources = config.get("resources", [])
    if not resources:
        return

    print_color(f"=== Copying Resources to {output_dir} ===", 36)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    count = 0
    for rule in resources:
        # 兼容简单的字符串列表 (如果用户偷懒没写对象)
        if isinstance(rule, str):
            rule = {"path": rule}

        src_rel = rule.get("path")
        if not src_rel: continue

        src_path = os.path.join(project_dir, src_rel)

        # 确定输出名称
        dst_name = rule.get("output", os.path.basename(src_rel))
        dst_path = os.path.join(output_dir, dst_name)

        if not os.path.exists(src_path):
            print_color(f"  [Warn] Resource not found: {src_rel}", 33)
            continue

        # 执行拷贝 (增量检查)
        try:
            # 如果是文件夹
            if os.path.isdir(src_path):
                # 目录拷贝比较麻烦，这里简单处理：如果目标存在先删除
                if os.path.exists(dst_path):
                    shutil.rmtree(dst_path)
                shutil.copytree(src_path, dst_path)
                print(f"  [Dir]  {src_rel} -> {dst_name}")
                count += 1
            else:
                # 如果是文件，检查时间戳
                do_copy = True
                if os.path.exists(dst_path):
                    if os.path.getmtime(src_path) <= os.path.getmtime(dst_path):
                        do_copy = False

                if do_copy:
                    shutil.copy2(src_path, dst_path)  # copy2 保留元数据
                    print(f"  [File] {src_rel} -> {dst_name}")
                    count += 1
        except Exception as e:
            print_color(f"  [Fail] Copying {src_rel}: {e}", 31)

    if count == 0:
        print("  Resources up to date.")


def main():
    parser = argparse.ArgumentParser(description="Chrono CMake 构建助手")
    parser.add_argument('target', help='目标目录 (例如 examples/MyGdiApp)')
    parser.add_argument('--clean', action='store_true', help='清理构建目录')
    parser.add_argument('--vs', action='store_true', help='使用 Visual Studio 生成器')
    parser.add_argument('--run', action='store_true', help='构建成功后运行')
    parser.add_argument('--config', default='Debug', help='构建配置 (Debug/Release)')

    args = parser.parse_args()

    root_dir = os.getcwd()
    target_dir = os.path.abspath(args.target)
    build_dir = os.path.join(target_dir, "build_cmake")

    # 0. 加载配置
    app_config = load_config(target_dir)

    # 1. 自动触发转译
    print_color(f"=== [1] Transpiling {args.target} ===", 32)
    run_command(f"python build.py transpile -d {args.target}", cwd=root_dir)

    # 2. 清理
    if args.clean and os.path.exists(build_dir):
        print_color(f"=== [Clean] Removing {build_dir} ===", 33)
        shutil.rmtree(build_dir)

    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    # 3. CMake Configure
    if not os.path.exists(os.path.join(build_dir, "CMakeCache.txt")):
        print_color(f"=== [2] Configuring CMake ===", 32)
        generator = "" if args.vs else "-G Ninja"
        run_command(f"cmake {generator} ..", cwd=build_dir)

    # 4. CMake Build
    print_color(f"=== [3] Building ({args.config}) ===", 32)
    run_command(f"cmake --build . --config {args.config}", cwd=build_dir)

    # ==========================================
    # [关键新增] 资源拷贝逻辑
    # ==========================================

    # 探测二进制输出目录
    # 逻辑：如果是 VS 生成器，exe 在 Debug/Release 下；如果是 Ninja，exe 在根目录
    bin_dir = build_dir
    if args.vs or os.path.exists(os.path.join(build_dir, args.config)):
        bin_dir = os.path.join(build_dir, args.config)

    # 无论是否运行，只要编译成功，就拷贝资源
    if app_config:
        copy_resources(target_dir, bin_dir, app_config)

    # 5. Run
    if args.run:
        print_color(f"=== [4] Running Application ===", 32)

        # 寻找 exe
        exe_name = os.path.basename(target_dir)

        # 尝试在探测到的 bin_dir 里找
        exe_path = os.path.join(bin_dir, f"{exe_name}.exe")

        # 如果找不到，尝试找 test runner
        if not os.path.exists(exe_path):
            exe_path = os.path.join(bin_dir, f"{exe_name}_test.exe")

        # 模糊搜索作为最后手段
        if not os.path.exists(exe_path):
            # ... (保留之前的模糊搜索逻辑，可选) ...
            pass

        if os.path.exists(exe_path):
            print_color(f"cmd> {os.path.basename(exe_path)}", 36)
            run_command(f"\"{exe_path}\"", cwd=os.path.dirname(exe_path))
        else:
            print_color("Error: Could not find executable to run.", 31)


if __name__ == "__main__":
    main()