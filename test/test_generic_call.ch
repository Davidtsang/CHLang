// file: test/test_generic_call.ch
// 目的: 验证泛型链式调用 (e.g., std::make_shared[T](...))
//
// [验证点]
// 1. 验证 'std.make_shared[People](...)' 语法
// 2. 验证 'visitSimpleExpression' 的新 'DOT IDENTIFIER [typeList] (params)' 逻辑

import <iostream> // 用于 @cpp std::cout
import <memory>   // 用于 std::make_shared
import <string>   // 用于 std::string

// 1. 定义一个用于测试的 "哑巴" struct
//    (它不需要继承任何东西)
struct People {
    var name: std.string;
    var age: i32;

    // 公共构造函数 (C++: public init)
    public init(n: std.string, a: i32) ;

    // 公共方法 (C++: public func)
    public func print() ;
}

implement People{
    // 公共构造函数 (C++: public init)
    init(n: std.string, a: i32) {
        this.name = n;
        this.age = a;
    }

    // 公共方法 (C++: public func)
    func print() {
        @cpp std::cout << "  People(Name=" << this->name << ", Age=" << this->age << ")" << std::endl; @end
    }
}
// 2. Main
func main() -> int {
    @cpp std::cout << "--- Generic Call Test ---" << std::endl; @end

    // [ [ 关键测试 1: 显式类型 ] ]
    //
    // C++ (丑陋): std::shared_ptr<People> p1 = std::make_shared<People>("Alice", 30);
    // Chrono (优雅):
    //
    // [验证] visitTypeSpecifier 必须能解析 std.shared_ptr[People]
    // [验证] visitSimpleExpression 必须能解析 std.make_shared[People]
    var p1: std.shared_ptr[People] = std.make_shared[People]("Alice", 30);

    // [ [ 关键测试 2: 类型推导 (如果 'var' 已实现) ] ]
    //
    // C++ (丑陋): auto p2 = std::make_shared<People>("Bob", 40);
    // Chrono (优雅):
    //
    // [验证] visitSimpleExpression 必须能解析 std.make_shared[People]
    // [验证] 'var' (如果已实现) 必须能正确推导类型

    // (如果您还未实现 'var', 请将此行改为
    //  'var p2: std.shared_ptr[People] = std.make_shared[People]("Bob", 40);' )
var p2: std.shared_ptr[People] = std.make_shared[People]("Bob", 40);

    // [ [ 验证 ] ]
    // 我们必须使用 @cpp 块来访问 p1 和 p2，
    // 因为我们还未实现“统一访问器” (p1.print() -> p1->print() 的魔法)
    @cpp
        std::cout << "Verifying p1 (Explicit Type):" << std::endl;
        p1->print(); // C++ 语法
        std::cout << "Verifying p2 (Inferred Type 'let'):" << std::endl;
        p2->print(); // C++ 语法
    @end

    @cpp std::cout << "--- Test End ---" << std::endl; @end
    return 0;
}