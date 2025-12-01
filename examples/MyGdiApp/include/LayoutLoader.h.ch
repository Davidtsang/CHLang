// examples/MyGdiApp/include/LayoutLoader.h.ch
#pragma once

import <string>
import <windows.h>
import "chui/Button" // 为了使用 ClickCallback 类型

class LayoutLoader {
    // 定义为一个静态工具方法
    // 参数:
    // path: json 文件路径
    // parent: 父窗口句柄 (用于挂载控件)
    // exitCb: 退出回调 (专门为了给 Button 绑定事件用)
    public static func load(path: std::string, parent: HWND, exitCb: ClickCallback) -> bool;
}