// file: test/test_arrays.ch
// 目的: 验证新的 Rust 风格数组语法 [char; 20]
// [已修改] 移除 Chrono.h 依赖，所有 'print' 替换为原生 '@cpp'

// 1. 导入 @cpp 块所需的原生 C++ 头文件
import <iostream>;
import <string>;
import <cstdint>;

// 2. 导入 Chrono 运行时 (仅为 ChronoObject，如果需要的话)
import "runtime/ChronoObject.h";
// import "runtime/Chrono.h"; // <-- 不再需要

// [修改] main 必须返回 'int' (C++ 原生类型)
func main() -> int {

    @cpp
        std::cout << "--- Array Syntax Test Start ---" << std::endl;
    @end

    // [测试 1: 声明和聚合初始化]
    // 预期翻译: int32_t numbers[5] = {10, 20, 30, 40, 50};
    var numbers: [i32; 5] = {10, 20, 30, 40, 50};

    @cpp
        std::cout << "Test 1: Array declared with size 5." << std::endl;
    @end

    // [测试 2: 数组索引 (读取)]
    // 预期翻译: numbers[2];
    @cpp
        std::cout << "Test 2: Accessing index [2]:" << std::endl;
        std::cout << numbers[2] << std::endl; // 预期: 30
    @end

    // [测试 3: 数组索引 (写入)]
    // 预期翻译: numbers[3] = 42;
    numbers[3] = 42;
    @cpp
        std::cout << "Test 3: Assigning index [3] = 42:" << std::endl;
        std::cout << numbers[3] << std::endl; // 预期: 42
    @end

    // [测试 4: 变量作为数组大小]
    var size: i32 = 3;
    // 预期翻译: std::string names[size] = {"Alice", "Bob", "Charlie"};
    var names: [std.string; 3] = {"Alice", "Bob", "Charlie"};

    @cpp
        std::cout << "Test 4: Variable size [size=3]." << std::endl;
        std::cout << "  names[0]: " << names[0] << std::endl; // 预期: Alice
        std::cout << "  names[2]: " << names[2] << std::endl; // 预期: Charlie
    @end

    @cpp
        std::cout << "--- Array Syntax Test End ---" << std::endl;
    @end

    return 0;
}