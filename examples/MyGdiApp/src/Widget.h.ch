// file: framework/Widget.h.ch
#pragma once

#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX


import <windows.h>
import <objidl.h>
import <gdiplus.h>
import "Geometry"
import "Events"

@cpp using namespace Gdiplus; @end

class Widget {
    public var m_hWnd: HWND;
    public var m_id: int;
    public var m_frame: CGRect;
    public var m_isMouseOver: bool;

    public init();
    public deinit;

    public func setFrame(frame: CGRect);
    public func getFrame() -> CGRect;

    public virtual func create(parent: HWND, id: int);
    public virtual func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;

    // --- 事件接口 ---
    public virtual func onPaint(g: Graphics*);
    public virtual func onMouseDown(e: MouseEvent);
    public virtual func onMouseUp(e: MouseEvent);
    public virtual func onMouseMove(e: MouseEvent);
    public virtual func onMouseEnter();
    public virtual func onMouseLeave();
    public virtual func onResize(w: int, h: int);

    public virtual func hitTest(x: int, y: int) -> int;

    // [关键修复] 加回 onCommand 声明
    public virtual func onCommand(notificationCode: int) -> bool;

    // --- [新增] 受保护的辅助函数 ---
    // 子类调用它来创建真实的 Win32 窗口
    // className: 窗口类名 (e.g. L"CHButton")
    // cursor: 光标资源 (e.g. IDC_HAND)
    // style: 窗口样式 (e.g. WS_CHILD | WS_VISIBLE)
    public func createStandardWindow(parent: HWND, className: LPCWSTR, cursor: LPCWSTR, style: DWORD);

}