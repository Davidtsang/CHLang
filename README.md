# Chrono 编程语言项目 (Chrono Lang)

## 1\. 项目概述

**Chrono** 是一个创新的编程语言项目，其核心定位是 **“C++ 的现代化前端”** (The TypeScript for C++)。

它不是一个重新发明轮子的编译器，而是一个 **智能翻译器 (Smart Transpiler)**。Chrono 代码 (`.ch`) 被 100% 翻译为现代标准 C++17 代码，然后由成熟的 C++ 编译器（如 MSVC `cl.exe`, GCC, Clang）进行编译。

### 核心使命

解决 C++ 开发中的痛点，同时保留其零开销性能：

1.  **消除头文件地狱**：采用 `import` 机制，自动处理声明与实现的分离。
2.  **内存安全与灵活并存**：提供 **双重内存模型** —— 用于高性能的 **MRC (手动引用计数)** 和用于现代开发的 **智能指针 (Smart Pointers)**。
3.  **语法糖与现代化**：提供 `interface`、`impl` 块、更清晰的泛型语法、Rust 风格的变量声明 (`var/const`) 以及统一的访问符。
4.  **无缝互操作**：通过 `@cpp` 逃生舱口，可以在 Chrono 中直接编写 C++ 代码，并在生成的代码中完美融合。

-----

## 2\. 快速开始

### 环境依赖

  * **Python 3.x**: 运行翻译器和构建脚本。
  * **ANTLR 4 Runtime**: 用于解析语法树 (`pip install antlr4-python3-runtime`)。
  * **C++ 编译器**: 目前构建脚本针对 Windows MSVC (`cl.exe`) 进行了优化，支持 C++17 标准。
  * **Java (可选)**: 仅在修改 `.g4` 语法文件并需要重新生成解析器时需要。

### 目录结构

  * `src/`: 编译器源代码 (Python)。
      * `transpiler.py`: 单文件翻译入口。
      * `ChronoVisitor.py`: 核心逻辑，将 AST 转换为 C++。
      * `parser/`: ANTLR 生成的 Lexer/Parser。
  * `runtime/`: Chrono 运行时库 (`ChronoObject.h`, `Chrono.h` 等)，提供 MRC 基类和工具函数。
  * `test/`: 包含大量 `.ch` 测试用例，展示了语言的各种特性。
  * `build.py`: 项目级构建脚本。
  * `run_tests.py`: 自动化测试套件。

-----

## 3\. 构建与使用方法

### 3.1. 翻译单个文件

如果您只想查看某个 `.ch` 文件生成的 C++ 代码：

```bash
# 用法: python src/transpiler.py <输入文件> <输出文件>
python src/transpiler.py test/test_basic.ch build/test_basic.cpp
```

### 3.2. 构建整个项目 (推荐)

使用 `build.py` 可以递归扫描目录，根据 `chrono.json` 配置批量翻译项目。

1.  确保项目根目录有 `chrono.json` 配置文件：
    ```json
    {
      "src_dir": "src",
      "out_dir": "build",
      "transpiler_script": "src/transpiler.py"
    }
    ```
2.  运行构建命令：
    ```bash
    python build.py transpile -d .
    ```

### 3.3. 运行测试套件

项目包含一个完整的自动化测试系统，通过 `run_tests.py` 执行“翻译 -\> 编译 (MSVC) -\> 运行 -\> 对比输出”的完整流程。

```bash
# 运行所有测试
python run_tests.py

# 运行单个测试
python run_tests.py test/test_interface.ch
```

-----

## 4\. 语法指南 (Language Reference)

Chrono 的语法融合了 Swift、Rust 和 C++ 的优点。

### 4.1. 变量与常量

使用 `var` 声明变量，`const` 声明常量。支持类型推导。

```chrono
var a: i32 = 10;        // 显式类型
var b = 20;             // 自动推导 (auto)
const PI: f32 = 3.14;   // 常量
var s: String*;         // 指针类型 (引用类型)
```

**基本数据类型映射：**
| Chrono 类型 | C++ 映射 | 说明 |
| :--- | :--- | :--- |
| `i8`, `u8` | `int8_t`, `uint8_t` | 8位整数/字节 |
| `i32`, `u32` | `int32_t`, `uint32_t` | 32位整数 |
| `f32`, `f64` | `float`, `double` | 浮点数 |
| `bool` | `bool` | 布尔值 |
| `void` | `void` | 空类型 |
| `std.string` | `std::string` | 标准字符串 (值类型) |

### 4.2. 流程控制

现代化的控制流，支持无括号条件（虽然当前测试用例仍习惯带括号），以及 Rust 风格的 switch。

```chrono
// If-Else
if (x > 0) {
    // ...
} else if (x == 0) {
    // ...
}

// For 循环 (C-Style)
for (var i: i32 = 0; i < 10; i += 1) {
    // ...
}

// While 循环
while (running) { ... }

// Switch (隐式 break)
switch (val) {
    case 1 { ... }      // 自动 break
    case 2 { ... }
    default { ... }
}
```

