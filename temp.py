import os

# 遍历所有目录
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".dep.json"):
            full_path = os.path.join(root, file)
            print(f"Deleting: {full_path}")
            os.remove(full_path)