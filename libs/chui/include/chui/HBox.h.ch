#pragma once
import "Widget"
import <vector>

@dynamic
class HBox : Widget {
    var m_children: std::vector<Widget*>;

    // 布局属性
    var m_spacing: f32;
    var m_padding: f32;
    var m_bgColor: CGColor;

    // 边框数据
    var m_bt: f32; var m_bb: f32; var m_bl: f32; var m_br: f32;
    var m_ct: CGColor; var m_cb: CGColor; var m_cl: CGColor; var m_cr: CGColor;

    public init();
    public deinit;

    public func addChild(w: Widget*);
    public func setSpacing(s: f32);
    public func setPadding(p: f32);
    public override func setBackgroundColor(c: CGColor);

    // [新增] 细粒度 Setter (解决 JSON 顺序依赖问题)
    public func setBorderTopWidth(w: f32);
    public func setBorderBottomWidth(w: f32);
    public func setBorderLeftWidth(w: f32);
    public func setBorderRightWidth(w: f32);

    public func setBorderTopColor(c: CGColor);
    public func setBorderBottomColor(c: CGColor);
    public func setBorderLeftColor(c: CGColor);
    public func setBorderRightColor(c: CGColor);

    public override func create(parent: HWND, id: int);
    public override func onResize(w: int, h: int);
    public override func onPaint(g: Graphics*);

    func performLayout();
}