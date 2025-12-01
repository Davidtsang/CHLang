import "runtime/CH.h"
import <functional>
import <string>
import <iostream>

// 定义别名以方便使用
using IntOp = std::function<i32(i32, i32)>;
using VoidCallback = std::function<void()>;

// 一个接受回调的辅助函数
func runTask(name: std::string, cb: VoidCallback) {
    std::cout << "Task: " << name << std::endl;
    cb();
}

// 一个接受数学运算回调的辅助函数
func compute(a: i32, b: i32, op: IntOp) -> i32 {
    return op(a, b);
}

func main() -> int {
    CH::Log("--- Closure Test Start ---");

    // --- 1. 标准箭头函数 (赋值给变量) ---
    var simple = () => {
        CH::Log("  [1] Simple arrow function executed.");
    };
    simple();

    // --- 2. 带参数的箭头函数 ---
    var add: IntOp = (a: i32, b: i32) => {
        return a + b;
    };
    var sum = add(10, 20);
    std::cout << "  [2] Sum (Explicit Return): " << sum << std::endl;

    // --- 3. 单行表达式 (隐式返回) ---
    // 直接作为参数传递给 compute
    var product = compute(5, 6, (x: i32, y: i32) => x * y);
    std::cout << "  [3] Product (Implicit Return): " << product << std::endl;

    // --- 4. 尾随闭包 (Trailing Closure) ---
    // 这是一个非常现代的 UI 编程风格
    runTask("Trailing Test") {
        CH::Log("  [4] This is a trailing closure block.");
    };

    // --- 5. 变量捕获 (Capture) ---
    var magicNum: i32 = 999;

    // 这里的闭包会自动捕获 magicNum (Copy capture [=])
    runTask("Capture Test") {
        std::cout << "  [5] Captured value is: " << magicNum << std::endl;
    };

    // --- 6. 混合使用 (参数 + 尾随闭包) ---
    // 这是一个模拟按钮点击的场景
    var clickCount: i32 = 0;

    // 注意：我们生成的 lambda 是 mutable 的，所以可以修改捕获的副本
    // 但请注意，std::function 可能会复制 lambda，所以这里的修改通常是针对副本的。
    // 为了测试，我们只读取。

    runTask("Mutable Check") {
        clickCount = clickCount + 1;
        std::cout << "  [6] Inside lambda, clickCount modified to: " << clickCount << std::endl;
    };

    // 外部的 clickCount 不会变，因为是按值捕获 [=]
    std::cout << "  [6] Outer clickCount remains: " << clickCount << std::endl;

    CH::Log("--- Closure Test End ---");
    return 0;
}