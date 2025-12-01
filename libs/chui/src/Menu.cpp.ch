import "chui/Menu"
import "runtime/CH.h"
import <windows.h>

@dynamic
implement Menu {
    init(isPopup: bool) {
        //@cpp
        if (isPopup) {
            this->m_hMenu = CreatePopupMenu();
        } else {
            this->m_hMenu = CreateMenu();
        }
        //@end
    }

    deinit {
        // 注意：如果菜单被 SetMenu 绑定到窗口，窗口销毁时会自动销毁菜单
        // 这里可以不做处理，或者为了安全手动 DestroyMenu
        if (this->m_hMenu) {
            DestroyMenu(this->m_hMenu);
        }
    }

    func addItem(text: std::string, id: i32) {
    // C++ 原代码:
    @cpp
    AppendMenuA(this->m_hMenu, MF_STRING, (UINT_PTR)id, text.c_str());
    @end

    }

    func addSeparator() {

        AppendMenuA(this->m_hMenu, MF_SEPARATOR, 0, NULL);

    }

    func addSubMenu(text: std::string, subMenu: Menu*) {
        @cpp
        // MF_POPUP: 把 subMenu 的句柄作为 ID 传入
        AppendMenuA(this->m_hMenu, MF_POPUP, (UINT_PTR)subMenu->m_hMenu, text.c_str());
        @end
        // 为了防止 subMenu 被提前释放（MRC机制），这里应该 retain 一下
        // 但为了演示简单，暂且假设调用者负责生命周期
        subMenu->retain();
    }
}