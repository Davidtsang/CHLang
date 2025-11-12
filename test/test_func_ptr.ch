// file: test/test_func_ptr.ch
// 目的: 验证函数指针语法 (最终方案)
// 方案:
// 1. (T...) -> R   => std::function<R(T...)>
// 2. ((T...) -> R)* => C-Style 指针 R (*p)(T...)

import <iostream>;
import <functional>;
import <cstdint>;
import <string>;
import "runtime/ChronoObject.h";

@cpp
// 目标 C++ 函数
int32_t global_add_func(int32_t a, int32_t b) {
    std::cout << "  [C++] global_add_func called." << std::endl;
    return a + b;
}
@end

func main() -> int {
    @cpp std::cout << "--- Function Pointer Test Start ---" << std::endl; @end

    // --- Test 1: 现代 std::function ---
    @cpp std::cout << "Test 1: Modern std::function (i32, i32) -> i32" << std::endl; @end

    // 语法: (i32, i32) -> i32
    // 预期: std::function<int32_t(int32_t, int32_t)> modernFunc;
    var modernFunc: (i32, i32) -> i32;

    modernFunc = global_add_func; // 赋值
    var resultA: i32 = modernFunc(10, 5); // 调用

    @cpp std::cout << "  Result A: " << resultA << std::endl; @end
    // 预期: Result A: 15

    // --- Test 2: C-Style 原始指针 ---
    @cpp std::cout << "Test 2: Raw C-Style Pointer ((i32, i32) -> i32)*" << std::endl; @end

    // 语法: ((i32, i32) -> i32)*
    // 预期: int32_t (*rawPtr)(int32_t, int32_t) = nullptr;
    var rawPtr: ((i32, i32) -> i32)*;

    rawPtr = global_add_func; // 赋值
    var resultB: i32 = rawPtr(20, 5); // 调用

    @cpp std::cout << "  Result B: " << resultB << std::endl; @end
    // 预期: Result B: 25

    // --- Test 3: C-Style Null 验证 ---
    @cpp std::cout << "Test 3: Raw C-Style Pointer Null Init" << std::endl; @end

    // 语法: (() -> void)*
    // 预期: void (*nullPtr)() = nullptr;
    var nullPtr: (() -> void)*;

    @cpp
        if (nullPtr == nullptr) {
            std::cout << "  PASS: Raw pointer correctly initialized to null." << std::endl;
        } else {
            std::cout << "  FAIL: Raw pointer was not null." << std::endl;
        }
    @end
    // 预期:   PASS: Raw pointer correctly initialized to null.

    @cpp std::cout << "--- Function Pointer Test End ---" << std::endl; @end
    return 0;
}