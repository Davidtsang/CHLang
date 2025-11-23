import "runtime/CHObject.h"
import <iostream>
import <string>

// --- 基类 ---
@dynamic
class Animal : CHObject {
    public init();
    public virtual func speak();      // 将被 Dog 重写
    public virtual func sleep();      // 将被子类继承
}

@dynamic
implement Animal {
    init() {}
    func speak() { @cpp std::cout << "Animal makes noise" << std::endl; @end }
    func sleep() { @cpp std::cout << "Zzzzz..." << std::endl; @end }
}

// --- 子类 1: Dog (重写了 speak) ---
@dynamic
class Dog : Animal {
    public init();
    public override func speak(); // 重写
    public func wagTail();        // 新增方法
}

@dynamic
implement Dog {
    init() {}
    func speak() { @cpp std::cout << "Woof! (Dog Override)" << std::endl; @end }
    func wagTail() { @cpp std::cout << "Dog wags tail" << std::endl; @end }
}

// --- 子类 2: Cat (完全继承) ---
@dynamic
class Cat : Animal {
    public init();
    // Cat 没有重写 speak，也没有重写 sleep
}

@dynamic
implement Cat {
    init() {}
}

func main() -> int {
    @cpp std::cout << "--- Inheritance Test ---" << std::endl; @end

    // 使用 dyn 容器
    var d: dyn;

    // 1. 测试 Dog (重写)
    d = new Dog();

    @cpp std::cout << "[Dog]" << std::endl; @end
    d~>speak();    // 预期: "Woof!" (找到了 Dog 的实现)
    d~>wagTail();  // 预期: "Dog wags tail" (找到了 Dog 的实现)
    d~>sleep();    // 预期: "Zzzzz..." (Dog 没找到，去 Animal 找)

    // 2. 测试 Cat (继承)
    d = new Cat();

    @cpp std::cout << "[Cat]" << std::endl; @end
    d~>speak();    // 预期: "Animal makes noise" (Cat 没找到，去 Animal 找)
    d~>sleep();    // 预期: "Zzzzz..." (Cat 没找到，去 Animal 找)
    d~>wagTail();  // 预期: Runtime Error (Cat 和 Animal 都没有)

    return 0;
}