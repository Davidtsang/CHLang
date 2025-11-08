// file: test/test_for_loop.ch
// 目的: 验证 C-Style for 循环的实现

import <iostream>;
import <cstdint>;
import "runtime/ChronoObject.h"; // (用于 main 函数)

func main() -> int {

    @cpp std::cout << "--- For Loop Test Start ---" << std::endl; @end

    // ---
    // 场景 1: 标准 'let' 声明循环
    // 预期: 翻译为 for (int32_t i = 0; i < 3; i = i + 1)
    // ---
    @cpp std::cout << "Test 1: Standard loop (0 to 2)" << std::endl; @end
    for (let i: i32 = 0; i < 3; i = i + 1) {
        @cpp
            std::cout << "  i = " << i << std::endl;
        @end
    }
    // 预期输出:
    //   i = 0
    //   i = 1
    //   i = 2

    // ---
    // 场景 2: 作用域测试
    // 预期: 'i' 在这里不应该存在。我们可以声明一个同名的新变量。
    // ---
    @cpp std::cout << "Test 2: Scoping (Declaring new 'i')" << std::endl; @end
    let i: i32 = 99; // 如果 'i' 仍在作用域中, C++ 编译会失败
    @cpp
        std::cout << "  New i = " << i << std::endl;
    @end
    // 预期输出:
    //   New i = 99

    // ---
    // 场景 3: 使用 'assignment' 的循环 (无 'let')
    // 预期: 翻译为 for (i = 99; i < 101; i = i + 1)
    // ---
    @cpp std::cout << "Test 3: Loop with existing variable (99 to 100)" << std::endl; @end
    // 'i' 此时是 99
    for (i = 99; i < 101; i = i + 1) {
        @cpp
            std::cout << "  i = " << i << std::endl;
        @end
    }
    // 预期输出:
    //   i = 99
    //   i = 100

    // 'i' 是在 main 作用域中声明的, 所以它会在这里保留它的值
    @cpp
        std::cout << "  After loop, i = " << i << std::endl;
    @end
    // 预期输出:
    //   After loop, i = 101

    // ---
    // 场景 4: 'while' 风格循环 (空 init 和 incr)
    // 预期: 翻译为 for ( ; i < 103; )
    // ---
    @cpp std::cout << "Test 4: Loop with empty init/incr (i=101)" << std::endl; @end
    // 'i' 此时是 101
    for ( ; i < 103; ) {
        @cpp
            std::cout << "  i = " << i << std::endl;
        @end
        i = i + 1; // 手动在循环体内递增
    }
    // 预期输出:
    //   i = 101
    //   i = 102

    @cpp std::cout << "--- For Loop Test End ---" << std::endl; @end
    return 0;
}