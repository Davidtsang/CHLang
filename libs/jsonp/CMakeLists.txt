cmake_minimum_required(VERSION 3.10)
project(jsonp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- Path Setup ---
set(RUNTIME_REL_PATH "../../runtime")
get_filename_component(RUNTIME_DIR "${CMAKE_CURRENT_SOURCE_DIR}/${RUNTIME_REL_PATH}" ABSOLUTE)
set(DIST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build/dist")

if(NOT EXISTS "${DIST_DIR}")
    message(FATAL_ERROR "Build artifacts not found. Run 'python build.py transpile' first.")
endif()

# --- Library Target ---
file(GLOB LIB_SOURCES "${DIST_DIR}/src/*.cpp")
add_library(jsonp STATIC ${LIB_SOURCES})

target_include_directories(jsonp PUBLIC 
    "${DIST_DIR}/include"
    ${RUNTIME_DIR}
)

# --- Test Target (Standalone Only) ---
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    message(STATUS "[jsonp] Building Tests (Standalone Mode)")
    file(GLOB TEST_SOURCES "${DIST_DIR}/test/*.cpp")

    add_executable(jsonp_test 
        ${TEST_SOURCES}
        "${RUNTIME_DIR}/CHString.cpp"
    )
    target_link_libraries(jsonp_test PRIVATE jsonp)
    set_target_properties(jsonp_test PROPERTIES VS_DEBUGGER_WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")
endif()
