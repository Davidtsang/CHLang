// file: framework/Window.h.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN

#pragma once
import <windows.h>
import <vector>  // [新增]
import <map>     // [新增]
import <memory>  // [新增]
import "Application"
import "Widget"

// 从 gdiplus_demo.ch 导入 C++ 回调签名
typemap C_LRESULT_CALLBACK = "LRESULT CALLBACK";
typemap C_HBRUSH = "HBRUSH"; //
// 声明我们的 C-style 桥接函数
extern func GlobalWindowProc(
    hWnd: HWND, uMsg: UINT, wParam: WPARAM, lParam: LPARAM
) -> C_LRESULT_CALLBACK;

class Window{
    public var m_hWnd: HWND;
    var m_app: Application*;

    // [新增] 子控件管理
    // 1. 所有权管理 (vector<unique_ptr>)
    var m_children: std.vector[unique[Widget]];
    // 2. 快速查找 (map<id, Widget*>)
    var m_lookup: std.map[int, Widget*];
    // 3. ID 计数器
    var m_nextId: int;

    public init(title: LPCWSTR, app: Application*);
    public deinit;
    public func show();

    // [新增] 添加子控件 API
    public func addChild(widget: unique[Widget]);

    public func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT;
}