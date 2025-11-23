#pragma once
#include <string_view>
#include <cstdint>

// 定义选择子 ID 类型
using SelectorID = size_t;

// FNV-1a Hash 算法 (constexpr 支持编译期计算)
constexpr SelectorID _CalcHash(std::string_view str) {
    SelectorID hash = 14695981039346656037ULL;
    for (char c : str) {
        hash ^= static_cast<SelectorID>(c);
        hash *= 1099511628211ULL;
    }
    return hash;
}

// 宏：用户/编译器使用的入口
// 用法: _SEL("setText") -> 编译成一个整数常量
#define _SEL(str) _CalcHash(str)