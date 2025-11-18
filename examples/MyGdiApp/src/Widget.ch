// file: src/Widget.ch
import "Widget"

implement Widget {
    init() {
        // [重构] 类内部 this 是指针，使用 ->
        this->m_hWnd = NULL;
        this->m_id = 0;
    }

    deinit {
        // [重构] 使用 ->
        if (this->m_hWnd != NULL) {
            DestroyWindow(this->m_hWnd);
        }
    }

    // 默认不处理命令
    func onCommand(notificationCode: int) -> bool {
        return false;
    }

    // create 是纯虚的，在 C++ 中通常不提供实现，但 Chrono 翻译器可能需要空体
    func create(parent: HWND, id: int) {
    }
}