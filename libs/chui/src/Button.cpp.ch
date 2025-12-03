// file: libs/chui/src/Button.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "chui/Button"
import "chui/Window"
import "chui/Geometry"
import "chui/Events"
import "chui/ImageView" // 引入实现
import <algorithm>
import <objidl.h>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

@dynamic
implement Button {
    init(text: std::string) {
        // 1. 基础样式
        this->m_bgColor = CGColor(220, 220, 220, 255);
        this->m_borderColor = CGColor(0, 0, 0, 255);
        this->m_borderWidth = 1.0;
        this->m_isPressed = false;
        this->m_isHovered = false;

        // 2. 布局默认值
        this->m_layout = ButtonLayout::TextOnly;
        this->m_spacing = 8.0f;

        // 3. 创建子控件
        this->m_internalLabel = @make<Label>(text);
        this->m_internalLabel->setBackgroundColor(CGColor::clear());
        this->m_internalLabel->setTextColor(CGColor::black());
        this->m_internalLabel->setAlignment(1, 1); // Center

        this->m_icon = @make<ImageView>();
        this->m_icon->setScaleMode(ImageScaleMode::AspectFit);
        this->m_icon->setBackgroundColor(CGColor::clear()); // 透明背景
    }

    deinit { }

    // --- 属性代理 ---

    func setText(text: std::string) {
        this->m_internalLabel->setText(text);
    }

    func setFont(name: std::string, size: f32) {
        this->m_internalLabel->setFont(name, size);
    }

    func setTextColor(c: CGColor) {
        this->m_internalLabel->setTextColor(c);
    }

    // [新增] 图标设置
    func setIconPath(path: std::string) {
        this->m_icon->setImagePath(path);
        // 如果当前是 TextOnly，自动切换到 IconLeft 方便用户看到
        if (this->m_layout == ButtonLayout::TextOnly) {
            this->setLayout(ButtonLayout::IconLeft);
        }
    }

    func setIconData(base64: std::string) {
        this->m_icon->setImageBase64(base64);
        if (this->m_layout == ButtonLayout::TextOnly) {
            this->setLayout(ButtonLayout::IconLeft);
        }
    }

    func setLayout(mode: ButtonLayout) {
        this->m_layout = mode;
        // 强制重新布局
        var frame = this->getFrame();
        this->onResize(frame.size.width as i32, frame.size.height as i32);
    }

    func setSpacing(s: f32) {
        this->m_spacing = s;
        var frame = this->getFrame();
        this->onResize(frame.size.width as i32, frame.size.height as i32);
    }

    // [修复] 之前缺失的背景色设置
    func setBackgroundColor(c: CGColor) {
        this->m_bgColor = c;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
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
        this->createStandardWindow(parent, L"CHCustomButton", IDC_HAND, WS_CHILD | WS_VISIBLE);

        // 创建 Label 子窗口
        if (this->m_internalLabel) {
            this->m_internalLabel->create(this->m_hWnd, 0);
        }

        // [新增] 创建 Icon 子窗口
        if (this->m_icon) {
            this->m_icon->create(this->m_hWnd, 1);
        }

        // 触发一次初始布局
        var f = this->getFrame();
        this->onResize(f.size.width as i32, f.size.height as i32);
    }

    // --- 核心布局引擎 (Strategy) ---

    func onResize(w: int, h: int) {
        if (!this->m_internalLabel || !this->m_icon) { return; }

        var fw = static_cast<f32>(w);
        var fh = static_cast<f32>(h);
        var spacing = this->m_spacing;

        // 简单的图标尺寸策略：高度的 60% 或固定值
        // 实际项目中可以添加 setIconSize API
        var iconSize = fh * 0.6f;
        if (iconSize > 32.0f){ iconSize = 32.0f;} // 限制最大
        if (iconSize < 16.0f){ iconSize = 16.0f;} // 限制最小

        if (this->m_layout == ButtonLayout::TextOnly) {
            // 1. 全文字模式
            this->m_internalLabel->setFrame(CGRect(0.0f, 0.0f, fw, fh));
            this->m_icon->setFrame(CGRect(0.0f, 0.0f, 0.f, 0.0f)); // 隐藏图标

        } else if (this->m_layout == ButtonLayout::IconOnly) {
            // 2. 全图标模式
            this->m_icon->setFrame(CGRect(0.0f, 0.0f, fw, fh));
            this->m_internalLabel->setFrame(CGRect(0.0f, 0.0f, 0.0f, 0.0f)); // 隐藏文字

        } else if (this->m_layout == ButtonLayout::IconLeft) {
            // 3. 图标在左
            var iconX = 10.0f; // 左边距
            var iconY = (fh - iconSize) / 2.0f;
            this->m_icon->setFrame(CGRect(iconX, iconY, iconSize, iconSize));

            var labelX = iconX + iconSize + spacing;
            var labelW = fw - labelX;
            this->m_internalLabel->setFrame(CGRect(labelX, 0.0f, labelW, fh));
            // Label 内部默认居中，可以设为左对齐优化观感
            this->m_internalLabel->setAlignment(0, 1); // Near, Center

        } else if (this->m_layout == ButtonLayout::IconRight) {
            // 4. 图标在右
            var iconX = fw - iconSize - 10.0f;
            var iconY = (fh - iconSize) / 2.0f;
            this->m_icon->setFrame(CGRect(iconX, iconY, iconSize, iconSize));

            var labelW = iconX - spacing;
            this->m_internalLabel->setFrame(CGRect(0.0f, 0.0f, labelW, fh));
            this->m_internalLabel->setAlignment(2, 1); // Far, Center

        } else {
            // Top/Bottom 暂略，默认回退到 TextOnly
            this->m_internalLabel->setFrame(CGRect(0.0f, 0.0f, fw, fh));
            this->m_icon->setFrame(CGRect(0.0f, 0.0f, 0.0f, 0.0f));
        }
    }

    // --- 绘制 (背景与边框) ---
    func onPaint(g: Graphics*) {
        // ... (这部分代码完全保持你原有的逻辑) ...
        // 获取 rect
        var rect: RECT;
        GetClientRect(this->m_hWnd, &rect);
        var w = rect.right;
        var h = rect.bottom;

        // 1. 状态颜色计算
        var c = this->m_bgColor;
        if (this->m_isPressed) {
            // ... Darken ...
            var darkR = static_cast<u8>(std::max(0, static_cast<int>(c.r) - 40));
            var darkG = static_cast<u8>(std::max(0, static_cast<int>(c.g) - 40));
            var darkB = static_cast<u8>(std::max(0, static_cast<int>(c.b) - 40));
            c = CGColor(darkR, darkG, darkB, c.a);
        } else if (this->m_isHovered) {
            // ... Lighten ...
            var lightR = static_cast<u8>(std::min(255, static_cast<int>(c.r) + 20));
            var lightG = static_cast<u8>(std::min(255, static_cast<int>(c.g) + 20));
            var lightB = static_cast<u8>(std::min(255, static_cast<int>(c.b) + 20));
            c = CGColor(lightR, lightG, lightB, c.a);
        }

        // 2. 绘制背景
        var gdiBg = Color(c.a, c.r, c.g, c.b);
        var brush = SolidBrush(gdiBg);
        g->FillRectangle(&brush, 0, 0, w, h);

        // 3. 绘制边框
        if (this->m_borderWidth > 0.0f) {
            var bc = this->m_borderColor;
            var gdiBorder = Color(bc.a, bc.r, bc.g, bc.b);
            var pen = Pen(gdiBorder, this->m_borderWidth);
            g->SetSmoothingMode(SmoothingModeNone);

            if (this->m_borderWidth == 1.0f) {
                g->DrawRectangle(&pen, 0, 0, w - 1, h - 1);
            } else {
                pen.SetAlignment(PenAlignmentInset);
                g->DrawRectangle(&pen, 0, 0, w, h);
            }
        }
        // 注意：Label 和 Icon 是子窗口，Windows 会负责让它们自己绘制自己，
        // 所以这里不需要 g->DrawImage 或 DrawString。
    }

    // --- 鼠标事件 (透传与状态管理) ---
    // Label 和 Icon 如果是子窗口，可能会拦截鼠标消息。
    // 需要在 Label/ImageView 的 hitTest 中返回 HTTRANSPARENT，
    // 或者在它们的 onMouseDown 中调用父类的 handler。
    // 为了简单，我们在 Label 和 ImageView 中让 hitTest 返回 HTTRANSPARENT (0)。

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
        if (e.button == 0) {
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