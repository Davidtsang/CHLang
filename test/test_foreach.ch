import "runtime/CH.h"
import <vector>
import <map>
import <string>
import <iostream>

func main() -> int {
    CH::Log("--- Foreach Test ---");

    // 1. Vector 遍历
    var vec: std::vector<i32>;
    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(30);

    CH::Log("Vector:");
    // 语法: for (var item in container)
    for (var num in vec) {
        CH::Log(num);
    }

    // 2. Map 遍历
    var dict: std::map<std::string, std::string>;
    dict["A"] = "Apple";
    dict["B"] = "Banana";

    CH::Log("Map:");
    // C++ map 迭代器解引用后是 std::pair<const Key, Value>
    // item.first 是 Key, item.second 是 Value
    for (var kv in dict) {
        @cpp
        std::cout << kv.first << " -> " << kv.second << std::endl;
        @end
    }

    // 3. 显式类型遍历 (测试 Parser)
    for (var x: i32 in vec) {
        // 这里的 x 是 int32_t 副本
    }

    return 0;
}