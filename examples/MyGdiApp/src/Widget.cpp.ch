// file: framework/Widget.cpp.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX

import "Widget"
import <iostream>
import <algorithm>
import <objidl.h>
import <gdiplus.h>

@cpp using namespace Gdiplus; @end

implement Widget {
    init() {
        this->m_hWnd = NULL;
        this->m_id = 0;
        this->m_frame = CGRect(0.0, 0.0, 100.0, 30.0);
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
    func create(parent: HWND, id: int) { }

    // --- [核心] 封装 Win32 创建逻辑 ---
    func createStandardWindow(parent: HWND, className: LPCWSTR, cursor: LPCWSTR, style: DWORD) {

        @cpp extern HINSTANCE g_hInstance; @end
        @cpp extern LRESULT CALLBACK GlobalWindowProc(HWND, UINT, WPARAM, LPARAM); @end

        // 1. 注册窗口类 (如果尚未注册)
        // 使用 GetClassInfoEx 检查，避免重复注册失败
        var wcCheck: WNDCLASSEX;
        if (!GetClassInfoEx(g_hInstance, className, &wcCheck)) {
            var wc: WNDCLASSEX = {};
            wc.cbSize = sizeof(WNDCLASSEX);
            wc.style = 0; // 默认样式
            wc.lpfnWndProc = GlobalWindowProc;
            wc.hInstance = g_hInstance;
            wc.hCursor = LoadCursor(NULL, cursor); // 使用传入的光标
            wc.lpszClassName = className;          // 使用传入的类名
            wc.hbrBackground = NULL;               // 自绘背景

            RegisterClassEx(&wc);
        }

        // 2. 创建窗口
        var f = this->m_frame;

        this->m_hWnd = CreateWindowExW(
            0,
            className,
            NULL,
            style, // 使用传入的样式
            static_cast<int>(f.getMinX()),
            static_cast<int>(f.getMinY()),
            static_cast<int>(f.getWidth()),
            static_cast<int>(f.getHeight()),
            parent,
            reinterpret_cast<HMENU>(static_cast<int64_t>(this->m_id)),
            g_hInstance,
            this // 传入 this 指针，供 GlobalWindowProc 绑定
        );
    }

    // --- 默认实现 ---
    func onPaint(g: Graphics*) { }
    func onMouseDown(e: MouseEvent) { }
    func onMouseUp(e: MouseEvent) { }
    func onMouseMove(e: MouseEvent) { }
    func onMouseEnter() { }
    func onMouseLeave() { }
    func onResize(w: int, h: int) { }
    func hitTest(x: int, y: int) -> int { return -1; }

    // [关键修复] 加回 onCommand 默认实现
    func onCommand(notificationCode: int) -> bool {
        return false;
    }

    // --- 消息分发 ---
    func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT {
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
                if (res == 0) { return (-1); } // HTTRANSPARENT
                if (res == 1) { return 1; }    // HTCLIENT
            }
        }
        return DefWindowProc(this->m_hWnd, uMsg, wParam, lParam);
    }
}