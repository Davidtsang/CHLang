// file: framework/Window.cpp.ch
import "Window"

func GlobalWindowProc(
    hWnd: HWND, uMsg: UINT, wParam: WPARAM, lParam: LPARAM
) -> C_LRESULT_CALLBACK
{
    var pWindow: Window* = NULL;
if (uMsg == WM_NCCREATE) {
        // [纯 Chrono 实现]

        // 1. 将 lParam (LPARAM/long) 强转为 CREATESTRUCT 指针
        var pCreate: CREATESTRUCT* = reinterpret_cast[CREATESTRUCT*](lParam);

        // 2. 获取创建时传入的 'this' 指针 (在 lpCreateParams 中)
        //    注意：这里使用 '.'，翻译器会自动翻译成 C++ 的 '->'
        pWindow = reinterpret_cast[Window*](pCreate.lpCreateParams);

        // 3. 将指针存入窗口的 UserData 中
        //    SetWindowLongPtr 需要 LONG_PTR 类型，所以进行强转
        SetWindowLongPtr(hWnd, GWLP_USERDATA, reinterpret_cast[LONG_PTR](pWindow));

        // 4. 保存 hWnd
        pWindow.m_hWnd = hWnd;

    } else {
        // [纯 Chrono 实现]

        // 5. 从 UserData 取回指针
        //    GetWindowLongPtr 返回 LONG_PTR，强转回 Window*
        var ptrVal: LONG_PTR = GetWindowLongPtr(hWnd, GWLP_USERDATA);
        pWindow = reinterpret_cast[Window*](ptrVal);
    }

    if (pWindow != NULL) {
        return pWindow.handleMessage(uMsg, wParam, lParam);
    }
    return DefWindowProc(hWnd, uMsg, wParam, lParam);
}

// --- 2. 实现 Window 类的成员 ---
implement Window {

    init(title: LPCWSTR, app: Application*) {
        this.m_app = app;
        this.m_nextId = 100; // ID 从 100 开始

        // ... (WNDCLASSEX 和 CreateWindowEx 代码保持不变) ...
        // ...
    }

    deinit { }

    func show() {
        var nCmdShow: int = this.m_app.getNCmdShow();
        ShowWindow(this.m_hWnd, nCmdShow);
        UpdateWindow(this.m_hWnd);
    }

    // [新增] 添加子控件实现
    func addChild(widget: unique[Widget]) {
        var id: int = this.m_nextId;
        this.m_nextId = this.m_nextId + 1;

        // 1. 获取原始指针用于创建和查找
        var ptr: Widget* = widget.get();

        // 2. 创建实际的 Win32 控件
        ptr.create(this.m_hWnd, id);

        // 3. 存入查找表
        this.m_lookup[id] = ptr;

        // 4. 转移所有权到 vector (使用 std::move)
        this.m_children.push_back(@move(widget));
    }

    // [修改] 增加消息路由逻辑
    func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT
    {
        switch (uMsg) {
            // [关键] 处理命令消息 (按钮点击等)
            case WM_COMMAND {
                // Win32: LOWORD(wParam) 是控件 ID
                var id: int = LOWORD(wParam);
                // Win32: HIWORD(wParam) 是通知码 (如 BN_CLICKED)
                var code: int = HIWORD(wParam);

                // 查找控件
                if (this.m_lookup.count(id) > 0) {
                    var widget: Widget* = this.m_lookup[id];
                    // 分发给控件
                    widget.onCommand(code);
                }
                // 按钮点击通常不需要 Default 处理，但返回 0 是个好习惯
                return 0;
            }
        }

        return DefWindowProc(this.m_hWnd, uMsg, wParam, lParam);
    }
}