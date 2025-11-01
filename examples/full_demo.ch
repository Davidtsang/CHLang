// examples/full_demo.ch

// 1. 导入依赖
import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";
import <iostream>; // C++ 标准库 for debug output

// 2. 假设的辅助函数 (用于演示方法调用)
func get_count() -> Int {
    // 假设 ChronoInt::create(5) 存在
    let five: Int = 5; 
    return five; // 返回 ARC-managed Int
}

// 3. 入口函数
func main() -> Int {
    // 变量声明 (let -> const Ref<String>)
    let greeting: String = "Hello, Chrono Partner!";
    
    // 方法调用 (Dot Syntax -> smart pointer ->)
    let length_obj: Int = greeting.length();
    
    // 原生 C++ 混编块：调用 C++ 标准函数和原生类型
    @cpp 
        // 这里的 length_obj 是一个 Ref<Int>
        // 我们可以调用它的 getValue() 方法获取原生 int
        if (length_obj->getValue() > 10) {
            std::cout << "String is long. ARC count: " << length_obj.use_count() << std::endl;
        } else {
            std::cout << "String is short." << std::endl;
        }
    @end  
    
    // I/O 输出
    print(length_obj);
    
    // 返回 (映射到 C++ int)
    return 0;
}