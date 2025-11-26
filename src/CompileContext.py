# src/CompileContext.py
import json
import os
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Union, Any


# ==========================================
# 1. 符号表数据结构 (Symbol Table Schema)
# ==========================================

@dataclass
class ArgInfo:
    name: str
    type: str  # C++ 类型 (例如: "int32_t", "std::string")

    def to_dict(self):
        return asdict(self)


@dataclass
class MethodInfo:
    name: str
    return_type: str
    args: List[ArgInfo] = field(default_factory=list)
    access: str = "public"  # public, private, protected
    is_static: bool = False
    is_virtual: bool = False
    is_override: bool = False
    is_optional: bool = False  # For interface methods

    def to_dict(self):
        return asdict(self)


@dataclass
class FieldInfo:
    name: str
    type: str
    access: str = "private"

    def to_dict(self):
        return asdict(self)


@dataclass
class ClassInfo:
    name: str
    kind: str  # "class", "struct", "interface"
    file: str  # 定义所在的文件路径
    parent: Optional[str] = None  # 基类名称
    is_dynamic: bool = False  # 是否标记为 @dynamic
    interfaces: List[str] = field(default_factory=list)  # 实现的接口列表
    fields: Dict[str, FieldInfo] = field(default_factory=dict)
    methods: Dict[str, MethodInfo] = field(default_factory=dict)

    def to_dict(self):
        # 使用 asdict 将 dataclass 转换为字典
        return asdict(self)


# ==========================================
# 2. 编译上下文 (Context Manager)
# ==========================================

class CompileContext:
    """
    全局编译上下文 & 符号表管理器。

    职责：
    1. 维护一个全局的符号字典 (Key: 类名 -> Value: ClassInfo)。
    2. 启动时加载所有依赖库的 symbols.json (只读)。
    3. 启动时加载当前项目的 symbols.json (用于增量编译)。
    4. 提供 API 供 Visitor 注册新发现的类/方法。
    5. 提供 API 供 Visitor 查询父类信息 (用于反射代码生成)。
    6. 编译结束/过程保存最新的符号表。
    """

    def __init__(self, current_symbol_path: str = None, dependency_symbol_paths: List[str] = None):
        self.current_symbol_path = current_symbol_path
        self.current_file_processing = ""  # 当前正在处理的源文件路径 (供 Visitor 设置)

        # 核心存储：符号表
        # Key: Class/Struct Name
        # Value: ClassInfo 对象 (如果是当前编译产生的) OR 字典 (如果是从 JSON 加载的)
        self.symbols: Dict[str, Union[ClassInfo, dict]] = {}

        # 1. 加载依赖 (只读，作为基础知识库)
        if dependency_symbol_paths:
            for path in dependency_symbol_paths:
                self._load_file(path, is_dependency=True)

        # 2. 加载自身 (读写，用于增量更新)
        # 这样我们能保留之前编译的其他文件的信息
        if current_symbol_path:
            self._load_file(current_symbol_path, is_dependency=False)

    def _load_file(self, path: str, is_dependency: bool):
        if not os.path.exists(path):
            return
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                loaded_symbols = data.get("symbols", {})

                # 合并策略：字典更新
                # 注意：如果有命名冲突，后加载的会覆盖先加载的。
                # 通常依赖项应该在前面加载，当前项目在后面加载。
                self.symbols.update(loaded_symbols)

                # print(f"[Context] Loaded {len(loaded_symbols)} symbols from {path}")
        except Exception as e:
            print(f"[Context] Error loading symbol file {path}: {e}")

    def save(self):
        """将当前内存中的符号表保存到 current_symbol_path"""
        if not self.current_symbol_path:
            return

        try:
            os.makedirs(os.path.dirname(self.current_symbol_path), exist_ok=True)

            # 序列化内存中的数据
            output_symbols = {}
            for name, sym in self.symbols.items():
                if hasattr(sym, "to_dict"):
                    output_symbols[name] = sym.to_dict()
                else:
                    # 已经是字典（来自依赖加载），直接保存
                    output_symbols[name] = sym

            output_data = {
                "meta": {
                    "generator": "Chrono Transpiler",
                    "version": "1.0.0"
                },
                "symbols": output_symbols
            }

            with open(self.current_symbol_path, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=4)

            # print(f"[Context] Saved symbols to {self.current_symbol_path}")

        except Exception as e:
            print(f"[Context] Error saving symbols: {e}")

    # --- Visitor 交互 API ---

    def set_current_file(self, filename: str):
        self.current_file_processing = filename

    def register_class(self, info: ClassInfo):
        """
        注册一个新的类/Struct定义。
        通常在 visitClassDefinition / visitStructDefinition 中调用。
        """
        self.symbols[info.name] = info
        # 实时保存，防止编译器崩溃导致数据丢失，同时也方便调试
        self.save()

    def get_parent_class(self, class_name: str) -> str:
        """
        查询指定类的父类名称。
        用于 visitImplementationBlock 生成正确的反射回退代码。
        """
        info = self.symbols.get(class_name)
        if not info:
            # 如果找不到，默认回退到 CHObject (最安全的假设)
            return "CHObject"

        # 处理 info 可能是对象也可能是字典的情况
        if isinstance(info, dict):
            return info.get("parent") or "CHObject"
        else:
            return info.parent or "CHObject"

    def is_dynamic_class(self, class_name: str) -> bool:
        """查询一个类是否被标记为 @dynamic"""
        info = self.symbols.get(class_name)
        if not info: return False

        if isinstance(info, dict):
            return info.get("is_dynamic", False)
        else:
            return info.is_dynamic