// file: project/Label.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Label"
import "Window" // for GlobalWindowProc if needed, or just use local class registration
import "Geometry"
import <algorithm>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

implement Label {

    init(text: std::string) {
        this.m_text = text;

        // 默认样式
        this.m_bgColor = CGColor::clear(); // 默认背景透明
        this.m_textColor = CGColor::black();

        this.m_fontName = L"Segoe UI";
        this.m_fontSize = 12.0;

        // 默认：左对齐(0)，垂直居中(1)
        // (GDI+ StringAlignment: Near=0, Center=1, Far=2)
        this.m_alignH = 1;
        this.m_alignV = 1;
    }

    func setText(text: std::string) {
        this.m_text = text;
        if (this.m_hWnd != NULL) { InvalidateRect(this.m_hWnd, NULL, true); }
    }

    func setTextColor(color: CGColor) {
        this.m_textColor = color;
        if (this.m_hWnd != NULL) { InvalidateRect(this.m_hWnd, NULL, true); }
    }

    func setBackgroundColor(color: CGColor) {
        this.m_bgColor = color;
        if (this.m_hWnd != NULL) { InvalidateRect(this.m_hWnd, NULL, true); }
    }

    func setFont(name: std::string, size: f32) {
        @cpp
        std::wstring wname(name.begin(), name.end());
        this.m_fontName = wname;
        @end
        this.m_fontSize = size;
        if (this.m_hWnd != NULL) { InvalidateRect(this.m_hWnd, NULL, true); }
    }

    func setAlignment(h: int, v: int) {
        this.m_alignH = h;
        this.m_alignV = v;
        if (this.m_hWnd != NULL) { InvalidateRect(this.m_hWnd, NULL, true); }
    }

    func create(parent: HWND, id: int) {
        this.m_id = id;

        @cpp extern HINSTANCE g_hInstance; @end

        // 注册 Label 窗口类
        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        @cpp extern LRESULT CALLBACK GlobalWindowProc(HWND, UINT, WPARAM, LPARAM); @end
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = g_hInstance;
        wc.hCursor = LoadCursor(NULL, IDC_ARROW);
        wc.lpszClassName = L"ChronoLabel";
        wc.hbrBackground = NULL; // 自定义绘制背景

        RegisterClassEx(&wc);

        // 使用 CGRect 属性创建窗口
        var f = this.m_frame;

        this.m_hWnd = CreateWindowExW(
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

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        switch (uMsg) {
            // [核心机制] 点击穿透
            // 当鼠标点击 Label 时，返回 HTTRANSPARENT 告诉 Windows：
            // "我不处理这个点击，请把消息发给我的父窗口 (Button)"
            case WM_NCHITTEST {
                return (-1); // HTTRANSPARENT
            }

            case WM_ERASEBKGND {
                // 减少闪烁，我们在 PAINT 中处理
                return 1;
            }

            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this.m_hWnd, &ps);
                var g = Graphics(hdc);

                // 开启高质量文字渲染
                g.SetTextRenderingHint(TextRenderingHintClearTypeGridFit);

                var rect: RECT;
                GetClientRect(this.m_hWnd, &rect);
                var f_w = static_cast<f32>(rect.right);
                var f_h = static_cast<f32>(rect.bottom);

                // 1. 画背景 (如果 Alpha > 0)
                if (this.m_bgColor.a > 0) {
                    var c = this.m_bgColor;
                    var gdiColor = Color(c.a, c.r, c.g, c.b);
                    var bgBrush = SolidBrush(gdiColor);
                    g.FillRectangle(&bgBrush, 0, 0, rect.right, rect.bottom);
                }

                // 2. 准备文字绘制
                var fontFamily = FontFamily(this.m_fontName.c_str());
                var font = Font(&fontFamily, this->m_fontSize, FontStyleRegular, UnitPoint);

                var tc = this.m_textColor;
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
                g.DrawString(wtext.c_str(), -1, &font, layoutRect, &format, &textBrush);

                EndPaint(this.m_hWnd, &ps);
                return 0;
            }
        }
        return DefWindowProc(this.m_hWnd, uMsg, wParam, lParam);
    }
}