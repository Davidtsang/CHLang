# Chrono 编程语言项目

## 项目概述

Chrono 是一个创新的编程语言项目，其目标是成为“C++ 的 TypeScript”，通过提供一个更简洁、美观的语法前端，同时保留 C++ 的全 部性能和生态系统。它不是一个独立的编译器，而是作为一个**智能翻译器（Smart Transpiler）**，将 Chrono 代码（.ch 文件）100% 翻译为标准 C++17 代码。这解决了 C++ 的常见痛点，如手动内存管理、`->` vs `.` 的混淆以及复杂的语法，但允许开发者通过 `@cpp` 逃生舱口嵌入原生 C++ 代码。

项目的使命是让 C++ 开发更高效和易用，同时通过双重类型系统（值类型和引用类型）实现自动内存管理（对于引用类型使用手动引用 计数 MRC）。

## 核心设计哲学

- **双重类型系统**：
  - 值类型（如 `var x: i32`）翻译为栈分配的 C++ 原生类型（如 `int32_t x`），零开销。
  - 引用类型（如 `var s: String*`）翻译为堆分配的指针（如 `String* s`），使用 MRC 进行内存管理。
- **统一的 `.` 语法**：消除 `->`，翻译器智能判断上下文（如实例调用翻译为 `->`，静态调用翻译为 `::`）。
- **`@cpp` 逃生舱口**：允许在任何位置注入原生 C++ 代码，保证顺序输出。
- **其他特性**：支持泛型（如 `std.vector[i32]`）、数组（如 `[char; 20]`）、流程控制（if/else/while/for）、运算符（算术、比较、位运算、复合赋值）、字面量（包括字节、浮点等），以及类、struct、接口定义、智能指针（unique/shared/weak）。

## 当前已实现的功能

根据基本信息和附加文件，项目已经实现了一个强大的 MVP（最小可行产品），包括：
- **基础语法**：`import`（支持别名和路径）、`class`、`struct`、`func`、`var`（可变声明）、`const`（常量声明）、`init`、`deinit`、`return`、`static`、`public`、`interface`、`impl`、`as`、`new`、`delete`、`if`、`else`、`while`、`for`、`true`/`false`、`bool` 类型、比较运算符（`==`、`!=`、`<`、`>`、`<=`、`>=`）、逻辑运算符（`&&`、`||`）。
- **面向对象**：`static func`、`init`（构造函数）、`deinit`（析构函数）、类继承（基类，使用 `:`）、接口实现（使用 `impl`）、`struct`（类似class，无继承，默认public）。
- **表达式和链式调用**：完整的链式调用（如 `s.toUpper().length()`）、赋值（支持复合赋值如 `+=`、`-=`）、方法调用、数组索引。
- **数据类型**：完整的整数类型（`i8/u8` 到 `i64/u64`）、浮点类型（`f32/f64`）、字符串、字节、字符字面量、数组语法（`[type; size]`）、泛型类型（支持嵌套）、智能指针（`unique[T]`、`shared[T]`、`weak[T]` ）。
- **运算符**：算术（`+`、`-`、`/`、`*`、`%`）、位运算（`&`、`|`、`^`、`~`、`<<`、`>>`）、复合赋值（`+=` 等）。
- **内存管理**：MRC（手动引用计数）通过 `retain()` 和 `release()`，支持 `new`/`delete` 关键字、智能指针工厂（`@make[T]` 、`@make_shared[T]`、`@move`）。
- **测试套件**：Python 脚本 `run_tests.py` 用于翻译、编译、运行和比较输出，支持单个文件或全部测试。

项目还包括多个测试文件（如 `test_flow_control.ch`、`test_arithmetic_ops.ch` 等），覆盖各种场景，确保翻译器的正确性。

## 语法概述

Chrono 的语法基于 ANTLR4 定义，支持模块化解析。程序由顶级语句（如导入、类定义、struct定义、函数定义、接口定义）组成。文 件扩展名为 `.ch`，编译目标为 C++17，使用 MSVC 编译器。

### 关键字

Chrono 的关键字（不区分大小写）包括：

- **控制和声明**：`import`, `var`, `const`, `func`, `class`, `struct`, `return`, `static`, `public`, `as`, `new`, `delete`, `if`, `else`, `while`, `for`, `interface`, `impl`, `init`, `deinit`, `this`, `true`, `false`。
- **智能指针**：`unique`, `shared`, `weak`, `@make`, `@make_shared`, `@move`。
- **其他**：`@cpp`（切换到 C++ 模式），`@end`（结束 C++ 块）。

示例：
```chrono
import "runtime/Chrono.h";  // 导入
var x: i32 = 5;  // 声明
if (true) { ... }  // 控制流
```

### 数据类型

Chrono 支持完整的类型系统，分为值类型和引用类型。类型在 `typeSpecifier` 规则中定义，支持泛型和数组。

