// file: framework/WinMain.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

// [关键] Include order
import <algorithm>
import <windows.h>
import <objidl.h>  // [修复] GDI+ 依赖
import <gdiplus.h>
import <cstdint>

#pragma comment(lib, "gdi32.lib")
#pragma comment(lib, "user32.lib")
#pragma comment(lib, "gdiplus.lib")

// 使用 GDI+ 命名空间
@cpp using namespace Gdiplus; @end

// typemaps (保留以兼容 Win32 宏类型)
typemap C_INT_WINAPI = "int WINAPI";
typemap C_IN_HINSTANCE = "_In_ HINSTANCE";
typemap C_IN_OPT_HINSTANCE = "_In_opt_ HINSTANCE";
typemap C_IN_LPSTR = "_In_ LPSTR";
typemap C_IN_INT = "_In_ int";

// 框架全局变量
var g_hInstance: HINSTANCE = NULL;
var g_nCmdShow: int = 0;
var g_gdiplusToken: ULONG_PTR;

// 声明用户必须提供的 "CHMain"
func CHMain() -> int;

// WinMain 入口点
func WinMain(
    hInstance: C_IN_HINSTANCE,
    hPrevInstance: C_IN_OPT_HINSTANCE,
    lpCmdLine: C_IN_LPSTR,
    nCmdShow: C_IN_INT
) -> C_INT_WINAPI
{
    g_hInstance = hInstance;
    g_nCmdShow = nCmdShow;

    // 初始化 GDI+ (栈对象使用 .)
    var gdiplusStartupInput: GdiplusStartupInput;
    GdiplusStartup(&g_gdiplusToken, &gdiplusStartupInput, NULL);

    var exit_code: int = CHMain();

    GdiplusShutdown(g_gdiplusToken);

    return exit_code;
}