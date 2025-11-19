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
import "Widget"

#define C_LRESULT_CALLBACK LRESULT CALLBACK

extern func GlobalWindowProc(
    hWnd: HWND, uMsg: UINT, wParam: WPARAM, lParam: LPARAM
) -> C_LRESULT_CALLBACK;

class Window {
    public var m_hWnd: HWND;
    var m_app: Application*;

    // [重构] 泛型使用 < >
    // 1. vector<unique<Widget>>
    var m_children: std::vector<unique<Widget> >;
    // 2. map<int, Widget*>
    var m_lookup: std::map<int, Widget*>;

    var m_nextId: int;

    public init(title: LPCWSTR, app: Application*);
    public deinit;
    public func show();

    // [重构] 泛型使用 < >
    public func addChild(widget: unique<Widget>);

    public func handleMessage(
        uMsg: UINT, wParam: WPARAM, lParam: LPARAM
    ) -> LRESULT;
}