// file: framework/Application.cpp.ch
import "Application"
import "WinMain" // 导入 g_hInstance 和 g_nCmdShow

implement Application {

    init() {
        // 从 WinMain 保存的全局变量中获取实例
        this.m_hInstance = g_hInstance;
        this.m_nCmdShow = g_nCmdShow; // [ [ [ 改进 3 ] ] ]
    }

    // [ [ [ 修复 2: 实现析构函数 ] ] ]
    deinit {
        // (空) 确保 C++ v-table (虚函数表) 正确
    }

    // app.exec() 封装了 gdiplus_demo.ch 中的消息循环
    func exec() -> int {
        var msg: MSG = {};
        while (GetMessage(&msg, NULL, 0, 0)) {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        return static_cast[int](msg.wParam);
    }

    func getHInstance() -> HINSTANCE {
        return this.m_hInstance;
    }

    // [ [ [ 改进 3: 实现 Getter ] ] ]
    func getNCmdShow() -> int {
        return this.m_nCmdShow;
    }
}