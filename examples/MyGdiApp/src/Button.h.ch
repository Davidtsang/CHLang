// file: project/Button.h.ch
#pragma once

import "Widget"
import <string>
import <functional>
import <objidl.h>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

using ClickCallback = std::function<void()>;

class Button : Widget {
    var m_text: std::string;
    var m_onClick: ClickCallback;

    var m_bgColor: Color;
    var m_hoverColor: Color;
    var m_pressedColor: Color;
    var m_textColor: Color;

    var m_borderColor: Color;
    var m_borderWidth: f32;

    var m_fontName: std::wstring;
    var m_fontSize: f32;

    var m_isHovered: bool;
    var m_isPressed: bool;

    public init(text: std::string);

    public func setStyle(bg: Color, text: Color, border: Color, borderWidth: f32, fontSize: f32);

    // [新增] 单独设置字体名称和大小
    public func setFont(name: std::string, size: f32);

    public func setOnClick(cb: ClickCallback);
    public func create(parent: HWND, id: int);
    public func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;
}