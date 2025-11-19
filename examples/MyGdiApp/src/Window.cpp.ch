import "Window"

// 全局窗口过程函数
func GlobalWindowProc(
    hWnd: HWND, uMsg: UINT, wParam: WPARAM, lParam: LPARAM
) -> C_LRESULT_CALLBACK
{
    var pWindow: Window* = NULL;

    if (uMsg == WM_NCCREATE) {
        // 1. 获取创建参数中的 this 指针
        var pCreate: CREATESTRUCT* = reinterpret_cast<CREATESTRUCT*>(lParam);
        pWindow = reinterpret_cast<Window*>(pCreate->lpCreateParams);

        // 2. 保存 this 指针到窗口句柄
        SetWindowLongPtr(hWnd, GWLP_USERDATA, reinterpret_cast<LONG_PTR>(pWindow));
        pWindow->m_hWnd = hWnd;
    } else {
        // 3. 取回 this 指针
        var ptrVal: LONG_PTR = GetWindowLongPtr(hWnd, GWLP_USERDATA);
        pWindow = reinterpret_cast<Window*>(ptrVal);
    }

    if (pWindow != NULL) {
        return pWindow->handleMessage(uMsg, wParam, lParam);
    }
    return DefWindowProc(hWnd, uMsg, wParam, lParam);
}

implement Window {

    init(title: LPCWSTR, app: Application*) {
        this->m_app = app;
        this->m_nextId = 100;

        // [调试]
        std::cout << "[Window] Registering Class..." << std::endl;

        // --- 1. 注册窗口类 ---
        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc; // 指向全局转发函数
        wc.hInstance = app->getHInstance();
        wc.hCursor = LoadCursor(NULL, IDC_ARROW);
        wc.lpszClassName = L"ChronoWindowClass";
        wc.hbrBackground = reinterpret_cast<HBRUSH>(COLOR_WINDOW + 1);

        // 注册失败不一定是错误（可能已注册），但为了调试我们打印一下
        if (RegisterClassEx(&wc) == 0) {
             std::cout << "[Window] Warning: RegisterClassEx failed (or already registered)." << std::endl;
        }

        std::cout << "[Window] Creating Window..." << std::endl;

        // --- 2. 创建窗口 (补全部分) ---
        this->m_hWnd = CreateWindowExW(
            0,
            L"ChronoWindowClass", // 必须与上面的类名一致
            title,
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT, CW_USEDEFAULT, 800, 600,
            NULL,
            NULL,
            app->getHInstance(),
            this // [关键] 将 'this' 传入，以便 GlobalWindowProc 获取
        );

        if (this->m_hWnd == NULL) {
            std::cout << "[Window] Error: CreateWindowExW failed!" << std::endl;
            // 可以在这里抛出异常或调用 exit(1)
        } else {
            std::cout << "[Window] Window Created Successfully. HWND: " << this->m_hWnd << std::endl;
        }
    }

    deinit { }

    func show() {
        var nCmdShow: int = this->m_app->getNCmdShow();
        ShowWindow(this->m_hWnd, nCmdShow);
        UpdateWindow(this->m_hWnd);
    }

    func addChild(widget: unique<Widget>) {
        var id: int = this->m_nextId;
        this->m_nextId = this->m_nextId + 1;

        var ptr: Widget* = widget.get();
        ptr->create(this->m_hWnd, id);

        this->m_lookup[id] = ptr;
        this->m_children.push_back(@move(widget));
    }

    func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT
    {
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
            // [新增] 处理关闭消息，否则点击 X 号虽然窗口关了，但进程还在后台挂起
            case WM_DESTROY {
                PostQuitMessage(0);
                return 0;
            }
        }

        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }
}