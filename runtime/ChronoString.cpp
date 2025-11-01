// runtime/ChronoString.cpp

// 包含它自己的头文件
#include "ChronoString.h" 

// 关键：现在我们在这里包含 ChronoInt.h
// 这为我们提供了 ChronoInt::create() 的完整定义
#include "ChronoInt.h" 

// (包含 C++ 库)
#include <string>
#include <algorithm> // for ::toupper

// --- 方法实现 ---

ChronoInt* ChronoString::length() const {
    // 现在我们可以安全地调用 ChronoInt::create()
    return ChronoInt::create(static_cast<int32_t>(m_value.length()));
}

ChronoString* ChronoString::toUpper() const {
    std::string upper_s = m_value;
    std::transform(upper_s.begin(), upper_s.end(), upper_s.begin(), ::toupper);
    return ChronoString::create(upper_s);
}