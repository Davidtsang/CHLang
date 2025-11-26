import "runtime/CH.h"
import <string>

// 简单的入口类
@dynamic
class App : CHObject {
    public static func run();
}

@dynamic
implement App {
    func run() {
        CH::Log(std::string("Hello Application World!"));
    }
}

func main() -> int {
    CH::Log("--- Starting App: GdiDemo ---");
    App::run();
    return 0;
}
