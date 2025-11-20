// file: framework/Widget.h.ch
#pragma once
import <windows.h>
import <vector>
import <map>

class Widget {
    public var m_hWnd: HWND;
    public var m_id: int;

    // [新增] 几何属性
    public var m_x: int;
    public var m_y: int;
    public var m_w: int;
    public var m_h: int;

    public init();
    public deinit;

    // [新增] 设置位置和大小
    public func setGeometry(x: int, y: int, w: int, h: int);

    public func create(parent: HWND, id: int);
    public func handleMessage(uMsg: UINT, wParam: WPARAM, lParam: LPARAM) -> LRESULT;
    public func onCommand(notificationCode: int) -> bool;
}