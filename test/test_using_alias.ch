// file: test/test_using_alias.ch
// 目的: 验证 'using' 关键字与新的 < > 泛型语法

import <iostream>
import <functional> // 用于 std::function
import <cstdint>
import <string>
import <vector>     // 用于 std::vector
import "runtime/ChronoObject.h"

// [重构] 使用 Chrono 定义全局函数 (会被翻译为标准的 C++ 函数)
func global_add_func(a: i32, b: i32) -> i32 {
     std::cout << "  [Chrono] global_add_func called." << std::endl; 
    return a + b;
}

// --- Test 1: 基础类型别名 ---
using MyInt = i32;

// --- Test 2: 泛型类型别名 ---
// [重构] 显式使用 :: 和 < >
// 预期翻译: using StringVec = std::vector<std::string>;
using StringVec = std::vector<std::string>;

// --- Test 3: std::function 别名 ---
// 预期翻译: using AddFunc = std::function<int32_t(int32_t, int32_t)>;
using AddFunc = (i32, i32) -> i32;

// --- Test 4: C-Style 函数指针别名 ---
// 预期翻译: using RawAdder = int32_t (*)(int32_t, int32_t);
using RawAdder = ((i32, i32) -> i32)*;

func main() -> int {
     std::cout << "--- Using Alias Test Start ---" << std::endl; 

    // T1: 测试 MyInt
     std::cout << "Test 1: Simple Alias" << std::endl; 
    var x: MyInt = 10;
     std::cout << "  MyInt x = " << x << std::endl; 

    // T2: 测试 StringVec
     std::cout << "Test 2: Generic Alias" << std::endl; 
    var names: StringVec;

    // [重构] 移除 ，使用原生语法
    // names 是值类型对象，使用 . 访问方法
    names.push_back("Hello Using");

    // [验证] 数组索引使用 [] (无歧义)
     std::cout << "  names[0] = " << names[0] << std::endl; 
    // 预期: Hello Using

    // T3: 测试 std::function 别名
     std::cout << "Test 3: std::function Alias" << std::endl; 
    var f1: AddFunc = global_add_func;
    var resA: i32 = f1(5, 5);
     std::cout << "  AddFunc result = " << resA << std::endl; 
    // 预期: 10

    // T4: 测试 C-Style 指针别名
     std::cout << "Test 4: C-Style Ptr Alias" << std::endl; 
    var p1: RawAdder = global_add_func;
    var resB: i32 = p1(20, 20);
     std::cout << "  RawAdder result = " << resB << std::endl; 
    // 预期: 40

     std::cout << "--- Using Alias Test End ---" << std::endl; 
    return 0;
}