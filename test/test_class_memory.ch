// file: test/test_class_memory.ch
// 目的: 验证 'class', 'deinit', 和 'release()' 的内存模型

import "runtime/ChronoObject.h";
import "<iostream>"; // for std::cout

// 1. 定义一个带 'deinit' 块的类
class MemTest : ChronoObject {
    
    // 2. 'deinit' (析构函数) 会打印一条消息
    deinit {
        // 我们在 deinit 中使用 @cpp 打印，
        // 因为 print() 会 create("...") 一个新对象，
        // 这在析构函数中可能很复杂
        @cpp
            std::cout << "DEINIT" << std::endl;
        @end
    }
}

// 3. 注入一个 C++ 静态 'create' 方法
// (因为我们的语法还不支持 'static func')
@cpp
    MemTest* MemTest::create() {
        return new MemTest();
    }
@end


func main() -> Int {
    
    @cpp
        std::cout << "Start" << std::endl;
    @end
    
    // 4. 创建对象 (RC=1)
    let obj: MemTest = MemTest::create();

    // 5. 释放对象 (RC=0, 触发 deinit)
    obj.release(); 
    
    @cpp
        std::cout << "End" << std::endl;
    @end
    
    return 0;
}