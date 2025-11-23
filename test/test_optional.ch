import "runtime/CHObject.h"
import <iostream>
import <string>

// --- 1. 定义协议 (Protocol) ---
interface Delegate {
    // [必须] 这是一个标准的 C++ 纯虚函数
    public func doRequired();

    // [可选] 这是一个“幻影”方法，不会生成 C++ 纯虚函数声明
    @optional
    public func doOptional(msg: std::string);
}

// --- 2. 场景 A: 全能工 (实现了所有方法) ---
@dynamic
class FullWorker : CHObject with Delegate {
    public init();

    // 实现必须方法 (C++ override)
    public override func doRequired();

    // 实现可选方法 (Dynamic Method)
    public func doOptional(msg: std::string);
}

@dynamic
implement FullWorker {
    init() {}

    func doRequired() {
        @cpp std::cout << "[Full] Required task done." << std::endl; @end
    }

    func doOptional(msg: std::string) {
        @cpp std::cout << "[Full] Optional task: " << msg << std::endl; @end
    }
}

// --- 3. 场景 B: 懒惰工 (只实现了必须方法) ---
@dynamic
class LazyWorker : CHObject with Delegate {
    public init();

    // 只实现必须的，不写 optional，C++ 编译器不应该报错
    public override func doRequired();
}

@dynamic
implement LazyWorker {
    init() {}

    func doRequired() {
        @cpp std::cout << "[Lazy] Required task done." << std::endl; @end
    }
    // 没有 doOptional
}

// --- 4. 测试逻辑 ---
func main() -> int {
    @cpp std::cout << "--- Optional Interface Test ---" << std::endl; @end

    // 1. 创建对象
    var full: FullWorker* = new FullWorker();
    var lazy: LazyWorker* = new LazyWorker();

    // 2. 静态调用测试 (->)
    // 必须方法可以通过静态接口调用
    var d1: Delegate* = full;
    var d2: Delegate* = lazy;

    @cpp std::cout << "1. Static Call (Required):" << std::endl; @end
    d1->doRequired();
    d2->doRequired();

    // 静态调用可选方法是不可能的，下面这行如果取消注释，编译会报错 (C2039)
    // d1->doOptional("Fail");

    // 3. 动态调用测试 (~>)
    // 我们把它们都当作 dyn (CHObject*)
    var dyn1: dyn = full;
    var dyn2: dyn = lazy;

    @cpp std::cout << "2. Dynamic Call (Optional on Full):" << std::endl; @end
    // FullWorker 实现了，应该成功
    dyn1~>doOptional(@"Hello World");

    @cpp std::cout << "3. Dynamic Call (Optional on Lazy):" << std::endl; @end
    // LazyWorker 没实现。
    // 预期行为：运行时安全失败 (打印 Selector not found)，但程序不会崩溃
    dyn2~>doOptional(@"Should not crash");

    full->release();
    lazy->release();
    return 0;
}