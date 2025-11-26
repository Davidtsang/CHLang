// file: project/MyWindow.h.ch
#pragma once
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import <objidl.h>
import <windows.h>
import <gdiplus.h>

import "Window"
import "Application"
import "Geometry" // [新增]

@cpp using namespace Gdiplus; @end

@dynamic
class MyWindow : Window {
    var m_bgColor: Color;

    public init(app: Application*, w: int, h: int);

    // [修复] 参数改为 CGColor
    public func setBackgroundColor(color: CGColor);

    public func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT;
}