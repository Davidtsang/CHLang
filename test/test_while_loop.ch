// file: test/test_while_loop.ch
// 目的: 验证 while 循环, 赋值, 和 i32 比较

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";
import "runtime/Chrono.h"; // <-- [新增] 'print' 需要它

func main() -> int {

    // --- 场景 1: 简单的 while 循环 (使用 bool) ---
    let keep_looping: bool = true;
    while (keep_looping) {
        Chrono.log("Test 1: Loop executing...");
        keep_looping = false; // 赋值
    }

    // --- 场景 2: 计数的 while 循环 (使用 i32) ---
    // [修改] 已取消注释，因为 < 和 + 运算符现在受支持
    let count: i32 = 0;
    while (count < 3) {
        Chrono.log("Test 2: Count:");
        // [修改] Chrono.log(i32) 是支持的，不需要 Int::create
        Chrono.log(count);
        count = count + 1;
    }

    // --- 场景 3: 永不执行的 while 循环 ---
    while (false) {
        Chrono.log("Test 3: (This should not print)");
    }

    Chrono.log("Test 4: Loop finished.");

    return 0;
}