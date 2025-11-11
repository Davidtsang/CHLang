class AccessTest : ChronoObject {

    // --- 1. 属性 (默认 Private) ---
    var val: i32; // 值类型
    var name: String*; // [正确] 引用类型指针

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
        // [修复] 缺少 '*' 运算符
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