- **基本类型**（值类型）：
  - 整数：`i8`, `u8`, `i16`, `u16`, `i32`/`int`, `u32`, `i64`, `u64`（翻译为 `int8_t` 等）。
  - 浮点：`f32`/`float`, `f64`/`double`。
  - 布尔：`bool`。
- **复合类型**：
  - 字符串：`std.string`（值类型，翻译为 `std::string`）。
  - 泛型：如 `std.vector[i32]`（翻译为 `std::vector<int32_t>`），支持嵌套（如 `std.map[std.string, std.vector[i32]]`）。
  - C-Style 数组：`[char; 20]`（翻译为 `char[20]`），支持动态大小（如 `[std.string; size]`）。
  - 智能指针：`unique[T]`（`std::unique_ptr<T>`）、`shared[T]`（`std::shared_ptr<T>`）、`weak[T]`（`std::weak_ptr<T>`） 。
- **特殊类型**：
  - `id`：指向 `ChronoObject` 的指针，用于 MRC。
  - 字节：`u8`（与 `b'A'` 字面量结合）。

示例：
```chrono
var x: i32 = 5;                // 值类型
var s: String* = String.create("hello");  // 引用类型
var v: std.vector[i32];         // 泛型
var arr: [char; 20] = {"a", "b"};  // 数组
var ptr: unique[Resource];      // 智能指针
```

### 字面量（Literals）

字面量支持多种格式：

- **整数**：十进制（`42`）、十六进制（`0x2A`）、二进制（`0b101010`）、八进制（`0o52`）。
- **浮点**：`3.14`（翻译为 `float` 或 `double`）。
- **布尔**：`true`, `false`。
- **字符串**：`"hello"`（翻译为 `std::string`）。
- **字符**：`'a'`（翻译为 `char`）。
- **字节**：`b'A'`（翻译为 `(uint8_t)'A'`）。
- **聚合初始化**：`{1, 2, 3}`（用于数组或对象初始化）。

示例：
```chrono
var num: i32 = 0x2A;     // 42
var pi: f32 = 3.14;      // 3.14
var flag: bool = true;   // true
var str: std.string = "hello";  // std::string
var byte: u8 = b'A';     // (uint8_t)'A'
var arr: [i32; 3] = {1, 2, 3};  // 初始化数组
```

### 表达式和运算符

表达式支持链式调用和优先级。

- **算术运算符**：`+`, `-`, `*`, `/`, `%`（二元和一元）。
- **比较运算符**：`==`, `!=`, `<`, `>`, `<=`, `>=`。
- **逻辑运算符**：`&&`, `||`。
- **位运算符**：`&`, `|`, `^`, `~`, `<<`, `>>`。
- **复合赋值**：`=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`。
- **链式调用**：`.foo()`（智能翻译为 `.` 或 `->`），支持数组索引 `[i]`。
- **函数调用**：`funcName(args)`。
- **优先级**：遵循标准数学规则，一元运算符优先级最高。

示例：
```chrono
var result: i32 = a + b * 2;  // 算术
if (x == 5) { ... }           // 比较
var len: Int* = s.length();  // 方法链
arr[0] = 10;                  // 数组索引
```

### 语句

语句包括声明、赋值、控制流等。

- **声明**：`var/const varName: type = value;`
- **赋值**：`target op value;`（支持复合赋值）。
- **返回**：`return expr;`。
- **表达式语句**：`expr;`（如函数调用）。
- **控制流**：
  - `if (condition) { ... } else if (condition) { ... } else { ... }`
  - `while (condition) { ... }`
  - `for (init; condition; increment) { ... }`
- **删除**：`delete expr;`（用于手动释放非 MRC 对象）。
- **C++ 块**：`@cpp ... @end`（嵌入原生 C++）。
- **块语句**：`{ ... }`（独立作用域）。

示例：
```chrono
var x: i32 = 5;
if (x > 0) { Chrono.log("positive"); } else { Chrono.log("non-positive"); }
while (x < 10) { x = x + 1; }
for (var i: i32 = 0; i < 3; i += 1) { ... }
@cpp std::cout << "native" << std::endl; @end
```

### 类、Struct 和面向对象

- **类定义**：`class Name : Base impl Interface1, Interface2 { ... }`（继承使用 `:`，接口使用 `impl`）。
- **Struct 定义**：`struct Name { ... }`（无继承，默认 public）。
- **成员**：`var/const varName: type;`（默认私有，可用 `public` 修饰）。
- **构造函数**：`init(params) { ... }`（默认私有）。
- **析构函数**：`deinit { ... }`（自动公开）。
- **方法**：`func name(params) -> returnType { ... }`（支持 `static` 和 `public`）。
- **接口**：`interface Name { func method(params) -> type; ... }`（纯虚方法）。
- **访问器**：`this`（在方法中使用），统一 `.` 语法。

