// test/test_virtual.ch
import "runtime/ChronoObject.h"
import <iostream>

class Animal : ChronoObject {
    public init();

    // 1. 普通方法 (非虚)
    public func speak();

    // 2. 虚方法 (显式 virtual)
    public virtual func move();
}

implement Animal {
    init() {}

    func speak() {
        @cpp std::cout << "Animal makes a sound (Static)" << std::endl; @end
    }

    func move() {
        @cpp std::cout << "Animal moves (Virtual)" << std::endl; @end
    }
}

class Dog : Animal {
    public init();

    // 子类普通方法
    public func speak();

    // 3. 重写方法 (显式 override)
    // 注意：父类必须是 virtual
    public override func move();
}

implement Dog {
    init() {}

    func speak() {
        @cpp std::cout << "Dog barks (Static Shadowing)" << std::endl; @end
    }

    func move() {
        @cpp std::cout << "Dog runs (Override)" << std::endl; @end
    }
}

func main() -> int {
    @cpp std::cout << "--- Virtual Test ---" << std::endl; @end

    var dog: Dog* = new Dog();
    var animal: Animal* = dog; // 多态指针

    // 1. 非虚函数调用 (静态绑定)
    // 看指针类型：animal 是 Animal*，调用 Animal::speak
    animal->speak();
    // 预期: "Animal makes a sound" (C++ 行为)

    // 2. 虚函数调用 (动态绑定)
    // 看实际对象：dog 是 Dog 对象，调用 Dog::move
    animal->move();
    // 预期: "Dog runs"

    dog->release();
    return 0;
}