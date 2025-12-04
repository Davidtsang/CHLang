# CH Programming Language (CH Lang)

**"The TypeScript for C++"**

  

## 1\. Project Overview

**CH** is a modern systems programming language project designed to resolve the long-standing pain points of C++ development while retaining its zero-overhead performance advantages. It is not an interpreted language running on a Virtual Machine; it is a **Smart Transpiler**.

CH source code (`.ch`) is translated 100% into modern standard C++17 code (`.cpp` / `.h`). The generated code is human-readable and can be directly integrated into any existing C++ project and compiled using MSVC, GCC, or Clang.

### Core Philosophy & Features

  * **Separation of Interface & Implementation**: CH enforces a strict separation between `class` definitions (interfaces) and `implement` blocks (logic). This creates a clean structure and **automatically resolves C++ circular dependency issues** (header hell).
  * **Dual Memory Model**:
      * **MRC (Manual Reference Counting)**: Inherit from `CHObject` to gain Objective-C style reference counting (`retain`/`release`), optimized for performance-critical paths.
      * **Modern Smart Pointers**: First-class language support for `unique`, `shared`, and `weak` pointers with syntax sugar (`@make`, `@move`). Includes a static **Borrow Checker** to prevent common use-after-move errors.
  * **Modern Syntax**: A fusion of Rust and Swift syntax, supporting `var`/`const` type inference, clear generics `< >`, interfaces, and C-style array/slice syntax.
  * **Seamless C++ Interop**:
      * **Zero-Overhead Mapping**: CH types map directly to native C++ types (e.g., `i32` -\> `int32_t`, `[i32; 5]` -\> `int32_t[5]`).
      * **@cpp Escape Hatch**: Embed raw C++ code anywhere using `@cpp ... @end` blocks.
      * **Smart Imports**: The `import` statement automatically handles namespace aliasing and header inclusion management.
  * **Dynamic Runtime**: A lightweight runtime (like Objective-C) that enables **Dynamic Dispatch** (`obj~>method()`) and Reflection, powering data-driven UI frameworks.

-----

## 2\. Project Structure

The project is organized as a self-hosting compiler ecosystem:

```text
CH/
├── src/                        # Compiler Core (Python)
│   ├── transpiler.py           # [Entry] Single file transpilation script
│   ├── CHVisitor.py            # [Core] AST traversal & C++ code generation logic
│   ├── CompileContext.py       # Symbol table & compilation context management
│   ├── generators/             # Code generation plugins (@codegen)
│   └── parser/                 # ANTLR4 generated Lexer & Parser
├── runtime/                    # CH Runtime Library (C++ Headers)
│   ├── CHObject.h              # Base class for MRC & Dynamic Dispatch
│   ├── CH.h                    # CH::Log
│   ├── Reflection.h            # Runtime type reflection utilities
│   └── ...
├── libs/                       # Standard Libraries & Ecosystem
│   ├── chui/                   # [GUI] Win32/GDI+ UI Framework (HBox, Widget...)
│   └── jsonp/                  # [Data] Recursive JSON Parser
├── examples/                   # Example Applications
│   └── MyGdiApp/               # A complete data-driven GUI showcase
├── build/                      # Build Artifacts (Generated .cpp/.exe)
│   ├── deps/                   # Dependency tracking files (.dep.json)
│   └── dist/                   # Final compiled binaries
├── build.py                    # [Tool] Two-phase incremental build system
├── make.py                     # [Tool] CMake wrapper & Resource copier
├── pkg.py                      # [Tool] Project scaffolding generator
└── run_tests.py                # [Tool] Automated test suite runner
```

-----

## 3\. Quick Start

### Prerequisites

1.  **Python 3.10+**: Required to run the transpiler scripts.
2.  **ANTLR 4 Runtime**: Install via pip: `pip install antlr4-python3-runtime`.
3.  **C++ Compiler**: A C++17 compatible compiler. **Visual Studio (MSVC)** is recommended on Windows.
4.  **CMake & Ninja**: For building the generated C++ projects.

### Usage Guide

#### 3.1. Transpile a Single File (`src/transpiler.py`)

To convert a single `.ch` file into C++ to inspect the generated code:

```bash
# Usage: python src/transpiler.py <input> <output> <dep_file>
python src/transpiler.py test/test_basic.ch build/test_basic.cpp build/test_basic.json
```

