import "PropertyInjector"
import "Reflection"
import "Geometry"
import <string>
import <vector>
import <any>
import <iostream>

// Hex 解析助手
func parseHex(hex: std::string) -> CGColor {
    @cpp
    if (hex.size() < 7) return CGColor::black();
    try {
        int r = std::stoi(hex.substr(1, 2), nullptr, 16);
        int g = std::stoi(hex.substr(3, 2), nullptr, 16);
        int b = std::stoi(hex.substr(5, 2), nullptr, 16);
        return CGColor((uint8_t)r, (uint8_t)g, (uint8_t)b, 255);
    } catch (...) { return CGColor::black(); }
    @end
}

implement PropertyInjector {

    func inject(obj: dyn, key: std::string, value: std::string) {
        var methodName: std::string = "";

        // 1. 映射逻辑
        if (key == @"text") {
            methodName = @"setText";
            var sel: u64 = Reflection::getSelector(methodName);

            @cpp
            // 动态调用: setText(string)
            std::vector<std::any> args = { value };
            obj->msgSend(sel, args);
            @end
        }
        else if (key == @"color") {
            methodName = @"setTextColor";
            var color = parseHex(value);
            var sel: u64 = Reflection::getSelector(methodName);

            @cpp
            // 动态调用: setTextColor(CGColor)
            std::vector<std::any> args = { color };
            obj->msgSend(sel, args);
            @end
        }
        else if (key == @"bg") {
            methodName = @"setBackgroundColor"; // Label/Button/Window 都可能支持
            var color = parseHex(value);
            var sel: u64 = Reflection::getSelector(methodName);
            @cpp
            std::vector<std::any> args = { color };
            obj->msgSend(sel, args);
            @end
        }
    }

    func injectInt(obj: dyn, key: std::string, value: i32) {
        // 映射 x, y, width, height -> setX, setY...
        var first: std::string = key.substr(0, 1);
        @cpp
        char c = first[0];
        if(c >= 'a' && c <= 'z') c -= 32;
        first = std::string(1, c);
        @end

        var methodName: std::string = "set" + first + key.substr(1);
        var sel: u64 = Reflection::getSelector(methodName);

        @cpp
        std::vector<std::any> args = { value };
        obj->msgSend(sel, args);
        @end
    }
}