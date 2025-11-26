# pkg.py - Chrono Package Manager
# Usage: python pkg.py create <path> [--type lib|app]

import os
import sys
import argparse

# ==========================================
# 1. 通用配置模板 (config.json)
# ==========================================
# 保持与 build.py 的 Phase 1/2 逻辑一致：include 目录被识别为头文件
TEMPLATE_CONFIG = """{{
    "package_name": "{name}",
    "version": "0.1.0",
    "transpiler_script": "{transpiler_path}",
    "build_rules": [
        {{
            "source_dir": "include",
            "output_dir": "build/dist/include",
            "note": "Public Headers (Phase 1)"
        }},
        {{
            "source_dir": "src",
            "output_dir": "build/dist/src",
            "note": "Source Files (Phase 2)"
        }},
        {{
            "source_dir": "test",
            "output_dir": "build/dist/test",
            "note": "Tests"
        }}
    ]
}}
"""

# ==========================================
# 2. CMake 模板 (关键升级)
# ==========================================

# 模板 A: 库模式 (好公民模式)
TEMPLATE_CMAKE_LIB = """cmake_minimum_required(VERSION 3.10)
project({name})

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- 1. Path Setup ---
set(RUNTIME_REL_PATH "{runtime_path}")
get_filename_component(RUNTIME_DIR "${{CMAKE_CURRENT_SOURCE_DIR}}/${{RUNTIME_REL_PATH}}" ABSOLUTE)
set(DIST_DIR "${{CMAKE_CURRENT_SOURCE_DIR}}/build/dist")

if(NOT EXISTS "${{DIST_DIR}}")
    message(FATAL_ERROR "Build artifacts not found. Run 'python build.py transpile -d .' first.")
endif()

# --- 2. Dependency Loading (Sync with build.py) ---
# build.py 会自动生成 cmake_deps.cmake，包含 add_subdirectory 指令
set(DEPS_FILE "${{CMAKE_CURRENT_SOURCE_DIR}}/build/cmake_deps.cmake")
if(EXISTS "${{DEPS_FILE}}")
    message(STATUS "[{name}] Loading dependencies from ${{DEPS_FILE}}")
    include("${{DEPS_FILE}}")
endif()

# --- 3. Library Target ---
file(GLOB LIB_SOURCES "${{DIST_DIR}}/src/*.cpp")

add_library({name} STATIC ${{LIB_SOURCES}})

# 让使用者能找到头文件 (PUBLIC)
target_include_directories({name} PUBLIC 
    "${{DIST_DIR}}/include"
    "${{RUNTIME_DIR}}"
)

# 链接 build.py 识别到的其他依赖库 (如果有)
if(DEFINED CHRONO_LIBS)
    target_link_libraries({name} PRIVATE ${{CHRONO_LIBS}})
endif()

# --- 4. Test Target (Standalone Only) ---
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    message(STATUS "[{name}] Building Tests (Standalone Mode)")
    file(GLOB TEST_SOURCES "${{DIST_DIR}}/test/*.cpp")

    add_executable({name}_test 
        ${{TEST_SOURCES}}
        "${{RUNTIME_DIR}}/CHString.cpp"
    )

    # 链接自身 + 依赖
    target_link_libraries({name}_test PRIVATE {name})

    set_target_properties({name}_test PROPERTIES VS_DEBUGGER_WORKING_DIRECTORY "${{CMAKE_CURRENT_SOURCE_DIR}}")
endif()
"""

# 模板 B: 应用程序模式 (直接生成 EXE)
TEMPLATE_CMAKE_APP = """cmake_minimum_required(VERSION 3.10)
project({name})

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- 1. Path Setup ---
set(RUNTIME_REL_PATH "{runtime_path}")
get_filename_component(RUNTIME_DIR "${{CMAKE_CURRENT_SOURCE_DIR}}/${{RUNTIME_REL_PATH}}" ABSOLUTE)
set(DIST_DIR "${{CMAKE_CURRENT_SOURCE_DIR}}/build/dist")

if(NOT EXISTS "${{DIST_DIR}}")
    message(FATAL_ERROR "Build artifacts not found. Run 'python build.py transpile -d .' first.")
endif()

# --- 2. Dependency Loading (Sync with build.py) ---
# 关键：加载由 build.py 生成的依赖描述文件
set(DEPS_FILE "${{CMAKE_CURRENT_SOURCE_DIR}}/build/cmake_deps.cmake")
if(EXISTS "${{DEPS_FILE}}")
    message(STATUS "[{name}] Loading dependencies from ${{DEPS_FILE}}")
    include("${{DEPS_FILE}}")
else()
    message(STATUS "[{name}] No external dependencies found (build/cmake_deps.cmake missing)")
endif()

# --- 3. Executable Target ---
file(GLOB APP_SOURCES "${{DIST_DIR}}/src/*.cpp")

# Win32 应用通常需要 WIN32 标志，如果是控制台应用去掉 WIN32
add_executable({name} 
    ${{APP_SOURCES}}
    "${{RUNTIME_DIR}}/CHString.cpp" # 链接运行时
)

# 包含路径
target_include_directories({name} PRIVATE 
    "${{DIST_DIR}}/include"
    "${{RUNTIME_DIR}}"
)

# --- 4. Linking ---
# 链接系统库
target_link_libraries({name} PRIVATE gdi32 user32 gdiplus)

# 链接 Chrono 依赖库 (由 build.py 计算并存入 CHRONO_LIBS)
if(DEFINED CHRONO_LIBS)
    message(STATUS "[{name}] Linking with: ${{CHRONO_LIBS}}")
    target_link_libraries({name} PRIVATE ${{CHRONO_LIBS}})
endif()

set_target_properties({name} PROPERTIES VS_DEBUGGER_WORKING_DIRECTORY "${{CMAKE_CURRENT_SOURCE_DIR}}")
"""

