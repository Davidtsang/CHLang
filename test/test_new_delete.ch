// file: test/test_new_delete.ch
// 目的: 验证工厂模式和显式的 'new'/'delete'

import "runtime/CHObject.h"
import "runtime/CHString.h"
import "runtime/CH.h" // <-- [新增] 'print' 需要它

// 1. MRC Class (使用工厂方法)
class MRCClass : CHObject {

    // init 默认是 private
    init() ;

    deinit;

    // [更改] 返回类型必须标记为 $
    public static func create() -> MRCClass*;
}

implement MRCClass{
    init() { CH::log("MRC Init"); }

    deinit { CH::log("MRC Deinit"); }

    // [更改] 返回类型必须标记为 $
    func create() -> MRCClass* {
        return new MRCClass();
    }

}
// 2. Native Class (测试 new/delete 的目标)
class NativeClass {

    // init 默认是 private
    init();

    // [更改] 返回类型必须标记为 $
    public static func create() -> NativeClass* ;
}

implement NativeClass{
    init() { CH::log("Native Init"); }

    // [更改] 返回类型必须标记为 $
    func create() -> NativeClass* {
        return new NativeClass();
    }
}

func main() -> int {

    CH::log("--- Test Start ---");

    // SCENARIO A: 安全的 MRC 模式 (通过工厂调用)
    var objA: MRCClass* = MRCClass::create();
    CH::log("A: MRC object created (Factory).");
    objA->release(); // 自动调用 deinit

    // SCENARIO B: 手动 NEW/DELETE 模式 (通过工厂调用)

    // [KEY TEST 1] 使用工厂方法创建对象
    var objB: NativeClass* = NativeClass::create();
    CH::log("B: Native object created (Factory).");

    // [KEY TEST 2] 使用 DELETE 关键字释放对象
    delete objB; // 手动调用 delete
    CH::log("B: Native object deleted (explicit DELETE).");

    CH::log("--- Test End ---");

    return 0;
}