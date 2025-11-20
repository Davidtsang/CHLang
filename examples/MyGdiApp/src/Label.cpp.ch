// file: project/Label.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Label"
import "Window" // for GlobalWindowProc
import <algorithm>

implement Label {

    init(text: std::string) {
        this->m_text = text;

        // 默认样式：透明背景，黑色文字
        this->m_bgColor = Color(0, 0, 0, 0); // Alpha=0 表示透明
        this->m_textColor = Color(255, 0, 0, 0);

        this->m_fontName = L"Segoe UI";
        this->m_fontSize = 12.0;

        // 默认：左对齐，垂直居中
        this->m_alignH = 0; // Near
        this->m_alignV = 1; // Center
    }

    func setText(text: std::string) {
        this->m_text = text;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setTextColor(color: Color) {
        this->m_textColor = color;
        if (this->m_hWnd != NULL) { InvalidateRect(this->m_hWnd, NULL, true); }
    }

    func setBackgroundColor(color: Color) {
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

func create(parent: HWND, id: int) {
        this->m_id = id;

        @cpp
        extern HINSTANCE g_hInstance;
        // extern "C++" LRESULT ... (之前已删除，不需要)
        @end

        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = g_hInstance;
        wc.hCursor = LoadCursor(NULL, IDC_ARROW);
        wc.lpszClassName = L"ChronoLabel";
        wc.hbrBackground = NULL;

        RegisterClassEx(&wc);

        this->m_hWnd = CreateWindowExW(
            0, L"ChronoLabel", NULL,
            WS_CHILD | WS_VISIBLE,
            // [修改] 使用存储的几何信息
            this->m_x, this->m_y, this->m_w, this->m_h,
            parent,
            reinterpret_cast<HMENU>(static_cast<int64_t>(id)),
            g_hInstance,
            this
        );
    }

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        switch (uMsg) {
            case WM_ERASEBKGND {
                // 如果背景是完全透明(Alpha=0)，我们返回0让父窗口画背景？
                // 或者返回1自己处理？
                // 简单起见，我们返回1，在 PAINT 里处理。
                // 注意：Win32 简单架构下，实现真透明需要父窗口配合，
                // 这里我们简化：如果 Alpha > 0 才画背景。
                return 1;
            }

            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this->m_hWnd, &ps);
                var g = Graphics(hdc);

                // 高质量文字
                g.SetTextRenderingHint(TextRenderingHintClearTypeGridFit);

                var rect: RECT;
                GetClientRect(this->m_hWnd, &rect);
                var f_w = static_cast<f32>(rect.right);
                var f_h = static_cast<f32>(rect.bottom);

                // 1. 画背景 (如果不是全透明)
                if (this->m_bgColor.GetAlpha() > 0) {
                    var bgBrush = SolidBrush(this->m_bgColor);
                    g.FillRectangle(&bgBrush, 0, 0, rect.right, rect.bottom);
                }

                // 2. 准备文字绘制
                var fontFamily = FontFamily(this->m_fontName.c_str());
                var font = Font(&fontFamily, this->m_fontSize, FontStyleRegular, UnitPoint);
                var textBrush = SolidBrush(this->m_textColor);

                var format = StringFormat();

                // 映射对齐方式 int -> StringAlignment Enum
                // 0=Near, 1=Center, 2=Far
                var alignH: StringAlignment = static_cast<StringAlignment>(this->m_alignH);
                var alignV: StringAlignment = static_cast<StringAlignment>(this->m_alignV);

                format.SetAlignment(alignH);      // 水平
                format.SetLineAlignment(alignV);  // 垂直

                @cpp
                std::wstring wtext(this->m_text.begin(), this->m_text.end());
                @end

                // 整个控件区域作为文字排版区域
                var layoutRect = RectF(0.0, 0.0, f_w, f_h);

                g.DrawString(wtext.c_str(), -1, &font, layoutRect, &format, &textBrush);

                EndPaint(this->m_hWnd, &ps);
                return 0;
            }

            // 标签通常不需要处理鼠标点击，但如果需要可以透传消息
            // 这里默认不做处理，作为一个静态控件
        }
        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }
}