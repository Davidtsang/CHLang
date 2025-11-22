import "runtime/ChronoObject.h"
import <iostream>
import <string>

// 1. 定义动态类
@dynamic
class Talker : ChronoObject {
    public init();
    public func say(msg: std::string);
    public func add(a: i32, b: i32);
}

@dynamic
implement Talker {
    init() {}

    func say(msg: std::string) {
        @cpp std::cout << "Talker says: " << msg << std::endl; @end
    }

    func add(a: i32, b: i32) {
        @cpp std::cout << "Sum: " << (a+b) << std::endl; @end
    }
}

func main() -> int {
    @cpp std::cout << "--- Chrono Dynamic Test ---" << std::endl; @end

    var d: dyn = new Talker();
    //var d: dyn = t;

    // 2. 动态调用
    d~>say("Hello World");
    d~>add(10, 20);

    // 3. 调用不存在的方法 (应该安全失败)
    d~>fly();

    d->release();
    return 0;
}