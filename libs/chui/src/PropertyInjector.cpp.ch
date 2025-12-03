import "chui/PropertyInjector"
import "chui/Geometry" // 包含 CGColor 的转换器特化
import "runtime/CH.h"
import "runtime/TypeConverters.h" // 包含基础模板
// [修复] 引入 Button 以识别 ClickCallback 类型
import "chui/Button"
import "chui/Menu"   // [新增] 必须引入 Menu，否则无法处理 setMenuBar
// [修改] 引入新的 C++ 头文件
import "runtime/Reflection.h"

implement PropertyInjector {
    func inject(obj: dyn, key: std::string, value: std::string) {

        // [用户介入] 处理特殊字段 (可选)
        if (key == "visible") {
            // 手动处理...
            return;
        }

        // [自动化] 编译器会在这里展开所有 Setter 的调用代码
        @codegen("PropertyInjector");

        CH::Log("Warning: Unknown property: " + key);
    }

    // (injectInt 暂时也可以保留，或者用同样的方式自动化，
    // 但上面的自动化逻辑是基于 string value 的。
    // 如果 layout.json 解析出来已经是 int，C++ 代码里需要 Converter<int>::fromInt?
    // 通常为了简单，JSON 库出来的都是 string 或 variant，这里假设输入是 string)
    func injectInt(obj: dyn, key: std::string, value: i32) {
         if (key == "x") { obj~>setX(value); return; }
         if (key == "y") { obj~>setY(value); return; }
         if (key == "width") { obj~>setWidth(value); return; }
         if (key == "height") { obj~>setHeight(value); return; }
    }

    // [新增]
    func injectBool(obj: dyn, key: std::string, value: bool) {
        if (key == "visible") {
            obj~>setVisible(value);
            return;
        }
    }

}