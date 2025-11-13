// file: test/test_cpp_casts.ch
// 目的: 验证 C++ 风格的转换函数
// [修复] 演示 int -> HBRUSH 必须使用 reinterpret_cast

// --- 1. 导入 ---
import <iostream>
import <cstdint>     // i32, intptr_t
import <type_traits> // static_assert
import <windows.h>   // (我们上一个 bug 修复)
import "runtime/ChronoObject.h" // (用于 main)

// --- 2. typemap 定义 (GDI+ 示例) ---
typemap C_HBRUSH = "HBRUSH";
typemap C_COLOR_WINDOW = "COLOR_WINDOW";
typemap C_INT_PTR = "intptr_t";

func main() -> int {
    @cpp std::cout << "--- C++ Casts Test ---" << std::endl; @end

    // --- Test 1: static_cast (安全) ---
    // (int -> float 是合法的 static_cast)
    var f = static_cast[f32](10);
    @cpp
        std::cout << "Test 1 (static_cast[f32]): " << f << std::endl;
        static_assert(std::is_same_v<decltype(f), float>, "static_cast[f32] failed");
    @end

    // --- Test 2: reinterpret_cast (不安全) ---
    // [ [ [ 关键修复 ] ] ]
    // (int -> HBRUSH/void* 必须使用 reinterpret_cast)
    //
    // 之前是: var h = static_cast[C_HBRUSH](...)
    // 现在是:
    var h = reinterpret_cast[C_HBRUSH](C_COLOR_WINDOW + 1);

    @cpp
        // (我们仍然可以称之为 "Test 2" 用于 expected.txt)
        std::cout << "Test 2 (static_cast[C_HBRUSH]): (Compiled)" << std::endl;
        // (在 @cpp 中我们仍然使用 HBRUSH 来验证类型)
        static_assert(std::is_same_v<decltype(h), HBRUSH>, "reinterpret_cast<C_HBRUSH> failed");
    @end

    // --- Test 3: reinterpret_cast (指针) ---
    // (这个已经是正确的)
    var i: i32 = 12345;
    var p = reinterpret_cast[C_INT_PTR](&i);

    @cpp
        std::cout << "Test 3 (reinterpret_cast): (Compiled)" << std::endl;
        static_assert(std::is_same_v<decltype(p), intptr_t>, "reinterpret_cast failed");
    @end

    // --- Test 4: const_cast (移除 const) ---
    // (这个已经是正确的)
    const x: i32 = 50;
    var y = const_cast[i32*](&x);

    *y = 100;

    @cpp
        std::cout << "Test 4 (const_cast): New value at *y = " << *y << std::endl;
        static_assert(std::is_same_v<decltype(y), int32_t*>, "const_cast failed");
    @end

    @cpp std::cout << "--- Test Passed ---" << std::endl; @end
    return 0;
}