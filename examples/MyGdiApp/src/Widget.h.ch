// file: framework/Widget.h.ch
#pragma once
import <windows.h>
import "Geometry" // 导入 CG 类型

class Widget {
    public var m_hWnd: HWND;
    public var m_id: int;

    // [修改] 使用 CGRect
    public var m_frame: CGRect;

    public init();
    public deinit;

    // [修改] 接收 CGRect
    public func setFrame(frame: CGRect);
    public func getFrame() -> CGRect;

    public func create(parent: HWND, id: int);
    public func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;
    public func onCommand(notificationCode: int) -> bool;
}