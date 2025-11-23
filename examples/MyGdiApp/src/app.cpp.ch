import "Application"
import "MyWindow"
import "UIFactory"
import "PropertyInjector"
import "Geometry"
import "runtime/CH.h"
import <vector>
import <string>

// [关键修复] 必须导入 Button，否则无法使用 'as Button'
import "Button"
import "Label"

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

    window->setBackgroundColor(CGColor(240, 240, 240, 255));

    // ---------------------------------------------------------
    // 1. 数据定义
    // ---------------------------------------------------------
    var layout: std::vector<UIElement>;

    var el1: UIElement;
    el1.type = "Label";
    el1.text = "Chrono Data-Driven UI";
    el1.color = "#0000FF";
    el1.bg = "#00000000";
    el1.x = 20; el1.y = 20; el1.w = 400; el1.h = 30;
    layout.push_back(el1);

    var el2: UIElement;
    el2.type = "Button";
    el2.text = "Dynamic Button";
    el2.color = "#000000";
    el2.bg = "#FFFFFF";
    el2.x = 20; el2.y = 80; el2.w = 200; el2.h = 50;
    layout.push_back(el2);

    // ---------------------------------------------------------
    // 2. 动态构建引擎
    // ---------------------------------------------------------
    CH::Log("--- Building UI from Data ---");

    for (var i: i32 = 0; i < 2; i = i + 1) {
        var data = layout[i];

        // [1] 动态创建
        var obj: dyn = UIFactory::createWidget(data.type);

        if (obj) {
            CH::Log("Creating " + data.type + " via Reflection...");

            // [2] 动态属性注入
            PropertyInjector::inject(obj, "text", data.text);
            PropertyInjector::inject(obj, "color", data.color);
            PropertyInjector::inject(obj, "bg", data.bg);

            PropertyInjector::injectInt(obj, "x", data.x);
            PropertyInjector::injectInt(obj, "y", data.y);
            PropertyInjector::injectInt(obj, "width", data.w);
            PropertyInjector::injectInt(obj, "height", data.h);

            // [3] 静态/动态混合使用
            var w: Widget* = obj as Widget;

            if (w) {
                w->create(window->m_hWnd, 100 + i);

                // 这里需要 Button 的定义，所以必须 import "Button"
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