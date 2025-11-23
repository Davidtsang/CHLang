// file: project/Button.h.ch
#pragma once
import "Widget"
import "Label"
import "Geometry"
import "Events" // 确保导入 Events
import <string>
import <functional>
import <windows.h>

using ClickCallback = std::function<void()>;

@dynamic
class Button : Widget {
    var m_internalLabel: unique<Label>;
    var m_onClick: ClickCallback;
    var m_bgColor: CGColor;
    var m_borderColor: CGColor;
    var m_borderWidth: f32;
    var m_isPressed: bool;
    var m_isHovered: bool;

    public init(text: std::string);
    public deinit;

    public func setText(text: std::string);
    public func setFont(name: std::string, size: f32);
    public func setTextColor(c: CGColor);
    public func setStyle(bg: CGColor, border: CGColor, width: f32);
    public func setOnClick(cb: ClickCallback);

    public override func create(parent: HWND, id: int);

    // [重要] 使用新的事件接口进行 Override
    public override func onPaint(g: Graphics*);
    public override func onMouseDown(e: MouseEvent);
    public override func onMouseUp(e: MouseEvent);
    public override func onMouseEnter();
    public override func onMouseLeave();
    public override func onResize(w: int, h: int);
}