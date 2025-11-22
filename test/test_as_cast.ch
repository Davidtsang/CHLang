import "runtime/ChronoObject.h"
import <iostream>

@dynamic
class Base : ChronoObject { public init(); }
@dynamic implement Base { init(){} }

@dynamic
class DerivedA : Base { public init(); public func funcA(); }
@dynamic implement DerivedA {
    init(){}
    func funcA() { @cpp std::cout << "Func A" << std::endl; @end }
}

@dynamic
class DerivedB : Base { public init(); }
@dynamic implement DerivedB { init(){} }

func main() -> int {
    @cpp std::cout << "--- As Cast Test ---" << std::endl; @end

    // 1. 创建 A 对象，向上转型为 dyn
    var objA: DerivedA* = new DerivedA();
    var d: dyn = objA;

    // 2. 正确转型 (dyn -> DerivedA)
    var a: DerivedA* = d as DerivedA;

    if (a != nullptr) {
        @cpp std::cout << "PASS: d as DerivedA success" << std::endl; @end
        a->funcA();
    } else {
        @cpp std::cout << "FAIL: d as DerivedA failed" << std::endl; @end
    }

    // 3. 错误转型 (dyn -> DerivedB)
    var b: DerivedB* = d as DerivedB;

    if (b == nullptr) {
        @cpp std::cout << "PASS: d as DerivedB returned null (Safe)" << std::endl; @end
    } else {
        @cpp std::cout << "FAIL: d as DerivedB should be null!" << std::endl; @end
    }

    objA->release();
    return 0;
}