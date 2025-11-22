import "runtime/ChronoObject.h"
import <iostream>
import <string>
import <any> // 必须导入，因为我们要操作返回值

@dynamic
class Calculator : ChronoObject {
    public init();
    public func add(a: i32, b: i32) -> i32;
    public func getName() -> std::string;
    public func doNothing();
}

@dynamic
implement Calculator {
    init() {}

    func add(a: i32, b: i32) -> i32 {
        return a + b;
    }

    func getName() -> std::string {
        return "Chrono Calc";
    }

    func doNothing() {
        std::cout << "  (Void function executed)" << std::endl; 
    }
}

func main() -> int {
    std::cout << "--- Dynamic Return Value Test ---" << std::endl; 

    var calc: dyn = new Calculator();

    // --- 测试 1: Void 返回值 ---
    std::cout << "[1] Testing void return..." << std::endl; 
    // 动态调用，返回值是 std::any (空的)
    var voidRes = calc~>doNothing();

    @cpp
    if (!voidRes.has_value()) {
        std::cout << "PASS: Void method returned empty std::any." << std::endl;
    } else {
        std::cout << "FAIL: Void method returned value!" << std::endl;
    }
    @end

    // --- 测试 2: Int 返回值 ---
    std::cout << "[2] Testing i32 return (10 + 20)..." << std::endl; 
    // 动态调用
    var intRes = calc~>add(10, 20);

    @cpp
    try {
        // 尝试解包
        int val = std::any_cast<int>(intRes);
        if (val == 30) {
            std::cout << "PASS: Result is " << val << std::endl;
        } else {
            std::cout << "FAIL: Result is " << val << " (expected 30)" << std::endl;
        }
    } catch (const std::bad_any_cast& e) {
        std::cout << "FAIL: Bad cast! " << e.what() << std::endl;
    }
    @end

    // --- 测试 3: String 返回值 ---
    std::cout << "[3] Testing string return..." << std::endl; 
    var strRes = calc~>getName();

    @cpp
    try {
        std::string s = std::any_cast<std::string>(strRes);
        if (s == "Chrono Calc") {
            std::cout << "PASS: Result is '" << s << "'" << std::endl;
        } else {
            std::cout << "FAIL: Result is '" << s << "'" << std::endl;
        }
    } catch (const std::bad_any_cast& e) {
        std::cout << "FAIL: Bad cast! " << e.what() << std::endl;
    }
    @end

    calc->release();
    return 0;
}