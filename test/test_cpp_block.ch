import "ChronoObject.h";
import <iostream>; // 用于 std::cout

func main() -> int {
    
    @cpp
        std::cout << "Hello from @cpp block!" << std::endl;
    @end
    
    return 0;
}