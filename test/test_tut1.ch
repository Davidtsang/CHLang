import <iostream>;

func main() -> int{

    let i:int = 2*5;
    let myNum:int;
    myNum = 99;
    @cpp
    std::cout << "Hello world";
    std::cout << "I am learning C++";
    std::cout << i ;
    std::cout << myNum;
    @end
    return 0;
}