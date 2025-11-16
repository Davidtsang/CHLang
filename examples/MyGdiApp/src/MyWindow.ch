// file: project/MyWindow.cpp.ch
import "MyWindow.h"

implement MyWindow {

    // 调用基类构造函数
    init(app: Application*) : Window(L"My Chrono GDI+ Window", app) {
        // (构造函数为空)
    }

    // [关键]
    // gdiplus_demo.ch 中 WindowProc 的 'switch' 逻辑
    func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT
    {
        switch (uMsg) {

            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this.m_hWnd, &ps);

                var graphics = Graphics(hdc);
                var pen = Pen(Color(255, 255, 0, 0), static_cast[f32](3.0));
                var brush = SolidBrush(Color(128, 0, 0, 255));

                graphics.FillRectangle(&brush, 10, 10, 300, 200);
                graphics.DrawEllipse(&pen, 10, 10, 300, 200);

                EndPaint(this.m_hWnd, &ps);
                return 0;
            }

            case WM_DESTROY {
                PostQuitMessage(0);
                return 0;
            }
        }

        // [ [ [ 修复: 调用基类 ] ] ]
        // 假设 'Window.handleMessage' 是调用基类方法的 Chrono 语法
        return Window.handleMessage(uMsg, wParam, lParam);
    }
}