# ==========================================
# 3. 源码模板 (适配新的 Symbol Table 风格)
# ==========================================

# Lib: Header
TEMPLATE_LIB_HEADER = """#pragma once
import "runtime/CHObject.h"
import <string>

@dynamic
class {class_name} : CHObject {{
    var m_name: std::string;

    public init(name: std::string);
    public func greet();

    // 你可以在这里添加更多方法，build.py 会自动收集它们到 symbols.json
}}
"""

# Lib: Source
TEMPLATE_LIB_SOURCE = """import "{name}/{class_name}"
import "runtime/CH.h"

@dynamic
implement {class_name} {{
    init(name: std::string) {{
        this->m_name = name;
    }}

    func greet() {{
        CH::Log(std::string("Hello library world from ") + this->m_name);
    }}
}}
"""

# Lib: Test
TEMPLATE_LIB_TEST = """import "{name}/{class_name}"
import "runtime/CH.h"

func main() -> int {{
    CH::Log("--- Testing Library {name} ---");

    var obj: {class_name}* = new {class_name}("Chrono");
    obj->greet();

    // 动态调用测试 (验证反射表是否生成成功)
    // obj~>greet(); 

    obj->release();
    return 0;
}}
"""

# App: Main
TEMPLATE_APP_MAIN = """import "runtime/CH.h"
import <string>

// 简单的应用入口类
@dynamic
class App : CHObject {{
    public static func run();
}}

@dynamic
implement App {{
    func run() {{
        CH::Log(std::string("Hello Application World!"));
        CH::Log(std::string("Symbols and Reflection are working!"));
    }}
}}

func main() -> int {{
    CH::Log("--- Starting App: {name} ---");
    App::run();
    return 0;
}}
"""


# ==========================================
# Logic
# ==========================================

def get_relative_path(from_dir, to_dir):
    rel = os.path.relpath(to_dir, from_dir)
    return rel.replace("\\", "/")


def create_project(target_path, project_type):
    full_path = os.path.abspath(target_path)
    package_name = os.path.basename(full_path)  # 自动推导包名

    if not package_name:
        print("错误: 路径无效，无法提取包名。")
        return False

    if os.path.exists(full_path):
        print(f"错误: 目录 '{full_path}' 已存在。")
        return False

    # 计算路径
    root_dir = os.getcwd()
    transpiler_abs = os.path.join(root_dir, "src/transpiler.py")
    rel_transpiler = get_relative_path(full_path, transpiler_abs)

    runtime_abs = os.path.join(root_dir, "runtime")
    rel_runtime = get_relative_path(full_path, runtime_abs)

    print(f"正在创建 [{project_type.upper()}]: {package_name}")
    print(f"  位置: {full_path}")

    # 创建目录 (符合 build.py 的 include/src 分离规范)
    dirs = [f"include/{package_name}", "src", "test"]
    for d in dirs:
        os.makedirs(os.path.join(full_path, d))

    # 准备文件列表
    files = []

    # 1. config.json (通用)
    files.append(("config.json", TEMPLATE_CONFIG.format(
        name=package_name, transpiler_path=rel_transpiler
    )))

    # 2. CMakeLists.txt (根据类型)
    cmake_content = TEMPLATE_CMAKE_LIB if project_type == "lib" else TEMPLATE_CMAKE_APP
    files.append(("CMakeLists.txt", cmake_content.format(
        name=package_name, runtime_path=rel_runtime
    )))

    # 3. 源码文件 (根据类型)
    class_name = package_name.capitalize()  # 首字母大写作为类名

    if project_type == "lib":
        # 库模式：头文件 + 实现 + 测试
        files.append((f"include/{package_name}/{class_name}.h.ch", TEMPLATE_LIB_HEADER.format(class_name=class_name)))
        files.append((f"src/{class_name}.cpp.ch", TEMPLATE_LIB_SOURCE.format(name=package_name, class_name=class_name)))
        files.append((f"test/test_main.ch", TEMPLATE_LIB_TEST.format(name=package_name, class_name=class_name)))
    else:
        # 应用模式：主程序入口
        files.append((f"src/main.cpp.ch", TEMPLATE_APP_MAIN.format(name=package_name)))

    # 写入文件
    for path, content in files:
        p = os.path.join(full_path, path)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [+] {path}")

    print(f"\n=== {project_type.upper()} '{package_name}' 创建成功！ ===")
    print("下一步操作：")
    print(f"  1. 转译代码: python build.py transpile -d {target_path}")
    print(f"  2. 生成工程: cd {target_path} && mkdir build_cmake && cd build_cmake")
    print(f"  3. 编译运行: cmake -G Ninja .. && cmake --build .")
    print(f"     (或者直接使用: python make.py {target_path} --run)")

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chrono 包管理器")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # create 命令
    cmd_create = subparsers.add_parser('create', help='创建新项目')
    cmd_create.add_argument('path', help='项目路径 (例如: libs/my_lib)')
    cmd_create.add_argument('--type', choices=['lib', 'app'], default='lib', help='项目类型 (默认: lib)')

    args = parser.parse_args()
    if args.command == "create":
        create_project(args.path, args.type)