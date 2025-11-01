//ChronoObject.h
#pragma once

#include <string>
#include <iostream>
#include <cstdint> // 用于 int32_t 等

// --- [ 1. MRC 基类 ] ---
// 
// 所有 Chrono 引用类型都继承自它
// 它实现了手动引用计数 (MRC)
//
class ChronoObject {
protected:
    // 引用计数器
    unsigned int m_retainCount;

public:
    // 'init': C++ 构造函数
    // 对象被创建时，引用计数 *必须* 为 1
    ChronoObject() : m_retainCount(1) {
        // (用于调试)
        // std::cout << "DEBUG: " << this << " INIT (RC=1)" << std::endl;
    }

    // 'deinit': C++ 析构函数
    // 这 *只* 应该在 'release()' 内部的 'delete this' 被调用时触发
    virtual ~ChronoObject() {
        // (用于调试)
        // std::cout << "DEBUG: " << this << " DEINIT" << std::endl;
    }

    // --- MRC 核心方法 ---

    // 'retain': 手动增加引用计数
    virtual ChronoObject* retain() {
        this->m_retainCount++;
        // std::cout << "DEBUG: " << this << " RETAIN (RC=" << m_retainCount << ")" << std::endl;
        return this; // 允许链式调用 [obj retain]
    }

    // 'release': 手动减少引用计数
    virtual void release() {
        // std::cout << "DEBUG: " << this << " RELEASE (RC=" << m_retainCount - 1 << ")" << std::endl;
        
        // 当引用计数降为 0 时，销毁对象
        if (--(this->m_retainCount) == 0) {
            // 这将触发调用析构函数 (~ChronoObject)
            delete this;
        }
    }

    // --- 辅助方法 ---
    
    // description() 用于 Print()
    virtual std::string description() const {
        return "<ChronoObject instance>";
    }
};


// --- [ 2. 'id' 类型 ] ---
//
// 'id' 现在是一个指向基类的 C++ 原始指针
using id = ChronoObject*;


// --- [ 3. Print() 函数 (重载) ] ---

// A. 打印 Chrono 对象 (id)
inline void Print(const id& obj) {
    if (obj != nullptr) {
        std::cout << obj->description() << std::endl;
    } else {
        std::cout << "(null)" << std::endl;
    }
}

// B. 打印 C++ 原生值类型
inline void Print(int32_t value) {
    std::cout << value << std::endl;
}
inline void Print(int64_t value) {
    std::cout << value << std::endl;
}
inline void Print(const char* value) {
     std::cout << value << std::endl;
}

// #pragma once

// #include <memory>     // 用于 std::shared_ptr (我们的 ARC 实现)
// #include <string>       // 用于 std::string
// #include <iostream>   // 用于 std::cout (Print 函数使用)

// // 1. ARC 类型别名：
// // Ref<T> 是 Chrono 语言中所有对象的标准持有方式
// template <typename T>
// using Ref = std::shared_ptr<T>;

// // 2. 'id' 类型：
// // 类似于 Objective-C 的 'id'，一个指向任何 Chrono 对象的引用
// using id = Ref<class ChronoObject>;

// // 3. Chrono 基类 (类似于 NSObject)
// // 所有 Chrono 类都必须继承自它
// class ChronoObject : public std::enable_shared_from_this<ChronoObject> {
// public:
//     // 虚析构函数对于基类至关重要
//     virtual ~ChronoObject() = default;

//     // 虚方法 'description'，用于 Print() 函数
//     virtual std::string description() const {
//         return "<ChronoObject instance>";
//     }
// };

// // 4. 全局 Print() 函数
// // 这是 Chrono 中 'print(obj)' 翻译后的目标 C++ 函数
// inline void Print(const id& obj) {
//     if (obj) {
//         // 多态调用 obj->description()
//         std::cout << obj->description() << std::endl;
//     } else {
//         // 优雅地处理 'nil' (nullptr)
//         std::cout << "(null)" << std::endl;
//     }
// }