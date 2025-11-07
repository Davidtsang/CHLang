// file: test/test_class_members.ch
// 目的: 验证 'public', 'static func', 构造器调用, 和默认 private

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";
import "runtime/Chrono.h";
import <iostream>; // C++ 库

class MemberTest : ChronoObject {

    // -------------------------------------------
    // 属性 (Properties)
    // -------------------------------------------
    let x: i32;       // 默认 private (值类型)
    let $s: String;    // 默认 private (指针)
    let $name: String; // 默认 private (指针)

    // -------------------------------------------
    // 生命周期
    // -------------------------------------------

    // 构造函数 (init)
    init(val: i32, $str: String) {
        this.x = val;
        this.$s = $str;   // <-- [已修复] 必须使用 $s
        this.$s.retain(); // <-- [已修复] 必须使用 $s
    }

    // 析构函数 (deinit)
    deinit {
        @cpp
            std::cout << "DEINIT" << std::endl;
        @end
        this.$s.release(); // <-- [已修复] 必须使用 $s
    }

    // [关键] 必须标记为 'public' 才能被 'main' 调用
    public func printAll() {
        Chrono.log(this.x);
        Chrono.log(this.$s);  // <-- [已修复] 必须使用 $s
    }

    // (默认 private)
    func getName() -> $String {
        return this.$name;     // <-- [已修复] 必须使用 $name
    }

    // [关键] 必须标记为 'public' 才能被 'main' 调用
    public static func create(val: i32, $str: String) -> $MemberTest {
        return new MemberTest(val, $str);
    }
}

// -------------------------------------------
// 全局 Main
// -------------------------------------------
func main() -> int {
    // a. 创建参数 (RC=1)
    let $s: String = String.create("Hello");

    // b. 创建对象 (RC=1)
    let $obj: MemberTest = MemberTest.create(100, $s);

    // c. 调用 'this.method()'
    $obj.printAll(); // 输出 100, "Hello"

    // d. 释放 'obj' (RC=0)
    $obj.release();

    // e. 释放 's' (RC=0)
    $s.release();
    
    return 0;
}