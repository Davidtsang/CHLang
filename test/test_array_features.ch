// file: test/test_array_features.ch
// 目的: 对数组语法进行压力测试 (类成员, 函数参数)
// [已修复] - 修正了 @cpp 块内部的 C++ 语法 (this->data -> this->data)

import <iostream>
import <cstdint>
import "runtime/CHObject.h"

// ---
// 场景 1: 数组作为函数参数
// ---
func printSum(arr: [i32; 3]) {
    var sum: i32 = arr[0] + arr[1] + arr[2];

    std::cout << "  Func Param Sum: " << sum << std::endl;

}

// ---
// 场景 2: 数组作为类成员
// ---
class ArrayTester : CHObject {

    var data: [i32; 3];
    var matrix: [[i32; 2]; 2];

    public init();

    public func printMemberData() ;

    public func testParamPassing();
}

implement ArrayTester{
    init() {
        std::cout << "ArrayTester Init" << std::endl; 

        // (由 Visitor 正确翻译为 this->data)
        this->data[0] = 10;
        this->data[1] = 20;
        this->data[2] = 30;
        this->matrix[0][0] = 1;
        this->matrix[1][1] = 99;
    }

    func printMemberData() {
        @cpp
            std::cout << "Test 2 (Class Member Access):" << std::endl;
            // [ [ 关键修复 ] ]
            // 在 C++ 中, 'this' 是一个指针, 必须使用 '->'
            std::cout << "  this->data[1]: " <<  this->data[1]  << std::endl; // 预期: 20
            std::cout << "  this->matrix[1][1]: " <<  this->matrix[1][1] << std::endl; // 预期: 99
        @end
    }

    func testParamPassing() {
        std::cout << "Test 3 (Passing 'this->data' to func):" << std::endl; 
        // (由 Visitor 正确翻译为 printSum(this->data))
        printSum(this->data);
    }

}
// ---
// 主函数
// ---
func main() -> int {
    std::cout << "--- Array Features Test Start ---" << std::endl; 

    // --- Test 1: 局部数组 (复习) ---
    var localArr: [i32; 3] = {1, 2, 3};
    std::cout << "Test 1 (Local Array Param):" << std::endl; 
    printSum(localArr);

    // --- Test 2 & 3: 类实例 ---
    var tester: ArrayTester* = new ArrayTester();
    tester->printMemberData();
    tester->testParamPassing();
    tester->release();

    std::cout << "--- Array Features Test End ---" << std::endl; 
    return 0;
}