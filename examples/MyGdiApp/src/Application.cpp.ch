// file: framework/Application.cpp.ch
import "Application"
import "WinMain" // 导入 g_hInstance 和 g_nCmdShow

implement Application {

    init() {
        // [重构] 类内部 this 是指针，使用 ->
        this->m_hInstance = g_hInstance;
        this->m_nCmdShow = g_nCmdShow;
    }

    deinit {
        // (空) 确保 C++ v-table (虚函数表) 正确
    }

    // app.exec() 封装了 gdiplus_demo.ch 中的消息循环
    func exec() -> int {
        var msg: MSG = {};
        // [重构] msg 是栈结构体，使用 .
        while (GetMessage(&msg, NULL, 0, 0)) {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        // [重构] static_cast 使用 <>
        return static_cast<int>(msg.wParam);
    }

    func getHInstance() -> HINSTANCE {
        return this->m_hInstance;
    }

    func getNCmdShow() -> int {
        return this->m_nCmdShow;
    }
}