// file: project/MyWindow.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "MyWindow"
import <iostream>

implement MyWindow {

    init(app: Application*, w: int, h: int) : Window(L"Chrono Showcase", app, w, h) {
        this->m_bgColor = Color(255, 255, 255, 255);
    }

    // [修复] 参数改为 CGColor 并进行转换
    func setBackgroundColor(c: CGColor) {
        // CGColor -> GDI+ Color
        this->m_bgColor = Color(c.a, c.r, c.g, c.b);

        if (this->m_hWnd != NULL) {
            InvalidateRect(this->m_hWnd, NULL, true);
            UpdateWindow(this->m_hWnd);
        }
    }

    func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT
    {
        switch (uMsg) {
            case WM_ERASEBKGND { return 1; }

            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this->m_hWnd, &ps);
                var graphics = Graphics(hdc);
                graphics.Clear(this->m_bgColor);
                EndPaint(this->m_hWnd, &ps);
                return 0;
            }

            case WM_DESTROY {
                PostQuitMessage(0);
                return 0;
            }
        }
        return Window::handleMessage(uMsg, wParam, lParam);
    }
}