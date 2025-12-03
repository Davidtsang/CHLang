// file: test/test_performance.ch
import "runtime/CHObject.h"
import <iostream>
import <chrono> // C++ 时间库

@dynamic
class Calculator : CHObject {
    public init();
    public func add(a: i32) -> i32;
}

@dynamic
implement Calculator {
    init() {}

    // 一个极其简单的函数，以突出调用本身的开销
    func add(a: i32) -> i32 {
        return a + 1;

    }
}

func main() -> int {
    @cpp std::cout << "--- Performance Benchmark (1M calls) ---" << std::endl; @end

    var calc: Calculator* = new Calculator();
    var dynCalc: dyn = calc;
    var count: i32 = 1000000; // 100万次
    var sum: i32 = 0;

    // --- 1. 静态调用 (Static Dispatch) ---
    // 这是 C++ 的原生虚函数调用速度，作为基准线
    @cpp
    auto start1 = std::chrono::high_resolution_clock::now();
    @end

    for (var i: i32 = 0; i < count; i = i + 1) {
        sum = calc->add(sum);
    }

    @cpp
    auto end1 = std::chrono::high_resolution_clock::now();
    auto dur1 = std::chrono::duration_cast<std::chrono::milliseconds>(end1 - start1).count();
    std::cout << "Static  (Direct): " << dur1 << " ms" << std::endl;
    @end

    // 重置
    sum = 0;

    // --- 2. 动态调用 (Dynamic Dispatch) ---
    // 第一次调用：预热缓存 (Warm up)
    dynCalc~>add(0);

    @cpp
    auto start2 = std::chrono::high_resolution_clock::now();
    @end

    for (var j: i32 = 0; j < count; j = j + 1) {
        // [关键] 这里测试缓存性能
        // 如果没有缓存，这里每次都会遍历继承树，速度会非常慢
        // 有了 thread_local 缓存，这里应该是 O(1) 的哈希查找
        var res = dynCalc~>add(sum);

        // 提取结果 (这一步也有 any_cast 开销，但在所难免)
        @cpp
        sum = std::any_cast<int32_t>(res);
        @end
    }

    @cpp
    auto end2 = std::chrono::high_resolution_clock::now();
    auto dur2 = std::chrono::duration_cast<std::chrono::milliseconds>(end2 - start2).count();
    std::cout << "Dynamic (Cached): " << dur2 << " ms" << std::endl;

    // 计算开销比例 (通常动态调用会比静态慢 3-10 倍，如果没有缓存则是 50倍+)
    if (dur1 > 0) {
        std::cout << "Ratio (Dyn/Sta):  " << (double)dur2 / (double)dur1 << "x" << std::endl;
    }
    @end

    calc->release();

    // 输出固定字符串以便 run_tests.py 通过
    @cpp std::cout << "Benchmark Completed" << std::endl; @end
    return 0;
}