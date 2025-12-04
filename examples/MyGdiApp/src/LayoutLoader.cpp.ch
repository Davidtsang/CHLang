// examples/MyGdiApp/src/LayoutLoader.cpp.ch
import "LayoutLoader"

import "chui/UIFactory"
import "chui/PropertyInjector"
import "chui/Widget"
import "chui/Button"
import "chui/HBox"
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

    // [新增] 内部递归解析函数
    // parent: 父窗口句柄
    // itemObj: JSON 对象节点
    // idBase: ID 起始值
    // exitCb: 回调
    func parseWidget(parent: HWND, itemObj: JObject*, id: int, exitCb: ClickCallback) -> Widget* {

        if (!itemObj) { return nullptr; }

        var typeNode: JString* = itemObj->get("type") as JString;
        if (!typeNode) { return nullptr; }

        var typeStr = typeNode->asString();
        var widgetDyn: dyn = UIFactory::createWidget(typeStr);
        if (!widgetDyn) { return nullptr; }

        CH::Log("  Building: " + typeStr);

        // 1. 注入属性
        var keys = itemObj->getKeys();
        for (var key in keys) {
            if (key == "type" || key == "children") { continue; } // 跳过 children

            var valNode: dyn = itemObj->get(key);

            // (这里保留之前的 PropertyInjector 逻辑: String, Number, Bool)
            var valStrNode: JString* = valNode as JString;
            if (valStrNode) {
                PropertyInjector::inject(widgetDyn, key, valStrNode->asString());
                continue;
            }
            var valNumNode: JNumber* = valNode as JNumber;
            if (valNumNode) {
                PropertyInjector::injectInt(widgetDyn, key, valNumNode->asInt());
                continue;
            }
            var valBoolNode: JBool* = valNode as JBool;
            if (valBoolNode) {
                PropertyInjector::injectBool(widgetDyn, key, valBoolNode->asBool());
                continue;
            }
        }

        // 2. 转换并创建 Win32 窗口
        var w: Widget* = widgetDyn as Widget;
        if (w) {
            w->create(parent, id);

            if (typeStr == "Button") {
                var btn: Button* = widgetDyn as Button;
                btn->setOnClick(exitCb);
            }

            // 3. [新增] 处理递归子控件 (HBox)
            if (typeStr == "HBox") {
                var hbox: HBox* = widgetDyn as HBox;
                var childrenNode: JArray* = itemObj->get("children") as JArray;

                if (childrenNode && hbox) {
                    var count = childrenNode->size();
                    for (var i: i32 = 0; i < count; i = i + 1) {
                        var childObj: JObject* = childrenNode->get(i) as JObject;
                        // 递归创建，父窗口是 HBox 的 hWnd
                        var childWidget = LayoutLoader::parseWidget(hbox->m_hWnd, childObj, id + 1000 + i, exitCb);                        if (childWidget) {
                            hbox->addChild(childWidget);
                            // 注意：LayoutLoader 不负责释放 childWidget，
                            // HBox 接管了它的生命周期。
                        }
                    }
                }
            }
        }
        return w;
    }

    func load(path: std::string, parent: HWND, exitCb: ClickCallback) -> bool {
        var jsonStr = readFile(path);
        if (jsonStr == "") { return false; }

        var parser: JsonParser* = new JsonParser();
        var rootDyn: dyn = parser->parse(jsonStr);

        if (!rootDyn) { parser->release(); return false; }

        var rootArr: JArray* = rootDyn as JArray;
        if (rootArr) {
            var count: i32 = rootArr->size();
            for (var i: i32 = 0; i < count; i = i + 1) {
                var itemObj: JObject* = rootArr->get(i) as JObject;
                // 调用递归函数
                // 注意：顶层控件通常是 create(parent)，我们这里返回的 Widget* // 如果没有父容器管理 (比如 MyWindow 里的 m_children)，可能会导致内存泄漏。
                // *但在当前架构中*，Widget::create 会创建 Win32 窗口，
                // MyWindow 销毁时会销毁所有子窗口。
                // 只是 C++ 对象本身的内存 (new Widget) 需要有人 delete。
                // 为了简单，我们暂时不做顶层对象的内存管理 (或者你可以加到 Window::addChild)。

            LayoutLoader::parseWidget(parent, itemObj, 100 + i, exitCb);
            }
            rootDyn->release();
        }

        parser->release();
        return true;
    }
}