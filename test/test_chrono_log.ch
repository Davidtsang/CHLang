// file: test/test_chrono_log.ch
// 目的: 验证 Chrono.log 运行时函数

import "runtime/Chrono.h" as Chrono;
import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";

func main() -> int {

    Chrono.log("--- Chrono.log Test Start ---");

    // Test 1: 打印 i32 (值类型)
    let x: i32 = 123;
    Chrono.log("Test 1 (i32):");
    Chrono.log(x); // 预期: 123

    // Test 2: 打印 bool (值类型)
    Chrono.log("Test 2 (bool):");
    Chrono.log(true); // 预期: true

    // Test 3: 打印 C++ 字符串字面量
    Chrono.log("Test 3 (Literal):");
    Chrono.log("Hello Literal"); // 预期: Hello Literal

    // Test 4: 打印 String (MRC 对象)
    // [ 更改 ] 使用 '$' 标记内存责任
    let $s: String = String.create("MRC String");
    Chrono.log("Test 4 (String):");
    Chrono.log($s);
    $s.release();

    // Test 5: 打印 Int (MRC 对象)
    // [ 更改 ] 使用 '$' 标记内存责任
    let $i: Int = Int.create(456);
    Chrono.log("Test 5 (Int):");
    Chrono.log($i);
    $i.release();

    Chrono.log("--- Chrono.log Test End ---");
    return 0;
}