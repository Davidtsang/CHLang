// file: test/test_inline.ch
import <iostream>
import "runtime/CHObject.h"

// --- 场景 1: 全局 Inline 变量 ---
// 预期 C++: inline int32_t g_inlineVal = 100;
// 这允许在头文件中定义全局变量而不会报重复定义错误
inline var g_inlineVal: i32 = 100;

// --- 场景 2: 全局 Inline 函数 ---
// 预期 C++: inline int32_t add_inline(int32_t a, int32_t b) { ... }
inline func add_inline(a: i32, b: i32) -> i32 {
    return a + b;
}

// --- 场景 3: 类/结构体 静态 Inline 成员 (C++17 特性) ---
struct AppConfig {
    // 预期 C++: static inline int32_t MaxConnections = 50;
    // 这允许直接在类声明中初始化静态成员
    public static inline var MaxConnections: i32 = 50;

    // 预期 C++: static inline const float Version = 1.5f;
    public static inline const Version: f32 = 1.5;
}

implement AppConfig {
    // 不需要在这里初始化，因为已经 inline 初始化了
}

func main() -> int {
    @cpp std::cout << "--- Inline Keyword Test ---" << std::endl; @end

    // 1. 测试全局变量
    @cpp std::cout << "1. Global Inline Var: " << g_inlineVal << std::endl; @end

    // 2. 测试全局函数
    var sum = add_inline(10, 20);
    @cpp std::cout << "2. Global Inline Func: " << sum << std::endl; @end

    // 3. 测试静态成员
    // 直接通过类名访问，证明它们被正确初始化了
    @cpp
    std::cout << "3. Static Inline Member: " << AppConfig::MaxConnections << std::endl;
    std::cout << "4. Static Inline Const: " << AppConfig::Version << std::endl;
    @end

    return 0;
}