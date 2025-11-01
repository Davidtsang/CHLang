import "ChronoObject.h";
import "ChronoString.h";
import "ChronoInt.h";

func main() -> Int {
    let greeting: String = "Hello";
    
    // 调用 greeting.length()，返回 Ref<ChronoInt>
    let len: Int = greeting.length();
    
    // 打印 ChronoInt 对象
    print(len);
    return 0;
}