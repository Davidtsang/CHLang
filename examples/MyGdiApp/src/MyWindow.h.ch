// file: project/MyWindow.h.ch
#pragma once
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

// [Critical Fix]
// Ensure windows.h is included BEFORE gdiplus.h
// AND ensure we don't have macro conflicts.
import <windows.h>
import <gdiplus.h>

import "Window"
import "Application"

@cpp using namespace Gdiplus; @end

class MyWindow : Window {
    public init(app: Application*);

    // 重写(Override)基类的虚拟函数
    public func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT;
}