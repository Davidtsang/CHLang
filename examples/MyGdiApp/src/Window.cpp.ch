// file: framework/Window.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Window"
import <iostream>
import "resource.h"
// 全局窗口过程
func GlobalWindowProc(
    hWnd: HWND, uMsg: UINT, wParam: WPARAM, lParam: LPARAM
) -> C_LRESULT_CALLBACK
{
    var pWidget: Widget* = NULL;

    if (uMsg == WM_NCCREATE) {
        // 获取 this 指针
        var pCreate: CREATESTRUCT* = reinterpret_cast<CREATESTRUCT*>(lParam);
        pWidget = reinterpret_cast<Widget*>(pCreate->lpCreateParams);

        // 保存到用户数据
        SetWindowLongPtr(hWnd, GWLP_USERDATA, reinterpret_cast<LONG_PTR>(pWidget));

        // [关键] 此时 pWidget 指向的是 Window 对象 (它是 Widget 的子类)
        // 这一步设置的是 Widget::m_hWnd
        pWidget->m_hWnd = hWnd;
    } else {
        var ptrVal: LONG_PTR = GetWindowLongPtr(hWnd, GWLP_USERDATA);
        pWidget = reinterpret_cast<Widget*>(ptrVal);
    }

    if (pWidget != NULL) {
        return pWidget->handleMessage(uMsg, wParam, lParam);
    }
    return DefWindowProc(hWnd, uMsg, wParam, lParam);
}

implement Window {

    init(title: LPCWSTR, app: Application*, width: int, height: int) {
        this->m_app = app;
        this->m_nextId = 100;

        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = app->getHInstance();

        wc.hIcon = LoadIcon(app->getHInstance(), MAKEINTRESOURCE(IDI_MAIN_ICON));
        wc.hIconSm = LoadIcon(app->getHInstance(), MAKEINTRESOURCE(IDI_MAIN_ICON));

        wc.hCursor = LoadCursor(NULL, IDC_ARROW);
        wc.lpszClassName = L"ChronoWindowClass";
        wc.hbrBackground = NULL;

        RegisterClassEx(&wc); // 忽略重复注册错误

        std::cout << "[Window] Creating Window (Inherits Widget)..." << std::endl;

        // 这里的 this 是 Window*，由于继承关系，它可以安全地转换为 Widget*
        // 赋值给基类的 m_hWnd
        this->m_hWnd = CreateWindowExW(
            0,
            L"ChronoWindowClass",
            title,
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT, CW_USEDEFAULT,
            width, height,
            NULL, NULL, app->getHInstance(),
            this
        );

        if (this->m_hWnd == NULL) {
            std::cout << "[Window] Error: Creation failed!" << std::endl;
        } else {
            std::cout << "[Window] Created. HWND: " << this->m_hWnd << std::endl;
        }
    }

    deinit { }

    func show() {
        if (this->m_hWnd == NULL) {
            std::cout << "[Window] Error: HWND is null." << std::endl;
        } else {
            // 强制显示
            ShowWindow(this->m_hWnd, 5); // SW_SHOW
            UpdateWindow(this->m_hWnd);
        }
    }

    func addChild(widget: unique<Widget>) {
        var id: int = this->m_nextId;
        this->m_nextId = this->m_nextId + 1;

        var ptr: Widget* = widget.get();
        ptr->create(this->m_hWnd, id);

        this->m_lookup[id] = ptr;
        this->m_children.push_back(@move(widget));
    }

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        switch (uMsg) {
            case WM_COMMAND {
                var id: int = LOWORD(wParam);
                var code: int = HIWORD(wParam);
                if (this->m_lookup.count(id) > 0) {
                    var widget: Widget* = this->m_lookup[id];
                    widget->onCommand(code);
                }
                return 0;
            }
            case WM_DESTROY {
                PostQuitMessage(0);
                return 0;
            }
        }
        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }
}