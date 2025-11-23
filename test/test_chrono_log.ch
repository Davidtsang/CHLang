// file: test/test_CH_log.ch
// 目的: 验证 CH::log 运行时函数

import "runtime/CH.h" as CH
import "runtime/CHObject.h"
import "runtime/CHString.h"
import "runtime/CHInt.h"

func main() -> int {

    CH::log("--- CH::log Test Start ---");

    // Test 1: 打印 i32 (值类型)
    var x: i32 = 123;
    CH::log("Test 1 (i32):");
    CH::log(x); // 预期: 123

    // Test 2: 打印 bool (值类型)
    CH::log("Test 2 (bool):");
    CH::log(true); // 预期: true

    // Test 3: 打印 C++ 字符串字面量
    CH::log("Test 3 (Literal):");
    CH::log("Hello Literal"); // 预期: Hello Literal

    // Test 4: 打印 String (MRC 对象)
    // [ 更改 ] 使用 '$' 标记内存责任
    var s: String* = String::create("MRC String");
    CH::log("Test 4 (String):");
    CH::log(s);
    s->release();

    // Test 5: 打印 Int (MRC 对象)
    // [ 更改 ] 使用 '$' 标记内存责任
    var i: Int* = Int::create(456);
    CH::log("Test 5 (Int):");
    CH::log(i);
    i->release();

    CH::log("--- CH::log Test End ---");
    return 0;
}