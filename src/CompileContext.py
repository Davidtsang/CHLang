# src/CompileContext.py
class CompileContext:
    """
    全局编译上下文。
    负责存储跨文件共享的信息，例如 typemaps。
    """

    def __init__(self):
        # 存储 typemap: Key -> C++ Value
        # 例如: {"C_HBRUSH": "HBRUSH", "C_INT_WINAPI": "int WINAPI"}
        self.typemap_registry = {}

        # 记录已扫描的文件路径 (绝对路径)，防止无限递归或重复扫描
        self.scanned_files = set()

    def register_typemap(self, name, value):
        # print(f"[Context] 注册 typemap: {name} -> {value}")
        self.typemap_registry[name] = value

    def get_typemap(self, name):
        return self.typemap_registry.get(name)

    def mark_as_scanned(self, file_path):
        self.scanned_files.add(file_path)

    def is_scanned(self, file_path):
        return file_path in self.scanned_files