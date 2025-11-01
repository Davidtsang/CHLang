// file: test/test_class_memory.ch

import "runtime/ChronoObject.h";
import <iostream>;

// 1. 定义一个带 'deinit' 块的类
class MemTest : ChronoObject {
    
    // 2. 'deinit' (析构函数)
    deinit {
        @cpp
            std::cout << "DEINIT" << std::endl;
        @end
    }
    
    // 3. [ 关键修正 ]
    // 我们必须在这里 *声明* C++ 静态方法
    @cpp
        public: // (可选，但良好)
        static MemTest* create();
    @end
}

// 4. [ 保持不变 ] 
// 在全局作用域 *定义* 该方法
@cpp
    MemTest* MemTest::create() {
        return new MemTest();
    }
@end


func main() -> Int {
    @cpp
        std::cout << "Start" << std::endl;
    @end
    
    // 5. 现在可以被正确调用
    let obj: MemTest = MemTest.create();
    obj.release(); 
    
    @cpp
        std::cout << "End" << std::endl;
    @end
    
    return 0;
}