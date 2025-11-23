// file: test/test_var_const.ch
// 目的: 验证 var/const/auto 声明 (适配显式语法)

import <iostream>
import "runtime/CHObject.h"

struct TestStruct {
    // 1. 成员变量 (显式, 可变)
    var x: i32;
    // 2. 成员变量 (显式, 不可变)
    const y: i32 = 20;
}

func main() -> int {
    //  块内部本身就是 C++，保持 std::cout 即可
     std::cout << "--- Var/Const/Auto Test ---" << std::endl; 

    // 3. 显式, 不可变
    const p1: i32 = 10;
    std::cout << "p1 (const explicit): " << p1 << std::endl;
    // p1 = 11; // (应该编译失败)

    // 4. 显式, 可变
    var p2: i32 = 20;
    p2 = 21;
     std::cout << "p2 (var explicit): " << p2 << std::endl; 

    // 5. 推导, 不可变 (C++: const auto)
    const p3 = 30;
     std::cout << "p3 (const auto): " << p3 << std::endl; 
    // p3 = 31; // (应该编译失败)

    // 6. 推导, 可变 (C++: auto)
    var p4 = 40;
    p4 = 41;
     std::cout << "p4 (var auto): " << p4 << std::endl; 

    // 7. 显式, 可变 (无初始化)
    var p5: i32;
    p5 = 50;
    std::cout << "p5 (var uninitialized): " << p5 << std::endl;

    // 8. For 循环
    std::cout << "For loop (var i):" << std::endl;
    for (var i = 0; i < 2; i = i + 1) {
         std::cout << "  i=" << i << std::endl; 
    }

    // 9. 指针类型推导
    // new CHObject() 返回的是 CHObject* (原始指针)
    var s = new CHObject();

    // [关键修改]
    // 因为 s 是指针类型，在新的严格语法下，必须显式使用 -> 访问成员
    // 原代码: s.release(); -> 错误 (error: request for member 'release' in 's', which is of pointer type)
    // 新代码:
    s->release();

    std::cout << "s (var auto pointer): OK" << std::endl;

    return 0;
}