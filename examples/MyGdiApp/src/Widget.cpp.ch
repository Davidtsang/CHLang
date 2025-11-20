// file: framework/Widget.cpp.ch
import "Widget"

implement Widget {
    init() {
        this->m_hWnd = NULL;
        this->m_id = 0;

        // [新增] 默认值
        this->m_x = 10;
        this->m_y = 10;
        this->m_w = 100;
        this->m_h = 30;
    }

    deinit {
        if (this->m_hWnd != NULL) {
            DestroyWindow(this->m_hWnd);
        }
    }

    // [新增] 实现
    func setGeometry(x: int, y: int, w: int, h: int) {
        this->m_x = x;
        this->m_y = y;
        this->m_w = w;
        this->m_h = h;

        // 如果窗口已经创建了，立刻应用
        if (this->m_hWnd != NULL) {
            MoveWindow(this->m_hWnd, x, y, w, h, true);
        }
    }

    func onCommand(notificationCode: int) -> bool {
        return false;
    }

    func create(parent: HWND, id: int) { }

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }
}