#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "chui/Widget"
import <iostream>
import <algorithm>
import <objidl.h>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

// [关键] 必须标记 @dynamic，否则 setX/setY 不会进入反射表
@dynamic
implement Widget {
    init() {
        this->m_hWnd = NULL;
        this->m_id = 0;
        this->m_frame = CGRect(0.0, 0.0, 100.0, 30.0); // 默认值
        this->m_isMouseOver = false;
    }

    deinit {
        if (this->m_hWnd != NULL) { DestroyWindow(this->m_hWnd); }
    }

    func setFrame(frame: CGRect) {
        this->m_frame = frame;
        if (this->m_hWnd != NULL) {
            MoveWindow(this->m_hWnd,
                static_cast<int>(frame.getMinX()), static_cast<int>(frame.getMinY()),
                static_cast<int>(frame.getWidth()), static_cast<int>(frame.getHeight()), true);
        }
    }

    func getFrame() -> CGRect { return this->m_frame; }

    // [关键] 必须实现这些 Setter，以便 PropertyInjector 调用
    func setX(v: i32) {
        this->m_frame.origin.x = static_cast<f32>(v);
        // 如果窗口已创建，实时更新位置 (可选)
    }
    func setY(v: i32) { this->m_frame.origin.y = static_cast<f32>(v); }
    func setWidth(v: i32) { this->m_frame.size.width = static_cast<f32>(v); }
    func setHeight(v: i32) { this->m_frame.size.height = static_cast<f32>(v); }

    // [关键] 通用 setText 接口 (虽然 Widget 没有 text 成员，但这里提供虚函数入口)
    func setText(t: std::string) { }
    func setBackgroundColor(c: CGColor) { }

    func create(parent: HWND, id: int) { }

    func createStandardWindow(parent: HWND, className: LPCWSTR, cursor: LPCWSTR, style: DWORD) {
        @cpp extern HINSTANCE g_hInstance; @end
        @cpp extern LRESULT CALLBACK GlobalWindowProc(HWND, UINT, WPARAM, LPARAM); @end

        var wcCheck: WNDCLASSEX;
        if (!GetClassInfoEx(g_hInstance, className, &wcCheck)) {
            var wc: WNDCLASSEX = {};
            wc.cbSize = sizeof(WNDCLASSEX);
            wc.style = 0;
            wc.lpfnWndProc = GlobalWindowProc;
            wc.hInstance = g_hInstance;
            wc.hCursor = LoadCursor(NULL, cursor);
            wc.lpszClassName = className;
            wc.hbrBackground = NULL;
            RegisterClassEx(&wc);
        }

        var f = this->m_frame;

        // [修改] 创建时应用可见性样式
        var finalStyle = style;
        // 如果当前是隐藏状态，移除 WS_VISIBLE
        if (!this->m_isVisible) {
            @cpp finalStyle &= ~WS_VISIBLE; @end
        }

        this->m_hWnd = CreateWindowExW(
            0, className, NULL, style,
            static_cast<int>(f.getMinX()), static_cast<int>(f.getMinY()),
            static_cast<int>(f.getWidth()), static_cast<int>(f.getHeight()),
            parent, reinterpret_cast<HMENU>(static_cast<int64_t>(this->m_id)),
            g_hInstance, this
        );
    }
    // [新增]
    func setVisible(v: bool) {
        this->m_isVisible = v;
        if (this->m_hWnd != NULL) {
            var flag: i32 = 0;
            if (v) { flag = 5; } else { flag = 0; } // SW_SHOW=5, SW_HIDE=0
            ShowWindow(this->m_hWnd, flag);
        }
    }

    // 默认实现
    func onPaint(g: Graphics*) { }
    func onMouseDown(e: MouseEvent) { }
    func onMouseUp(e: MouseEvent) { }
    func onMouseMove(e: MouseEvent) { }
    func onMouseEnter() { }
    func onMouseLeave() { }
    func onResize(w: int, h: int) { }
    func hitTest(x: int, y: int) -> int { return -1; }
    func onCommand(n: int) -> bool { return false; }

    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
        // ... (这里保持原来的 handleMessage 逻辑，太长省略，不要改动它) ...
        // (请保留您之前已经写好的完整 handleMessage Switch 块)
        switch (uMsg) {
            case WM_PAINT {
                var ps: PAINTSTRUCT;
                var hdc: HDC = BeginPaint(this->m_hWnd, &ps);
                var g = Graphics(hdc);
                g.SetSmoothingMode(SmoothingModeAntiAlias);
                this->onPaint(&g);
                EndPaint(this->m_hWnd, &ps);
                return 0;
            }
            case WM_ERASEBKGND { return 1; }
            case WM_LBUTTONDOWN {
                var x = static_cast<int>(LOWORD(lParam));
                var y = static_cast<int>(HIWORD(lParam));
                var e = MouseEvent(x, y, 0);
                SetCapture(this->m_hWnd);
                this->onMouseDown(e);
                return 0;
            }
            case WM_LBUTTONUP {
                var x = static_cast<int>(LOWORD(lParam));
                var y = static_cast<int>(HIWORD(lParam));
                var e = MouseEvent(x, y, 0);
                ReleaseCapture();
                this->onMouseUp(e);
                return 0;
            }
            case WM_MOUSEMOVE {
                var x = static_cast<int>(LOWORD(lParam));
                var y = static_cast<int>(HIWORD(lParam));
                var e = MouseEvent(x, y, 0);
                if (!this->m_isMouseOver) {
                    this->m_isMouseOver = true;
                    var tme: TRACKMOUSEEVENT;
                    tme.cbSize = sizeof(TRACKMOUSEEVENT);
                    tme.dwFlags = TME_LEAVE;
                    tme.hwndTrack = this->m_hWnd;
                    TrackMouseEvent(&tme);
                    this->onMouseEnter();
                }
                this->onMouseMove(e);
                return 0;
            }
            case WM_MOUSELEAVE {
                this->m_isMouseOver = false;
                this->onMouseLeave();
                return 0;
            }
            case WM_SIZE {
                var w = static_cast<int>(LOWORD(lParam));
                var h = static_cast<int>(HIWORD(lParam));
                this->onResize(w, h);
                return 0;
            }
            case WM_NCHITTEST {
                var res = this->hitTest(0, 0);
                if (res == 0) { return (-1); }
                if (res == 1) { return 1; }
            }
        }
        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }
}