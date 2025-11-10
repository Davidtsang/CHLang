// file: test/test_logical_ops.ch
// 目的: 验证逻辑运算符 (&&, ||, !) 和取模 (%)

import "runtime/Chrono.h";
import "runtime/ChronoObject.h";

func main() -> int {
    Chrono.log("--- Logical/Modulo Ops Test ---");

    var a: i32 = 10;
    var b: i32 = 3;
    var c: i32 = -5;

    // --- 测试 1: 取模 (%) ---
    // 预期: 1 (10 % 3)
    var mod_result: i32 = a % b;
    Chrono.log("Test 1: 10 % 3");
    Chrono.log(mod_result);

    // --- 测试 2: 逻辑非 (!) ---
    if (!false) {
        Chrono.log("Test 2: !false PASS");
    }

    // --- 测试 3: 逻辑与 (&&) ---
    if (true && (a > 0)) {
        Chrono.log("Test 3: true && (a > 0) PASS");
    }
    if (true && (c > 0)) {
        // c 是 -5, (c > 0) 是 false
        Chrono.log("Test 3: && FAIL (Should not print)");
    } else {
        Chrono.log("Test 3: true && (c > 0) is false PASS");
    }

    // --- 测试 4: 逻辑或 (||) ---
    if (false || (a > 0)) {
        Chrono.log("Test 4: false || (a > 0) PASS");
    }

    // --- 测试 5: 优先级 (C++ 处理) ---
    // 预期: (10 % 3) == 1 -> true
    // 预期: (10 > 5) && (3 < 0) -> true && false -> false
    if ((a % b == 1) && (a > 5) && (b < 0 || c < 0)) {
        // (true) && (true) && (false || true) -> true
        Chrono.log("Test 5: Precedence test PASS");
    } else {
        Chrono.log("Test 5: Precedence test FAIL");
    }

    Chrono.log("--- Test End ---");
    return 0;
}