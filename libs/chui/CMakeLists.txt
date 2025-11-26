cmake_minimum_required(VERSION 3.10)
project(chui)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 1. 路径配置
set(RUNTIME_REL_PATH "../../runtime")
get_filename_component(RUNTIME_DIR "${CMAKE_CURRENT_SOURCE_DIR}/${RUNTIME_REL_PATH}" ABSOLUTE)

set(DIST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build/dist")

# 安全检查
if(NOT EXISTS "${DIST_DIR}")
    message(FATAL_ERROR "[chui] Build artifacts not found in ${DIST_DIR}. Please run 'python build.py transpile -d libs/chui' first.")
endif()

set(INCLUDE_DIR "${DIST_DIR}/include")
set(SRC_DIR     "${DIST_DIR}/src")

# 2. 定义库
# 扫描所有源文件 (包括 WinMain.cpp)
file(GLOB LIB_SOURCES "${SRC_DIR}/*.cpp")

add_library(chui STATIC ${LIB_SOURCES})

# [核心修复] 必须是 PUBLIC，这样 MyGdiApp 才能继承这个路径
target_include_directories(chui PUBLIC
    "${INCLUDE_DIR}" # 让外部能找到 <chui/Application.h>
    "${RUNTIME_DIR}" # 让外部能找到 <CHObject.h>
)

# 3. 测试目标 (仅在独立构建时启用)
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    message(STATUS "[chui] Standalone mode: Tests enabled")
    # ... (测试相关配置可以略过，不影响 MyGdiApp)
else()
    message(STATUS "[chui] Library mode: Tests disabled")
endif()