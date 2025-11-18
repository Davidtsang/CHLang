// file: project/MyWindow.cpp.ch
import "MyWindow"

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
                // [重构] this->m_hWnd
                var hdc: HDC = BeginPaint(this->m_hWnd, &ps);

                var graphics = Graphics(hdc);
                // [重构] static_cast<f32>
                var pen = Pen(Color(255, 255, 0, 0), static_cast<f32>(3.0));
                var brush = SolidBrush(Color(128, 0, 0, 255));

                // [重构] graphics 是栈对象，使用 .
                graphics.FillRectangle(&brush, 10, 10, 300, 200);
                graphics.DrawEllipse(&pen, 10, 10, 300, 200);

                EndPaint(this->m_hWnd, &ps);
                return 0;
            }

            case WM_DESTROY {
                PostQuitMessage(0);
                return 0;
            }
        }

        // [重构] 显式调用基类方法使用 ::
        return Window::handleMessage(uMsg, wParam, lParam);
    }
}