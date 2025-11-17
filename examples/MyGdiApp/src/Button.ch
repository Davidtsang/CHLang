import "Button"

// 需要 HMENU 类型转换用于传递 ID
typemap C_HMENU = "HMENU";

implement Button {
    init(text: std.string) {
        this.m_text = text;
    }

    func setOnClick(cb: ClickCallback) {
        this.m_onClick = cb;
    }

    func create(parent: HWND, id: int) {
        this.m_id = id;

        @cpp
            std::wstring wtext(this->m_text.begin(), this->m_text.end());
            LPCWSTR ptrText = wtext.c_str();
            // 获取 hInstance (假设 g_hInstance 在 WinMain.h 中全局可用，或者通过 Application 获取)
            // 这里我们直接使用全局变量，需要在 C++ 层面可见
            extern HINSTANCE g_hInstance;
        @end

        // 修正参数数量为 12 个
        this.m_hWnd = CreateWindowEx(
            0,
            L"BUTTON",
            ptrText,
            WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 10, 100, 30,
            parent,
            reinterpret_cast[C_HMENU](static_cast[int64](id)),
            g_hInstance, // [修复] 添加 hInstance
            NULL
        );
    }

    func onCommand(notificationCode: int) -> bool {
        if (notificationCode == BN_CLICKED) {
            if (this.m_onClick) {
                this.m_onClick(); // 调用 std::function
            }
            return true;
        }
        return false;
    }
}