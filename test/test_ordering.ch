// file: test/test_ordering.ch
// 
// 目的：验证 @cpp 块和 Chrono 语句
// 是否在全局和函数作用域内按正确顺序翻译。

// 1. 导入 C++ 库，为全局 @cpp 块做准备
import <iostream>;
import <string>;

// 2. 一个全局 @cpp 块 (用于声明)
// 这应该出现在所有 'func' 定义之前
@cpp
    // 声明一个 C++ 原生全局变量
    std::string global_test_string = "Global C++ Variable";
@end

// 3. 导入 Chrono 库 (用于 'main' 函数)
import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/Chrono.h"; // <-- [新增] 'print' 需要它

// 4. 入口函数
func main() -> Int {

    // 输出 #1: 应该首先出现
    print("Chrono Statement 1");

    // 输出 #2: C++ 块
    @cpp
        std::cout << "C++ Block 1" << std::endl;
    @end

    // Chrono 声明
    // [更改] 必须使用 '$' 和 'String.create'
    let $s: String = String.create("Chrono Statement 2");

    // 输出 #3: Chrono 打印
    print($s); // <-- [更改] 访问 '$s'

    // 输出 #4: 另一个 C++ 块，
    // 它还测试它是否能 "看到" 全局 @cpp 块中声明的变量。
    @cpp
        std::cout << "C++ Block 2 (Accessing: " << global_test_string << ")" << std::endl;
    @end

    // [新增] 必须释放 $s
    $s.release();

    return 0;
}