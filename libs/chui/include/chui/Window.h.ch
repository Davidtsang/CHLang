// file: framework/Window.h.ch
#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN

#pragma once
import <iostream>
import <windows.h>
import <vector>
import <map>
import <memory>
import "Application"
import "Widget" // 必须导入基类
import "Menu" // <--- [必须有这行]
#define C_LRESULT_CALLBACK LRESULT CALLBACK

extern func GlobalWindowProc(
    hWnd: HWND, uMsg: UINT, wParam: WPARAM, lParam: LPARAM
) -> C_LRESULT_CALLBACK;

// [修复 1] 继承 Widget
@dynamic
class Window : Widget {
    // [修复 2] 删除重复的 m_hWnd (使用 Widget 的)
    // public var m_hWnd: HWND; <--- 删除这行

    var m_app: Application*;
    var m_children: std::vector<unique<Widget> >;
    var m_lookup: std::map<int, Widget*>;
    var m_nextId: int;
    // [新增] 菜单回调映射表: ID -> Function
    var m_menuCallbacks: std::map<int, std::function<void()> >;

    public init(title: LPCWSTR, app: Application*, width: int, height: int);
    public deinit;
    public func show();

    public func addChild(widget: Widget*);

    // [新增] 设置菜单条
    public func setMenuBar(menu: Menu*);

    // [新增] 注册菜单回调
    public func bindMenuAction(id: i32, cb: std::function<void()>);

    // 重写基类虚函数
    public func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT;
}