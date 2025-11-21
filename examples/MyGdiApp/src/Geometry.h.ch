// file: framework/Geometry.h.ch
#pragma once
import <cstdint> // 必须导入，用于 u8 等类型

// --- 1. 基础几何结构 ---

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

    // 方法声明 (无函数体)
    public func getMinX() -> f32;
    public func getMinY() -> f32;
    public func getWidth() -> f32;
    public func getHeight() -> f32;
}

// --- 2. 颜色结构体 ---

struct CGColor {
    public var r: u8;
    public var g: u8;
    public var b: u8;
    public var a: u8;

    public init();
    public init(r: u8, g: u8, b: u8, a: u8);

    // 静态方法声明
    public static func black() -> CGColor;
    public static func white() -> CGColor;
    public static func clear() -> CGColor;
    public static func red() -> CGColor;
}