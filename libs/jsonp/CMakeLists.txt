cmake_minimum_required(VERSION 3.10)
project(jsonp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- 1. 路径配置 ---
# 这里的相对路径根据你的实际情况可能需要微调
set(RUNTIME_REL_PATH "../../runtime")
get_filename_component(RUNTIME_DIR "${CMAKE_CURRENT_SOURCE_DIR}/${RUNTIME_REL_PATH}" ABSOLUTE)

set(DIST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build/dist")

if(NOT EXISTS "${DIST_DIR}")
    message(FATAL_ERROR "Build artifacts not found. Run 'python build.py transpile' first.")
endif()

set(INCLUDE_DIR "${DIST_DIR}/include")
set(SRC_DIR     "${DIST_DIR}/src")
set(TEST_DIR    "${DIST_DIR}/test")

# --- 2. 定义库 (jsonp) ---
file(GLOB LIB_SOURCES "${SRC_DIR}/*.cpp")

add_library(jsonp STATIC ${LIB_SOURCES})

target_include_directories(jsonp PUBLIC
    "${INCLUDE_DIR}"
    ${RUNTIME_DIR}
)

# --- 3. 自动构建所有测试 (每个文件一个 Exe) ---
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    message(STATUS "[jsonp] Building Tests...")

    # 扫描所有测试源文件
    file(GLOB TEST_FILES "${TEST_DIR}/*.cpp")

    foreach(TEST_SRC ${TEST_FILES})
        # 获取文件名 (无后缀)，例如 "test_parser"
        get_filename_component(TEST_NAME ${TEST_SRC} NAME_WE)

        message(STATUS "  + Adding Test Target: ${TEST_NAME}")

        add_executable(${TEST_NAME}
            ${TEST_SRC}
            "${RUNTIME_DIR}/CHString.cpp"
        )

        target_link_libraries(${TEST_NAME} PRIVATE jsonp)

        # 设置调试目录
        set_target_properties(${TEST_NAME} PROPERTIES VS_DEBUGGER_WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")
    endforeach()
else()
    message(STATUS "[jsonp] Building in Library Mode (Tests Disabled)")
endif()