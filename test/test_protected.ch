import "runtime/ChronoObject.h"
import <iostream>

class Parent : ChronoObject {
    // 私有
    var secret: i32;

    // 受保护 (子类可见，外部不可见)
    protected var legacy: i32;

    public init();

    protected func internalHelper();
}

implement Parent {
    init() {
        this->secret = 1;
        this->legacy = 100;
    }

    func internalHelper() {
        @cpp std::cout << "Parent::internalHelper called" << std::endl; @end
    }
}

class Child : Parent {
    public init();
    public func testAccess();
}

implement Child {
    init() {}

    func testAccess() {
        // 1. 访问父类 protected 变量 -> 应该成功
        var val = this->legacy;
        @cpp std::cout << "Child accessing protected var: " << val << std::endl; @end

        // 2. 调用父类 protected 方法 -> 应该成功
        this->internalHelper();

        // 3. 访问父类 private 变量 -> C++ 编译器会报错 (如果取消注释)
        // var fail = this->secret;
    }
}

func main() -> int {
    @cpp std::cout << "--- Protected Test ---" << std::endl; @end

    var c: Child* = new Child();
    c->testAccess();

    // 外部访问 protected -> C++ 编译器会报错 (如果取消注释)
    // c->internalHelper();

    c->release();
    return 0;
}