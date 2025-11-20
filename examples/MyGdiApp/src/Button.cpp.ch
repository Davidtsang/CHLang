// file: project/Button.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Button"
import "Window"
// [新增] 用于 std::min, std::max
import <algorithm>

implement Button {
    init(text: std::string) {
        this->m_text = text;

        this->m_bgColor = Color(255, 220, 220, 220);
        this->m_hoverColor = Color(255, 240, 240, 240);
        this->m_pressedColor = Color(255, 180, 180, 180);
        this->m_borderColor = Color(255, 0, 0, 0);
        this->m_textColor = Color(255, 0, 0, 0);
        this->m_borderWidth = 1.0;

        this->m_fontName = L"Segoe UI";
        this->m_fontSize = 12.0;

        this->m_isHovered = false;
        this->m_isPressed = false;
    }

    func setStyle(bg: Color, text: Color, border: Color, borderWidth: f32, fontSize: f32) {
        this->m_bgColor = bg;
        this->m_textColor = text;
        this->m_borderColor = border;
        this->m_borderWidth = borderWidth;
        this->m_fontSize = fontSize;

        // [修复] 使用 std::min / std::max
        // 注意：GDI+ Color 的 R,G,B 是 BYTE (u8)，计算结果可能是 int，需要强转回 u8 避免警告
        // 或者直接让 Color 构造函数处理 int
        this->m_hoverColor = Color(255,
            static_cast<u8>(std::min(static_cast<int>(bg.GetR()) + 20, 255)),
            static_cast<u8>(std::min(static_cast<int>(bg.GetG()) + 20, 255)),
            static_cast<u8>(std::min(static_cast<int>(bg.GetB()) + 20, 255)));

        this->m_pressedColor = Color(255,
            static_cast<u8>(std::max(static_cast<int>(bg.GetR()) - 40, 0)),
            static_cast<u8>(std::max(static_cast<int>(bg.GetG()) - 40, 0)),
            static_cast<u8>(std::max(static_cast<int>(bg.GetB()) - 40, 0)));
    }

    func setOnClick(cb: ClickCallback) {
        this->m_onClick = cb;
    }

    // [新增] 实现 setFont
    func setFont(name: std::string, size: f32) {
        // 将 std::string (ANSI/UTF8) 转换为 std::wstring (Wide) 以供 GDI+ 使用
        @cpp
        std::wstring wname(name.begin(), name.end());
        this->m_fontName = wname;
        @end

        this->m_fontSize = size;

        // 如果窗口已创建，触发重绘以应用新字体
        if (this->m_hWnd != NULL) {
            InvalidateRect(this->m_hWnd, NULL, true);
        }
    }

    func create(parent: HWND, id: int) {
        this->m_id = id;

        @cpp
        extern HINSTANCE g_hInstance;
        @end

        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        // [重要提醒] 确保你之前删除了 CS_DBLCLKS，否则点击迟钝
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = g_hInstance;
        wc.hCursor = LoadCursor(NULL, IDC_HAND);
        wc.lpszClassName = L"ChronoCustomButton";
        wc.hbrBackground = NULL;

        RegisterClassEx(&wc);

        this->m_hWnd = CreateWindowExW(
            0, L"ChronoCustomButton", NULL,
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
            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this->m_hWnd, &ps);
                var g = Graphics(hdc);

                var rect: RECT;
                GetClientRect(this->m_hWnd, &rect);
                var w = static_cast<int>(rect.right);
                var h = static_cast<int>(rect.bottom);

                // [优化 1] 提前准备好整数宽高减 1，用于画边框
                var w_minus_1 = w - 1;
                var h_minus_1 = h - 1;

                var f_w = static_cast<f32>(w);
                var f_h = static_cast<f32>(h);

                // --- 1. 画背景 (无需抗锯齿) ---
                // 默认模式就是非抗锯齿，填充矩形本来就是锐利的
                g.SetSmoothingMode(SmoothingModeNone);

                var currentBgColor = this->m_bgColor;
                if (this->m_isPressed) {
                    currentBgColor = this->m_pressedColor;
                } else if (this->m_isHovered) {
                    currentBgColor = this->m_hoverColor;
                }

                var bgBrush = SolidBrush(currentBgColor);
                // 填充要填满整个区域，所以用原始 w, h
                g.FillRectangle(&bgBrush, 0, 0, w, h);

                // --- 2. 画边框 (关键修改：像素对齐) ---
                if (this->m_borderWidth > 0.0) {
                    var borderPen = Pen(this->m_borderColor, this->m_borderWidth);

                    // [关键] 关闭抗锯齿，确保线条是实心的 1px
                    g.SetSmoothingMode(SmoothingModeNone);

                    // [关键] GDI+ 绘制 1px 边框的最佳实践：
                    // 只要画笔宽是 1，且没开抗锯齿，画在 (0, 0, w-1, h-1)
                    // 就能得到完美的、贴合内边缘的 1px 边框。
                    // 不要用浮点数 offset 0.5，那只适合开启抗锯齿的情况。
                    g.DrawRectangle(&borderPen, 0, 0, w_minus_1, h_minus_1);
                }

                // --- 3. 画文字 (需要抗锯齿) ---
                // [关键] 重新开启抗锯齿，否则文字会有锯齿，很难看
                g.SetSmoothingMode(SmoothingModeAntiAlias);
                g.SetTextRenderingHint(TextRenderingHintClearTypeGridFit);

                var textOffsetX: f32 = 0.0;
                var textOffsetY: f32 = 0.0;
                if (this->m_isPressed) {
                    textOffsetX = 1.0;
                    textOffsetY = 1.0;
                }

                var fontFamily = FontFamily(this->m_fontName.c_str());
                var font = Font(&fontFamily, this->m_fontSize, FontStyleRegular, UnitPoint);
                var textBrush = SolidBrush(this->m_textColor);
                var format = StringFormat();
                format.SetAlignment(StringAlignmentCenter);
                format.SetLineAlignment(StringAlignmentCenter);

                @cpp
                std::wstring wtext(this->m_text.begin(), this->m_text.end());
                @end

                var layoutRect = RectF(textOffsetX, textOffsetY, f_w, f_h);
                g.DrawString(wtext.c_str(), -1, &font, layoutRect, &format, &textBrush);

                EndPaint(this->m_hWnd, &ps);
                return 0;
            }

            // ... (其他 case 保持不变) ...
            case WM_MOUSEMOVE {
                if (!this->m_isHovered) {
                    this->m_isHovered = true;
                    var tme: TRACKMOUSEEVENT;
                    tme.cbSize = sizeof(TRACKMOUSEEVENT);
                    tme.dwFlags = TME_LEAVE;
                    tme.hwndTrack = this->m_hWnd;
                    TrackMouseEvent(&tme);
                    InvalidateRect(this->m_hWnd, NULL, true);
                }
                return 0;
            }

            case WM_MOUSELEAVE {
                this->m_isHovered = false;
                this->m_isPressed = false;
                InvalidateRect(this->m_hWnd, NULL, true);
                return 0;
            }

            case WM_LBUTTONDOWN {
                this->m_isPressed = true;
                SetCapture(this->m_hWnd);
                InvalidateRect(this->m_hWnd, NULL, true);
                return 0;
            }

            case WM_LBUTTONUP {
                if (this->m_isPressed) {
                    this->m_isPressed = false;
                    ReleaseCapture();
                    InvalidateRect(this->m_hWnd, NULL, true);
                    if (this->m_onClick) {
                        this->m_onClick();
                    }
                }
                return 0;
            }
        }
        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }
}