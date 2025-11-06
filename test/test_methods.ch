import "Chrono.h";
import "ChronoObject.h";
import "ChronoString.h";
import "ChronoInt.h";

func main() -> int {
    // [修复] 必须使用 '$' 标记并显式调用 'String.create'
    let $greeting: String = String.create("Hello");

    // [修复] 必须使用 '$greeting' 访问
    let $len: Int = $greeting.length();

    // 打印 ChronoInt 对象
    Chrono.log($len);

    // [修复] 必须释放所有 MRC 对象
    $greeting.release();
    $len.release();

    return 0;
}