#### 3.2. Build a Project (`build.py` / `make.py`)

The build system reads `config.json` to manage dependencies and compilation order (Headers Phase 1 -\> Sources Phase 2).

To build and run an example project:

```bash
# Transpile, Compile (CMake), and Run
python make.py examples/MyGdiApp --run
```

#### 3.3. Run the Test Suite (`run_tests.py`)

This validates the compiler's correctness by transpiling, compiling, running, and comparing stdout against `.expected.txt`.

```bash
# Run all tests
python run_tests.py

# Run a specific test case
python run_tests.py test/test_smart_ptr.ch
```

-----

## 4\. Language Reference

### 4.1. Variables & Primitive Types

CH uses `var` for mutable variables and `const` for immutable constants. Type inference is supported.

```swift
// Explicit typing
var age: i32 = 18;
var pi: f32 = 3.14;

// Type inference (auto)
var name = "CH"; // Inferred as const char*
const MAX_COUNT = 100;

// Native C++ String (Value type)
var s: std::string = "Hello World";
```

**Type Mapping Table:**

| CH Type       | C++ Equivalent | CH Type | C++ Equivalent |
|:--------------| :--- | :--- | :--- |
| `i8`, `u8`    | `int8_t`, `uint8_t` | `bool` | `bool` |
| `i32`, `u32`  | `int32_t`, `uint32_t` | `f32`, `f64` | `float`, `double` |
| `i64`, `u64`  | `int64_t`, `uint64_t` | `void` | `void` |
| `std::string` | `std::string` | `dyn` | `CHObject*` (Dynamic) |

### 4.2. Arrays & Spans

CH provides a unified syntax for Arrays (Storage) and Spans (Views).

```swift
// Fixed-Size Array (Storage)
// Allocates on Stack. Zero overhead.
// C++: int32_t numbers[5] = {1, 2, 3, 4, 5};
var numbers: [i32; 5] = {1, 2, 3, 4, 5};

// Access
numbers[0] = 10;

// Slice / Span (View)
// Used for function parameters. Automatic bounds checking in debug mode.
// C++: CH::Span<int32_t>
func process(data: [i32]) {
    if (data.length() > 0) {
        var x = data[0];
    }
}

// Implicit conversion from Array to Span
process(numbers);
```

### 4.3. Functions & Closures

```swift
// Global Function
func add(a: i32, b: i32) -> i32 {
    return a + b;
}

// Void return type can be omitted
func log(msg: std.string) {
    @cpp std::cout << msg << std::endl; @end
}

// Lambda / Function Pointer Alias
using Callback = (i32) -> void;

// Closure syntax
var cb = (val: i32) => {
    log("Value is: " + val);
};
```

### 4.4. Object Oriented Programming (Class & Struct)

The distinction between `class` and `implement` blocks is mandatory.

#### Struct (Value Type)

Lightweight, stack-allocated, default `public` access. Maps to C++ `struct`.

```swift
struct Point {
    var x: i32;
    var y: i32;
    
    // Declaration only
    init(v: i32);
}

implement Point {
    init(v: i32) {
        this.x = v; // 'this' is a reference/value in struct
        this.y = v;
    }
}
```

#### Class (Reference Type)

Usually inherits from `CHObject`. Supports inheritance, virtual functions, and default `private` access.

```swift
@dynamic // Enables runtime reflection
class Shape : CHObject {
    var area: f32;
    
    public init();
    public func calculate() -> f32;
    deinit; // Destructor declaration
}

implement Shape {
    init() {
        this.area = 0.0; // 'this' is a pointer in class
    }
    
    func calculate() -> f32 {
        return this.area;
    }
    
    deinit {
        // Maps to virtual ~Shape()
    }
}
```

#### Interfaces

Supports multiple inheritance via interfaces.

```swift
interface IDrawable {
    func draw() -> void;
}

// Use 'with' to implement interfaces
class Button : CHObject with IDrawable {
    public func draw() -> void;
}
```

### 4.5. Smart Pointers & Memory Safety

CH treats C++ smart pointers as first-class citizens.

