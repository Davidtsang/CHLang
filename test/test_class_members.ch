// file: test/test_class_members.ch
// 目的: 验证 'public', 'static func', 构造器调用, 和默认 private

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";
import <iostream>; // C++ 库 (我们仍用于 deinit)

class MemberTest : ChronoObject {

    // -------------------------------------------
    // 属性 (Properties)
    // -------------------------------------------

    // [修复] 这些属性必须是 public，以便 'init' (构造函数)
    // 和 'printAll' (方法) 可以被正确地声明为 public。
    // （或者，我们可以让它们保持 private，但 'init' 和 'printAll' 必须是 public）
    // 为了最严格的测试，我们将它们保持为默认 private。

    let x: i32;       // 默认 private
    let s: String;    // 默认 private
    let name: String; // 默认 private

    // -------------------------------------------
    // 生命周期
    // -------------------------------------------

    // 构造函数 (init)
    // 默认 private。这是好的，因为它强制使用 'create' 工厂方法。
    func init(val: i32, str: String) {
        this.x = val;
        this.s = str;
        this.s.retain();
    }

    // 析构函数 (deinit)
    // (我们的 Visitor 逻辑会自动将其放入 public: 区块)
    deinit {
        @cpp
            std::cout << "DEINIT" << std::endl;
        @end
        this.s.release();
    }

    // [关键修复] 必须标记为 'public' 才能被 'main' 调用
    public func printAll() {
        print(this.x);
        print(this.s);
    }

    // (默认 private)
    func getName() -> String {
        return this.name;
    }

    // [关键修复] 必须标记为 'public' 才能被 'main' 调用
    public static func create(val: i32, str: String) -> MemberTest {
        // 'MemberTest(...)' 翻译为 'new MemberTest(...)'
        return MemberTest(val, str);
    }
}

// -------------------------------------------
// 全局 Main
// -------------------------------------------
func main() -> Int {
    // a. 创建参数 (RC=1)
    let s: String = "Hello";

    // b. 创建对象 (RC=1)
    //    (现在可以调用，因为 create 是 public)
    let obj: MemberTest = MemberTest.create(100, s);

    // c. 调用 'this.method()'
    //    (现在可以调用，因为 printAll 是 public)
    obj.printAll(); // 输出 100, "Hello"
    
    // d. 释放 'obj' (RC=0)
    obj.release();
    
    // e. 释放 's' (RC=0)
    s.release();
    
    return 0;
}