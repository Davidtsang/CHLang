// file: test/test_namespace_import.ch
// 目的: 验证 'import as' 和 C++ 原生打印

import "runtime/ChronoObject.h";
import <iostream>; // [新增] 导入 C++ 原生打印

// [测试 1: 自动别名]
import "lib/MyMath.h";

// [测试 2: 自定义别名]
import "lib/MyMath.h" as Math;

func main() -> Int {

    // [修改] 使用 @cpp 块
    @cpp
        std::cout << "--- Namespace Import Test ---" << std::endl;
    @end

    // [测试 1 调用]
    // 预期翻译: MyMath::add(10, 5)
    let x: i32 = MyMath.add(10, 5);

    // [修改] 使用 @cpp 块打印 i32 变量 'x'
    @cpp
        std::cout << "Test 1 (Auto Alias) Result:" << std::endl;
        std::cout << x << std::endl; // 预期: 15
    @end

    // [测试 2 调用]
    // 预期翻译: Math::multiply(x, 2)
    let y: i32 = Math.multiply(x, 2);

    // [修改] 使用 @cpp 块打印 i32 变量 'y'
    @cpp
        std::cout << "Test 2 (Custom 'as') Result:" << std::endl;
        std::cout << y << std::endl; // 预期: 30
    @end

    return 0;
}