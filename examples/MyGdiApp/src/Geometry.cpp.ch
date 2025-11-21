// file: framework/Geometry.cpp.ch
import "Geometry"

// --- CGPoint 实现 ---
implement CGPoint {
    init() {
        this->x = 0.0;
        this->y = 0.0;
    }
    init(x: f32, y: f32) {
        this->x = x;
        this->y = y;
    }
}

// --- CGSize 实现 ---
implement CGSize {
    init() {
        this->width = 0.0;
        this->height = 0.0;
    }
    init(w: f32, h: f32) {
        this->width = w;
        this->height = h;
    }
}

// --- CGRect 实现 ---
implement CGRect {
    init() { }

    init(x: f32, y: f32, w: f32, h: f32) {
        this->origin.x = x;
        this->origin.y = y;
        this->size.width = w;
        this->size.height = h;
    }

    // [修复] 使用 -> 访问 this
    func getMinX() -> f32 { return this->origin.x; }
    func getMinY() -> f32 { return this->origin.y; }
    func getWidth() -> f32 { return this->size.width; }
    func getHeight() -> f32 { return this->size.height; }
}

// --- CGColor 实现 ---
implement CGColor {
    init() {
        this->r=0; this->g=0; this->b=0; this->a=255;
    }
    init(r: u8, g: u8, b: u8, a: u8) {
        this->r = r; this->g = g; this->b = b; this->a = a;
    }

    func black() -> CGColor { return CGColor(0, 0, 0, 255); }
    func white() -> CGColor { return CGColor(255, 255, 255, 255); }
    func clear() -> CGColor { return CGColor(0, 0, 0, 0); }
    func red()   -> CGColor { return CGColor(255, 0, 0, 255); }
}