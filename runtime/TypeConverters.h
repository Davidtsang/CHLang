#pragma once
#include <string>
#include <iostream>
#include <vector>

namespace CH {

    // 1. 基础模板 (默认实现：如果未特化，编译期报错或安全跳过)
    template <typename T>
    struct Converter {
        // SFINAE 标记：默认没有实现
        static constexpr bool is_implemented = false;

        static T fromString(const std::string& val) {
            // 这里的代码永远不应该被运行，因为会被 if constexpr 保护
            return T();
        }
    };

    // 2. 基础类型特化 (int)
    template <>
    struct Converter<int32_t> {
        static constexpr bool is_implemented = true;
        static int32_t fromString(const std::string& val) {
            try { return std::stoi(val); } catch(...) { return 0; }
        }
    };

    // 3. 基础类型特化 (float)
    template <>
    struct Converter<float> {
        static constexpr bool is_implemented = true;
        static float fromString(const std::string& val) {
            try { return std::stof(val); } catch(...) { return 0.0f; }
        }
    };

    // 4. 基础类型特化 (string)
    template <>
    struct Converter<std::string> {
        static constexpr bool is_implemented = true;
        static std::string fromString(const std::string& val) {
            return val;
        }
    };

    // ... 你可以在这里添加更多基础类型 (bool, double 等)
}