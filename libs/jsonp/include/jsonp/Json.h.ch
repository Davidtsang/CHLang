#pragma once
import "runtime/CHObject.h"
import <string>
import <map>
import <vector>

// 枚举节点类型
enum JType {
    J_NULL,
    J_OBJECT,
    J_ARRAY,
    J_STRING,
    J_NUMBER
}

// 基类
@dynamic
class JNode : CHObject {
    public init();
    public virtual func getType() -> JType;

    // 辅助转换方法
    public virtual func asString() -> std::string;
    public virtual func asInt() -> i32;
}

// 字符串节点
@dynamic
class JString : JNode {
    var m_val: std::string;
    public init(v: std::string);
    public override func getType() -> JType;
    public override func asString() -> std::string;
}

// 数字节点 (简化：只支持 int)
@dynamic
class JNumber : JNode {
    var m_val: i32;
    public init(v: i32);
    public override func getType() -> JType;
    public override func asInt() -> i32;
}

// 对象节点 { "k": v }
@dynamic
class JObject : JNode {
    // 使用 dyn 存储值，实现多态
    var m_map: std::map<std::string, dyn>;

    public init();
    public override func getType() -> JType;

    public func put(key: std::string, val: dyn);
    public func get(key: std::string) -> dyn;

    // 获取所有 Key (用于 for-in 遍历)
    public func getKeys() -> std::vector<std::string>;
}

// 数组节点 [ v1, v2 ]
@dynamic
class JArray : JNode {
    var m_list: std::vector<dyn>;

    public init();
    public override func getType() -> JType;

    public func add(val: dyn);
    public func get(index: i32) -> dyn;
    public func size() -> i32;
}