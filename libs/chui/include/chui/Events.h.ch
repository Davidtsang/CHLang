// file: framework/Events.h.ch
#pragma once

// 定义鼠标事件结构体
struct MouseEvent {
    public var x: int;
    public var y: int;
    public var button: int; // 0=Left, 1=Right, 2=Middle

    // 声明构造函数
    public init(x: int, y: int, btn: int);
}