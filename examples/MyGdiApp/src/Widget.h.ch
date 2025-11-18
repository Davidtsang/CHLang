#pragma once
import <windows.h>
// [新增] 必要的 STL 头文件
import <vector>
import <map>

class Widget {
    public var m_hWnd: HWND;
    public var m_id: int;

    public init();
    public deinit;

    // 纯虚函数
    public func create(parent: HWND, id: int);

    // 虚函数
    public func onCommand(notificationCode: int) -> bool;
}