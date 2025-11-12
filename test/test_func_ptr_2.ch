import <iostream>;
import <functional>;
import <cstdint>;
import <string>;


func add(i:int) -> void {
   @cpp std::cout << i << std::endl; @end
}

struct Boy{

    var funcCall:((int)-> void)*;
}
func main()-> int {

    var boy:Boy;

    boy.funcCall = add ;
    boy.funCall(6);
    //add(5);

}