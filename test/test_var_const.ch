// file: test/test_var_const.ch
// 目的: 验证 var/const/auto 声明

import <iostream>;
import "runtime/ChronoObject.h";

struct TestStruct {
    // 1. 成员变量 (显式, 可变)
    var x: i32;
    // 2. 成员变量 (显式, 不可变)
    const y: i32 = 20;
}

func main() -> int {
    @cpp std::cout << "--- Var/Const/Auto Test ---" << std::endl; @end

    // 3. 显式, 不可变
    const p1: i32 = 10;
    @cpp std::cout << "p1 (const explicit): " << p1 << std::endl; @end
    // p1 = 11; // (应该编译失败)

    // 4. 显式, 可变
    var p2: i32 = 20;
    p2 = 21;
    @cpp std::cout << "p2 (var explicit): " << p2 << std::endl; @end

    // 5. 推导, 不可变 (C++: const auto)
    const p3 = 30;
    @cpp std::cout << "p3 (const auto): " << p3 << std::endl; @end
    // p3 = 31; // (应该编译失败)

    // 6. 推导, 可变 (C++: auto)
    var p4 = 40;
    p4 = 41;
    @cpp std::cout << "p4 (var auto): " << p4 << std::endl; @end

    // 7. 显式, 可变 (无初始化)
    var p5: i32;
    p5 = 50;
    @cpp std::cout << "p5 (var uninitialized): " << p5 << std::endl; @end

    // 8. For 循环
    @cpp std::cout << "For loop (var i):" << std::endl; @end
    for (var i = 0; i < 2; i = i + 1) {
        @cpp std::cout << "  i=" << i << std::endl; @end
    }

    // 9. $ 指针推导
    var s = new ChronoObject(); // C++: auto _s = new ChronoObject();
    s.release();
    @cpp std::cout << "$s (var auto pointer): OK" << std::endl; @end

    return 0;
}