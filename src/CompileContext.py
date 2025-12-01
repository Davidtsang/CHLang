# src/CompileContext.py
import json
import os
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Union, Any


# ... (ArgInfo, MethodInfo, FieldInfo, ClassInfo 等数据类保持不变) ...
@dataclass
class ArgInfo:
    name: str
    type: str

    def to_dict(self): return asdict(self)


@dataclass
class MethodInfo:
    name: str
    return_type: str
    args: List[ArgInfo] = field(default_factory=list)
    access: str = "public"
    is_static: bool = False
    is_virtual: bool = False
    is_override: bool = False
    is_optional: bool = False
    attributes: Dict[str, str] = field(default_factory=dict)  # [新增] 支持属性

    def to_dict(self): return asdict(self)


@dataclass
class FieldInfo:
    name: str
    type: str
    access: str = "private"
    attributes: Dict[str, str] = field(default_factory=dict)  # [新增] 支持属性

    def to_dict(self): return asdict(self)


@dataclass
class ClassInfo:
    name: str
    kind: str
    file: str
    parent: Optional[str] = None
    is_dynamic: bool = False
    interfaces: List[str] = field(default_factory=list)
    fields: Dict[str, FieldInfo] = field(default_factory=dict)
    methods: Dict[str, MethodInfo] = field(default_factory=dict)

    def to_dict(self): return asdict(self)


class CompileContext:
    # [修改] 增加 project_root 参数
    def __init__(self, current_symbol_path: str = None, dependency_symbol_paths: List[str] = None,
                 project_root: str = None):
        self.current_symbol_path = current_symbol_path
        self.current_file_processing = ""
        self.project_root = project_root  # [新增] 保存项目根目录

        self.symbols: Dict[str, Union[ClassInfo, dict]] = {}

        if dependency_symbol_paths:
            for path in dependency_symbol_paths:
                self._load_file(path, is_dependency=True)

        if current_symbol_path:
            self._load_file(current_symbol_path, is_dependency=False)

    def _load_file(self, path: str, is_dependency: bool):
        if not os.path.exists(path): return
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                loaded_symbols = data.get("symbols", {})
                self.symbols.update(loaded_symbols)
        except Exception as e:
            print(f"[Context] Error loading symbol file {path}: {e}")

    def save(self):
        if not self.current_symbol_path: return
        try:
            os.makedirs(os.path.dirname(self.current_symbol_path), exist_ok=True)

            output_symbols = {}
            for name, sym in self.symbols.items():
                if hasattr(sym, "to_dict"):
                    output_symbols[name] = sym.to_dict()
                else:
                    output_symbols[name] = sym

            output_data = {
                "meta": {"version": "1.0.0"},
                "symbols": output_symbols
            }

            # 智能写入逻辑
            new_content = json.dumps(output_data, indent=4)
            if os.path.exists(self.current_symbol_path):
                with open(self.current_symbol_path, 'r', encoding='utf-8') as f:
                    if f.read() == new_content: return

            with open(self.current_symbol_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

        except Exception as e:
            print(f"[Context] Error saving symbols: {e}")

    def set_current_file(self, filename: str):
        self.current_file_processing = filename

    def register_class(self, info: ClassInfo):
        self.symbols[info.name] = info
        self.save()

    def get_parent_class(self, class_name: str) -> str:
        info = self.symbols.get(class_name)
        if not info: return "CHObject"
        if isinstance(info, dict):
            return info.get("parent") or "CHObject"
        else:
            return info.parent or "CHObject"

    def is_dynamic_class(self, class_name: str) -> bool:
        info = self.symbols.get(class_name)
        if not info: return False
        if isinstance(info, dict):
            return info.get("is_dynamic", False)
        else:
            return info.is_dynamic