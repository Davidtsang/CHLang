import "Application"
import "MyWindow"
import "UIFactory"
import "PropertyInjector"
import "Geometry"
import "runtime/CH.h" // for Log
import <vector>
import <string>

// 模拟 JSON 数据结构
struct UIElement {
    var type: std::string;
    var text: std::string;
    var color: std::string;
    var bg: std::string;
    var x: i32;
    var y: i32;
    var w: i32;
    var h: i32;
}

func onExit() {
    @cpp exit(0); @end
}

func CHMain() -> int {
    var app = @make<Application>();
    var window = @make<MyWindow>(app.get(), 600, 400);

    // 窗口本身也是动态类，也可以反射设置
    var dynWin: dyn = window.get(); // .get() 获取裸指针
    // PropertyInjector::inject(dynWin, "bg", "#F0F0F0");
    window->setBackgroundColor(CGColor(240, 240, 240, 255)); // 暂时保留静态调用

    // ---------------------------------------------------------
    // 1. 数据定义 (模拟 Layout 文件)
    // ---------------------------------------------------------
    var layout: std::vector<UIElement>;

    var el1: UIElement;
    el1.type = "Label"; el1.text = "Reflected Label";
    el1.color = "#FF0000"; el1.bg = "#00000000";
    el1.x = 20; el1.y = 20; el1.w = 400; el1.h = 30;
    layout.push_back(el1);

    var el2: UIElement;
    el2.type = "Button"; el2.text = "Reflected Button";
    el2.color = "#000000"; el2.bg = "#FFFFFF";
    el2.x = 20; el2.y = 70; el2.w = 200; el2.h = 50;
    layout.push_back(el2);

    // ---------------------------------------------------------
    // 2. 动态构建引擎
    // ---------------------------------------------------------
    CH::Log("--- Building UI from Data ---");

    for (var i: i32 = 0; i < 2; i = i + 1) {
        var data = layout[i];

        // [1] 动态创建: 不需要知道是 Button 还是 Label
        var obj: dyn = UIFactory::createWidget(data.type);

        if (obj) {
            // [2] 动态属性注入 (~> msgSend)
            // 编译器完全不知道 obj 有没有 setText 或 setX，全靠运行时反射
            PropertyInjector::inject(obj, "text", data.text);
            PropertyInjector::inject(obj, "color", data.color);
            PropertyInjector::inject(obj, "bg", data.bg);

            PropertyInjector::injectInt(obj, "x", data.x);
            PropertyInjector::injectInt(obj, "y", data.y);
            PropertyInjector::injectInt(obj, "width", data.w);
            PropertyInjector::injectInt(obj, "height", data.h);

            // [3] 静态/动态混合使用
            // 我们需要把它加到窗口里，addChild 需要 Widget*
            // 使用 as 进行安全向下转型
            var w: Widget* = obj as Widget;

            if (w) {
                w->create(window->m_hWnd, 100 + i);

                // 特殊逻辑：绑定事件
                var btn: Button* = obj as Button;
                if (btn) {
                    btn->setOnClick(onExit);
                }
            }
        }
    }

    CH::Log("--- UI Build Complete ---");

    window->show();
    return app->exec();
}