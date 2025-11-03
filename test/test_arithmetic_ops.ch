import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";

func main() -> Int {
    let a: i32 = 10;
    let b: i32 = 5;
    let result: i32 = 0; // 可变局部变量 (得益于我们移除了 const)

    print("--- Arithmetic Tests ---");

    // Test 1: 加法 (+) (10 + 5 = 15)
    result = a + b;
    if (result == 15) {
        print("T1: ADDITION PASS");
    } else {
        print("T1: ADDITION FAIL");
    }

    // Test 2: 减法 (-) (10 - 5 = 5)
    result = a - b;
    if (result == 5) {
        print("T2: SUBTRACTION PASS");
    } else {
        print("T2: SUBTRACTION FAIL");
    }

    // Test 3: 乘法 (*) (10 * 5 = 50)
    result = a * b;
    if (result == 50) {
        print("T3: MULTIPLICATION PASS");
    } else {
        print("T3: MULTIPLICATION FAIL");
    }

    // Test 4: 除法 (/) (10 / 5 = 2)
    result = a / b;
    if (result == 2) {
        print("T4: DIVISION PASS");
    } else {
        print("T4: DIVISION FAIL");
    }

    // Test 5: 组合赋值与比较 (10 * 5 == 50)
    if ((a * b) == 50) {
        print("T5: COMBINATION PASS");
    } else {
        print("T5: COMBINATION FAIL");
    }

    return 0;
}