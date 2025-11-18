#pragma once

import "Widget"
import <string>
import <functional>

// [重构] 移除 @cpp，直接使用 Chrono 别名语法
// 预期翻译: using ClickCallback = std::function<void()>;
using ClickCallback = std::function<void()>;

class Button : Widget {
    var m_text: std::string;
    var m_onClick: ClickCallback; // 存储回调

    public init(text: std::string);

    public func setOnClick(cb: ClickCallback);

    // 重写基类方法
    public func create(parent: HWND, id: int);
    public func onCommand(notificationCode: int) -> bool;
}