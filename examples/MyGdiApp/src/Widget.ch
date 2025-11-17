import "Widget.h"

implement Widget {
    init() {
        this.m_hWnd = NULL;
        this.m_id = 0;
    }

    deinit {
        if (this.m_hWnd != NULL) {
            DestroyWindow(this.m_hWnd);
        }
    }

    // 默认不处理命令
    func onCommand(notificationCode: int) -> bool {
        return false;
    }

    // create 是纯虚的，这里可以留空或抛错，但在 Chrono 需提供空实现以通过编译
    func create(parent: HWND, id: int) {
    }
}