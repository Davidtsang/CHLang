// file: test/test_interface.ch
// 目的: 验证 'interface' 和 'impl' 关键字

import <iostream>
import <string>
import "runtime/ChronoObject.h"

// ---
// 1. 接口定义
// ---

// 接口 I: 简单的日志接口
interface ILoggable {
    func logMessage() -> void;
}

// 接口 II: 形状接口，返回一个值
interface IShape {
    func getName() -> std::string;
    func getArea() -> f32;
}

// ---
// 2. 类实现
// ---

// 类 A: "Circle"
// - 继承自 ChronoObject (用于 MRC)
// - 实现 ILoggable 和 IShape
class Circle : ChronoObject impl ILoggable, IShape {

    var radius: f32;
//    var radius: unique[Cat] = @make[Cat]();
//    var radius: shared[Dog] = @make_shread[Dog];
//    var radius: weak[Dog] = @move a;
    public init(r: f32) ;

    // 实现 ILoggable
    public func logMessage() -> void ;

    // 实现 IShape
    public func getName() -> std::string ;

    public func getArea() -> f32 ;
}

implement Circle{
    init(r: f32) {
        this->radius = r;
    }

    // 实现 ILoggable
    func logMessage() -> void {
        @cpp
            std::cout << "Log: Circle (r=" << this->radius << ")" << std::endl;
        @end
    }

    // 实现 IShape
    func getName() -> std::string {
        return "Circle";
    }

    func getArea() -> f32 {
        return 3.14159 * this->radius * this->radius;
    }
}
// 类 B: "Square"
// - 继承自 ChronoObject (用于 MRC)
// - 只实现 IShape
class Square : ChronoObject impl IShape {

    var side: f32;

    public init(s: f32);

    // 实现 IShape
    public func getName() -> std::string ;
    public func getArea() -> f32 ;
}

implement Square{
    init(s: f32) {
        this->side = s;
    }

    // 实现 IShape
    func getName() -> std::string {
        return "Square";
    }
    func getArea() -> f32 {
        return this->side * this->side;
    }
}
// ---
// 3. 多态性测试函数
// ---

// 函数 1: 接受任何实现了 IShape 的对象
// [关键] 接口作为参数，必须使用 $ 引用类型
func printShapeDetails(s: IShape*) {
    var name: std::string = s->getName();
    var area: f32 = s->getArea();

    @cpp
        std::cout << "  Detail: Name=" << name << ", Area=" << area << std::endl;
    @end
}

// 函数 2: 接受任何实现了 ILoggable 的对象
func triggerLog(l: ILoggable*) {
    @cpp std::cout << "  Log Trigger:" << std::endl; @end
    l->logMessage(); // 调用接口方法
}


// ---
// 4. 主函数
// ---
func main() -> int {
    @cpp std::cout << "--- Interface Test Start ---" << std::endl; @end

    // 创建实例
    var c: Circle* = new Circle(10.0); // area = 314.159
    var s: Square* = new Square(10.0); // area = 100

    // --- 测试 1: IShape 多态性 ---
    @cpp std::cout << "Test 1: Polymorphism with IShape" << std::endl; @end
    // 声明一个 $IShape 变量
    var shape_ref: IShape*;

    // 1a. 将 Circle 赋给 $IShape 引用
    shape_ref = c;
    printShapeDetails(shape_ref); // 预期: Circle, 314.159

    // 1b. 将 Square 赋给 $IShape 引用
    shape_ref = s;
    printShapeDetails(shape_ref); // 预期: Square, 100

    // --- 测试 2: ILoggable 多态性 ---
    @cpp std::cout << "Test 2: Polymorphism with ILoggable" << std::endl; @end
    triggerLog(c); // 预期: Log: Circle (r=10)

    // (Square 没有实现 ILoggable，所以 triggerLog($s) 会导致编译失败, 这是正确的)

    // 清理
    c->release();
    s->release();

    @cpp std::cout << "--- Interface Test End ---" << std::endl; @end
    return 0;
}