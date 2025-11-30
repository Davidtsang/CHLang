#pragma once
#include <string>
#include <cstdint>
#include <string_view>
#include "CHSelector.h" // 包含 _CalcHash 宏

class Reflection {
public:
    // 静态内联函数，无需 cpp 文件
    static uint64_t getSelector(const std::string& name) {
        // 直接调用核心宏
        return _CalcHash(name);
    }
};