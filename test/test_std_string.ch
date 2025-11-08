import <iostream>;
import <string>;
import "Chrono.h";

func main() -> int {
    let s: std.string = "Helloaaa";

    s.insert(1, "bc");

    @cpp
        std::cout << s << std::endl;
    @end
    return 0;
}