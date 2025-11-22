#pragma once

#include <string>
#include <iostream>
#include <cstdint>
#include <vector>
#include <any>        // [修复] 必须包含，用于 std::any
#include <functional> // [修复] 必须包含，用于 std::function

// [修复] 引入 Selector 定义
// 如果编译器报错找不到这个文件，请确保编译命令里加了 /I.
#include "ChronoSelector.h"

// [定义] 动态类型别名
class ChronoObject;
using dyn = ChronoObject*;
using AnyVar = std::any;
using ArgsList = std::vector<AnyVar>;

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


    using MethodTrampoline = std::function<AnyVar(void* instance, ArgsList& args)>;

    // 2. 消息发送入口 (objc_msgSend)
    // 所有的 obj~>method(...) 最终都会调用这里
    virtual AnyVar msgSend(SelectorID sel, ArgsList args) {
        // 查找
        MethodTrampoline method = this->findMethodImpl(sel);

        if (method) {
            try {
                // 调用
                return method(this, args);
            } catch (const std::bad_any_cast& e) {
                std::cerr << "[ChronoRuntime] Type mismatch: " << e.what() << std::endl;
            }
        } else {
            // 没找到
            // 这里可以打印出 sel 的整数 ID，虽然不可读，但在调试器里能看
            std::cerr << "[ChronoRuntime] Selector ID " << sel << " not recognized." << std::endl;
        }
        return {};
    }

    // 3. 查找表 (由 @dynamic 自动生成的代码覆盖)
    virtual MethodTrampoline findMethodImpl(SelectorID sel) {
        return nullptr; // 基类没有任何动态方法
    }

    // --- 辅助方法 ---
    // [新增] 纯虚函数，强制所有子类实现
    virtual void printValue() {
        std::cout << "[ChronoObject <" << typeid(*this).name()
                  << "> at: " << static_cast<void*>(this) << "]" << std::endl;
    }
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

// [ 新增 ] 打印 bool 类型
inline void Print(bool value) {
    std::cout << (value ? "true" : "false") << std::endl;
}

