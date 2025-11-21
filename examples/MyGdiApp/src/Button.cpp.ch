// file: project/Button.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Button"
import "Window"
import "Geometry"
import <algorithm>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

implement Button {
    init(text: std::string) {
        // 1. 初始化自身样式
        this.m_bgColor = CGColor(220, 220, 220, 255); // 浅灰
        this.m_borderColor = CGColor(0, 0, 0, 255);   // 黑边
        this.m_borderWidth = 1.0;

        this.m_isPressed = false;
        this.m_isHovered = false;

        // 2. [核心] 创建内部 Label
        // 使用 @make 创建独占智能指针
        this.m_internalLabel = @make<Label>(text);

        // 配置 Label：背景透明，不拦截鼠标
        this.m_internalLabel->setBackgroundColor(CGColor::clear());
        this.m_internalLabel->setTextColor(CGColor::black());
        // 对齐方式默认居中
        this.m_internalLabel->setAlignment(1, 1);
    }

    deinit {
        // unique<Label> 会自动释放
    }

    // --- 代理方法 (Proxy Methods) ---
    func setText(text: std::string) {
        this.m_internalLabel->setText(text);
    }

    func setFont(name: std::string, size: f32) {
        this.m_internalLabel->setFont(name, size);
    }

    func setTextColor(c: CGColor) {
        this.m_internalLabel->setTextColor(c);
    }

    func setStyle(bg: CGColor, border: CGColor, width: f32) {
        this.m_bgColor = bg;
        this.m_borderColor = border;
        this.m_borderWidth = width;
        if (this.m_hWnd != NULL) { InvalidateRect(this.m_hWnd, NULL, true); }
    }

    func setOnClick(cb: ClickCallback) {
        this.m_onClick = cb;
    }

    func create(parent: HWND, id: int) {
        this.m_id = id;

        @cpp extern HINSTANCE g_hInstance; @end
        @cpp extern LRESULT CALLBACK GlobalWindowProc(HWND, UINT, WPARAM, LPARAM); @end

        // 注册 Button 类
        var wc: WNDCLASSEX = {};
        wc.cbSize = sizeof(WNDCLASSEX);
        wc.style = CS_HREDRAW | CS_VREDRAW;
        wc.lpfnWndProc = GlobalWindowProc;
        wc.hInstance = g_hInstance;
        wc.hCursor = LoadCursor(NULL, IDC_HAND); // 手型光标
        wc.lpszClassName = L"ChronoCustomButton";
        wc.hbrBackground = NULL;

        RegisterClassEx(&wc);

        // 创建 Button 窗口
        var f = this.m_frame;
        this.m_hWnd = CreateWindowExW(
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

        // [核心] 创建内部 Label 子窗口
        if (this.m_internalLabel) {
            // Label 的 Frame 是相对于 Button 的 (Local Coordinates)
            // 所以 Origin 是 (0, 0)，大小填满 Button
            var contentRect = CGRect(0.0, 0.0, f.getWidth(), f.getHeight());
            this.m_internalLabel->setFrame(contentRect);

            // 创建 Label，父窗口是 Button (this.m_hWnd)
            // ID 设为 0 或其他内部 ID 均可
            this.m_internalLabel->create(this.m_hWnd, 0);
        }
    }

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        switch (uMsg) {
            // [核心] 当 Button 大小改变时，同步调整 Label 大小
            case WM_SIZE {
                var w = LOWORD(lParam);
                var h = HIWORD(lParam);
                if (this.m_internalLabel) {
                    var r = CGRect(0.0, 0.0, static_cast<f32>(w), static_cast<f32>(h));
                    this.m_internalLabel->setFrame(r);
                }
                return 0;
            }

            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this.m_hWnd, &ps);
                var g = Graphics(hdc);

                var rect: RECT;
                GetClientRect(this.m_hWnd, &rect);
                var w = static_cast<int>(rect.right);
                var h = static_cast<int>(rect.bottom);
                var w_minus_1 = w - 1;
                var h_minus_1 = h - 1;

                // 1. 计算动态背景色
                var c = this.m_bgColor;
                if (this.m_isPressed) {
                    // 按下变暗
                    var darkR = static_cast<u8>(std::max(0, static_cast<int>(c.r) - 40));
                    var darkG = static_cast<u8>(std::max(0, static_cast<int>(c.g) - 40));
                    var darkB = static_cast<u8>(std::max(0, static_cast<int>(c.b) - 40));
                    c = CGColor(darkR, darkG, darkB, c.a);
                } else if (this.m_isHovered) {
                    // 悬停变亮
                    var lightR = static_cast<u8>(std::min(255, static_cast<int>(c.r) + 20));
                    var lightG = static_cast<u8>(std::min(255, static_cast<int>(c.g) + 20));
                    var lightB = static_cast<u8>(std::min(255, static_cast<int>(c.b) + 20));
                    c = CGColor(lightR, lightG, lightB, c.a);
                }

                // 2. 绘制背景
                var gdiBg = Color(c.a, c.r, c.g, c.b);
                var brush = SolidBrush(gdiBg);
                g.FillRectangle(&brush, 0, 0, w, h);

                // 3. 绘制边框
                if (this.m_borderWidth > 0.0) {
                    var bc = this.m_borderColor;
                    var gdiBorder = Color(bc.a, bc.r, bc.g, bc.b);
                    var pen = Pen(gdiBorder, this.m_borderWidth);

                    // 像素对齐绘制
                    g.SetSmoothingMode(SmoothingModeNone);
                    g.DrawRectangle(&pen, 0, 0, w_minus_1, h_minus_1);
                }

                // [注意] 不需要绘制文字，Label 会自己画

                EndPaint(this.m_hWnd, &ps);
                return 0;
            }

            case WM_MOUSEMOVE {
                if (!this.m_isHovered) {
                    this.m_isHovered = true;
                    var tme: TRACKMOUSEEVENT;
                    tme.cbSize = sizeof(TRACKMOUSEEVENT);
                    tme.dwFlags = TME_LEAVE;
                    tme.hwndTrack = this.m_hWnd;
                    TrackMouseEvent(&tme);
                    InvalidateRect(this.m_hWnd, NULL, true);
                }
                return 0;
            }

            case WM_MOUSELEAVE {
                this.m_isHovered = false;
                this.m_isPressed = false;
                InvalidateRect(this.m_hWnd, NULL, true);
                return 0;
            }

            case WM_LBUTTONDOWN {
                this.m_isPressed = true;
                SetCapture(this.m_hWnd);
                // 移动文字以产生按压效果 (可选：这里可以通过调整 Label 的 frame 实现)
                // this.m_internalLabel->setFrame(...)
                InvalidateRect(this.m_hWnd, NULL, true);
                return 0;
            }

            case WM_LBUTTONUP {
                if (this.m_isPressed) {
                    this.m_isPressed = false;
                    ReleaseCapture();
                    InvalidateRect(this.m_hWnd, NULL, true);
                    if (this.m_onClick) {
                        this.m_onClick();
                    }
                }
                return 0;
            }
        }
        return DefWindowProc(this.m_hWnd, uMsg, wParam, lParam);
    }
}