// file: test/test_compound_assignment.ch
// 目的: 验证复合赋值运算符 (+=, -=, *=, /=, %=)
// [修改] 移除 Chrono.log，使用原生 @cpp std::cout

import <iostream> // <-- [新增] 导入 C++ IO
import "runtime/ChronoObject.h"
// [移除] 不再需要 import "runtime/Chrono.h"

func main() -> int {
    @cpp std::cout << "--- Compound Assignment Test ---" << std::endl; @end

    var x: i32 = 100;
    @cpp std::cout << "Start:" << std::endl; @end
    @cpp std::cout << x << std::endl; @end // 100

    // --- 测试 1: += ---
    x += 10;
    @cpp std::cout << "After += 10:" << std::endl; @end
    @cpp std::cout << x << std::endl; @end // 110

    // --- 测试 2: -= ---
    x -= 20;
    @cpp std::cout << "After -= 20:" << std::endl; @end
    @cpp std::cout << x << std::endl; @end // 90

    // --- 测试 3: *= ---
    x *= 2;
    @cpp std::cout << "After *= 2:" << std::endl; @end
    @cpp std::cout << x << std::endl; @end // 180

    // --- 测试 4: /= ---
    x /= 4;
    @cpp std::cout << "After /= 4:" << std::endl; @end
    @cpp std::cout << x << std::endl; @end // 45

    // --- 测试 5: %= ---
    x %= 40;
    @cpp std::cout << "After %= 40:" << std::endl; @end
    @cpp std::cout << x << std::endl; @end // 5

    // --- 测试 6: 在 'for' 循环中使用 (i += 2) ---
    // (这验证了 assignment_no_semicolon 规则)
    @cpp std::cout << "Test For-Loop (i += 2):" << std::endl; @end

    for (var i: i32 = 0; i < 5; i += 2) {
        // [修改] @cpp 块在 for 循环的 Chrono 作用域内
        @cpp std::cout << i << std::endl; @end
    }
    // 预期: 0, 2, 4

    @cpp std::cout << "--- Test End ---" << std::endl; @end
    return 0;
}