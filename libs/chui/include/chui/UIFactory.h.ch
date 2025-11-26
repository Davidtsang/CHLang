#pragma once
import "runtime/CHObject.h"
import <string>

class UIFactory {
    // 返回 dyn (CHObject*)
    public static func createWidget(className: std::string) -> dyn;
}