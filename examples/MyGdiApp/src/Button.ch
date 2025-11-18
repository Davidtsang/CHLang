import "Button"

// 需要 HMENU 类型转换用于传递 ID
typemap C_HMENU = "HMENU";

implement Button {
    init(text: std::string) {
        this->m_text = text;
    }

    func setOnClick(cb: ClickCallback) {
        this->m_onClick = cb;
    }

    func create(parent: HWND, id: int) {
        this->m_id = id;

        @cpp
            std::wstring wtext(this->m_text.begin(), this->m_text.end());
            LPCWSTR ptrText = wtext.c_str();
            extern HINSTANCE g_hInstance;
        @end

        // [修复] 强制使用 CreateWindowExW (Wide Char 版本)
        this->m_hWnd = CreateWindowExW(
            0,
            L"BUTTON",
            ptrText,
            WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 10, 100, 30,
            parent,
            reinterpret_cast<C_HMENU>(static_cast<int64_t>(id)),
            g_hInstance,
            NULL
        );
    }

    func onCommand(notificationCode: int) -> bool {
        if (notificationCode == BN_CLICKED) {
            // [重构] m_onClick 是对象（std::function），使用 . (重载了 operator bool)
            // 注意：C++ 中 std::function 既可以作为 bool 检查，也可以直接调用
            if (this->m_onClick) {
                this->m_onClick(); // 调用 std::function
            }
            return true;
        }
        return false;
    }
}