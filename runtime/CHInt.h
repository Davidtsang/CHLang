//CHInt.h
#pragma once
#include "CHObject.h"

// (CHInt 不需要包含 CHString，所以它更简单)

class CHInt : public CHObject {
private:
    int32_t m_value;
    explicit CHInt(int32_t val) : m_value(val) {}

public:
    // [已修正] 工厂方法返回一个原始指针
    static CHInt* create(int32_t val) {
        return new CHInt(val);
    }

    int32_t getValue() const {
        return m_value;
    }

    std::string description() const override {
        return std::to_string(m_value);
    }

    // [新增] 实现 Print 虚函数
    void printValue() override {
        std::cout << m_value << std::endl;
    }
};

using Int = CHInt;