// file: libs/chui/include/chui/Button.h.ch
#pragma once

import "Widget"
import "Label"
import "ImageView" // [新增] 引入全能 ImageView
import "Geometry"
import "Events"
import <string>
import <functional>
import <windows.h>

// [新增] 按钮布局策略
enum ButtonLayout {
    TextOnly,   // 默认
    IconOnly,
    IconLeft,   // 图标在左
    IconRight,  // 图标在右
    IconTop,    // 图标在上
    IconBottom  // 图标在下
}

using ClickCallback = std::function<void()>;

@dynamic
class Button : Widget {
    // 内部组件 (组合模式)
    var m_internalLabel: unique<Label>;
    var m_icon: unique<ImageView>; // [新增] 图标组件

    // 样式与数据
    var m_layout: ButtonLayout;    // [新增]
    var m_spacing: f32;            // [新增] 间距

    var m_onClick: ClickCallback;
    var m_bgColor: CGColor;
    var m_borderColor: CGColor;
    var m_borderWidth: f32;
    var m_isPressed: bool;
    var m_isHovered: bool;

    public init(text: std::string);
    public deinit;

    // --- 文本 API ---
    public func setText(text: std::string);
    public func setFont(name: std::string, size: f32);
    public func setTextColor(c: CGColor);

    // --- 图标 API [新增] ---
    public func setIconPath(path: std::string);     // 文件模式
    public func setIconData(base64: std::string);   // 内存模式
    public func setLayout(mode: ButtonLayout);      // 设置布局
    public func setSpacing(s: f32);

    // --- 通用样式 ---
    public override func setBackgroundColor(c: CGColor); // 之前缺失的
    public func setStyle(bg: CGColor, border: CGColor, width: f32);
    public func setOnClick(cb: ClickCallback);

    // --- 生命周期 ---
    public override func create(parent: HWND, id: int);

    // --- 事件 ---
    public override func onPaint(g: Graphics*);
    public override func onMouseDown(e: MouseEvent);
    public override func onMouseUp(e: MouseEvent);
    public override func onMouseEnter();
    public override func onMouseLeave();
    public override func onResize(w: int, h: int);
}