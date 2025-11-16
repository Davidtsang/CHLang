// file: project/MyWindow.h.ch
#pragma once
import "Window.h"
import "Application.h"
import <gdiplus.h>
@cpp using namespace Gdiplus; @end

class MyWindow : Window {
    public init(app: Application*);

    // 重写(Override)基类的虚拟函数
    public func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT;
}