| Concept | CH Syntax | C++ Generated |
| :--- | :--- | :--- |
| Unique Ptr Type | `var p: unique<Box>;` | `std::unique_ptr<Box> p;` |
| Shared Ptr Type | `var p: shared<Box>;` | `std::shared_ptr<Box> p;` |
| Make Unique | `@make<Box>(10)` | `std::make_unique<Box>(10)` |
| Make Shared | `@make_shared<Box>(10)` | `std::make_shared<Box>(10)` |
| Move Semantics | `@move(p)` | `std::move(p)` |

**Borrow Checker**:
The compiler tracks variable states (`Alive`, `Moved`). Attempting to use a moved variable results in a compile-time error.

```swift
var u = @make<Box>();
var u2 = @move(u); // 'u' state becomes 'Moved'
// u->id = 1;      // Compiler Error: Use of moved variable 'u'
```

### 4.6. Flow Control

```swift
// If / Else
if (x > 10) { ... } else { ... }

// While
while (running) { ... }

// For Loop (C-Style)
for (var i: i32 = 0; i < 10; i = i + 1) { ... }

// Range-based For
for (var item in collection) { ... }

// Switch (Modern block scope, no implicit fallthrough)
switch (val) {
    case 1 { ... }
    case 2 { ... }
    default { ... }
}
```

### 4.7. Dynamic Dispatch & Reflection

For UI development, strict static typing can be rigid. CH introduces `@dynamic` classes and the `~>` operator.

```swift
var widget: dyn = someObject; // 'dyn' is CHObject*

// Dynamic Call (Message Send)
// Looks up 'setVisible' at runtime. Safe failure if not found.
widget~>setVisible(true); 
```

### 4.8. C++ Interop

#### Direct Embedding (`@cpp`)

```swift
func legacyCall() {
    @cpp
    // Raw C++ code is emitted directly
    printf("Hello from native C++\n");
    @end
}
```

#### Imports & Aliases

```swift
import <iostream>               // System header
import "runtime/CHObject.h"     // Local header
import "lib/Math.h" as Math     // Namespace aliasing
```
Here are the **English translations** for the missing language reference sections. You can insert these into the **"4. Language Reference"** section of your `README.md`.

-----

### Enums

*(Based on `test_enum.ch`)*

Chrono supports both standard C++ enums and scoped enums (strongly typed), allowing specifications for the underlying type.

```swift
// 1. Standard Enum (Unscoped)
enum Color {
    Red,
    Green,
    Blue
}

// 2. Scoped Enum with Underlying Type
// Maps to: enum class State : uint8_t { ... }
enum class State : u8 {
    Idle = 0,
    Running = 1,
    Error = 0xFF
}

// Usage
var s: State = State::Running;
```

### Namespaces

*(Based on `test_namespace.ch`)*

Chrono uses block structures or file-level directives to define namespaces, supporting nested syntax to organize code logic.

```swift
// Define a namespace block
namespace MyGame.Physics;

class Body : CHObject {
    // This class is now inside the C++ namespace MyGame::Physics
}

func calculate() { ... }

// Must close the namespace at the end of the scope/file
endnamespace;

// Usage in other files
var b = new MyGame.Physics.Body();
```

### Type Casting

*(Based on `test_as_cast.ch` and `test_cpp_casts.ch`)*

Chrono provides two casting mechanisms: one for safe object downcasting and one for native C++ type conversions.

#### Safe Dynamic Cast (`as`)

Similar to Swift/Kotlin, this is used for downcasting within the inheritance hierarchy. It returns `nullptr` if the cast fails.

```swift
var obj: dyn = new Button(); // dyn is CHObject*

// Safe cast: returns Button* or nullptr
var btn = obj as Button; 

if (btn) {
    btn->setText("Click");
}
```

#### Native C++ Casts

Direct mapping to C++ casting operators, used for primitive values or low-level pointer manipulation.

```swift
var f: f32 = 10.5;
var i = static_cast<i32>(f);

var rawPtr = reinterpret_cast<void*>(0x1234);
var constPtr = const_cast<i32*>(someConstPtr);
```

### String Literals

*(Based on `test_string_literals.ch`)*

To ensure full compatibility with the C++ ecosystem, Chrono supports various string literal prefixes.

```swift
// 1. Standard String (std::string)
// Automatically wrapped as std::string("...")
var s = "Hello World"; 

// 2. C-Style String (const char*)
// Maps to "..." directly
var raw = c"Legacy C String";

// 3. Wide String (const wchar_t*)
// Maps to L"..."
var wide = L"Unicode String";

// 4. UTF-8 String (C++17 u8)
// Maps to u8"..."
var utf8 = u8"UTF-8 Content";
```

