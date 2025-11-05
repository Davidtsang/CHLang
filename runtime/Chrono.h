// runtime/Chrono.h
#pragma once
#include <iostream>
#include <stdint.h>     // 用于 int32_t
#include <type_traits>  // 用于 C++17 的 'if constexpr'
#include "ChronoObject.h" // 必须包含，用于 is_base_of

// [关键] 我们将所有日志功能封装在 'Chrono' 命名空间中
namespace Chrono {

    // --- 1. 针对已知“值类型”的函数重载 ---
    inline void log(int32_t val) {
        std::cout << val << std::endl;
    }

    inline void log(bool val) {
        std::cout << (val ? "true" : "false") << std::endl;
    }

    inline void log(const char* s) {
        std::cout << s << std::endl;
    }

    // --- 2. 针对“指针类型”的模板 ---
    template <typename T>
    void log(T* ptr) {
        if (ptr == nullptr) {
            std::cout << "(null)" << std::endl;
            return;
        }

        // [ 关键 ] C++17 的 'if constexpr'
        // 这是一个编译时 if 语句，用于智能区分类型

        // 检查 T 是否继承自 ChronoObject
        if constexpr (std::is_base_of<ChronoObject, T>::value) {

            // 场景 A: 它是 MRC 对象 (ChronoString, MyClass, etc.)
            ptr->printValue(); // 多态调用虚函数

        } else {

            // 场景 B: 它是原生 C++ 对象 (e.g., NativeClass)
            // 我们打印它的类型名和内存地址
            std::cout << "[Native C++ Object <" << typeid(T).name()
                      << "> at: " << static_cast<void*>(ptr) << "]" << std::endl;
        }
    }

} // namespace Chrono