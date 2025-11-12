// file: test/test_using_alias.ch
// 目的: 验证 'using' 关键字是否适用于所有类型

import <iostream>;
import <functional>; // 用于 std::function
import <cstdint>;
import <string>;
import <vector>;    // 用于 std::vector
import "runtime/ChronoObject.h";

@cpp
// 目标 C++ 函数
int32_t global_add_func(int32_t a, int32_t b) {
    std::cout << "  [C++] global_add_func called." << std::endl;
    return a + b;
}
@end

// --- Test 1: 基础类型别名 ---
// 预期: using MyInt = int32_t;
using MyInt = i32;

// --- Test 2: 泛型类型别名 ---
// 预期: using StringVec = std::vector<std::string>;
using StringVec = std.vector[std.string];

// --- Test 3: std::function 别名 ---
// 预期: using AddFunc = std::function<int32_t(int32_t, int32_t)>;
using AddFunc = (i32, i32) -> i32;

// --- Test 4: C-Style 函数指针别名 (关键测试) ---
// 预期: using RawAdder = int32_t (*)(int32_t, int32_t);
using RawAdder = ((i32, i32) -> i32)*;


func main() -> int {
    @cpp std::cout << "--- Using Alias Test Start ---" << std::endl; @end

    // T1: 测试 MyInt
    @cpp std::cout << "Test 1: Simple Alias" << std::endl; @end
    var x: MyInt = 10;
    @cpp std::cout << "  MyInt x = " << x << std::endl; @end
    // 预期: 10

    // T2: 测试 StringVec
    @cpp std::cout << "Test 2: Generic Alias" << std::endl; @end
    var names: StringVec;
    @cpp names.push_back("Hello Using"); @end
    @cpp std::cout << "  names[0] = " << names[0] << std::endl; @end
    // 预期: Hello Using

    // T3: 测试 std::function 别名
    @cpp std::cout << "Test 3: std::function Alias" << std::endl; @end
    var f1: AddFunc = global_add_func;
    var resA: i32 = f1(5, 5);
    @cpp std::cout << "  AddFunc result = " << resA << std::endl; @end
    // 预期: 10

    // T4: 测试 C-Style 指针别名
    @cpp std::cout << "Test 4: C-Style Ptr Alias" << std::endl; @end
    var p1: RawAdder = global_add_func;
    var resB: i32 = p1(20, 20);
    @cpp std::cout << "  RawAdder result = " << resB << std::endl; @end
    // 预期: 40

    @cpp std::cout << "--- Using Alias Test End ---" << std::endl; @end
    return 0;
}