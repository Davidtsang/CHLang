
// --- @cpp Block Start ---
#define UNICODE
#define _UNICODE
// --- @cpp Block End ---

#include <windows.h>
#include <gdiplus.h>
#include <cstdint>

// --- @cpp Block Start ---
#pragma comment(lib, "gdi32.lib")
#pragma comment(lib, "user32.lib")
#pragma comment(lib, "gdiplus.lib")

// --- 3. 使用 Gdiplus 命名空间 ---
using namespace Gdiplus;

// --- 4. 全局变量 ---
ULONG_PTR g_gdiplusToken;
// --- @cpp Block End ---

LRESULT CALLBACK WindowProc(HWND hWnd, UINT uMsg, WPARAM wParam,
                            LPARAM lParam) {
  switch (uMsg) {
  case WM_PAINT: {
    PAINTSTRUCT ps;
    HDC hdc = BeginPaint(hWnd, &ps);
    auto graphics = Graphics(hdc);
    auto pen = Pen(Color(255, 255, 0, 0), static_cast<float>(3.0));
    auto brush = SolidBrush(Color(128, 0, 0, 255));
    graphics.FillRectangle(&brush, 10, 10, 300, 200);
    graphics.DrawEllipse(&pen, 10, 10, 300, 200);
    EndPaint(hWnd, &ps);
    return 0;
  }
  case WM_DESTROY: {
    PostQuitMessage(0);
    return 0;
  }
  }
  return DefWindowProc(hWnd, uMsg, wParam, lParam);
}

int WINAPI WinMain(_In_ HINSTANCE hInstance, _In_opt_ HINSTANCE hPrevInstance,
                   _In_ LPSTR lpCmdLine, _In_ int nCmdShow) {
  GdiplusStartupInput gdiplusStartupInput;
  GdiplusStartup(&g_gdiplusToken, &gdiplusStartupInput, NULL);
  WNDCLASSEX wc = {};
  wc.cbSize = sizeof(WNDCLASSEX);
  wc.style = CS_HREDRAW | CS_VREDRAW;
  wc.lpfnWndProc = WindowProc;
  wc.hInstance = hInstance;
  wc.lpszClassName = L"GDIPlusDemoWindow";
  wc.hCursor = LoadCursor(NULL, IDC_ARROW);
  wc.hbrBackground = reinterpret_cast<HBRUSH>(COLOR_WINDOW + 1);
  if (!RegisterClassEx(&wc)) {
    MessageBox(NULL, L"窗口类注册失败!", L"错误", MB_ICONEXCLAMATION | MB_OK);
    return 0;
  }
  HWND hWnd = CreateWindowEx(WS_EX_CLIENTEDGE, L"GDIPlusDemoWindow",
                             L"纯 Chrono GDI+ 演示 (翻译版)",
                             WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT,
                             640, 480, NULL, NULL, hInstance, NULL);
  if (hWnd == NULL) {
    MessageBox(NULL, L"窗口创建失败!", L"错误", MB_ICONEXCLAMATION | MB_OK);
    return 0;
  }
  ShowWindow(hWnd, nCmdShow);
  UpdateWindow(hWnd);
  MSG msg = {};
  while (GetMessage(&msg, NULL, 0, 0)) {
    TranslateMessage(&msg);
    DispatchMessage(&msg);
  }
  GdiplusShutdown(g_gdiplusToken);
  return static_cast<int32_t>(msg.wParam);
}
