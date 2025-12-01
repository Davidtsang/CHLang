// test/test_codegen.ch
import "runtime/CH.h"
import <iostream>

// 1. 调用代码生成器
// 编译器会去 test/generators/ 找 MagicGen.py
// 并把它返回的 C++ 代码 (get_magic_number 函数) 插入到这里
@codegen("MagicGen");

func main() -> int {
    CH::Log("--- Codegen Test ---");

    // 2. 调用生成的 C++ 函数
    // 注意：这个函数在 CH 源码里没定义，是插件生成的，但 C++ 编译器能看到它
    var num: int = get_magic_number();

    CH::Log("Magic Number is:");
    CH::Log(num);

    return 0;
}