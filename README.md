

### 演示：Chrono 泛型语法

Chrono 语法 (新),C++ 翻译 (目标),架构规则
let v: std.vector[i32];,std::vector<int32_t> v;,值类型 (无 $ 变量)
let $v: std.vector[i32];,std::vector<int32_t>* _v;,指针类型 ($ 变量)
"let m: std.map[std.string, i32];","std::map<std::string, int32_t> m;",值类型 (嵌套命名空间)
let $o: MyClass[$String];,MyClass<String*>* _o;,指针类型 (泛型参数是 $ 类型)
 
##未实现功能：

interface


## 函数指针
方案 A：类型别名（Type Alias）(最清晰)
这是我之前建议的方案。我们首先定义一个可重用的类型，然后使用它。

Code snippet

// 1. 定义一个类型 (我们未来需要 'typealias' 关键字)
typealias OperationFunc = (i32, i32) -> i32;

// 2. 声明该类型的变量
let myFunc: OperationFunc;
 
方案 B：内联类型签名（Inline Type Signature）(最灵活)
这是 Swift 和 Go 采用的模式，也是你可能真正想要的。函数签名本身就是类型。

Code snippet

// Chrono 语法 (提议)
let myFunc: (i32, f64) -> i32;