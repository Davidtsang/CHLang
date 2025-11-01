// file: test/test_class_members.ch
// 目的: [已更新] 验证 'static func', 构造器调用, 和 MRC

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";
import <iostream>; // C++ 库 (我们仍用于 deinit)

class MemberTest : ChronoObject {
    // 1. 成员 (保持不变)
    let x: i32;
    let s: String;

    // 2. 构造函数 (init) (保持不变)
    func init(val: i32, str: String) {
        this.x = val;
        this.s = str;
        this.s.retain();
    }
    
    // 5. 析构函数 (deinit) (保持不变)
    deinit {
        // [ 可选 ] 我们甚至可以把这个 @cpp 换成 print("DEINIT");
        @cpp
            std::cout << "DEINIT" << std::endl;
        @end
        this.s.release();
    }
    
    // 7. 成员方法 (保持不变)
    func printAll() {
        print(this.x);
        print(this.s);
    }
    
    // 8. [ 关键测试 1: 'static func' ]
    // 我们用纯 Chrono 的 'static func' 替换了旧的 @cpp 声明
    static func create(val: i32, str: String) -> MemberTest {
        
        // 9. [ 关键测试 2: "构造器调用" ]
        // 我们用 'MemberTest(...)' 替换了旧的 @cpp 'new MemberTest(...)'
        // 访问者应将其翻译为 C++: 'return new MemberTest(val, str);'
        return MemberTest(val, str);
    }
    
    // (之前在这里的两个 @cpp 块现在都已删除)
}

// 10. 'main' 函数保持不变
// 它现在调用的是我们上面定义的纯 Chrono 'static func'
func main() -> Int {
    // a. 创建参数 (RC=1)
    let s: String = "Hello";
    
    // b. 创建对象 (RC=1)
    let obj: MemberTest = MemberTest.create(100, s);
    
    // c. 调用 'this.method()'
    obj.printAll(); // 输出 100, "Hello"
    
    // d. 释放 'obj' (RC=0)
    obj.release();
    
    // e. 释放 's' (RC=0)
    s.release();
    
    return 0;
}