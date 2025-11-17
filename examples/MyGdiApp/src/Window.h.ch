// file: framework/Window.h.ch
#define UNICODE     // <--- [ [ [ 修复 ] ] ] 添加此行
#define _UNICODE    // <--- [ [ [ 修复 ] ] ] 添加此行

#pragma once
import <windows.h>
import "Application" // 必须导入

// 从 gdiplus_demo.ch 导入 C++ 回调签名
typemap C_LRESULT_CALLBACK = "LRESULT CALLBACK";
typemap C_HBRUSH = "HBRUSH"; //
// 声明我们的 C-style 桥接函数
extern func GlobalWindowProc(
    hWnd: HWND, uMsg: UINT, wParam: WPARAM, lParam: LPARAM
) -> C_LRESULT_CALLBACK;

class Window{
    // 成员
    public var m_hWnd: HWND;
    var m_app: Application*; // [ [ [ 改进 3: 保存 App 指针 ] ] ]

    // API
    public init(title: LPCWSTR, app: Application*);
    public deinit; // [ [ [ 修复 2: 虚拟析构函数 ] ] ]
    public func show();

    // 核心：OOP 消息处理器 (必须是 virtual)
    public func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT;
}