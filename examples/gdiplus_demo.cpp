#define UNICODE
#define _UNICODE
#include <windows.h>
#include <gdiplus.h>
#include <cstdint>
#pragma comment(lib, "gdi32.lib")
#pragma comment(lib, "user32.lib")
#pragma comment(lib, "gdiplus.lib")

// --- @cpp Block Start ---
using namespace Gdiplus;
// --- @cpp Block End ---

// Line 20
ULONG_PTR g_gdiplusToken;

// Line 38 (func WindowProc)

LRESULT CALLBACK WindowProc(HWND hWnd, UINT uMsg, WPARAM wParam,
                            LPARAM lParam) {
  switch (uMsg) {
  case WM_PAINT: {
    // Line 50
    PAINTSTRUCT ps;
    // Line 51
    HDC hdc = BeginPaint(hWnd, &ps);
    // Line 53
    auto graphics = Graphics(hdc);
    // Line 54
    auto pen = Pen(Color(255, 255, 0, 0), static_cast<float>(3.0));
    // Line 55
    auto brush = SolidBrush(Color(128, 0, 0, 255));
    // Line 57
    graphics.FillRectangle(&brush, 10, 10, 300, 200);
    // Line 58
    graphics.DrawEllipse(&pen, 10, 10, 300, 200);
    // Line 60
    EndPaint(hWnd, &ps);
    // Line 61
    return 0;
  }
  case WM_DESTROY: {
    // Line 65
    PostQuitMessage(0);
    // Line 66
    return 0;
  }
  }
  // Line 70
  return DefWindowProc(hWnd, uMsg, wParam, lParam);
  // --- Function End ---
}

// Line 74 (func WinMain)

int WINAPI WinMain(_In_ HINSTANCE hInstance, _In_opt_ HINSTANCE hPrevInstance,
                   _In_ LPSTR lpCmdLine, _In_ int nCmdShow) {
  // Line 81
  GdiplusStartupInput gdiplusStartupInput;
  // Line 82
  GdiplusStartup(&g_gdiplusToken, &gdiplusStartupInput, NULL);
  // Line 84
  WNDCLASSEX wc = {};
  // Line 86
  wc.cbSize = sizeof(WNDCLASSEX);
  // Line 87
  wc.style = CS_HREDRAW | CS_VREDRAW;
  // Line 88
  wc.lpfnWndProc = WindowProc;
  // Line 89
  wc.hInstance = hInstance;
  // Line 90
  wc.lpszClassName = L"GDIPlusDemoWindow";
  // Line 91
  wc.hCursor = LoadCursor(NULL, IDC_ARROW);
  // Line 94
  wc.hbrBackground = reinterpret_cast<HBRUSH>(COLOR_WINDOW + 1);
  if (!RegisterClassEx(&wc)) {
    // Line 97
    MessageBox(NULL, L"窗口类注册失败!", L"错误", MB_ICONEXCLAMATION | MB_OK);
    // Line 98
    return 0;
  }
  // Line 101
  HWND hWnd = CreateWindowEx(WS_EX_CLIENTEDGE, L"GDIPlusDemoWindow",
                             L"纯 CH GDI+ 演示 (翻译版)",
                             WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT,
                             640, 480, NULL, NULL, hInstance, NULL);
  if (hWnd == NULL) {
    // Line 111
    MessageBox(NULL, L"窗口创建失败!", L"错误", MB_ICONEXCLAMATION | MB_OK);
    // Line 112
    return 0;
  }
  // Line 115
  ShowWindow(hWnd, nCmdShow);
  // Line 116
  UpdateWindow(hWnd);
  // Line 118
  MSG msg = {};
  while (GetMessage(&msg, NULL, 0, 0)) {
    // Line 120
    TranslateMessage(&msg);
    // Line 121
    DispatchMessage(&msg);
  }
  // Line 124
  GdiplusShutdown(g_gdiplusToken);
  // Line 126
  return static_cast<int>(msg.wParam);
  // --- Function End ---
}