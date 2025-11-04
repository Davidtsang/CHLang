// file: test/test_access_control.ch
// 目的: 全面验证 public/private 属性和方法

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";

class AccessTest : ChronoObject {

    // --- 1. 属性 (默认 Private) ---
    let val: i32;
    let name: String;

    // --- 2. 构造函数 (默认 Private) ---
    // 这强制用户使用 'create' 工厂方法
    init(v: i32, n: String) {
        print("Init (Private)");
        this.val = v;
        this.name = n;
        this.name.retain();
    }

    // --- 3. 析构函数 (自动 Public) ---
    deinit {
        print("Deinit (Public)");
        this.name.release();
    }

    // --- 4. 私有方法 (Private by Default) ---
    // 预期：这个方法不能被 'main' 调用
    func doInternalCalc() -> i32 {
        print("Private Method: doInternalCalc()");
        // [测试] 私有方法可以访问私有属性
        return this.val * 2;
    }

    // --- 5. 公共方法 (Public) ---
    // 预期：这个方法可以被 'main' 调用
    public func getCalculatedValue() -> Int {
        print("Public Method: getCalculatedValue()");
        // [测试] 公共方法调用私有方法
        let result: i32 = this.doInternalCalc();
        return Int.create(result);
    }

    // --- 6. 公共静态工厂 (Public Static) ---
    // 预期：这个方法可以被 'main' 调用
    public static func create(v: i32, n: String) -> AccessTest {
        print("Public Static: create()");
        // [测试] 静态方法调用私有构造函数
        return AccessTest(v, n);
    }
}


func main() -> Int {

    print("--- Test Start ---");

    let s: String = "Test";

    // 1. 调用 Public Static 方法
    let obj: AccessTest = AccessTest.create(10, s);

    // 2. 调用 Public Instance 方法
    let val_obj: Int = obj.getCalculatedValue();

    // 3. 验证结果
    print("Final Value:");
    print(val_obj); // 预期: 20

    // 4. 释放
    s.release();
    obj.release(); // 这将触发 Deinit
    val_obj.release();

    print("--- Test End ---");
    return 0;
}