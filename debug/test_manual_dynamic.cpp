// test_manual_dynamic.cpp
// 编译命令: cl /std:c++17 /EHsc /Iruntime test_manual_dynamic.cpp

#include <iostream>
#include <string>
#include "runtime/CHObject.h"

// --- 模拟用户定义的类 ---
class Person : public CHObject {
public:
    // 普通的 C++ 方法
    void sayHello(std::string name) {
        std::cout << "Hello, " << name << "! (Static Call Executed)" << std::endl;
    }

    void add(int a, int b) {
        std::cout << a << " + " << b << " = " << (a + b) << std::endl;
    }

    // --- 模拟 @dynamic 自动生成的胶水代码 ---
    // 未来这段代码由 CHVisitor 自动生成
    virtual MethodTrampoline findMethodImpl(SelectorID sel) override {

        // 映射 1: "sayHello"
        if (sel == _SEL("sayHello")) {
            return [](void* inst, ArgsList& args) -> AnyVar {
                // 1. 恢复 this 指针
                Person* self = static_cast<Person*>(inst);
                // 2. 解包参数 (Unboxing)
                std::string arg0 = std::any_cast<std::string>(args[0]);
                // 3. 调用
                self->sayHello(arg0);
                return {};
            };
        }

        // 映射 2: "add"
        if (sel == _SEL("add")) {
            return [](void* inst, ArgsList& args) -> AnyVar {
                Person* self = static_cast<Person*>(inst);
                int arg0 = std::any_cast<int>(args[0]);
                int arg1 = std::any_cast<int>(args[1]);
                self->add(arg0, arg1);
                return {};
            };
        }

        // 默认查父类
        return CHObject::findMethodImpl(sel);
    }
};

int main() {
    std::cout << "--- Manual Dynamic Dispatch Test ---" << std::endl;

    // 1. 创建对象
    Person* p = new Person();

    // 2. 转换为动态类型 (dyn)
    dyn d = p;

    // 3. 模拟 d~>sayHello("CH")
    std::cout << "[1] Testing sayHello..." << std::endl;
    {
        ArgsList args;
        args.push_back(std::string("CH")); // 装箱

        // 发送消息
        d->msgSend(_SEL("sayHello"), args);
    }

    // 4. 模拟 d~>add(10, 20)
    std::cout << "[2] Testing add..." << std::endl;
    {
        ArgsList args;
        args.push_back(10);
        args.push_back(20);

        d->msgSend(_SEL("add"), args);
    }

    // 5. 模拟调用不存在的方法
    std::cout << "[3] Testing invalid selector..." << std::endl;
    {
        ArgsList args;
        d->msgSend(_SEL("flyToMoon"), args); // 应该报错但不会崩溃
    }

    delete p;
    return 0;
}