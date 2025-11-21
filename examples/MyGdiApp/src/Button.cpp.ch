// file: project/Button.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Button"
import "Window"
import "Geometry"
import "Events"
import <algorithm>

// [重要] 必须先导入 objidl.h，再导入 gdiplus.h
import <objidl.h>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

implement Button {
    init(text: std::string) {
        // 初始化自身样式
        this->m_bgColor = CGColor(220, 220, 220, 255);
        this->m_borderColor = CGColor(0, 0, 0, 255);
        this->m_borderWidth = 1.0;

        this->m_isPressed = false;
        this->m_isHovered = false;

        // 创建内部 Label (组合模式)
        this->m_internalLabel = @make<Label>(text);

        // 配置 Label
        this->m_internalLabel->setBackgroundColor(CGColor::clear());
        this->m_internalLabel->setTextColor(CGColor::black());
        this->m_internalLabel->setAlignment(1, 1); // 居中
    }

    deinit { }

    // --- 代理方法 ---
    func setText(text: std::string) {
        this->m_internalLabel->setText(text);
    }

    func setFont(name: std::string, size: f32) {
        this->m_internalLabel->setFont(name, size);
    }

    func setTextColor(c: CGColor) {
        this->m_internalLabel->setTextColor(c);
    }

    func setStyle(bg: CGColor, border: CGColor, width: f32) {
        this->m_bgColor = bg;
        this->m_borderColor = border;
        this->m_borderWidth = width;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setOnClick(cb: ClickCallback) {
        this->m_onClick = cb;
    }

    // --- 核心生命周期 ---

    func create(parent: HWND, id: int) {
        this->m_id = id;

        @cpp extern HINSTANCE g_hInstance; @end
        @cpp extern LRESULT CALLBACK GlobalWindowProc(HWND, UINT, WPARAM, LPARAM); @end

        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = 0;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = g_hInstance;
        wc.hCursor = LoadCursor(NULL, IDC_HAND);
        wc.lpszClassName = L"ChronoCustomButton";
        wc.hbrBackground = NULL;

        RegisterClassEx(&wc);

        var f = this->m_frame;

        // [关键修复] 移除 WS_CLIPCHILDREN
        // 允许 Button 在 Label 下方绘制背景和边框
        var style = WS_CHILD | WS_VISIBLE;

        this->m_hWnd = CreateWindowExW(
            0, L"ChronoCustomButton", NULL,
            style,
            static_cast<int>(f.getMinX()),
            static_cast<int>(f.getMinY()),
            static_cast<int>(f.getWidth()),
            static_cast<int>(f.getHeight()),
            parent,
            reinterpret_cast<HMENU>(static_cast<int64_t>(id)),
            g_hInstance,
            this
        );

        if (this->m_internalLabel) {
            var contentRect = CGRect(0.0, 0.0, f.getWidth(), f.getHeight());
            this->m_internalLabel->setFrame(contentRect);
            this->m_internalLabel->create(this->m_hWnd, 0);
        }
    }

    // --- 事件处理 (Qt 风格) ---

    func onResize(w: int, h: int) {
        // 同步调整 Label 大小
        if (this->m_internalLabel) {
            var r = CGRect(0.0, 0.0, static_cast<f32>(w), static_cast<f32>(h));
            this->m_internalLabel->setFrame(r);
        }
    }

    func onPaint(g: Graphics*) {
        // 获取当前客户区大小
        var rect: RECT;
        GetClientRect(this->m_hWnd, &rect);
        var w = rect.right;
        var h = rect.bottom;

        // 1. 计算动态颜色
        var c = this->m_bgColor;
        if (this->m_isPressed) {
            var darkR = static_cast<u8>(std::max(0, static_cast<int>(c.r) - 40));
            var darkG = static_cast<u8>(std::max(0, static_cast<int>(c.g) - 40));
            var darkB = static_cast<u8>(std::max(0, static_cast<int>(c.b) - 40));
            c = CGColor(darkR, darkG, darkB, c.a);
        } else if (this->m_isHovered) {
            var lightR = static_cast<u8>(std::min(255, static_cast<int>(c.r) + 20));
            var lightG = static_cast<u8>(std::min(255, static_cast<int>(c.g) + 20));
            var lightB = static_cast<u8>(std::min(255, static_cast<int>(c.b) + 20));
            c = CGColor(lightR, lightG, lightB, c.a);
        }

        // 2. 绘制背景
        var gdiBg = Color(c.a, c.r, c.g, c.b);
        var brush = SolidBrush(gdiBg);

        // 注意：使用指针访问 g->
        g->FillRectangle(&brush, 0, 0, w, h);

        // 3. 绘制边框
        if (this->m_borderWidth > 0.0) {
            var bc = this->m_borderColor;
            var gdiBorder = Color(bc.a, bc.r, bc.g, bc.b);
            var pen = Pen(gdiBorder, this->m_borderWidth);

            g->SetSmoothingMode(SmoothingModeNone);

            // [关键修复] 边框内缩算法
            var inset = this->m_borderWidth / 1.0;
            var drawW = static_cast<f32>(w) - this->m_borderWidth;
            var drawH = static_cast<f32>(h) - this->m_borderWidth;

            g->DrawRectangle(&pen, inset, inset, drawW, drawH);
        }
    }

    func onMouseEnter() {
        this->m_isHovered = true;
        InvalidateRect(this->m_hWnd, NULL, true);
    }

    func onMouseLeave() {
        this->m_isHovered = false;
        this->m_isPressed = false;
        InvalidateRect(this->m_hWnd, NULL, true);
    }

    func onMouseDown(e: MouseEvent) {
        if (e.button == 0) { // 左键
            this->m_isPressed = true;
            InvalidateRect(this->m_hWnd, NULL, true);
        }
    }

    func onMouseUp(e: MouseEvent) {
        if (this->m_isPressed) {
            this->m_isPressed = false;
            InvalidateRect(this->m_hWnd, NULL, true);
            if (this->m_onClick) {
                this->m_onClick();
            }
        }
    }
}