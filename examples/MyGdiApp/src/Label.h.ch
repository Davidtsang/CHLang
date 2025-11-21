#pragma once
import "Widget"
import "Geometry"
import <string>
import <gdiplus.h> // GDI+ 仅用于实现，不用于接口类型

class Label : Widget {
    var m_text: std::string;

    // [修改] 使用 CGColor
    var m_textColor: CGColor;
    var m_bgColor: CGColor;

    var m_fontName: std::wstring;
    var m_fontSize: f32;

    var m_alignH: int;
    var m_alignV: int;

    public init(text: std::string);

    public func setText(text: std::string);
    // [修改] 接口使用 CGColor
    public func setTextColor(color: CGColor);
    public func setBackgroundColor(color: CGColor);
    public func setFont(name: std::string, size: f32);

    public func create(parent: HWND, id: int);
    public func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;
}