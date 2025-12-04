#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "chui/HBox"
import "chui/Geometry"
import <iostream>
import <algorithm>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

@dynamic
implement HBox {
    init() {
        this->m_spacing = 10.0;
        this->m_padding = 5.0;
        this->m_bgColor = CGColor(200, 200, 200, 255);

        this->m_bt = 0.0; this->m_bb = 0.0;
        this->m_bl = 0.0; this->m_br = 0.0;

        var black = CGColor::black();
        this->m_ct = black; this->m_cb = black;
        this->m_cl = black; this->m_cr = black;
    }

    deinit {
        @cpp
        for (auto* child : this->m_children) {
            if (child) delete child;
        }
        this->m_children.clear();
        @end
    }

    func create(parent: HWND, id: int) {
        this->m_id = id;
        this->createStandardWindow(parent, L"CHHBox", IDC_ARROW, WS_CHILD | WS_VISIBLE | WS_CLIPCHILDREN);
    }

    func addChild(w: Widget*) {
        if (!w) { return; }
        this->m_children.push_back(w);

        // [修复] 防止由 LayoutLoader 传入已创建的 Widget 时发生“双重创建”
        // 只有当 w->m_hWnd 为空时，HBox 才负责创建它
        if (this->m_hWnd != NULL && w->m_hWnd == NULL) {
            var childId = 2000 + static_cast<int>(this->m_children.size());
            w->create(this->m_hWnd, childId);
        }

        this->performLayout();
    }

    func setSpacing(s: f32) { this->m_spacing = s; this->performLayout(); }
    func setPadding(p: f32) { this->m_padding = p; this->performLayout(); }

    func setBackgroundColor(c: CGColor) {
        this->m_bgColor = c;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    // --- 细粒度 Setter ---
    func setBorderTopWidth(w: f32)    { this->m_bt = w; this->performLayout(); if(this->m_hWnd!=NULL) {InvalidateRect(this->m_hWnd, NULL, true);} }
    func setBorderBottomWidth(w: f32) { this->m_bb = w; this->performLayout(); if(this->m_hWnd!=NULL){ InvalidateRect(this->m_hWnd, NULL, true);} }
    func setBorderLeftWidth(w: f32)   { this->m_bl = w; this->performLayout(); if(this->m_hWnd!=NULL){ InvalidateRect(this->m_hWnd, NULL, true);} }
    func setBorderRightWidth(w: f32)  { this->m_br = w; this->performLayout(); if(this->m_hWnd!=NULL){ InvalidateRect(this->m_hWnd, NULL, true);} }

    func setBorderTopColor(c: CGColor)    { this->m_ct = c; if(this->m_hWnd!=NULL) {InvalidateRect(this->m_hWnd, NULL, true);} }
    func setBorderBottomColor(c: CGColor) { this->m_cb = c; if(this->m_hWnd!=NULL){ InvalidateRect(this->m_hWnd, NULL, true);} }
    func setBorderLeftColor(c: CGColor)   { this->m_cl = c; if(this->m_hWnd!=NULL) {InvalidateRect(this->m_hWnd, NULL, true);} }
    func setBorderRightColor(c: CGColor)  { this->m_cr = c; if(this->m_hWnd!=NULL){ InvalidateRect(this->m_hWnd, NULL, true);} }

    func onResize(w: int, h: int) {
        this->performLayout();
    }

    func performLayout() {
        if (this->m_children.empty()) { return; }

        var currentX = this->m_padding + this->m_bl;
        var containerH = this->m_frame.getHeight();
        var availableH = containerH - this->m_bt - this->m_bb;
        var centerY = this->m_bt + (availableH / 2.0);

        for (var child in this->m_children) {
            var f = child->getFrame();
            var y = centerY - (f.getHeight() / 2.0);
            var newFrame = CGRect(currentX, y, f.getWidth(), f.getHeight());
            child->setFrame(newFrame);
            currentX = currentX + f.getWidth() + this->m_spacing;
        }
    }

    // --- 绘制 ---
    func onPaint(g: Graphics*) {
        // [修复] 移除 PixelOffsetModeHalf，保证 1px 对齐到物理像素网格
        g->SetSmoothingMode(SmoothingModeNone);
        g->SetPixelOffsetMode(PixelOffsetModeNone);

        var rect: RECT;
        GetClientRect(this->m_hWnd, &rect);
        var w = static_cast<f32>(rect.right);
        var h = static_cast<f32>(rect.bottom);

        // 1. 绘制背景
        var c = this->m_bgColor;
        var brush = SolidBrush(Color(c.a, c.r, c.g, c.b));
        g->FillRectangle(&brush, 0.0f, 0.0f, w, h);

        // 2. 绘制边框
        // Top
        if (this->m_bt > 0.0) {
            var col = this->m_ct;
            var b = SolidBrush(Color(col.a, col.r, col.g, col.b));
            g->FillRectangle(&b, 0.0f, 0.0f, w, this->m_bt);
        }

        // Bottom
        if (this->m_bb > 0.0) {
            var col = this->m_cb;
            var b = SolidBrush(Color(col.a, col.r, col.g, col.b));
            g->FillRectangle(&b, 0.0f, h - this->m_bb, w, this->m_bb);
        }

        // Left
        if (this->m_bl > 0.0) {
            var col = this->m_cl;
            var b = SolidBrush(Color(col.a, col.r, col.g, col.b));
            g->FillRectangle(&b, 0.0f, this->m_bt, this->m_bl, h - this->m_bt - this->m_bb);
        }

        // Right
        if (this->m_br > 0.0) {
            var col = this->m_cr;
            var b = SolidBrush(Color(col.a, col.r, col.g, col.b));
            g->FillRectangle(&b, w - this->m_br, this->m_bt, this->m_br, h - this->m_bt - this->m_bb);
        }
    }
}