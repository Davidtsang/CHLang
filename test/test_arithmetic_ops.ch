// test_arithmetic.ch
import "runtime/CHObject.h"
import "runtime/CHString.h"
import "runtime/CHInt.h"
import "runtime/CH.h" // <-- [新增] 导入 CH 命名空间

// 'main' 必须返回 'Int' 或 'i32'，访问者会将其转为 C++ 'int'
func main() -> int {
    var a: i32 = 10;
    var b: i32 = 5;
    var result: i32 = 0;

    CH::log("--- Arithmetic Tests ---"); // <-- [更改]

    // Test 1: 加法 (+) (10 + 5 = 15)
    result = a + b;
    if (result == 15) {
        CH::log("T1: ADDITION PASS"); // <-- [更改]
    } else {
        CH::log("T1: ADDITION FAIL"); // <-- [更改]
    }

    // Test 2: 减法 (-) (10 - 5 = 5)
    result = a - b;
    if (result == 5) {
        CH::log("T2: SUBTRACTION PASS"); // <-- [更改]
    } else {
        CH::log("T2: SUBTRACTION FAIL"); // <-- [更改]
    }

    // Test 3: 乘法 (*) (10 * 5 = 50)
    result = a * b;
    if (result == 50) {
        CH::log("T3: MULTIPLICATION PASS"); // <-- [更改]
    } else {
        CH::log("T3: MULTIPLICATION FAIL"); // <-- [更改]
    }

    // Test 4: 除法 (/) (10 / 5 = 2)
    result = a / b;
    if (result == 2) {
        CH::log("T4: DIVISION PASS"); // <-- [更改]
    } else {
        CH::log("T4: DIVISION FAIL"); // <-- [更改]
    }

    // Test 5: 组合赋值与比较 (10 * 5 == 50)
    if ((a * b) == 50) {
        CH::log("T5: COMBINATION PASS"); // <-- [更改]
    } else {
        CH::log("T5: COMBINATION FAIL"); // <-- [更改]
    }

    return 0;
}