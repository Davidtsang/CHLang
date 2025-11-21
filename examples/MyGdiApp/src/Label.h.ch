// file: project/Label.h.ch
#pragma once

import "Widget"
import "Geometry" // 引入 CG 类型
import <string>
import <windows.h>

class Label : Widget {
    // 数据
    var m_text: std::string;

    // 样式 (使用 CG 类型)
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
    public func setTextColor(color: CGColor);
    public func setBackgroundColor(color: CGColor);
    public func setFont(name: std::string, size: f32);
    public func setAlignment(h: int, v: int);

    // --- 虚函数重写 (声明时使用 override) ---
    public override func create(parent: HWND, id: int);

    // [重构] 使用新的事件系统，不再直接处理 handleMessage
    public override func onPaint(g: Graphics*);

    // [重构] 命中测试 (用于点击穿透)
    public override func hitTest(x: int, y: int) -> int;
}