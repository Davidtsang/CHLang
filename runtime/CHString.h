 //CHString.h
#pragma once
#include "CHObject.h"
// #include "CHInt.h" // <-- 循环依赖！我们不能在这里包含 CHInt.h
                         // 我们必须使用 "前向声明"

// --- [ 关键修正 ] ---
// 前向声明 (Forward Declaration)
// 我们告诉 C++ "CHInt 这个类存在"，
// 但我们不在这个头文件中包含它的全部定义。
// 这可以防止 A.h 包含 B.h，同时 B.h 包含 A.h 的循环依赖错误。
class CHInt;
// --- [ 修正结束 ] ---


class CHString : public CHObject {
private:
    std::string m_value;
    explicit CHString(const std::string& str) : m_value(str) {}

public:
    // [已修正] 工厂方法返回一个原始指针
    static CHString* create(const std::string& str) {
        return new CHString(str);
    }

    // [已修正] 所有方法现在都返回原始指针
    CHInt* length() const; // <--- 修正
    
    CHString* toUpper() const; // <--- 修正

    std::string description() const override {
        return m_value;
    }
    
    std::string& getValue() { return m_value; }

    // [新增] 实现 Print 虚函数
    void printValue() override {
        std::cout << m_value << std::endl;
    }
};

using String = CHString;
