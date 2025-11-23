import <iostream>
import <string>
import "CH.h"

func change(s: std.string*){

    *s = "Hbcelloaaa";
}

func change2(s: std::string&){

    s = "Hbcelloaaa";
}

func main() -> int {

    var s: std::string = "Hello";

    change2(s);

    @cpp
        std::cout << s << std::endl;
    @end
    return 0;
}
