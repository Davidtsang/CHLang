// examples/MyGdiApp/include/LayoutLoader.h.ch
#pragma once

import <string>
import <windows.h>
import "chui/Button"
import "chui/Widget" // [新增]
import "jsonp/Json"  // [新增] 需要 JObject

class LayoutLoader {
    // [新增] 声明为 static private (或 public，这里无所谓)
    // 注意：需要导入 chui/Widget 和 jsonp/Json 才能识别类型
    public static func parseWidget(parent: HWND, itemObj: JObject*, id: int, exitCb: ClickCallback) -> Widget*;

    public static func load(path: std::string, parent: HWND, exitCb: ClickCallback) -> bool;
}