// file: test/test_while_loop.ch
// 目的: 验证 while 循环, 赋值, 和 i32 比较

import "runtime/CHObject.h"
import "runtime/CHString.h"
import "runtime/CHInt.h"
import "runtime/CH.h" // <-- [新增] 'print' 需要它

func main() -> int {

    // --- 场景 1: 简单的 while 循环 (使用 bool) ---
    var keep_looping: bool = true;
    while (keep_looping) {
        CH::Log("Test 1: Loop executing...");
        keep_looping = false; // 赋值
    }

    // --- 场景 2: 计数的 while 循环 (使用 i32) ---
    // [修改] 已取消注释，因为 < 和 + 运算符现在受支持
    var count: i32 = 0;
    while (count < 3) {
        CH::Log("Test 2: Count:");
        // [修改] CH::Log(i32) 是支持的，不需要 Int::create
        CH::Log(count);
        count = count + 1;
    }

    // --- 场景 3: 永不执行的 while 循环 ---
    while (false) {
        CH::Log("Test 3: (This should not print)");
    }

    CH::Log("Test 4: Loop finished.");

    return 0;
}