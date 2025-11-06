// file: test/test_new_delete.ch
// 目的: 验证工厂模式和显式的 'new'/'delete'

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/Chrono.h"; // <-- [新增] 'print' 需要它

// 1. MRC Class (使用工厂方法)
class MRCClass : ChronoObject {

    // init 默认是 private
    init() { print("MRC Init"); }

    deinit { print("MRC Deinit"); }

    // [更改] 返回类型必须标记为 $
    public static func create() -> $MRCClass {
        return new MRCClass();
    }
}

// 2. Native Class (测试 new/delete 的目标)
class NativeClass {

    // init 默认是 private
    init() { print("Native Init"); }

    // [更改] 返回类型必须标记为 $
    public static func create() -> $NativeClass {
        return new NativeClass();
    }
}

func main() -> Int {

    print("--- Test Start ---");

    // SCENARIO A: 安全的 MRC 模式 (通过工厂调用)
    let $objA: MRCClass = MRCClass.create();
    print("A: MRC object created (Factory).");
    $objA.release(); // 自动调用 deinit

    // SCENARIO B: 手动 NEW/DELETE 模式 (通过工厂调用)

    // [KEY TEST 1] 使用工厂方法创建对象
    let $objB: NativeClass = NativeClass.create();
    print("B: Native object created (Factory).");

    // [KEY TEST 2] 使用 DELETE 关键字释放对象
    delete $objB; // 手动调用 delete
    print("B: Native object deleted (explicit DELETE).");

    print("--- Test End ---");

    return 0;
}