// file: framework/Widget.h.ch
#pragma once
import <windows.h>
import "Geometry"

class Widget {
    public var m_hWnd: HWND;
    public var m_id: int;
    public var m_frame: CGRect;

    public init();
    public deinit;

    public func setFrame(frame: CGRect);
    public func getFrame() -> CGRect;

    // [关键修改] 添加 virtual 关键字
    // 因为子类(Button/Label)使用了 override，所以基类必须是 virtual
    public virtual func create(parent: HWND, id: int);
    public virtual func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;

    public virtual func onCommand(notificationCode: int) -> bool;
}