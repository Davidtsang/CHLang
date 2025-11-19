// file: test/test_switch.ch
// 目的: 验证 'switch' 语句 (现代语法)
// 1. 验证 case 块
// 2. 验证 default 块
// 3. 验证 隐式 'break' (没有 "掉落")
// 4. 验证 'typemap' 常量在 case 中

import "runtime/ChronoObject.h" // (用于 main)
import <iostream>

// (用于测试 'typemap' 代换)
#define  C_CASE_2 2
#define  C_CASE_3 3

// 一个辅助函数
func testSwitch(val: i32) {
    @cpp std::cout << "--- Testing value: " << val << " ---" << std::endl; @end

    switch (val) {

        case 1 {
            @cpp std::cout << "  Case 1 executed." << std::endl; @end
            var x: i32 = 100; // 测试 case 内部作用域
        } // (隐式 break)

        case C_CASE_2 { // [关键] 测试 typemap 代换
            @cpp std::cout << "  Case 2 (from typemap) executed." << std::endl; @end
        } // (隐式 break)

        case C_CASE_3 {
             @cpp std::cout << "  Case 3 (from typemap) executed." << std::endl; @end
        }

        default {
            @cpp std::cout << "  Default executed." << std::endl; @end
        } // (隐式 break)
    }

    @cpp std::cout << "  Switch finished." << std::endl; @end
}


func main() -> int {
    @cpp std::cout << "--- Switch Test Start ---" << std::endl; @end

    testSwitch(1); // 测试 Case 1
    testSwitch(2); // 测试 Case 2 (typemap)
    testSwitch(3); // 测试 Case 3 (typemap)
    testSwitch(99); // 测试 Default

    @cpp std::cout << "--- Switch Test End ---" << std::endl; @end
    return 0;
}