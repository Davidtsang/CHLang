// file: project/Button.h.ch
#pragma once

import "Widget"
import "Label"    // [核心] 引入 Label 用于组合
import "Geometry" // 引入 CG 类型
import <string>
import <functional>
import <windows.h>

// 定义回调类型
using ClickCallback = std::function<void()>;

class Button : Widget {
    // [核心变化] 组合模式：Button 拥有一个 Label
    // 使用 unique 指针管理生命周期，无需手动 delete
    var m_internalLabel: unique<Label>;

    var m_onClick: ClickCallback;

    // 样式属性 (使用 CGColor)
    var m_bgColor: CGColor;
    var m_borderColor: CGColor;

    var m_borderWidth: f32;
    var m_isPressed: bool;
    var m_isHovered: bool;

    public init(text: std::string);
    public deinit;

    // --- 代理方法 (Proxy Methods) ---
    // 这些方法将调用转发给内部的 Label
    public func setText(text: std::string);
    public func setFont(name: std::string, size: f32);
    public func setTextColor(c: CGColor);

    // --- Button 自身样式 ---
    public func setStyle(bg: CGColor, border: CGColor, width: f32);
    public func setOnClick(cb: ClickCallback);

    // --- 虚函数重写 (Explicit Override) ---
    public override func create(parent: HWND, id: int);
    public override func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;
}