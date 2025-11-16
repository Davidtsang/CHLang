// file: gdiplus_demo.ch
// 目的: 完整的 GDI+ 演示程序 (Chrono 版本)
// [最终方案] "typemap" 只用于 Chrono 解析器无法处理的 C++ 语法。
//           "WM_PAINT", "NULL" 等宏常量 *不* 需要 typemap。
#define UNICODE
#define _UNICODE

// --- 1. 包含核心头文件 ---
import <windows.h>
import <gdiplus.h>
import <cstdint>
// --- 2. 链接 GDI+ 库 ---

#pragma comment(lib, "gdi32.lib")
#pragma comment(lib, "user32.lib")
#pragma comment(lib, "gdiplus.lib")

@cpp
// --- 3. 使用 Gdiplus 命名空间 ---
using namespace Gdiplus;
@end

var g_gdiplusToken: ULONG_PTR;
// --- 5. [typemap] C++ 互操作性映射 ---
// [关键] 我们只映射 Chrono 解析器无法识别的 "多词" 或 "带属性" 的类型。
typemap C_LRESULT_CALLBACK = "LRESULT CALLBACK";
typemap C_INT_WINAPI = "int WINAPI";
typemap C_IN_HINSTANCE = "_In_ HINSTANCE";
typemap C_IN_OPT_HINSTANCE = "_In_opt_ HINSTANCE";
typemap C_IN_LPSTR = "_In_ LPSTR";
typemap C_IN_INT = "_In_ int";
typemap C_HBRUSH = "HBRUSH" ;// (因为 reinterpret_cast[T] 需要一个类型)

//
// 像 "WM_PAINT", "NULL", "COLOR_WINDOW" 这样的宏常量
// 都是合法的 Chrono 标识符, 它们 *不* 需要 typemap。
// 翻译器会原样传递它们, C++ 预处理器会处理它们。
//

// --- 6. 窗口过程 (Window Procedure) ---
func WindowProc(
    hWnd: HWND,
    uMsg: UINT,
    wParam: WPARAM,
    lParam: LPARAM
) -> C_LRESULT_CALLBACK
{
    // [关键] 直接使用 C++ 宏常量
    switch (uMsg) {

        case WM_PAINT {

            var ps: PAINTSTRUCT;
            var hdc: HDC = BeginPaint(hWnd, &ps);

            var graphics = Graphics(hdc);
            var pen = Pen(Color(255, 255, 0, 0), static_cast[f32](3.0));
            var brush = SolidBrush(Color(128, 0, 0, 255));

            graphics.FillRectangle(&brush, 10, 10, 300, 200);
            graphics.DrawEllipse(&pen, 10, 10, 300, 200);

            EndPaint(hWnd, &ps);
            return 0;
        }

        case WM_DESTROY {
            PostQuitMessage(0);
            return 0;
        }
    }

    return DefWindowProc(hWnd, uMsg, wParam, lParam);
}

// --- 7. Windows 程序入口 (WinMain) ---
func WinMain(
    hInstance: C_IN_HINSTANCE,
    hPrevInstance: C_IN_OPT_HINSTANCE,
    lpCmdLine: C_IN_LPSTR,
    nCmdShow: C_IN_INT
) -> C_INT_WINAPI
{
    var gdiplusStartupInput: GdiplusStartupInput;
    GdiplusStartup(&g_gdiplusToken, &gdiplusStartupInput, NULL);

    var wc: WNDCLASSEX = {};

    wc.cbSize = sizeof(WNDCLASSEX);
    wc.style = CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = L"GDIPlusDemoWindow";
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);

    // [关键] reinterpret_cast + 宏常量
    wc.hbrBackground = reinterpret_cast[C_HBRUSH](COLOR_WINDOW + 1);

    if (!RegisterClassEx(&wc)) {
        MessageBox(NULL, L"窗口类注册失败!", L"错误", MB_ICONEXCLAMATION | MB_OK);
        return 0;
    }

    var hWnd: HWND = CreateWindowEx(
        WS_EX_CLIENTEDGE,
        L"GDIPlusDemoWindow",
        L"纯 Chrono GDI+ 演示 (翻译版)",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 640, 480,
        NULL, NULL, hInstance, NULL
    );

    if (hWnd == NULL) {
        MessageBox(NULL, L"窗口创建失败!", L"错误", MB_ICONEXCLAMATION | MB_OK);
        return 0;
    }

    ShowWindow(hWnd, nCmdShow);
    UpdateWindow(hWnd);

    var msg: MSG = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    GdiplusShutdown(g_gdiplusToken);

    return static_cast[int](msg.wParam);
}