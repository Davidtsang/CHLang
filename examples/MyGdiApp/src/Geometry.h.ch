// file: framework/Geometry.ch
#pragma once

// --- 1. 基础几何结构 ---

struct CGPoint {
    var x: f32;
    var y: f32;

    init(x: f32, y: f32);
}
implement CGPoint {
    init(x: f32, y: f32) { this.x = x; this.y = y; }
}

struct CGSize {
    var width: f32;
    var height: f32;

    init(w: f32, h: f32);
}
implement CGSize {
    init(w: f32, h: f32) { this.width = w; this.height = h; }
}

struct CGRect {
    var origin: CGPoint;
    var size: CGSize;

    init(x: f32, y: f32, w: f32, h: f32);

    // 辅助方法
    func getMinX() -> f32;
    func getMinY() -> f32;
    func getWidth() -> f32;
    func getHeight() -> f32;
}
implement CGRect {
    init(x: f32, y: f32, w: f32, h: f32) {
        this.origin.x = x;
        this.origin.y = y;
        this.size.width = w;
        this.size.height = h;
    }
    func getMinX() -> f32 { return this.origin.x; }
    func getMinY() -> f32 { return this.origin.y; }
    func getWidth() -> f32 { return this.size.width; }
    func getHeight() -> f32 { return this.size.height; }
}

// --- 2. 颜色结构体 ---

struct CGColor {
    var r: u8;
    var g: u8;
    var b: u8;
    var a: u8;

    init(r: u8, g: u8, b: u8, a: u8);

    // 预设颜色工厂方法
    static func black() -> CGColor;
    static func white() -> CGColor;
    static func clear() -> CGColor; // 透明
    static func red() -> CGColor;
}

implement CGColor {
    init(r: u8, g: u8, b: u8, a: u8) {
        this.r = r; this.g = g; this.b = b; this.a = a;
    }

    func black() -> CGColor { return CGColor(0, 0, 0, 255); }
    func white() -> CGColor { return CGColor(255, 255, 255, 255); }
    func clear() -> CGColor { return CGColor(0, 0, 0, 0); }
    func red()   -> CGColor { return CGColor(255, 0, 0, 255); }
}