// file: test/test_bitwise_ops.ch
// 目的: 验证位运算符 (&, |, ^, ~, <<, >>)
// [已修正] 增加了括号 ( ) 来强制执行我们想要测试的优先级，
// 因为 C++ 默认的 '+' 优先级高于 '<<'。

import <iostream>;
import <cstdint>; // For int32_t
import "runtime/ChronoObject.h";

func main() -> int {
    @cpp std::cout << "--- Bitwise Ops Test ---" << std::endl; @end

    let a: i32 = 60;  // 0011 1100
    let b: i32 = 13;  // 0000 1101
    let result: i32 = 0;

    // --- 测试 1-6 (保持不变) ---
    result = a & b;
    @cpp std::cout << "Test 1: (60 & 13)" << std::endl; @end
    @cpp std::cout << result << std::endl; @end // 12

    result = a | b;
    @cpp std::cout << "Test 2: (60 | 13)" << std::endl; @end
    @cpp std::cout << result << std::endl; @end // 61

    result = a ^ b;
    @cpp std::cout << "Test 3: (60 ^ 13)" << std::endl; @end
    @cpp std::cout << result << std::endl; @end // 49

    result = ~a;
    @cpp std::cout << "Test 4: (~60)" << std::endl; @end
    @cpp std::cout << result << std::endl; @end // -61

    result = a << 2;
    @cpp std::cout << "Test 5: (60 << 2)" << std::endl; @end
    @cpp std::cout << result << std::endl; @end // 240

    result = a >> 2;
    @cpp std::cout << "Test 6: (60 >> 2)" << std::endl; @end
    @cpp std::cout << result << std::endl; @end // 15

    // --- [ 修正 测试 7 ] ---
    // 强制优先级: (a & ((a << 1) + b))
    // 60 & (120 + 13)
    // 60 & 133 = 4
    result = a & ( (a << 1) + b ); // <-- [修改]
    @cpp std::cout << "Test 7: Precedence (a & ( (a << 1) + b ))" << std::endl; @end
    @cpp std::cout << result << std::endl; @end // 4

    // --- [ 修正 测试 8 ] ---
    // 强制优先级: (((a & a) << 1) + b)
    // (60 << 1) + 13
    // 120 + 13 = 133
    result = ( (a & a) << 1 ) + b; // <-- [修改]
    @cpp std::cout << "Test 8: Precedence with ()" << std::endl; @end
    @cpp std::cout << result << std::endl; @end // 133

    @cpp std::cout << "--- Test End ---" << std::endl; @end
    return 0;
}