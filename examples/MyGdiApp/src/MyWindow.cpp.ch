// file: project/MyWindow.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "MyWindow"
import <iostream>

implement MyWindow {

    init(app: Application*, w: int, h: int) : Window(L"Chrono Showcase", app, w, h) {
        // 默认背景色
        this->m_bgColor = Color(255, 255, 255, 255);
    }

    func setBackgroundColor(r: u8, g: u8, b: u8) {
        this->m_bgColor = Color(255, r, g, b);

        if (this->m_hWnd != NULL) {
            // 请求重绘
            InvalidateRect(this->m_hWnd, NULL, true);
            UpdateWindow(this->m_hWnd);
        }
    }

    func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT
    {
        switch (uMsg) {
            // 拦截擦除背景消息，防止闪烁
            case WM_ERASEBKGND {
                return 1;
            }

            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this->m_hWnd, &ps);

                var graphics = Graphics(hdc);

                // [核心] 使用设定的背景色清除全屏
                // 这次肯定能工作，因为之前的蓝色方块证明了 graphics 对象是有效的
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