好的，基于您提供的项目源代码（Visitor、Parser、Lexer）、测试用例（Test files）以及构建脚本（Build scripts），我为您重写了一份完善、详细且结构清晰的 `README.md`。

这份文档旨在不仅作为项目介绍，更作为一份开发者的使用手册。

-----

# CH 编程语言 (CH Lang)

**"The TypeScript for C++"**

## 1\. 项目概述

**CH** 是一个现代化的编程语言项目，旨在解决 C++ 开发中的痛点，同时保留其零开销的性能优势。它不是一个运行在虚拟机上的解释型语言，而是一个 **智能转译器 (Smart Transpiler)**。

CH 源代码 (`.ch`) 会被 100% 翻译为现代标准 C++17 代码 (`.cpp` / `.h`)，生成的代码可以直接集成到任何现有的 C++ 项目中，并使用 MSVC、GCC 或 Clang 进行编译。

### 核心特性

  * **声明与实现分离**：通过 `class` 定义接口，通过 `implement` 块编写逻辑，彻底告别手动维护头文件的繁琐。
  * **双重内存模型**：
      * **MRC (手动引用计数)**：通过 `CHObject` 提供类似 Objective-C 的引用计数管理，适合高性能场景。
      * **现代智能指针**：内置 `unique`, `shared`, `weak` 关键字和 `@make`, `@move` 语法，并配备静态 **借用检查器 (Borrow Checker)** 以防止常见的内存错误。
  * **现代化语法**：融合了 Rust 和 Swift 的语法糖，支持 `var/const` 类型推导、清晰的泛型 `< >`、接口 `interface` 以及 C-Style 数组切片语法。
  * **无缝 C++ 互操作**：
      * **零开销调用**：CH 类型直接映射为 C++ 原生类型（如 `i32` -\> `int32_t`）。
      * **@cpp 逃生舱**：允许在任何地方嵌入原生 C++ 代码。
      * **智能导入**：`import` 语句自动处理命名空间别名和头文件包含。

-----

## 2\. 项目结构

```text
CH/
├── src/                    # 编译器核心源码 (Python)
│   ├── transpiler.py       # [入口] 单文件转译脚本
│   ├── CHVisitor.py    # [核心] AST 遍历与代码生成逻辑
│   ├── CompileContext.py   # 编译上下文管理
│   └── parser/             # ANTLR4 生成的 Lexer 和 Parser
├── runtime/                # CH 运行时库 (C++ 头文件)
│   ├── CHObject.h      # MRC 基类
│   ├── CH.h            # 工具函数与日志
│   └── ...
├── test/                   # 测试套件 (包含 .ch 源码与预期输出)
├── build/                  # 构建输出目录 (生成的 .cpp/.exe)
├── build.py                # [脚本] 项目级构建工具
├── run_tests.py            # [脚本] 自动化测试运行器
├── gen.bat                 # [脚本] 生成 ANTLR Parser 的批处理
└── CH.json             # 项目配置文件
```

-----

## 3\. 快速开始

### 环境要求

1.  **Python 3.x**: 运行编译器脚本。
2.  **ANTLR 4 Runtime**: `pip install antlr4-python3-runtime`。
3.  **C++ 编译器**: 推荐 **Visual Studio (MSVC)** (脚本默认配置为 `cl.exe`)，需支持 C++17。

### 脚本使用指南

#### 3.1. 翻译单个文件 (`src/transpiler.py`)

如果您只想将一个 `.ch` 文件转换为 `.cpp` 文件以查看生成的代码：

```bash
# 语法: python src/transpiler.py <输入文件> <输出文件>
python src/transpiler.py test/test_basic.ch build/test_basic.cpp
```

#### 3.2. 构建整个项目 (`build.py`)

`build.py` 读取 `CH.json` 配置，递归扫描源码目录并批量转译。

1.  确保根目录存在 `CH.json`：
    ```json
    {
        "src_dir": "src",
        "out_dir": "build/src",
        "transpiler_script": "src/transpiler.py"
    }
    ```
2.  运行构建：
    ```bash
    python build.py transpile -d .
    ```

#### 3.3. 运行测试套件 (`run_tests.py`)

这是验证编译器功能最直接的方法。它会执行：**转译 -\> 编译 (cl.exe) -\> 运行 -\> 比对输出**。

```bash
# 运行所有测试
python run_tests.py

# 运行指定测试
python run_tests.py test/test_smart_ptr.ch
```

-----

## 4\. 语法指南 (Language Reference)

### 4.1. 变量与基本类型

使用 `var` 声明变量，`const` 声明常量。支持类型推导。

```CH
// 显式类型声明
var age: i32 = 18;
var pi: f32 = 3.14;

// 类型推导 (auto)
var name = "CH"; // 推导为 const char*
const MAX_COUNT = 100;

// 原生 C++ 字符串 (值类型)
var s: std.string = "Hello";
```

**类型映射表：**

