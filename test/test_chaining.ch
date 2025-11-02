// file: test/test_chaining.ch
// 目的: 验证复杂的 '.' 链式调用

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";

// 1. 定义一个用于 'this' 链测试的类
class Wrapper : ChronoObject {
    let s: String;

    func init(str: String) {
        this.s = str;
        this.s.retain();
    }
    
    deinit {
        this.s.release();
    }

    // 使用 'static func' 和 'Constructor Call'
    static func create(str: String) -> Wrapper {
        return Wrapper(str);
    }

    // [ 测试点 A ] 'this.member.method().method()'
    // 返回一个 ChronoInt 对象
    func getUpperLength() -> Int {
        return this.s.toUpper().length();
    }
}

func main() -> Int {
    
    // [ 测试点 B ] 静态 -> 实例 -> 实例
    // String.create("...") -> ChronoString*
    // .toUpper()          -> ChronoString*
    // .length()           -> ChronoInt*
    let len1: Int = String.create("Hello World").toUpper().length();
    print(len1); // 应该输出 11
    len1.release();

    // [ 测试点 C ] 实例 -> 实例 (赋值)
    let s: String = "lowercase";
    let upper: String = s.toUpper();
    print(upper); // 应该输出 "LOWERCASE"
    s.release();
    upper.release();

    // [ 测试点 D ] 'this' 链调用
    let w_str: String = "wrapped";
    let w: Wrapper = Wrapper.create(w_str);
    
    // 调用 getUpperLength(), 它内部执行 'this.s.toUpper().length()'
    let len2: Int = w.getUpperLength();
    print(len2); // 应该输出 7
    
    // 清理
    w_str.release();
    w.release();
    len2.release();

    return 0;
}