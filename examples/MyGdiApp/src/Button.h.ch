// file: project/Button.h.ch
#pragma once
import "Widget"
import "Label"
import "Geometry" // 引入 CG 类型
import <string>
import <functional>

using ClickCallback = std::function<void()>;

class Button : Widget {
    // 组合：内部包含一个 Label
    var m_internalLabel: unique<Label>;
    var m_onClick: ClickCallback;

    // [修改] 使用 CGColor
    var m_bgColor: CGColor;
    var m_borderColor: CGColor;

    var m_borderWidth: f32;
    var m_isPressed: bool;
    var m_isHovered: bool;

    public init(text: std::string);
    public deinit;

    // 代理方法
    public func setText(text: std::string);
    public func setFont(name: std::string, size: f32);
    public func setTextColor(c: CGColor);

    // [修改] 使用 CGColor
    public func setStyle(bg: CGColor, border: CGColor, width: f32);
    public func setOnClick(cb: ClickCallback);

    public func create(parent: HWND, id: int);
    public func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;
}