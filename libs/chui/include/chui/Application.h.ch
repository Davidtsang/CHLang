// file: framework/Application.h.ch
#pragma once
import <windows.h>

class Application{
    // 私有成员
    var m_hInstance: HINSTANCE;
    var m_nCmdShow: int;

    // 公共 API
    public init();
    public deinit;

    // 阻塞的消息循环
    public func exec() -> int;

    // 供 Window 内部使用
    public func getHInstance() -> HINSTANCE;
    public func getNCmdShow() -> int;
}