// file: test/test_chaining.ch
// 目的: 验证 'public' 关键字, '$' 标记和链式调用

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";
import "runtime/Chrono.h"; // <-- [新增]

// 1. 定义一个用于 'this' 链测试的类
class Wrapper : ChronoObject {
    var $s: String; // <-- [更改] 's' 是一个指针 ($)

    // 默认 private (只能被 'create' 调用)
    init($str: String) { // <-- [更改] 'str' 是一个指针 ($)
        this.$s = $str;   // <-- [更改]
        this.$s.retain(); // <-- [更改]
    }

    deinit {
        this.$s.release(); // <-- [更改]
    }

    // [关键] 必须是 public 才能被 'main' 调用
    public static func create($str: String) -> $Wrapper { // <-- [更改]
        return new Wrapper($str); // <-- [更改] 'new' 和 ';'
    }

    // [关键] 必须是 public 才能被 'main' 调用
    public func getUpperLength() -> $Int { // <-- [更改]
        // [ 测试点 A ] 'this.member.method().method()'
        return this.$s.toUpper().length(); // <-- [更改]
    }
}

func main() -> int { // 'Int' 或 'i32' 都可以, 都会被转为 C++ 'int'

    // [ 测试点 B ] 静态 -> 实例 -> 实例
    var $len1: Int = String.create("Hello World").toUpper().length(); // <-- [更改]
    Chrono.log($len1); // 应该输出 11 // <-- [更改]
    $len1.release(); // <-- [更改]

    // [ 测试点 C ] 实例 -> 实例 (赋值)
    var $s: String = String.create("lowercase"); // <-- [更改]
    var $upper: String = $s.toUpper(); // <-- [更改]
    Chrono.log($upper); // 应该输出 "LOWERCASE" // <-- [更改]
    $s.release(); // <-- [更改]
    $upper.release(); // <-- [更改]

    // [ 测试点 D ] 'this' 链调用
    var $w_str: String = String.create("wrapped"); // <-- [更改]

    // (现在可以调用，因为 create 是 public)
    var $w: Wrapper = Wrapper.create($w_str); // <-- [更改]

    // (现在可以调用，因为 getUpperLength 是 public)
    var $len2: Int = $w.getUpperLength(); // <-- [更改]
    Chrono.log($len2); // 应该输出 7 // <-- [更改]

    // 清理
    $w_str.release(); // <-- [更改]
    $w.release(); // <-- [更改]
    $len2.release(); // <-- [更改]

    return 0; // <-- [更改]
}