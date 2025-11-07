import <iostream>;
import <string>;
import "Chrono.h";

func main() -> int {
    let s: std.string = "Helloaaa";

    s.erase(1, 3);

    @cpp
        std::cout << s << std::endl;
    @end
    return 0;
}