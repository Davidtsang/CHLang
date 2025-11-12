// file: test/test_access_control.ch
// 目的: [已修复] 验证 '*' 引用标记和 public/private

import "runtime/Chrono.h"
import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";

class AccessTest : ChronoObject {

    // --- 1. 属性 (默认 Private) ---
    var val: i32;
    var name: String*; // [正确]

    // --- 2. 构造函数 (默认 Private) ---
    // [修复] 参数 'n' 必须是 String*
    init(v: i32, n: String*) {
        Chrono.log("Init (Private)");
        this.val = v;
        this.name = n;
        this.name.retain();
    }

    // --- 3. 析构函数 (自动 Public) ---
    deinit {
        Chrono.log("Deinit (Public)");
        this.name.release();
    }

    // --- 4. 私有方法 (Private by Default) ---
    func doInternalCalc() -> i32 {
        Chrono.log("Private Method: doInternalCalc()");
        return this.val * 2;
    }

    // --- 5. 公共方法 (Public) ---
    // [修复] 返回类型必须是 Int*
    public func getCalculatedValue() -> Int* {
        Chrono.log("Public Method: getCalculatedValue()");
        var result: i32 = this.doInternalCalc();
        return Int.create(result);
    }

    // --- 6. 公共静态工厂 (Public Static) ---
    // [修复] 'n' 和返回类型必须是 'String*' 和 'AccessTest*'
    public static func create(v: i32, n: String*) -> AccessTest* {
        Chrono.log("Public Static: create()");
        return new AccessTest(v, n);
    }
}


// Why: main 必须返回 'int' (C++ 值类型)，而不是 'Int'
func main() -> int {


    @cpp std::cout <<  "--- Test Start ---" << std::endl; @end

    // [正确]
    var s: String* = String.create("Test");

    // [正确] (现在将匹配修复后的 create 签名)
    var obj: AccessTest* = AccessTest.create(10, s);

    // [正确] (现在将匹配修复后的 getCalculatedValue 签名)
    var val_obj: Int* = obj.getCalculatedValue();

    // 3. 验证结果
    Chrono.log("Final Value:");
    Chrono.log(val_obj); // 预期: 20

    // 4. 释放
    s.release();
    obj.release(); // 这将触发 Deinit
    val_obj.release();

    Chrono.log("--- Test End ---");
    return 0; // 返回一个 C++ int 值
}