### 4.3. 函数 (Functions)

函数使用 `func` 关键字。支持全局函数、成员函数和静态函数。

```chrono
// 全局函数
func add(a: i32, b: i32) -> i32 {
    return a + b;
}

// 箭头语法定义函数类型别名
using Handler = (i32, i32) -> void;
```

### 4.4. 面向对象编程 (OOP)

Chrono 严格区分 **Class (引用类型)** 和 **Struct (值类型)**，并引入了 **Declaration (定义)** 与 **Implementation (实现)** 分离的概念。

#### Class (引用类型)

通常继承自 `ChronoObject` 以获得 MRC 能力。

```chrono
// 1. 类声明 (通常在 .h.ch 中)
class Circle : ChronoObject {
    var radius: f32; // 默认 private
    
    public init(r: f32);         // 构造函数声明
    public func getArea() -> f32;// 方法声明
    deinit;                      // 析构函数声明
}

// 2. 类实现 (通常在 .ch 中)
implement Circle {
    init(r: f32) {
        this->radius = r;
    }
    
    func getArea() -> f32 {
        return 3.14 * this->radius * this->radius;
    }
    
    deinit {
        // 清理逻辑
    }
}
```

#### Struct (值类型)

轻量级，栈分配，不支持继承。

```chrono
struct Point {
    var x: i32;
    var y: i32;
}
```

#### 接口 (Interfaces)

支持类似于 Java/C\# 的接口定义。

```chrono
interface IShape {
    func getArea() -> f32;
}

// 实现接口
class Square : ChronoObject impl IShape {
    // ...
}
```

### 4.5. 智能指针与内存管理

这是 Chrono 的一大亮点。除了传统的 MRC (`retain`/`release`)，Chrono 提供了一流的智能指针语法支持。

| 概念 | Chrono 语法 | 对应 C++ |
| :--- | :--- | :--- |
| **独占指针** | `var p: unique[Type];` | `std::unique_ptr<Type> p;` |
| **共享指针** | `var p: shared[Type];` | `std::shared_ptr<Type> p;` |
| **弱指针** | `var p: weak[Type];` | `std::weak_ptr<Type> p;` |
| **创建独占** | `@make[Type](args)` | `std::make_unique<Type>(args)` |
| **创建共享** | `@make_shared[Type](args)` | `std::make_shared<Type>(args)` |
| **移动语义** | `@move(p)` | `std::move(p)` |
| **类型转换** | `static_cast<T>(v)` | `static_cast<T>(v)` |

### 4.6. 泛型 (Generics)

支持 C++ 模板的完整映射，语法更加统一。

```chrono
// 定义泛型变量
var list: std.vector<i32>; 
var map: std.map<std.string, i32>;

// 使用命名空间的点号会被翻译为 ::
// std.vector -> std::vector
```

### 4.7. 数组 (Arrays)

支持 Rust 风格的数组声明，并自动处理为 C++ 风格。

```chrono
// 声明固定大小数组
var arr: [i32; 5] = {1, 2, 3, 4, 5};

// 访问
var x = arr[0];
```

### 4.8. 互操作性 (Interop)

#### Import

```chrono
import "runtime/ChronoObject.h"  // 导入用户头文件
import <iostream>                // 导入系统头文件
import "lib/Math.h" as Math      // 支持别名 (namespace alias)
```

#### @cpp 逃生舱口

当 Chrono 语法无法满足需求时，可以直接嵌入 C++ 代码。

```chrono
func heavyWork() {
    @cpp
    // 这里的代码会原样输出到生成的 .cpp 文件中
    std::cout << "Native C++ performance!" << std::endl;
    // 可以访问 Chrono 定义的变量
    @end
}
```

-----

## 5\. 进阶特性

### 5.1. 命名空间 (Namespace)

支持文件级命名空间包裹。

```chrono
namespace MyGame.Physics; // 开始命名空间

class Body { ... }

endnamespace; // 结束命名空间 (必须显式调用)
```

### 5.2. 属性与访问控制

  * `public`: 公开访问。
  * `static`: 静态成员/函数。
  * 默认情况下，类成员变量是 `private`。

### 5.3. 翻译器智能处理

  * **自动头文件推导**: 引用 `import "Path/File"` 会尝试自动推导生成的 C++ `#include` 路径。
  * **后缀处理**: 智能识别 `.h.ch` (用于声明) 和 `.ch` (用于实现)。
  * **Typemap**: 翻译器内部维护类型映射，确保 `i32` 正确转换为 `int32_t`。

-----

## 6\. 贡献与开发

### 生成解析器

如果您修改了 `src/parser/*.g4` 文件，请运行以下命令重新生成 Python 解析器代码：

```batch
gen.bat
```

(需要 Java 环境运行 antlr jar 包)

### 已知问题

  * 目前主要针对 Windows/MSVC 环境测试。
  * 错误提示主要依赖 Python 异常堆栈，尚未实现友好的编译器错误报告。

-----

*Chrono Project - Making C++ Fun Again.*