// file: project/Label.h.ch
#pragma once

import "Widget"
import <string>
import <objidl.h>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

class Label : Widget {
    // 数据
    var m_text: std::string;

    // 样式
    var m_textColor: Color;
    var m_bgColor: Color;

    var m_fontName: std::wstring;
    var m_fontSize: f32;

    // 对齐 (0=Near, 1=Center, 2=Far)
    var m_alignH: int; // 水平
    var m_alignV: int; // 垂直

    public init(text: std::string);

    // --- API ---
    public func setText(text: std::string);
    public func setTextColor(color: Color);
    public func setBackgroundColor(color: Color);
    public func setFont(name: std::string, size: f32);

    // 设置对齐: h(0,1,2), v(0,1,2)
    public func setAlignment(h: int, v: int);

    // 虚函数实现
    public func create(parent: HWND, id: int);
    public func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;
}