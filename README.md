

### 演示：Chrono 泛型语法

Chrono 语法 (新),C++ 翻译 (目标),架构规则
let v: std.vector[i32];,std::vector<int32_t> v;,值类型 (无 $ 变量)
let $v: std.vector[i32];,std::vector<int32_t>* _v;,指针类型 ($ 变量)
"let m: std.map[std.string, i32];","std::map<std::string, int32_t> m;",值类型 (嵌套命名空间)
let $o: MyClass[$String];,MyClass<String*>* _o;,指针类型 (泛型参数是 $ 类型)
 
##未实现功能：

interface


高级功能：
类型扩展
转发
