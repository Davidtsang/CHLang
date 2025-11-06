// file: test/test_nested_flow.ch
// 目的: 验证 if/else 和 while 嵌套流

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/Chrono.h"; // <-- [新增] 'Chrono.log' 翻译为 'Chrono::log'

func main() -> Int {

    // --- Test 1: IF 块中嵌套 WHILE ---
    if (true) {
        Chrono.log("T1: IF entered"); // 1. IF 块开始执行

        // 'bool' 是值类型，不需要 $
        let flag_a: bool = true;

        while (flag_a) {
            Chrono.log("T1: Inner WHILE executing"); // 2. WHILE 循环执行一次
            flag_a = false; // 终止循环
        }

        Chrono.log("T1: IF block finished"); // 3. IF 块完成
    } else {
        Chrono.log("T1: ELSE skipped"); // 不执行
    }

    // --- Test 2: ELSE 块中嵌套 WHILE ---
    if (false) {
        Chrono.log("T2: IF skipped"); // 不执行
    } else {
        Chrono.log("T2: ELSE entered"); // 4. ELSE 块开始执行

        let flag_b: bool = true;

        while (flag_b) {
            Chrono.log("T2: Inner WHILE executing"); // 5. WHILE 循环执行一次
            flag_b = false; // 终止循环
        }

        Chrono.log("T2: ELSE block finished"); // 6. ELSE 块完成
    }

    return 0;
}