// file: test/test_namespace.ch
// 目的: 验证命名空间 (namespace) 语法
//
// 验证:
// 1. `namespace Test.Internal;` 会环绕整个文件。
// 2. class, struct, global funcs 都在 `Test::Internal` C++ 命名空间中。
// 3. `main()` 函数被*豁免*，保持在 C++ 全局命名空间中。
// 4. `main()` 内部可以通过 `Test.Internal.MyClass` 访问命名空间中的代码。

// 1. 声明命名空间 (必须是文件中的第一个语句)


// 2. 导入
import <iostream>
import "runtime/CHObject.h"
import "runtime/CH.h"

namespace Test.Internal;
// 3. 命名空间中的 Struct
// (C++: namespace Test { namespace Internal { struct MyStruct { ... }; } })
struct MyStruct {
    public var x: i32;
}

// 4. 命名空间中的 Class
// (C++: namespace Test { namespace Internal { class MyClass ... } })
class MyClass : CHObject {
    public var s: MyStruct;
    public init();
    public func testMethod(val: i32);
}

// 5. 命名空间中的 Global Function
// (C++: namespace Test { namespace Internal { void globalFunc() { ... } } })
func globalFunc() {
    CH::Log("  (globalFunc in Test::Internal)");
}

// 6. 命名空间中的 Class 实现
// (C++: namespace Test { namespace Internal { ... } })
implement MyClass {
    init() {
        // Line 48
        this->s.x = 123;
    }

    func testMethod(val: i32) {
        // Line 53
        CH::Log("  (MyClass::testMethod)");
        // Line 55
        this->s.x = this->s.x + val;
        // Line 57
        CH::Log(this->s.x);
    }
}

endnamespace;

// 7. [关键测试] main 函数
// (C++: int main() { ... } -- 必须在全局!)
func main() -> int {
    // Line 65
    CH::Log("--- Namespace Test Start ---");

    // 调用全局 namespaced 函数
    // (C++: Test::Internal::globalFunc();)
    // Line 70
    Test::Internal::globalFunc();

    // 访问 namespaced class
    // (C++: Test::Internal::MyClass* c = new Test::Internal::MyClass();)
    // Line 75
    var c: Test::Internal::MyClass* = new Test::Internal::MyClass();

    // 调用
    // (C++: c->testMethod(7);)
    // Line 80
    c->testMethod(7); // 123 + 7 = 130

    // 释放
    // Line 84
    c->release();

    // Line 87
    CH::Log("--- Namespace Test End ---");
    // Line 89
    return 0;
}