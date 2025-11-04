// file: test/test_chaining.ch
// 目的: [已修复] 验证 'public' 关键字和链式调用

import "runtime/ChronoObject.h";
import "runtime/ChronoString.h";
import "runtime/ChronoInt.h";

// 1. 定义一个用于 'this' 链测试的类
class Wrapper : ChronoObject {
    let s: String; // 默认 private

    // 默认 private (只能被 'create' 调用)
    func init(str: String) {
        this.s = str;
        this.s.retain();
    }

    deinit {
        this.s.release();
    }

    // [关键修复] 必须是 public 才能被 'main' 调用
    public static func create(str: String) -> Wrapper {
        return Wrapper(str);
    }

    // [关键修复] 必须是 public 才能被 'main' 调用
    public func getUpperLength() -> Int {
        // [ 测试点 A ] 'this.member.method().method()'
        return this.s.toUpper().length();
    }
}

func main() -> Int {

    // [ 测试点 B ] 静态 -> 实例 -> 实例
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
    // (现在可以调用，因为 create 是 public)
    let w: Wrapper = Wrapper.create(w_str);

    // (现在可以调用，因为 getUpperLength 是 public)
    let len2: Int = w.getUpperLength();
    print(len2); // 应该输出 7
    
    // 清理
    w_str.release();
    w.release();
    len2.release();

    return 0;
}