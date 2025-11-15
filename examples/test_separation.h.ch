// file: test/test_separation.h.ch
// 目的: 测试 .h.ch (头文件) 的声明语法

//namespace Test.API;

// 包含 C++ 指令
// (假设我们保留了 #[...] 和 #... 语法)
//#[version(major = 1)];
//#pragma once

// 包含 using
using MyHandle = i32*;

// 包含 typemap
typemap C_HWND = "HWND";

// 包含全局函数*声明*
func GetGlobalValue() -> i32;

var n:int = 8;
// 包含接口 (保持不变)
interface IMyInterface {
    func onEvent();
}

// 包含 Struct *声明*
struct MyPoint {
    var x: i32;
    var y: i32;
    public init(x: i32, y: i32); // 构造函数声明
    public func getSum() -> i32; // 方法声明
}

// 包含 Class *声明*
class MyClass impl IMyInterface {
    
    // 包含变量 (带和不带初始化)
    var m_name: std.string = "default";
    var m_handle: MyHandle;

    // 包含 'public' 成员
    public var m_id: i32;
    
    // 包含 'public' 构造函数*声明*
    public init(id: i32);
    
    // 包含 'private' init *声明*
    init(); 
    
    // 包含 'public' deinit *声明*
    public deinit;

    // 包含 'public static' 方法*声明*
    public static func create() -> MyClass*;
    
    // 包含 'public' 方法*声明*
    public func getName() -> std.string;
    
    // 包含 'private' 方法*声明*
    func setName(name: std.string);
    
    // (实现 'IMyInterface' 的接口)
    public func onEvent();
}