// libs/chui/include/chui/Geometry.h.ch
#pragma once
import <cstdint>
import <string>   // [关键] std::string, std::stoi
import <iostream> // [关键] std::cerr (如果需要)
import "runtime/TypeConverters.h" // [关键] 基础模板定义

// --- 1. 基础几何结构定义 ---

struct CGPoint {
    public var x: f32;
    public var y: f32;

    public init();
    public init(x: f32, y: f32);
}

struct CGSize {
    public var width: f32;
    public var height: f32;

    public init();
    public init(w: f32, h: f32);
}

struct CGRect {
    public var origin: CGPoint;
    public var size: CGSize;

    public init();
    public init(x: f32, y: f32, w: f32, h: f32);

    public func getMinX() -> f32;
    public func getMinY() -> f32;
    public func getWidth() -> f32;
    public func getHeight() -> f32;
}

struct CGColor {
    public var r: u8;
    public var g: u8;
    public var b: u8;
    public var a: u8;

    public init();
    public init(r: u8, g: u8, b: u8, a: u8);

    public static func black() -> CGColor;
    public static func white() -> CGColor;
    public static func clear() -> CGColor;
    public static func red() -> CGColor;
}

// --- 2. C++ 模板特化 (放在最后) ---

@cpp
// 辅助函数：解析 Hex 颜色 (#RRGGBB)
inline CGColor _ParseHexColor(const std::string& hex) {
    if (hex.size() < 7) return CGColor::black();
    try {
        // 使用 std::stoi 进行转换
        int r = std::stoi(hex.substr(1, 2), nullptr, 16);
        int g = std::stoi(hex.substr(3, 2), nullptr, 16);
        int b = std::stoi(hex.substr(5, 2), nullptr, 16);
        return CGColor((uint8_t)r, (uint8_t)g, (uint8_t)b, 255);
    } catch (...) {
        return CGColor::black();
    }
}

// 特化 CH::Converter<CGColor>
namespace CH {
    template <>
    struct Converter<CGColor> {
        // 标记为已实现，这样 visitCodegenInjectorStatement 生成的 if constexpr 就会为真
        static constexpr bool is_implemented = true;

        static CGColor fromString(const std::string& val) {
            return _ParseHexColor(val);
        }
    };
}
@end