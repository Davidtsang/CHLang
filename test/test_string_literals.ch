// file: test/test_string_literals.ch
// 目的: 验证所有 C++ 字符串字面量前缀
// L"..." (Wide), u8"..." (UTF-8), u"..." (UTF-16), U"..." (UTF-32)

// --- 1. 导入 (用于 C++ 类型检查和打印) ---
import <iostream>
import <string>
import <type_traits> // [关键] 用于 static_assert 和 std::is_same_v
import <cwchar>      // [关键] 用于 C++ 打印 L"..." (std::wcout)
import <cuchar>      // [关键] 用于 char16_t, char32_t
import "runtime/CHObject.h" // (用于 main)

func main() -> int {

    @cpp std::cout << "--- C++ String Literals Test ---" << std::endl; @end

    // --- Test 1: L"..." (Wide String) ---
    // 预期: auto wide_str = L"Hello Wide";
    var wide_str = L"Hello Wide";

    // --- Test 2: u8"..." (UTF-8 String) ---
    // 预期: auto utf8_str = u8"Hello UTF-8";
    var utf8_str = u8"Hello UTF-8";

    // --- Test 3: u"..." (UTF-16 String) ---
    // 预期: auto utf16_str = u"Hello UTF-16";
    var utf16_str = u"Hello UTF-16";

    // --- Test 4: U"..." (UTF-32 String) ---
    // 预期: auto utf32_str = U"Hello UTF-32";
    var utf32_str = U"Hello UTF-32";

    // --- Test 5: "..." (Standard ANSI/UTF-8 String) ---
    // 预期: auto std_str = "Hello Standard";
    var std_str = "Hello Standard";

    // --- 验证 (在 @cpp 中) ---
    @cpp
        // 1. 打印 (我们可以打印的)
        // L"..." 必须使用 std::wcout
        std::wcout << L"Test 1 (L\"...\"): " << wide_str << std::endl;

        // "..." 和 u8"..." (在 C++17 中) 都是 const char*
        std::cout << "Test 2 (u8\"...\"): " << utf8_str << std::endl;
        std::cout << "Test 5 (\"...\"): " << std_str << std::endl;

        // (u"..." 和 U"..." 打印起来很复杂, 我们跳过打印)
        std::cout << "Test 3/4 (u\"...\"/U\"...\"): Types asserted at compile time." << std::endl;

        // 2. [ [ 核心测试 ] ]
        // 使用 static_assert 在编译时验证类型。
        // 如果翻译器错误，*编译将会失败*。

        // Test 1: L"..." -> const wchar_t*
        static_assert(std::is_same_v<decltype(wide_str), const wchar_t*>, "L\"...\" failed");

        // Test 2: u8"..." -> const char* (在 /std:c++17 模式下)
        static_assert(std::is_same_v<decltype(utf8_str), const char*>, "u8\"...\" failed");

        // Test 3: u"..." -> const char16_t*
        static_assert(std::is_same_v<decltype(utf16_str), const char16_t*>, "u\"...\" failed");

        // Test 4: U"..." -> const char32_t*
        static_assert(std::is_same_v<decltype(utf32_str), const char32_t*>, "U\"...\" failed");

        // Test 5: "..." -> const char*
        static_assert(std::is_same_v<decltype(std_str), const char*>, "\"...\" failed");

    @end

    @cpp std::cout << "--- Test Passed ---" << std::endl; @end
    return 0;
}