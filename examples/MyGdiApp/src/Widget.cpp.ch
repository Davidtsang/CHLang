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