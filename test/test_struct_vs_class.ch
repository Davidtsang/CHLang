// file: test/test_struct_vs_class.ch
// 目的: 验证 struct (值类型) 和 class (引用类型) 的区别

import <iostream>
import "runtime/ChronoObject.h" // (用于 class)

// ---
// 1. 值类型 STRUCT
// ---
struct Point {
    // 默认 public
    var x: i32;
    var y: i32;

    // init (默认 public)
    init(val: i32) {
        // [测试 1] struct 内部访问 'this'
        // 应该翻译为: this.x = val; (使用 '.')
        this.x = val;
        this.y = val * 2;
    }

    // method (默认 public)
    func getX() -> i32 {
        // [测试 2] struct 内部访问 'this'
        // 应该翻译为: return this.x; (使用 '.')
        return this.x;
    }
}

// ---
// 2. 引用类型 CLASS
// ---
class RefPoint : ChronoObject {
    // 默认 private
    var x: i32;
    var y: i32;

    // init (必须设为 public 才能 'new')
    public init(val: i32) {
        // [测试 3] class 内部访问 'this'
        // 应该翻译为: this->x = val; (使用 '->')
        this.x = val;
        this.y = val * 2;
    }

    // method (必须设为 public 才能调用)
    public func getX() -> i32 {
        // [测试 4] class 内部访问 'this'
        // 应该翻译为: return this->x; (使用 '->')
        return this.x;
    }
}


func main() -> int {
    @cpp std::cout << "--- Struct vs Class Test ---" << std::endl; @end

    // --- 场景 A: Struct (值类型) ---
    @cpp std::cout << "Testing Struct (Value Type)..." << std::endl; @end

    // 声明在 C++ 栈上
    var p: Point = Point(10);

    // [测试 5] 外部访问 struct
    // 应该翻译为: p.getX() (使用 '.')
    var val_a: i32 = p.getX();
    @cpp std::cout << val_a << std::endl; @end // 10

    // [测试 6] 外部访问 struct 成员
    // 应该翻译为: p.y = 50; (使用 '.')
    p.y = 50;
    @cpp std::cout << p.y << std::endl; @end // 50


    // --- 场景 B: Class (引用类型) ---
    @cpp std::cout << "Testing Class (Reference Type)..." << std::endl; @end

    // 声明在 C++ 堆上
    var rp: RefPoint* = new RefPoint(100);

    // [测试 7] 外部访问 class
    // 应该翻译为: _rp->getX() (使用 '->')
    var val_b: i32 = rp.getX();
    @cpp std::cout << val_b << std::endl; @end // 100

    // [测试 8] 外部访问 class (成员是 private, 无法访问)
    // $rp.y = 500; // <- 这在 Chrono 中是非法的 (private)

    rp.release(); // 释放堆内存

    @cpp std::cout << "--- Test End ---" << std::endl; @end
    return 0;
}