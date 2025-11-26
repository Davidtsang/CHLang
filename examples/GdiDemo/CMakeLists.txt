cmake_minimum_required(VERSION 3.10)
project(GdiDemo)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- Path Setup ---
set(RUNTIME_REL_PATH "../../runtime")
get_filename_component(RUNTIME_DIR "${CMAKE_CURRENT_SOURCE_DIR}/${RUNTIME_REL_PATH}" ABSOLUTE)
set(DIST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build/dist")

if(NOT EXISTS "${DIST_DIR}")
    message(FATAL_ERROR "Build artifacts not found. Run 'python build.py transpile' first.")
endif()

# --- Executable Target ---
# App 模式下，src 包含 main 函数，test 目录通常为空或作为辅助
file(GLOB APP_SOURCES "${DIST_DIR}/src/*.cpp")

add_executable(GdiDemo 
    ${APP_SOURCES}
    "${RUNTIME_DIR}/CHString.cpp" # 链接运行时
)

# 包含路径
target_include_directories(GdiDemo PRIVATE 
    "${DIST_DIR}/include"
    ${RUNTIME_DIR}
)

# 链接其他库 (示例)
# target_link_libraries(GdiDemo PRIVATE some_lib)

set_target_properties(GdiDemo PROPERTIES VS_DEBUGGER_WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")
