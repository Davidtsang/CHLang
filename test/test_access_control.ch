// file: test/test_access_control.ch
// 目的: [已更新] 验证 '$' 引用标记和 public/private

import "runtime/Chrono.h";
import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";

class AccessTest : ChronoObject {

    // --- 1. 属性 (默认 Private) ---
    let val: i32; // 值类型，无 $

    // Why: 'String' 是引用类型，必须使用 $
    let $name: String;

    // --- 2. 构造函数 (默认 Private) ---
    // Why: 'n' 是引用类型，必须使用 $
    init(v: i32, $n: String) {
        // Why: 翻译器现在将 print() 映射到 Chrono.log()
        Chrono.log("Init (Private)");
        this.val = v;
        this.$name = $n;
        this.$name.retain();
    }

    // --- 3. 析构函数 (自动 Public) ---
    deinit {
        Chrono.log("Deinit (Public)");
        this.$name.release();
    }

    // --- 4. 私有方法 (Private by Default) ---
    func doInternalCalc() -> i32 { // 'i32' 是值类型
        Chrono.log("Private Method: doInternalCalc()");
        return this.val * 2;
    }

    // --- 5. 公共方法 (Public) ---
    // Why: 'Int' (ChronoInt) 是引用类型，返回值必须使用 $
    public func getCalculatedValue() -> $Int {
        Chrono.log("Public Method: getCalculatedValue()");
        let result: i32 = this.doInternalCalc();
        return Int.create(result);
    }

    // --- 6. 公共静态工厂 (Public Static) ---
    // Why: 'n' 和 'AccessTest' 都是引用类型，必须使用 $
    public static func create(v: i32, $n: String) -> $AccessTest {
        Chrono.log("Public Static: create()");
        // Why: 'new' 关键字现在是必需的
        return new AccessTest(v, $n);
    }
}


// Why: main 必须返回 'int' (C++ 值类型)，而不是 '$Int'
func main() -> int {


    @cpp std::cout <<  "--- Test Start ---" << std::endl; @end
    // Why: String.create 返回一个引用类型，必须使用 $s
    let $s: String = String.create("Test");

    // 1. 调用 Public Static 方法
    // Why: AccessTest.create 返回引用类型，必须使用 $obj
    let $obj: AccessTest = AccessTest.create(10, $s);

    // 2. 调用 Public Instance 方法
    // Why: getCalculatedValue 返回引用类型，必须使用 $val_obj
    let $val_obj: Int = $obj.getCalculatedValue();

    // 3. 验证结果
    Chrono.log("Final Value:");
    Chrono.log($val_obj); // 预期: 20

    // 4. 释放 (现在所有变量名都正确地以 $ 开头)
    $s.release();
    $obj.release(); // 这将触发 Deinit
    $val_obj.release();

    Chrono.log("--- Test End ---");
    return 0; // 返回一个 C++ int 值
}