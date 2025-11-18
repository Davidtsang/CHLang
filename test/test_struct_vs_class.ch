// file: test/test_struct_vs_class.ch
// 目的: 实现 struct/class 并运行 main() (显式语法版)

// [1] 导入我们自己的头文件
// [2] 导入 main() 所需的私有依赖
import <iostream>
import "runtime/ChronoObject.h" // (用于 class)

// ---
// 1. 值类型 STRUCT 声明
// ---
struct Point {
    // 默认 public
    var x: i32;
    var y: i32;

    // init 声明 (无函数体)
    init(val: i32);

    // method 声明 (无函数体)
    func getX() -> i32;
}

// ---
// 2. 引用类型 CLASS 声明
// ---
class RefPoint : ChronoObject {

    // 默认 private
    var x: i32;
    var y: i32;

    // init 声明 (必须设为 public 才能 'new')
    public init(val: i32);

    // method 声明 (必须设为 public 才能调用)
    public func getX() -> i32;
}

// ---
// 1. 值类型 STRUCT 实现
// ---
implement Point {
    // init 实现
    init(val: i32) {
        // [显式语法] 在 C++ 中 struct 的 'this' 是指针，所以必须用 '->'
        this->x = val;
        this->y = val * 2;
    }

    // method 实现
    func getX() -> i32 {
        // [显式语法] 使用 '->' 访问成员
        return this->x;
    }
}

// ---
// 2. 引用类型 CLASS 实现
// ---
implement RefPoint {
    // init 实现
    init(val: i32) {
        // [显式语法] class 的 'this' 是指针，必须用 '->'
        this->x = val;
        this->y = val * 2;
    }

    // method 实现
    func getX() -> i32 {
        // [显式语法] 使用 '->' 访问成员
        return this->x;
    }
}

// ---
// 3. 应用程序入口点
// ---
func main() -> int {
    // [关键改进] 直接使用 Chrono 语法调用 std::cout，无需 @cpp
    // 因为 :: 和 << 现在都是原生支持的操作符
    std::cout << "--- Struct vs Class Test ---" << std::endl;

    // --- 场景 A: Struct (值类型) ---
    std::cout << "Testing Struct (Value Type)..." << std::endl;

    // 声明在 C++ 栈上
    var p: Point = Point(10);

    // [测试 5] 外部访问 struct (值类型)
    // 显式使用 '.'
    var val_a: i32 = p.getX();
    std::cout << val_a << std::endl; // 10

    // [测试 6] 外部访问 struct 成员 (值类型)
    // 显式使用 '.'
    p.y = 50;
    std::cout << p.y << std::endl; // 50


    // --- 场景 B: Class (引用类型) ---
    std::cout << "Testing Class (Reference Type)..." << std::endl;

    // 声明在 C++ 堆上 (返回指针)
    var rp: RefPoint* = new RefPoint(100);

    // [测试 7] 外部访问 class (指针类型)
    // 显式使用 '->' (不再有魔法自动转换)
    var val_b: i32 = rp->getX();
    std::cout << val_b << std::endl; // 100

    // [测试 8] 显式释放 (指针类型)
    // 显式使用 '->'
    rp->release();

    std::cout << "--- Test End ---" << std::endl;
    return 0;
}