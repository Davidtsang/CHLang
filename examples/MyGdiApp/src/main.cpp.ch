import "chui/Application"
import "MyWindow"
import "chui/UIFactory"
import "chui/PropertyInjector"
import "chui/Geometry"
import "runtime/CH.h"
import "jsonp/Json"       // [新增] JSON 数据模型
import "jsonp/JsonParser" // [新增] JSON 解析器

// [关键修复] 必须显式导入 Button 和 Label，否则 as Button 会报错
import "chui/Button"
import "chui/Label"
import "chui/Widget"

import <string>
import <fstream> // 用于读取文件
import <sstream>

// [辅助] 读取文件内容到字符串
func readFile(path: std::string) -> std::string {
    @cpp
    std::ifstream t(path);
    if (!t.is_open()) return "";
    std::stringstream buffer;
    buffer << t.rdbuf();
    return buffer.str();
    @end
}

func onExit() {
    @cpp PostQuitMessage(0); @end
}

func CHMain() -> int {
    var app = @make<Application>();
    var window = @make<MyWindow>(app.get(), 600, 400);
    window->setBackgroundColor(CGColor(240, 240, 240, 255));

    CH::Log("--- Starting Data-Driven Engine ---");

    // 1. 读取文件
    var jsonStr = readFile("layout.json");
    if (jsonStr == "") {
        CH::Log("Error: Could not read layout.json");
        return -1;
    }

    CH::Log("Loaded JSON: " + jsonStr);

    // 2. 解析 JSON
    var parser: JsonParser* = new JsonParser();
    var rootDyn: dyn = parser->parse(jsonStr);

    if (rootDyn) {
        // 3. 遍历数组
        // 我们的根节点是一个 Array [...]
        var rootArr: JArray* = rootDyn as JArray;
        var count: i32 = rootArr->size();

        for (var i: i32 = 0; i < count; i = i + 1) {
            var itemDyn: dyn = rootArr->get(i);
            var itemObj: JObject* = itemDyn as JObject;

            if (itemObj) {
                // 提取 type
                var typeNode: JString* = itemObj->get("type") as JString;
                var typeStr = typeNode->asString();

                // [工厂] 创建控件
                var widgetDyn: dyn = UIFactory::createWidget(typeStr);

                if (widgetDyn) {
                    CH::Log("Building Widget: " + typeStr);

                    // [注入] 遍历 JSON 对象的所有 Key 并注入
                    var keys = itemObj->getKeys();
                    for (var key in keys) {
                        // 跳过 "type"
                        if (key == "type") {continue;}

                        var valNode: dyn = itemObj->get(key);

                        // 简单的类型分发
                        // 这里的 as JString 需要运行时检查 (dynamic_cast)
                        // 为了简化 demo，我们假设只有 string 和 int 两种属性

                        var valStrNode: JString* = valNode as JString;
                        if (valStrNode) {
                            PropertyInjector::inject(widgetDyn, key, valStrNode->asString());
                        } else {
                            var valNumNode: JNumber* = valNode as JNumber;
                            if (valNumNode) {
                                PropertyInjector::injectInt(widgetDyn, key, valNumNode->asInt());
                            }
                        }
                    }

                    // [挂载]
                    var w: Widget* = widgetDyn as Widget;
                    if (w) {
                        w->create(window->m_hWnd, 100 + i);

                        // 绑定事件
                        if (typeStr == "Button") {
                            var btn: Button* = widgetDyn as Button;
                            btn->setOnClick(onExit);
                        }
                    }
                }
            }
        }

        // 释放 JSON 树 (parser 不负责持有 parse 出来的结果，需要手动释放)
        // 注意：如果没有实现析构函数级联释放，这里会泄露子节点内存。
        // 但作为 Demo 足够了。
        rootDyn->release();
    } else {
        CH::Log("JSON Parse Failed!");
    }

    parser->release();
    window->show();
    return app->exec();
}