示例：
```chrono
interface IShape {
    func getArea() -> f32;
}

class Circle : ChronoObject impl IShape {
    var radius: f32;
    public init(r: f32) { this.radius = r; }
    public func getArea() -> f32 { return 3.14 * this.radius * this.radius; }
}

struct Point {
    public var x: i32;
    public var y: i32;
}
```

### 函数

- **全局函数**：`func name(params) -> returnType { ... }`（支持 `static`）。
- **方法**：类似，但属于类，支持 `this`。
- **参数**：`name: type`
- **返回类型**：`-> type`。

示例：
```chrono
func add(a: i32, b: i32) -> i32 { return a + b; }
func main() -> int { return 0; }  // 主函数必须返回 int
```

### 导入（Import）

- **语法**：`import "path" as alias;`（路径可为字符串或 `<path>`，支持别名）。
- **功能**：翻译为 `#include`，自动推断命名空间（如 `"runtime/Chrono.h"` 映射到 `Chrono`）。
- **别名**：`as Name`（默认使用文件名推断）。

示例：
```chrono
import "runtime/Chrono.h";       // #include "runtime/Chrono.h"
import <iostream> as IO;         // #include <iostream>
import "lib/MyMath.h" as Math;   // 别名 Math
```

## 特殊特性

- **@cpp 逃生舱口**：允许顺序嵌入 C++ 代码，无语法限制。
- **作用域栈**：在 `ChronoVisitor.py` 中实现，支持嵌套作用域和变量查找。
- **类型推导**：`var` 支持可选类型声明。
- **常量**：`const` 用于不可变声明。
- **内存管理**：MRC 需开发者手动管理引用类型内存、智能指针自动管理。
- **格式化**：可选使用 `clang-format` 美化生成代码。

## 项目结构

项目采用模块化结构，主要文件和文件夹如下：
- **语法定义**：
  - `ChronoLexer.g4`：词法分析器，使用 ANTLR4 定义关键字、运算符、字面量等。
  - `ChronoParser.g4`：语法分析器，定义规则如 `program`、`classDefinition`、`expression` 等。
- **翻译器**：
  - `src/ChronoVisitor.py`：访问者模式实现，负责将 AST 翻译为 C++ 代码。包含作用域栈、类型映射、访问器处理等逻辑。
  - `src/transpiler.py`：主翻译脚本，使用 ANTLR4 生成词法/语法分析器，调用 Visitor 进行翻译，并可选使用 clang-format 格 式化输出。
- **测试和构建**：
  - `test/`：包含多个 .ch 测试文件和对应的 .expected.txt 输出文件。
  - `run_tests.py`：自动化测试脚本，支持编译（使用 MSVC `cl.exe`）和运行。
  - `gen.bat`：批处理脚本，使用 ANTLR4 生成 Python 词法/语法分析器。
- **其他**：`build/` 用于输出文件，`lib/`（假设存在，用于第三方库如 MyMath.h）。

## 技术细节和依赖

- **解析和翻译**：基于 ANTLR4（Python 3），生成词法/语法分析器。
- **目标平台**：C++17，使用 MSVC 编译器（`cl.exe`）进行测试。
- **错误处理**：`transpiler.py` 使用自定义错误监听器，抛出异常以停止翻译。
- **格式化**：可选使用 `clang-format` 格式化生成代码。
- **依赖**：需要 ANTLR4 JAR 文件（`antlr-4.13.2-complete.jar`）、Python 3、MSVC（Windows）、clang-format（可选）。

## 当前状态和挑战

- **已完成**：MVP 功能完整，支持复杂表达式、类、struct、接口、智能指针、测试自动化。测试套件覆盖广泛，输出与预期匹配。
- **潜在问题**：
  - 作用域栈和访问器逻辑复杂，可能在嵌套上下文中出错（但测试文件显示已修复）。
  - 依赖 ANTLR4 和 MSVC，可能在其他平台（如 Linux）需要调整编译命令。
  - 泛型和数组语法新颖，但需确保与 C++ 标准兼容。
- **性能**：翻译为纯 C++，零运行时开销（除了 MRC）。

## 演示：Chrono 智能指针语法

| Chrono 语法 (新) | C++ 翻译 (目标) | 架构规则 |
|------------------|------------------|----------|
| `var p: unique[Resource] = @make[Resource](args);` | `std::unique_ptr<Resource> p = std::make_unique<Resource>(args);` | 独占指针 |
| `var p: shared[Resource] = @make_shared[Resource](args);` | `std::shared_ptr<Resource> p = std::make_shared<Resource>(args);` | 共享指针 |
| `var p2 = @move(p);` | `auto p2 = std::move(p);` | 移动语义 |

---

这个 README.md 全面总结了项目的当前状态，并融入了最新的语法改动。如果您需要进一步修改、添加示例或调试代码，请告诉我！