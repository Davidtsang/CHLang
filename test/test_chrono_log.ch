// file: test/test_CH_log.ch
// 目的: 验证 CH::Log 运行时函数

import "runtime/CH.h" as CH
import "runtime/CHObject.h"
import "runtime/CHString.h"
import "runtime/CHInt.h"

func main() -> int {

    CH::Log("--- CH::Log Test Start ---");

    // Test 1: 打印 i32 (值类型)
    var x: i32 = 123;
    CH::Log("Test 1 (i32):");
    CH::Log(x); // 预期: 123

    // Test 2: 打印 bool (值类型)
    CH::Log("Test 2 (bool):");
    CH::Log(true); // 预期: true

    // Test 3: 打印 C++ 字符串字面量
    CH::Log("Test 3 (Literal):");
    CH::Log("Hello Literal"); // 预期: Hello Literal

    // Test 4: 打印 String (MRC 对象)
    // [ 更改 ] 使用 '$' 标记内存责任
    var s: String* = String::create("MRC String");
    CH::Log("Test 4 (String):");
    CH::Log(s);
    s->release();

    // Test 5: 打印 Int (MRC 对象)
    // [ 更改 ] 使用 '$' 标记内存责任
    var i: Int* = Int::create(456);
    CH::Log("Test 5 (Int):");
    CH::Log(i);
    i->release();

    CH::Log("--- CH::Log Test End ---");
    return 0;
}