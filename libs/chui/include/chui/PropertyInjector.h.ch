#pragma once
import "runtime/CHObject.h"
import <string>

class PropertyInjector {
    // 注入字符串/颜色属性
    public static func inject(obj: dyn, key: std::string, value: std::string);
    // 注入整数属性
    public static func injectInt(obj: dyn, key: std::string, value: i32);

    public static func injectBool(obj: dyn, key: std::string, value: bool);
}