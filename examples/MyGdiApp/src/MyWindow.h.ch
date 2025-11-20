// file: project/MyWindow.h.ch
#pragma once
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import <objidl.h>
import <windows.h>
import <gdiplus.h>

import "Window"
import "Application"

@cpp using namespace Gdiplus; @end

class MyWindow : Window {
    // [新增] 存储背景颜色 (GDI+ Color 对象)
    var m_bgColor: Color;

    // [修改] 构造函数增加宽高
    public init(app: Application*, w: int, h: int);

    // [新增] 设置背景色 API
    public func setBackgroundColor(r: u8, g: u8, b: u8);

    public func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT;
}