### Type Aliases

*(Based on `test_using_alias.ch`)*

Use the `using` keyword to define type aliases. This is particularly useful for simplifying complex generic types or function pointers.

```swift
// Simple alias
using MyInt = i32;

// Generic alias
// Maps to: using StringVec = std::vector<std::string>;
using StringVec = std::vector<std::string>;

// Function Pointer alias
// Maps to: using Callback = std::function<void(int)>;
using Callback = (i32) -> void;
```

-----

## ⚙️ Build System Configuration

The Chrono build system relies on two core components: **`config.json`** (The Blueprint) and **`make.py`** (The Construction Team).

### 1\. `config.json` — Project Manifest

This file is required at the root of every Chrono project (App or Lib). It defines the project structure, dependencies, and compilation rules.

#### Example Configuration

```json
{
    "package_name": "MyGdiApp",        // CMake project name
    "version": "1.0.0",
    "transpiler_script": "../../src/transpiler.py", 

    // [Dependencies]
    // build.py scans these recursively and adds them to CMake
    "dependencies": {
        "chui":  { "path": "../../libs/chui" },
        "jsonp": { "path": "../../libs/jsonp" }
    },

    // [Build Rules]
    // Defines the Two-Phase Compilation (Headers -> Sources)
    "build_rules": [
        {
            "source_dir": "include",
            "output_dir": "build/dist/include",
            "note": "Public Headers (Phase 1)"
        },
        {
            "source_dir": "src",
            "output_dir": "build/dist/src",
            "note": "Source Files (Phase 2)"
        }
    ],

    // [Resources]
    // Assets to be copied next to the executable after build
    "resources": [
        { "path": "layout.json" },
        { "path": "assets/icon.png", "output": "icon.png" }
    ]
}
```

#### Key Fields:

  * **`dependencies`**: Defines external Chrono libraries. The build system pre-compiles these dependencies to generate `symbols.json` (symbol tables), enabling cross-project referencing.
  * **`build_rules`**: Maps `.ch` source directories to `.cpp` output directories. This separation helps resolve C++ circular dependencies.
  * **`resources`**: Defines runtime assets (e.g., JSON layouts, images). `make.py` automatically copies these to the binary output directory (Debug/Release).

-----

### 2\. `make.py` — Automated Build Runner

`make.py` is a high-level wrapper script. It automates the tedious process of transpilation, CMake configuration, binary compilation, and resource management.

#### The Workflow

When you run `python make.py examples/MyApp --run`, it performs the following steps in order:

1.  **Load Config**: Parses `config.json`.
2.  **Transpile**: Invokes `build.py`. It translates `.ch` files to C++ and regenerates symbol tables. Dependencies are re-transpiled automatically if changed.
3.  **Configure**: Invokes `cmake ..` to generate the build system (Ninja/Visual Studio).
4.  **Build**: Invokes `cmake --build .` to compile the C++ code into binaries (`.exe` / `.lib`).
5.  **Sync Resources**: Copies files defined in the `resources` section to the output folder.
6.  **Run**: Automatically finds and executes the generated binary (if `--run` is specified).

#### Command Arguments

| Argument | Description | Example |
| :--- | :--- | :--- |
| `target` | **[Required]** The project directory path. | `examples/MyGdiApp` |
| `--run` | Run the executable immediately after a successful build. | `python make.py ... --run` |
| `--clean` | Remove the `build_cmake` directory before building. | `python make.py ... --clean` |
| `--config` | Specify build configuration (Debug/Release). | `python make.py ... --config Release` |
| `--vs` | Force usage of the Visual Studio generator. | `python make.py ... --vs` |

-----

## 5\. Contribution Guide

We welcome contributions\! The compiler is written in Python for ease of modification.

1.  **Modify Syntax**: Edit `src/parser/CHLexer.g4` or `CHParser.g4`.
2.  **Regenerate Parser**: Run `gen.bat` (requires Java/ANTLR jar).
3.  **Modify Logic**: Edit `src/CHVisitor.py` (The main transpiler logic).
4.  **Verify**: Run `python run_tests.py` to ensure no regressions.

-----

*Designed for performance, built for clarity.*