| CH | C++ (stdint) | CH | C++ (Native) |
| :--- | :--- | :--- | :--- |
| `i8`, `u8` | `int8_t`, `uint8_t` | `bool` | `bool` |
| `i32`, `u32` | `int32_t`, `uint32_t` | `f32`, `f64` | `float`, `double` |
| `i64`, `u64` | `int64_t`, `uint64_t` | `void` | `void` |

### 4.2. 数组 (Arrays)

采用类似 Rust 的数组语法。

```CH
// 固定大小数组声明
var numbers: [i32; 5] = {1, 2, 3, 4, 5};

// 访问与赋值
numbers[0] = 10;
var x = numbers[2];

// 多维数组
var matrix: [[i32; 3]; 2]; // 2行3列
```

### 4.3. 函数 (Functions)

```CH
// 全局函数
func add(a: i32, b: i32) -> i32 {
    return a + b;
}

// 无返回值函数 (-> void 可省略)
func log(msg: std.string) {
    @cpp std::cout << msg << std::endl; @end
}

// 函数指针/Lambda 类型别名
using Callback = (i32) -> void;
```

### 4.4. 面向对象 (Class & Struct)

CH 强制将 **声明 (Declaration)** 与 **实现 (Implementation)** 分离。

#### Struct (值类型)

轻量级，分配在栈上，默认 `public`。

```CH
struct Point {
    var x: i32;
    var y: i32;
    
    // 只有声明
    init(v: i32);
}

implement Point {
    init(v: i32) {
        this.x = v; // struct 内部 this 使用 . 访问
        this.y = v;
    }
}
```

#### Class (引用类型)

通常继承自 `CHObject`，支持继承和虚函数，默认 `private`。

```CH
class Shape : CHObject {
    var area: f32;
    
    // 声明部分
    public init();
    public func calculate() -> f32;
    deinit; // 析构函数声明
}

implement Shape {
    init() {
        this->area = 0.0; // class 内部 this 是指针，使用 ->
    }
    
    func calculate() -> f32 {
        return this->area;
    }
    
    deinit {
        // 自动生成 virtual ~Shape()
    }
}
```

#### Interface (接口)

支持多继承接口。

```CH
interface IDrawable {
    func draw() -> void;
}

// 使用 'with' 关键字实现接口
class Button : CHObject with IDrawable {
    public func draw() -> void;
}
```

### 4.5. 智能指针与内存安全

CH 将 C++ 智能指针提升为语言级的一等公民。

#### 语法糖

| 概念 | CH 写法 | 生成 C++ 代码 |
| :--- | :--- | :--- |
| 独占指针类型 | `var p: unique[Box];` | `std::unique_ptr<Box> p;` |
| 共享指针类型 | `var p: shared[Box];` | `std::shared_ptr<Box> p;` |
| 创建独占对象 | `@make[Box](10)` | `std::make_unique<Box>(10)` |
| 创建共享对象 | `@make_shared[Box](10)` | `std::make_shared<Box>(10)` |
| 所有权转移 | `@move(p)` | `std::move(p)` |
| 强制移动 | `@unsafe_move(p)` | `std::move(p)` (跳过安全检查) |

#### 借用检查 (Safety Checks)

编译器会跟踪变量的状态。如果在循环或条件分支中尝试 `move` 外部变量，编译器会报错，防止 Use-After-Move 或重复释放。

```CH
var u = @make[Box]();
// var u2 = @move(u); // u 变成 "Moved" 状态
// u->id = 1;         // 编译错误：使用了已移动的变量
```

### 4.6. 流程控制

```CH
// If / Else
if (x > 10) { ... } else { ... }

// While
while (running) { ... }

// For 循环
for (var i: i32 = 0; i < 10; i += 1) { ... }

// Switch (现代化的 case，无需 break)
switch (val) {
    case 1 {
        // 自动 break
    }
    case 2 { ... }
    default { ... }
}
```

### 4.7. C++ 互操作 (Interop)

#### 直接嵌入 C++ (`@cpp`)

```CH
func legacyCall() {
    @cpp
    // 这里的代码会原样输出
    printf("Hello from native C++\n");
    @end
}
```

#### 导入与别名

```CH
import <iostream>                 // 系统头文件
import "runtime/CHObject.h"   // 用户头文件
import "lib/Math.h" as Math       // 命名空间别名
```

#### 类型转换

支持 C++ 风格的转换语法：

```CH
var f = static_cast<f32>(10);
var ptr = reinterpret_cast<void*>(addr);
```

-----

## 5\. 贡献指南

1.  **修改语法**：编辑 `src/parser/CHLexer.g4` 或 `CHParser.g4`。
2.  **重新生成 Parser**：运行 `gen.bat` (需要 Java 环境)。
3.  **修改逻辑**：编辑 `src/CHVisitor.py`。
4.  **验证**：运行 `python run_tests.py` 确保没有破坏现有功能。

-----

*Designed for performance, built for clarity.*