#pragma once
import <windows.h>
import <map>
import <vector>
class Widget {
    // 允许子类访问
    public var m_hWnd: HWND;
    public var m_id: int;

    public init();
    public deinit;

    // 纯虚函数: 创建 Win32 控件
    // parent: 父窗口句柄
    // id: 由 Window 分配的唯一 ID
    public func create(parent: HWND, id: int);

    // 虚函数: 处理命令 (如点击)
    // 返回 true 表示已处理
    public func onCommand(notificationCode: int) -> bool;
}