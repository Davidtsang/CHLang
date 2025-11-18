// file: project/MyWindow.h.ch
#pragma once
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

// [关键修复] 必须在 gdiplus.h 之前包含 objidl.h
import <objidl.h>
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