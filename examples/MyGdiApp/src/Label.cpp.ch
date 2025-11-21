// file: project/Label.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Label"
import "Window"
import "Geometry"
import "Events"
import <algorithm>

// [关键] 必须先导入 objidl.h
import <objidl.h>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

implement Label {
    init(text: std::string) {
        this->m_text = text;

        // 默认样式
        this->m_bgColor = CGColor::clear(); // 透明背景
        this->m_textColor = CGColor::black();

        this->m_fontName = L"Segoe UI";
        this->m_fontSize = 12.0;

        this->m_alignH = 1; // Center
        this->m_alignV = 1; // Center
    }

    // --- API 实现 ---

    func setText(text: std::string) {
        this->m_text = text;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setTextColor(color: CGColor) {
        this->m_textColor = color;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setBackgroundColor(color: CGColor) {
        this->m_bgColor = color;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setFont(name: std::string, size: f32) {
        @cpp
        std::wstring wname(name.begin(), name.end());
        this->m_fontName = wname;
        @end
        this->m_fontSize = size;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setAlignment(h: int, v: int) {
        this->m_alignH = h;
        this->m_alignV = v;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    // --- 核心生命周期 (无 override 关键字) ---

    func create(parent: HWND, id: int) {
        this->m_id = id;

        @cpp extern HINSTANCE g_hInstance; @end
        @cpp extern LRESULT CALLBACK GlobalWindowProc(HWND, UINT, WPARAM, LPARAM); @end

        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = g_hInstance;
        wc.hCursor = LoadCursor(NULL, IDC_ARROW);
        wc.lpszClassName = L"ChronoLabel";
        wc.hbrBackground = NULL;

        RegisterClassEx(&wc);

        var f = this->m_frame;

        this->m_hWnd = CreateWindowExW(
            0, L"ChronoLabel", NULL,
            WS_CHILD | WS_VISIBLE,
            static_cast<int>(f.getMinX()),
            static_cast<int>(f.getMinY()),
            static_cast<int>(f.getWidth()),
            static_cast<int>(f.getHeight()),
            parent,
            reinterpret_cast<HMENU>(static_cast<int64_t>(id)),
            g_hInstance,
            this
        );
    }

    // --- 事件处理 (无 override 关键字) ---

    func hitTest(x: int, y: int) -> int {
        // 返回 0 表示透明 (HTTRANSPARENT)
        // 这允许鼠标点击穿透 Label 传递给底下的 Button
        return 0;
    }

    func onPaint(g: Graphics*) {
        // 1. 准备区域
        var rect: RECT;
        GetClientRect(this->m_hWnd, &rect);
        var f_w = static_cast<f32>(rect.right);
        var f_h = static_cast<f32>(rect.bottom);

        // 2. 画背景 (如果 Alpha > 0)
        // 必须使用 this-> 访问成员
        if (this->m_bgColor.a > 0) {
            var c = this->m_bgColor;
            var gdiColor = Color(c.a, c.r, c.g, c.b);
            var bgBrush = SolidBrush(gdiColor);
            // 必须使用 g-> 调用方法
            g->FillRectangle(&bgBrush, 0, 0, rect.right, rect.bottom);
        }

        // 3. 画文字
        var fontFamily = FontFamily(this->m_fontName.c_str());
        var font = Font(&fontFamily, this->m_fontSize, FontStyleRegular, UnitPoint);

        var tc = this->m_textColor;
        var textBrush = SolidBrush(Color(tc.a, tc.r, tc.g, tc.b));

        var format = StringFormat();
        var alignH: StringAlignment = static_cast<StringAlignment>(this->m_alignH);
        var alignV: StringAlignment = static_cast<StringAlignment>(this->m_alignV);
        format.SetAlignment(alignH);
        format.SetLineAlignment(alignV);

        @cpp
        std::wstring wtext(this->m_text.begin(), this->m_text.end());
        @end

        var layoutRect = RectF(0.0, 0.0, f_w, f_h);
        g->DrawString(wtext.c_str(), -1, &font, layoutRect, &format, &textBrush);
    }
}