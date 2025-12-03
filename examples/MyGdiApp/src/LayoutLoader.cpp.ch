// examples/MyGdiApp/src/LayoutLoader.cpp.ch
import "LayoutLoader"

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

func readFile(path: std::string) -> std::string {
    var t: std::ifstream = std::ifstream(path);
    if (!t.is_open()) {
        return "";
    }
    var buffer: std::stringstream;
    buffer << t.rdbuf();
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
                    var typeNode: JString* = itemObj->get("type") as JString;
                    if (!typeNode) { continue; }

                    var typeStr = typeNode->asString();
                    var widgetDyn: dyn = UIFactory::createWidget(typeStr);

                    if (widgetDyn) {
                        CH::Log("Building Widget: " + typeStr);

                        var keys = itemObj->getKeys();
                        for (var key in keys) {
                            if (key == "type") { continue; }

                            var valNode: dyn = itemObj->get(key);

                            // 1. String
                            var valStrNode: JString* = valNode as JString;
                            if (valStrNode) {
                                PropertyInjector::inject(widgetDyn, key, valStrNode->asString());
                                continue;
                            }

                            // 2. Number
                            var valNumNode: JNumber* = valNode as JNumber;
                            if (valNumNode) {
                                PropertyInjector::injectInt(widgetDyn, key, valNumNode->asInt());
                                continue;
                            }

                            // 3. [新增] Bool
                            var valBoolNode: JBool* = valNode as JBool;
                            if (valBoolNode) {
                                PropertyInjector::injectBool(widgetDyn, key, valBoolNode->asBool());
                                continue;
                            }
                        }

                        // [挂载与绑定]
                        var w: Widget* = widgetDyn as Widget;
                        if (w) {
                            w->create(parent, 100 + i);

                            if (typeStr == "Button") {
                                var btn: Button* = widgetDyn as Button;
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