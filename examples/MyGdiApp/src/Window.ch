// file: framework/Window.cpp.ch
import "Window.h"
// Application.h 已在 Window.h 中导入

//typemap C_LRESULT_CALLBACK = "LRESULT CALLBACK";
//typemap C_HBRUSH = "HBRUSH";

// --- 1. 实现 C-Style 桥接函数 (来自 Window.ch) ---
// (此部分与您在 Window.ch 中提供的代码相同，它是正确的)
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
        this.m_app = app; // [ [ [ 改进 3: 保存 App 指针 ] ] ]

        var wc: WNDCLASSEX = {};
        var className = L"ChronoFrameworkWindow";

        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = app.getHInstance(); // (OK)
        wc.lpszClassName = className;
        wc.hCursor = LoadCursor(NULL, IDC_ARROW);
        wc.hbrBackground = reinterpret_cast[C_HBRUSH](COLOR_WINDOW + 1);

        RegisterClassEx(&wc);

        this.m_hWnd = CreateWindowEx(
            WS_EX_CLIENTEDGE,
            className,
            title,
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT, CW_USEDEFAULT, 640, 480,
            NULL, NULL,
            app.getHInstance(),
            this // (OK: 传递 'this' 指针)
        );
    }

    // [ [ [ 修复 2: 实现析构函数 ] ] ]
    deinit {
        // (空) 确保 C++ v-table (虚函数表) 正确
    }

    // [ [ [ 改进 3: 移除 @cpp hack ] ] ]
    func show() {
        // 不再使用 extern hack，而是从 m_app 成员获取
        var nCmdShow: int = this.m_app.getNCmdShow();
        ShowWindow(this.m_hWnd, nCmdShow);

        UpdateWindow(this.m_hWnd);
    }

    // 默认实现 (来自 gdiplus_demo.ch)
    func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT
    {
        return DefWindowProc(this.m_hWnd, uMsg, wParam, lParam);
    }
}