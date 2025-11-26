cmake_minimum_required(VERSION 3.10)
project(MyGdiApp)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory("../../libs/jsonp" jsonp_lib)
add_subdirectory("../../libs/chui"  chui_lib)

set(DIST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build/dist")
file(GLOB APP_SOURCES "${DIST_DIR}/src/*.cpp")

get_filename_component(RUNTIME_DIR "../../runtime" ABSOLUTE)

# [关键修复] 添加 WIN32 关键字
# 这会告诉链接器使用 /SUBSYSTEM:WINDOWS，从而寻找 WinMain 入口点
add_executable(MyGdiApp WIN32
    ${APP_SOURCES}
    # ${APP_RESOURCES} (已注释)
    #"${RUNTIME_DIR}/CHString.cpp"
)

target_link_libraries(MyGdiApp PRIVATE
    gdi32 user32 gdiplus
    jsonp
    chui
)

target_include_directories(MyGdiApp PRIVATE
    "${DIST_DIR}/include"
    "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/chui/build/dist/include"
)