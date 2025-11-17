#pragma once

import "Widget"
import <string>
import <functional>

// 定义回调类型
@cpp
using ClickCallback = std::function<void()>;
@end

class Button : Widget {
    var m_text: std.string;
    var m_onClick: ClickCallback; // 存储回调

    public init(text: std.string);

    public func setOnClick(cb: ClickCallback);

    // 重写基类方法
    public func create(parent: HWND, id: int);
    public func onCommand(notificationCode: int) -> bool;
}