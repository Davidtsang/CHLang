import "Chrono.h"
import "runtime/ChronoObject.h"
import "runtime/ChronoString.h"

func main() -> int {

    // --- 场景 1: IF (单语句) ---
    // 验证：单语句块 (我们的核心 bug)
    if (true) {
        Chrono.log("Test 1: IF (Single)");
    }

    // --- 场景 2: IF (多语句) ---
    // 验证：多语句块 (这个一直能用)
    if (true) {
        Chrono.log("Test 2: IF (Multi 1)");
        Chrono.log("Test 2: IF (Multi 2)");
    }

    // --- 场景 3: IF / ELSE ---
    // 验证：IF (单) / ELSE (单)
    if (false) {
        Chrono.log("Test 3: IF (FAIL)");
    } else {
        Chrono.log("Test 3: ELSE (Single)");
    }

    // --- 场景 4: IF / ELSE IF / ELSE ---
    // 验证：IF (空) / ELSE IF (单) / ELSE (多)
    if (false) {
        // 空块
    } else if (true) {
        Chrono.log("Test 4: ELSE IF (Single)");
    } else {
        Chrono.log("Test 4: ELSE (FAIL 1)");
        Chrono.log("Test 4: ELSE (FAIL 2)");
    }

    // --- 场景 5: IF / ELSE IF (全 false) / ELSE ---
    // 验证：链条落入最终的 ELSE 块
    if (false) {
        Chrono.log("Test 5: IF (FAIL)");
    } else if (false) {
        Chrono.log("Test 5: ELSE IF (FAIL)");
    } else {
        Chrono.log("Test 5: ELSE (Multi 1)");
        Chrono.log("Test 5: ELSE (Multi 2)");
    }

    // --- 场景 6: 嵌套在 IF 块中 ---
    // 验证：嵌套的 IF / ELSE
    if (true) {
        Chrono.log("Test 6: Outer IF");
        if (false) {
            Chrono.log("Test 6: Inner IF (FAIL)");
        } else {
            Chrono.log("Test 6: Inner ELSE");
        }
    }

    // --- 场景 7: 嵌套在 ELSE IF 块中 ---
    // 验证：嵌套的 IF / ELSE IF
    if (false) {
        Chrono.log("Test 7: IF (FAIL)");
    } else if (true) {
        Chrono.log("Test 7: Outer ELSE IF");
        if (false) {
            Chrono.log("Test 7: Inner IF (FAIL)");
        } else if (true) {
            Chrono.log("Test 7: Inner ELSE IF");
        }
    }

    // --- 场景 8: 嵌套在 ELSE 块中 ---
    // 验证：嵌套的 IF (单) / ELSE (多)
    if (false) {
        Chrono.log("Test 8: IF (FAIL)");
    } else {
        Chrono.log("Test 8: Outer ELSE");
        if (true) {
            Chrono.log("Test 8: Inner IF (Single)");
        } else {
            Chrono.log("Test 8: Inner ELSE (FAIL 1)");
            Chrono.log("Test 8: Inner ELSE (FAIL 2)");
        }
    }

    return 0;
}