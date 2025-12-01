#pragma once
import "runtime/CHObject.h"
import <string>
import <functional>
import <windows.h>

// 定义菜单回调
using MenuCallback = std::function<void()>;

@dynamic
class Menu : CHObject {
    public var m_hMenu: HMENU;

    // 构造函数: isPopup=true 创建下拉菜单，false 创建顶层菜单条
    public init(isPopup: bool);
    public deinit;

    // 添加普通项 (返回 Item ID)
    public func addItem(text: std::string, id: i32) -> void;

    // 添加分割线
    public func addSeparator() -> void;

    // 添加子菜单 (例如 "File" -> 下拉列表)
    public func addSubMenu(text: std::string, subMenu: Menu*) -> void;
}