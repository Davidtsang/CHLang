// file: project/Button.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Button"
import "Window"
import "Geometry"
import <algorithm>
import <objidl.h>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

implement Button {
    init(text: std::string) {
        // [Strict Mode] this 是指针，必须用 ->
        this->m_bgColor = CGColor(220, 220, 220, 255);
        this->m_borderColor = CGColor(0, 0, 0, 255);
        this->m_borderWidth = 1.0;

        this->m_isPressed = false;
        this->m_isHovered = false;

        // m_internalLabel 是成员，用 this-> 访问
        this->m_internalLabel = @make<Label>(text);

        // m_internalLabel 是 unique_ptr，调用其方法用 ->
        this->m_internalLabel->setBackgroundColor(CGColor::clear());
        this->m_internalLabel->setTextColor(CGColor::black());
        this->m_internalLabel->setAlignment(1, 1);
    }

    deinit { }

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

    func create(parent: HWND, id: int) {
        this->m_id = id;

        @cpp extern HINSTANCE g_hInstance; @end
        @cpp extern LRESULT CALLBACK GlobalWindowProc(HWND, UINT, WPARAM, LPARAM); @end

        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = g_hInstance;
        wc.hCursor = LoadCursor(NULL, IDC_HAND);
        wc.lpszClassName = L"ChronoCustomButton";
        wc.hbrBackground = NULL;

        RegisterClassEx(&wc);

        // this->m_frame 是成员，使用 -> 访问
        // f 是本地结构体变量 (CGRect)，使用 . 访问
        var f = this->m_frame;

        this->m_hWnd = CreateWindowExW(
            0, L"ChronoCustomButton", NULL,
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

        if (this->m_internalLabel) {
            var contentRect = CGRect(0.0, 0.0, f.getWidth(), f.getHeight());
            this->m_internalLabel->setFrame(contentRect);
            this->m_internalLabel->create(this->m_hWnd, 0);
        }
    }

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        switch (uMsg) {
            case WM_SIZE {
                var w = LOWORD(lParam);
                var h = HIWORD(lParam);
                if (this->m_internalLabel) {
                    var r = CGRect(0.0, 0.0, static_cast<f32>(w), static_cast<f32>(h));
                    this->m_internalLabel->setFrame(r);
                }
                return 0;
            }

            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this->m_hWnd, &ps);
                var g = Graphics(hdc);

                var rect: RECT;
                GetClientRect(this->m_hWnd, &rect);
                var w = static_cast<int>(rect.right);
                var h = static_cast<int>(rect.bottom);

                // [Strict Mode Fix] this->m_bgColor
                var c = this->m_bgColor;

                // [Strict Mode Fix] this->m_isPressed
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

                var gdiBg = Color(c.a, c.r, c.g, c.b);
                var brush = SolidBrush(gdiBg);
                g.FillRectangle(&brush, 0, 0, w, h);

                // [Strict Mode Fix] this->m_borderWidth
                if (this->m_borderWidth > 0.0) {
                    var bc = this->m_borderColor;
                    var gdiBorder = Color(bc.a, bc.r, bc.g, bc.b);
                    var pen = Pen(gdiBorder, this->m_borderWidth);

                    g.SetSmoothingMode(SmoothingModeNone);

                    // 边框内缩算法
                    var inset = this->m_borderWidth / 2.0;
                    var drawW = static_cast<f32>(w) - this->m_borderWidth;
                    var drawH = static_cast<f32>(h) - this->m_borderWidth;

                    g.DrawRectangle(&pen, inset, inset, drawW, drawH);
                }

                EndPaint(this->m_hWnd, &ps);
                return 0;
            }

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