#pragma once
#include <stdint.h>

// 1. 定义一个 C++ 命名空间，名称必须与文件名 (MyMath) 匹配
//    以便我们的 "自动别名" 逻辑可以正确推断它
namespace MyMath {

    // 2. 定义两个我们将从 CH 调用的函数
    inline int32_t add(int32_t a, int32_t b) {
        return a + b;
    }

    inline int32_t multiply(int32_t a, int32_t b) {
        return a * b;
    }

} // namespace MyMath