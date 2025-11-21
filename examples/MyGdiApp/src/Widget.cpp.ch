// file: framework/Widget.cpp.ch
import "Widget"

implement Widget {
    init() {
        this->m_hWnd = NULL;
        this->m_id = 0;
        // [修复] 使用 ->
        this->m_frame = CGRect(10.0, 10.0, 100.0, 30.0);
    }

    deinit {
        if (this->m_hWnd != NULL) {
            DestroyWindow(this->m_hWnd);
        }
    }

    func setFrame(frame: CGRect) {
        this->m_frame = frame;
        if (this->m_hWnd != NULL) {
            // frame 是栈上的值类型，使用 . 访问
            MoveWindow(this->m_hWnd,
                static_cast<int>(frame.getMinX()),
                static_cast<int>(frame.getMinY()),
                static_cast<int>(frame.getWidth()),
                static_cast<int>(frame.getHeight()),
                true);
        }
    }

    func getFrame() -> CGRect {
        return this->m_frame;
    }

    func onCommand(notificationCode: int) -> bool {
        return false;
    }

    func create(parent: HWND, id: int) { }

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }
}