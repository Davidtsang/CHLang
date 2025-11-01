#pragma once
#include "ChronoObject.h"

// (ChronoInt 不需要包含 ChronoString，所以它更简单)

class ChronoInt : public ChronoObject {
private:
    int32_t m_value;
    explicit ChronoInt(int32_t val) : m_value(val) {}

public:
    // [已修正] 工厂方法返回一个原始指针
    static ChronoInt* create(int32_t val) {
        return new ChronoInt(val);
    }

    int32_t getValue() const {
        return m_value;
    }

    std::string description() const override {
        return std::to_string(m_value);
    }
};