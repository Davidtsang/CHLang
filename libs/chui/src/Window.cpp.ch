// file: framework/Window.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "chui/Window"
import <iostream>

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

@dynamic
implement Window {

    init(title: LPCWSTR, app: Application*, width: int, height: int) {
        this->m_app = app;
        this->m_nextId = 100;

        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = app->getHInstance();

        //wc.hIcon = LoadIcon(app->getHInstance(), MAKEINTRESOURCE(IDI_MAIN_ICON));
        //wc.hIconSm = LoadIcon(app->getHInstance(), MAKEINTRESOURCE(IDI_MAIN_ICON));
        wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);
        wc.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

        wc.hCursor = LoadCursor(NULL, IDC_ARROW);
        wc.lpszClassName = L"CHWindowClass";
        wc.hbrBackground = NULL;

        RegisterClassEx(&wc); // 忽略重复注册错误

        std::cout << "[Window] Creating Window (Inherits Widget)..." << std::endl;

        // 这里的 this 是 Window*，由于继承关系，它可以安全地转换为 Widget*
        // 赋值给基类的 m_hWnd
        this->m_hWnd = CreateWindowExW(
            0,
            L"CHWindowClass",
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

    func addChild(widget: Widget*) {
        var id: int = this->m_nextId;
        this->m_nextId = this->m_nextId + 1;

        widget->create(this->m_hWnd, id);
        this->m_lookup[id] = widget;

        // 这里我们需要管理生命周期。
        // 因为 vector 存的是 unique_ptr，我们需要把裸指针包回去。
        // 警告：这假设调用者放弃了 widget 的所有权（这在 createWidget 之后是合理的）
        @cpp
        this->m_children.push_back(std::unique_ptr<Widget>(widget));
        @end
    }

    func setMenuBar(menu: Menu*) {
        //@cpp
        SetMenu(this->m_hWnd, menu->m_hMenu);
        DrawMenuBar(this->m_hWnd);
        //@end
    }

    func bindMenuAction(id: i32, cb: std::function<void()>) {
        this->m_menuCallbacks[id] = cb;
    }

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        switch (uMsg) {
            case WM_COMMAND {
                var id = LOWORD(wParam);
                var code = HIWORD(wParam);
                var hControl = lParam; // 控件句柄

                // 1. 检查是否是菜单消息 (lParam == 0 表示不是控件发的)
                if (hControl == 0 && code == 0) {
                    // 查找回调
                    if (this->m_menuCallbacks.count(id) > 0) {
                        var cb = this->m_menuCallbacks[id];
                        if (cb) { cb(); }
                    }
                    return 0;
                }

                // 2. 否则是控件消息 (交给 Widget 处理)
                if (this->m_lookup.count(id) > 0) {
                    var widget: Widget* = this->m_lookup[id];
                    widget->onCommand(code);
                }
                return 0;
            }
            // ... 其他 case ...
        }
        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }

}