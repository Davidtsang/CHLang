// examples/MyGdiApp/src/LayoutLoader.cpp.ch
import "LayoutLoader"

// 引入必要的依赖
import "chui/UIFactory"
import "chui/PropertyInjector"
import "chui/Widget"
import "chui/Button"
import "jsonp/Json"
import "jsonp/JsonParser"
import "runtime/CH.h"

import <string>
import <fstream>
import <sstream>

// 将 readFile 移动作为内部辅助函数
func readFile(path: std::string) -> std::string {
// 1. C++ 栈对象初始化
    // Chrono 翻译: std::ifstream t = std::ifstream(path);
    // C++17 支持这种移动构造/复制消除
    var t: std::ifstream = std::ifstream(path);

    // 2. 逻辑判断与方法调用
    // Chrono 原生支持 ! 操作符和 .is_open() 调用
    if (!t.is_open()) {
        return "";
    }

    // 3. 声明 stringstream
    var buffer: std::stringstream;

    // 4. 流操作符 (<<)
    // Chrono 的 parser 支持位移运算符 <<，这里会被 C++ 重载为流写入
    buffer << t.rdbuf();

    // 5. 返回结果
    return buffer.str();
}

implement LayoutLoader {

    func load(path: std::string, parent: HWND, exitCb: ClickCallback) -> bool {

        // 1. 读取文件
        var jsonStr = readFile(path);
        if (jsonStr == "") {
            CH::Log("Error: Could not read " + path);
            return false;
        }
        CH::Log("Loaded JSON from: " + path);

        // 2. 解析 JSON
        var parser: JsonParser* = new JsonParser();
        var rootDyn: dyn = parser->parse(jsonStr);

        if (!rootDyn) {
            CH::Log("JSON Parse Failed!");
            parser->release();
            return false;
        }

        // 3. 遍历数组并创建控件
        var rootArr: JArray* = rootDyn as JArray;
        if (rootArr) {
            var count: i32 = rootArr->size();

            for (var i: i32 = 0; i < count; i = i + 1) {
                var itemDyn: dyn = rootArr->get(i);
                var itemObj: JObject* = itemDyn as JObject;

                if (itemObj) {
                    // 提取 type
                    var typeNode: JString* = itemObj->get("type") as JString;
                    if (!typeNode) { continue; } // 保护检查

                    var typeStr = typeNode->asString();

                    // [工厂] 创建控件
                    var widgetDyn: dyn = UIFactory::createWidget(typeStr);

                    if (widgetDyn) {
                        CH::Log("Building Widget: " + typeStr);

                        // [注入] 遍历属性
                        var keys = itemObj->getKeys();
                        for (var key in keys) {
                            if (key == "type") { continue; }

                            var valNode: dyn = itemObj->get(key);
                            var valStrNode: JString* = valNode as JString;

                            if (valStrNode) {
                                // 使用 PropertyInjector 注入字符串属性
                                PropertyInjector::inject(widgetDyn, key, valStrNode->asString());
                            } else {
                                var valNumNode: JNumber* = valNode as JNumber;
                                if (valNumNode) {
                                    // 使用 PropertyInjector 注入数字属性
                                    PropertyInjector::injectInt(widgetDyn, key, valNumNode->asInt());
                                }
                            }
                        }

                        // [挂载与绑定]
                        var w: Widget* = widgetDyn as Widget;
                        if (w) {
                            // 使用传入的 parent 句柄
                            w->create(parent, 100 + i);

                            // 特殊处理 Button 事件
                            if (typeStr == "Button") {
                                var btn: Button* = widgetDyn as Button;
                                // 使用传入的回调
                                btn->setOnClick(exitCb);
                            }
                        }
                    }
                }
            }
            rootDyn->release();
        }

        parser->release();
        return true;
    }
}