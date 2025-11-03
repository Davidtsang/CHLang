import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";

func main() -> Int {

    // --- Test 1: IF 块中嵌套 WHILE ---
    if (true) {
        print("T1: IF entered"); // 1. IF 块开始执行

        // 我们使用一个可变的 let 变量 (现在可以工作了)
        let flag_a: bool = true;

        while (flag_a) {
            print("T1: Inner WHILE executing"); // 2. WHILE 循环执行一次
            flag_a = false; // 终止循环
        }

        print("T1: IF block finished"); // 3. IF 块完成
    } else {
        print("T1: ELSE skipped"); // 不执行
    }

    // --- Test 2: ELSE 块中嵌套 WHILE ---
    if (false) {
        print("T2: IF skipped"); // 不执行
    } else {
        print("T2: ELSE entered"); // 4. ELSE 块开始执行

        let flag_b: bool = true;

        while (flag_b) {
            print("T2: Inner WHILE executing"); // 5. WHILE 循环执行一次
            flag_b = false; // 终止循环
        }

        print("T2: ELSE block finished"); // 6. ELSE 块完成
    }

    return 0;
}