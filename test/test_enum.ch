// file: test/test_enum.ch
// 目的: 验证 enum 和 enum class 语法

import <iostream>
import <cstdint>
import "runtime/ChronoObject.h" // [新增] 导入基类

// 1. 传统枚举 (Unscoped)
enum Color {
    Red,
    Green,
    Blue
}

// 2. 强类型枚举 (Scoped) + 指定底层类型 + 显式赋值
enum class State : u8 {
    Idle = 0,
    Running = 1,
    Error = 0xFF // 测试 u8 (255)
}

// 3. 类定义 (只包含声明)
class Machine : ChronoObject{
    // 类内部定义枚举 (允许)
    public enum class Mode {
        Auto,
        Manual
    }

    public var currentMode: Mode;

    // [修复] 这里只能写声明，以分号结尾
    public init();
}

// 4. 类实现 (包含代码体)
implement Machine {
    init() {
        // [修复] 使用显式访问器 ->
        // 访问内部枚举最好带上类作用域，或者因为在成员函数内，直接用 Mode::Auto 也可以
        // 为了演示 C++ 兼容性，我们写全
        this->currentMode = Machine::Mode::Auto;
    }
}

func main() -> int {
    std::cout << "--- Enum Test ---" << std::endl;

    // 测试 1: Unscoped (可以直接访问成员)
    var c: Color = Red;
    c = Green; // 也可以省略 Color::，因为是 Unscoped

    if (c == Green) {
        std::cout << "Color is Green" << std::endl;
    }

    // 测试 2: Scoped (必须使用 ::)
    var s: State = State::Error;

    if (s == State::Error) {
        std::cout << "State is Error" << std::endl;
    }

    // 测试 3: Class Nested
    // new 返回指针，所以 m 是 Machine*
    var m = new Machine();

    // 验证是否初始化正确 (m 是指针，使用 -> 访问成员)
    // Machine::Mode::Auto 是枚举值
    if (m->currentMode == Machine::Mode::Auto) {
        std::cout << "Machine Mode is Auto" << std::endl;
    }

    // 释放内存
    m->release();

    std::cout << "Enum Test Finished." << std::endl;
    return 0;
}