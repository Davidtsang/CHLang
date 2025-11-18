// file: test/test_access_control.ch
// 目的: [已重构] 验证分离的声明 (class) 和实现 (implement)

import "runtime/Chrono.h"
import "runtime/ChronoObject.h"
import "runtime/ChronoString.h"
import "runtime/ChronoInt.h"

// ---------------------------------------------------
// 1. API 声明 (Declaration Block)
// (这类似于 .h.ch 文件的内容)
// ---------------------------------------------------
class AccessTest : ChronoObject {

    // --- 1. 属性 (默认 Private) ---
    var val: i32;
    var name: String*; // [正确]

    // --- 2. 构造函数 (私有 声明) ---
    init(v: i32, n: String*); // <-- [重构] 移除了函数体

    // --- 3. 析构函数 (自动 Public 声明) ---
    deinit; // <-- [重构] 移除了函数体

    // --- 4. 私有方法 (私有 声明) ---
    func doInternalCalc() -> i32; // <-- [重构] 移除了函数体

    // --- 5. 公共方法 (Public 声明) ---
    public func getCalculatedValue() -> Int*; // <-- [重构] 移除了函数体

    // --- 6. 公共静态工厂 (Public 声明) ---
    public static func create(v: i32, n: String*) -> AccessTest*; // <-- [重构] 移除了函数体
}

// ---------------------------------------------------
// 2. API 实现 (Implementation Block)
// [ [ [ 新增 ] ] ]
// ---------------------------------------------------
implement AccessTest {

    // --- 2. 构造函数 (实现) ---
    init(v: i32, n: String*) {
        Chrono::log("Init (Private)");
        this->val = v; // 'this->' 在 class 中被 Visitor 翻译为 'this->'
        this->name = n;
        this->name->retain();
    }

    // --- 3. 析构函数 (实现) ---
    deinit {
        Chrono::log("Deinit (Public)");
        this->name->release();
    }

    // --- 4. 私有方法 (实现) ---
    func doInternalCalc() -> i32 {
        Chrono::log("Private Method: doInternalCalc()");
        return this->val * 2;
    }

    // --- 5. 公共方法 (实现) ---
   func getCalculatedValue() -> Int* {
        Chrono::log("Public Method: getCalculatedValue()");
        var result: i32 = this->doInternalCalc();
        return Int::create(result);
    }

    // --- 6. 公共静态工厂 (实现) ---
    func create(v: i32, n: String*) -> AccessTest* {
        Chrono::log("Public Static: create()");
        return new AccessTest(v, n);
    }
}


// ---------------------------------------------------
// 3. 应用程序 (Application Block)
// ---------------------------------------------------
func main() -> int {

    std::cout <<  "--- Test Start ---" << std::endl;

    // [正确]
    var s: String* = String::create("Test");

    // [正确]
    var obj: AccessTest* = AccessTest::create(10, s);

    // [正确] (ChronoVisitor 会将 '.' 翻译为 '->')
    var val_obj: Int* = obj->getCalculatedValue();

    // 3. 验证结果
    Chrono::log("Final Value:");
    Chrono::log(val_obj); // 预期: 20

    // 4. 释放
    s->release();
    obj->release(); // 这将触发 Deinit
    val_obj->release();

    Chrono::log("--- Test End ---");
    return 0; // 返回一个 C++ int 值
}