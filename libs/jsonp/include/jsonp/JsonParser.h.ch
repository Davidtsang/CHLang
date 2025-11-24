#pragma once
import "jsonp/Json"
import "runtime/CHObject.h"
import <string>

@dynamic
class JsonParser : CHObject {
    // 解析状态
    var m_input: std::string;
    var m_pos: i32;
    var m_length: i32;

    public init();

    // 对外入口：解析字符串，返回 JNode (dyn)
    public func parse(json: std::string) -> dyn;

    // --- 内部递归方法 (protected/private) ---
    // 即使是 private，在动态类里也可以通过方法名反射调用，方便单元测试
    func parseValue() -> dyn;
    func parseObject() -> dyn;
    func parseArray() -> dyn;
    func parseString() -> dyn;
    func parseNumber() -> dyn;

    // 辅助
    func skipWhitespace();
    func peek() -> i8; // 看当前字符
    func next() -> i8; // 消费并返回当前字符
    func match(c: i8) -> bool; // 匹配并消费
}