// file: test/test_data_types.ch
// 目的: 验证所有新的基本数据类型、字面量和 C++ 交互

// 1. 导入 @cpp 块所需的原生 C++ 头文件
import <iostream>
import <string>
import <cstdint> // <-- [关键] 确保 (u)int8_t 可用于 @cpp

// 2. 导入 CH 运行时 (为了 main)
import "runtime/CHObject.h"
import "runtime/CH.h" // (虽然不用 print, 但导入是好习惯)

func main() -> int {

    @cpp
        std::cout << "--- Data Types Test Start ---" << std::endl;
    @end

    // [测试 1: 声明所有整数类型]
    // 翻译器 应将它们映射到 <cstdint>
    var i8_val: i8 = -8;
    var u8_val: u8 = 8;
    var i16_val: i16 = -1616;
    var u16_val: u16 = 1616;
    var i32_val: i32 = -3232;
    var u32_val: u32 = 3232;
    var i64_val: i64 = -6464;
    var u64_val: u64 = 6464;

    @cpp
        std::cout << "Test 1: Integer Declarations" << std::endl;
        // [注意] 必须 (int) 转换 i8/u8 才能打印为数字, 否则 std::cout 会打印 ASCII 字符
        std::cout << "  i8: " << (int)i8_val << std::endl;
        std::cout << "  u8: " << (int)u8_val << std::endl;
        std::cout << "  i16: " << i16_val << std::endl;
        std::cout << "  u16: " << u16_val << std::endl;
        std::cout << "  i32: " << i32_val << std::endl;
        std::cout << "  u32: " << u32_val << std::endl;
        std::cout << "  i64: " << i64_val << std::endl;
        std::cout << "  u64: " << u64_val << std::endl;
    @end

    // [测试 2: 声明所有浮点类型]
    // 翻译器 应将它们映射到 float/double
    var f32_val: f32 = 3.14;
    var f64_val: f64 = 1.6180339887;

    @cpp
        std::cout << "Test 2: Float Declarations" << std::endl;
        std::cout << "  f32: " << f32_val << std::endl;
        std::cout << "  f64: " << f64_val << std::endl;
    @end

    // [测试 3: 验证所有数字字面量]
    // 翻译器 应原样传递它们
    var dec_val: i32 = 42;
    var hex_val: i32 = 0x2A;    // 42
    var bin_val: i32 = 0b101010; // 42
    var oct_val: i32 = 0o52;    // 42

    // [测试 4: 验证 Byte 和 Char 字面量]
    // 翻译器 应将 b'A' 翻译为 (uint8_t)'A'
    var byte_val: u8 = b'A'; // 65
    var char_val: i8 = 'C'; // 67 (i8 或 u8 都可以)

    @cpp
        std::cout << "Test 3: Numeric Literals" << std::endl;
        std::cout << "  Decimal (42): " << dec_val << std::endl;
        std::cout << "  Hex (42): " << hex_val << std::endl;
        std::cout << "  Binary (42): " << bin_val << std::endl;
        std::cout << "  Octal (42): " << oct_val << std::endl;

        std::cout << "Test 4: Byte & Char Literals" << std::endl;
        std::cout << "  Byte (b'A' -> 65): " << (int)byte_val << std::endl;
        std::cout << "  Char ('C' -> 67): " << (int)char_val << std::endl;
    @end

    @cpp
        std::cout << "--- Data Types Test End ---" << std::endl;
    @end

    return 0;
}