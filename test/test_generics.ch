// file: test/test_generics.ch
// 目的: 验证新的泛型和命名空间类型语法

// 1. 导入 @cpp 块所需的原生 C++ 头文件
import <iostream>;
import <vector>;
import <string>;
import <map>; // 用于测试嵌套泛型

// 2. 导入 Chrono 运行时
import "runtime/ChronoObject.h";
import "runtime/Chrono.h"; // 'print' 函数需要它

func main() -> Int {

    //print("--- Generics Test Start ---");

    // [测试 1: std.vector[i32] (值类型)]
    // Chrono 声明 (无 $)
    // 预期翻译: std::vector<int32_t> v;
    var v: std.vector[i32];
    //print("Declared std.vector[i32] (value type)");

    @cpp
        // C++ 块操作在 Chrono 中声明的 'v'
        v.push_back(100);
        v.push_back(200);
        std::cout << "[C++] v[0]: " << v[0] << std::endl; // 预期: 100
    @end

    // [测试 2: std.string (值类型)]
    // Chrono 声明 (无 $)
    // 预期翻译: std::string s = "Hello";
    var s: std.string = "Hello";
    //print("Declared std.string (value type)");

    @cpp
        // C++ 块操作在 Chrono 中声明的 's'
        s.append(" Generics!");
        std::cout << "[C++] s: " << s << std::endl; // 预期: Hello Generics!
    @end

    // [测试 3: 嵌套泛型 std.map[std.string, std.vector[i32]]]
    // Chrono 声明 (无 $)
    // 预期翻译: std::map<std::string, std::vector<int32_t>> m;
    var m: std.map[std.string, std.vector[i32]];
    //print("Declared nested map (value type)");

    @cpp
        // C++ 块操作在 Chrono 中声明的 'm'
        m["test_key"] = v; // 'v' 是来自测试 1 的 vector
        m["test_key"].push_back(300);
        // 预期: v[2] (即 300)
        std::cout << "[C++] m['test_key'][2]: " << m["test_key"][2] << std::endl;
    @end

   // print("--- Generics Test End ---");
    return 0;
}