# rename_project_safe.py
import os


def batch_rename(root_dir, old_str, new_str, exclude_dirs):
    print(f"=== 开始重命名: '{old_str}' -> '{new_str}' ===")
    print(f"=== 忽略目录: {exclude_dirs} ===\n")

    # 收集所有需要重命名的路径
    targets = []

    # os.walk 遍历目录树
    for root, dirs, files in os.walk(root_dir, topdown=True):
        # [关键步骤] 修改 dirs 列表以实现修剪 (Pruning)
        # 如果我们在 topdown=True 时修改了 dirs 列表，os.walk 就不会进入被移除的目录
        # 这里我们移除在排除列表中的目录
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        # 1. 检查当前目录下的文件
        for filename in files:
            if filename == "rename_project_safe.py": continue  # 跳过脚本自己

            if old_str in filename:
                full_path = os.path.join(root, filename)
                targets.append(full_path)

        # 2. 检查当前目录本身（将在稍后处理）
        for dirname in dirs:
            if old_str in dirname:
                full_path = os.path.join(root, dirname)
                targets.append(full_path)

    # [关键步骤] 按路径长度降序排序
    # 这样确保我们先重命名 "src/CH/TestCH.ch" (子文件)
    # 然后再重命名 "src/CH" (父目录)
    # 否则父目录改名后，子文件路径就失效了
    targets.sort(key=lambda s: len(s), reverse=True)

    count = 0
    for old_path in targets:
        # 解析路径
        dir_name = os.path.dirname(old_path)
        file_name = os.path.basename(old_path)

        # 生成新名字
        new_file_name = file_name.replace(old_str, new_str)
        new_path = os.path.join(dir_name, new_file_name)

        try:
            # 执行重命名
            os.rename(old_path, new_path)
            print(f"  [√] {file_name} -> {new_file_name}")
            count += 1
        except Exception as e:
            print(f"  [X] 失败: {old_path}")
            print(f"      原因: {e}")

    print(f"\n=== 完成。共重命名了 {count} 个文件/目录。 ===")


if __name__ == "__main__":
    # --- 配置区域 ---
    PROJECT_ROOT = "."  # 当前目录
    OLD_KEYWORD = "CH"
    NEW_KEYWORD = "CH"

    # [排除列表] 这里列出你不想触碰的文件夹名字
    EXCLUDE_DIRS = {
        ".git",
        ".idea",
        ".vscode",
        "__pycache__",
        "build",  # 通常构建目录也不需要改，反正会重新生成
        "cmake-build-debug"
    }
    # ----------------

    print(f"警告：即将在 '{os.path.abspath(PROJECT_ROOT)}' 执行批量重命名。")
    confirm = input(f"请确认将文件名中的 '{OLD_KEYWORD}' 替换为 '{NEW_KEYWORD}' (yes/no): ")

    if confirm.lower() == 'yes':
        batch_rename(PROJECT_ROOT, OLD_KEYWORD, NEW_KEYWORD, EXCLUDE_DIRS)

        print("\n----------- 后续手动操作提醒 -----------")
        print("1. 打开 PyCharm，按 Ctrl+Shift+R (全局替换)。")
        print(f"   将文件内容中的 '{OLD_KEYWORD}' 替换为 '{NEW_KEYWORD}'。")
        print("2. 修改 gen.bat: antlr-4.x... -o src/parser CHLexer.g4 ...")
        print("3. 修改 build.py: 检查是否有硬编码路径。")
        print("4. 重新运行 gen.bat。")
    else:
        print("操作已取消。")