import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h"; // 需要 Int::create

func main() -> Int {

    // --- 场景 1: 简单的 while 循环 (使用 bool) ---
    let keep_looping: bool = true;
    while (keep_looping) {
        print("Test 1: Loop executing...");
        keep_looping = false; // 赋值 (现在可以工作了)
    }

    // --- 场景 2: 计数的 while 循环 (使用 i32) ---
    // (这个测试需要我们下一步添加 + 运算符)
    // let count: i32 = 0;
    // while (count < 3) {
    //     print("Test 2: Count:");
    //     print(Int::create(count));
    //     count = count + 1;
    // }

    // --- 场景 3: 永不执行的 while 循环 ---
    while (false) {
        print("Test 3: (This should not print)");
    }

    print("Test 4: Loop finished.");

    return 0;
}