// file: framework/WinMain.ch
#define UNICODE
#define _UNICODE

// --- 1. 包含核心头文件 ---
import <windows.h>
import <gdiplus.h> // [ [ [ 修复 1 ] ] ]
import <cstdint>
import "WinMain"

// --- 2. 链接库 ---
#pragma comment(lib, "gdi32.lib")
#pragma comment(lib, "user32.lib")
#pragma comment(lib, "gdiplus.lib") // [ [ [ 修复 1 ] ] ]

@cpp using namespace Gdiplus; @end

// --- 3. typemaps (来自 gdiplus_demo) ---
typemap C_INT_WINAPI = "int WINAPI";
typemap C_IN_HINSTANCE = "_In_ HINSTANCE";
typemap C_IN_OPT_HINSTANCE = "_In_opt_ HINSTANCE";
typemap C_IN_LPSTR = "_In_ LPSTR";
typemap C_IN_INT = "_In_ int";

// --- 4. 框架全局变量 ---
// (Application 构造函数将读取它们)
var g_hInstance: HINSTANCE = NULL;
var g_nCmdShow: int = 0;
var g_gdiplusToken: ULONG_PTR; // [ [ [ 修复 1 ] ] ]

// --- 5. 声明用户必须提供的 "CHMain" ---
func CHMain() -> int;

// --- 6. 实现 *真正* 的 C++ WinMain 入口点 ---
func WinMain(
    hInstance: C_IN_HINSTANCE,
    hPrevInstance: C_IN_OPT_HINSTANCE,
    lpCmdLine: C_IN_LPSTR,
    nCmdShow: C_IN_INT
) -> C_INT_WINAPI
{
    // 1. 保存句柄
    g_hInstance = hInstance;
    g_nCmdShow = nCmdShow;

    // 2. [ [ [ 修复 1: 初始化 GDI+ ] ] ]
    var gdiplusStartupInput: GdiplusStartupInput;
    GdiplusStartup(&g_gdiplusToken, &gdiplusStartupInput, NULL);

    // 3. 调用用户的 Chrono 入口点
    var exit_code: int = CHMain();

    // 4. [ [ [ 修复 1: 关闭 GDI+ ] ] ]
    GdiplusShutdown(g_gdiplusToken);

    return exit_code;
}