// file: framework/Application.h.ch
#pragma once
import <windows.h>

class Application{
    // 私有成员
    var m_hInstance: HINSTANCE;
    var m_nCmdShow: int; // [ [ [ 改进 3 ] ] ]

    // 公共 API
    public init();
    public deinit; // [ [ [ 修复 2: 虚拟析构函数 ] ] ]

    // 阻塞的消息循环
    public func exec() -> int;

    // 供 Window 内部使用
    public func getHInstance() -> HINSTANCE;
    public func getNCmdShow() -> int; // [ [ [ 改进 3 ] ] ]
}