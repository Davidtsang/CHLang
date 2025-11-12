import <iostream>;

func add(i: int&){
    i +=1;
}
func remove(i: int*){
    *i -=1;
}
func main() -> int{

    var i:int = 2*5;
    var myNum:int;
    myNum = 99;
    add(i);
    remove(&i);

    @cpp
    std::cout << "Hello world";
    std::cout << "I am learning C++";
    std::cout << i ;
    std::cout << myNum;
    @end
    return 0;
}