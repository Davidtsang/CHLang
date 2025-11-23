// file: test/test_class_members.ch
// 目的: 验证 'public', 'static func', 构造器调用, 和默认 private

import "runtime/CHObject.h"
import "runtime/CHString.h"
import "runtime/CHInt.h"
import "runtime/CH.h"
import <iostream> // C++ 库



class MemberTest : CHObject {

    // -------------------------------------------
    // 属性 (Properties)
    // -------------------------------------------
    var x: i32;       // 默认 private (值类型)
    var s: String*;    // 默认 private (指针)
    var name: String*; // 默认 private (指针)

    // -------------------------------------------
    // 生命周期
    // -------------------------------------------

    // 构造函数 (init)
    init(val: i32, str: String*) ;

    // 析构函数 (deinit)
    deinit;

    // [关键] 必须标记为 'public' 才能被 'main' 调用
    public func printAll();

    // (默认 private)
    func getName() -> String*;

    // [关键] 必须标记为 'public' 才能被 'main' 调用
    public static func create(val: i32, str: String*) -> MemberTest*;
}

implement MemberTest{
    init(val: i32, str: String*) {
            this->x = val;
            this->s = str;   // <-- [已修复] 必须使用 $s
            this->s->retain(); // <-- [已修复] 必须使用 $s
        }

    // 析构函数 (deinit)
    deinit {

        std::cout << "DEINIT" << std::endl;

        this->s->release(); // <-- [已修复] 必须使用 $s
    }

    // [关键] 必须标记为 'public' 才能被 'main' 调用
    func printAll() {
        CH::Log(this->x);
        CH::Log(this->s);  // <-- [已修复] 必须使用 $s
    }

    // (默认 private)
    func getName() -> String* {
        return this->name;     // <-- [已修复] 必须使用 $name
    }

    // [关键] 必须标记为 'public' 才能被 'main' 调用
    func create(val: i32, str: String*) -> MemberTest* {
        return new MemberTest(val, str);
    }
}
// -------------------------------------------
// 全局 Main
// -------------------------------------------
func main() -> int {
    // a. 创建参数 (RC=1)
    var s: String* = String::create("Hello");

    // b. 创建对象 (RC=1)
    var obj: MemberTest* = MemberTest::create(100, s);

    // c. 调用 'this->method()'
    obj->printAll(); // 输出 100, "Hello"

    // d. 释放 'obj' (RC=0)
    obj->release();

    // e. 释放 's' (RC=0)
    s->release();
    
    return 0;
}