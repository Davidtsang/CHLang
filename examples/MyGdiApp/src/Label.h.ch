// file: project/Label.h.ch
#pragma once

import "Widget"
import "Geometry" // 引入 CGRect, CGColor
import <string>
import <windows.h>

// 注意：这里我们尽量不暴露 GDI+ 类型在头文件中，使用 CGColor 替代
// 这样头文件更干净，编译更快

class Label : Widget {
    // 数据
    var m_text: std::string;

    // 样式 (使用新的 CG 类型)
    var m_textColor: CGColor;
    var m_bgColor: CGColor;

    // 字体信息
    var m_fontName: std::wstring;
    var m_fontSize: f32;

    // 对齐 (0=Near, 1=Center, 2=Far)
    var m_alignH: int;
    var m_alignV: int;

    public init(text: std::string);

    // --- API ---
    public func setText(text: std::string);

    // [修改] 使用 CGColor
    public func setTextColor(color: CGColor);
    public func setBackgroundColor(color: CGColor);

    public func setFont(name: std::string, size: f32);

    // 设置对齐
    public func setAlignment(h: int, v: int);

    // --- 虚函数重写 (Explicit Override) ---
    public override func create(parent: HWND, id: int);
    public override func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;
}