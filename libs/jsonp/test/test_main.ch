import "jsonp/Json"
import "runtime/CH.h"
import <iostream>

func main() -> int {
    CH::Log("--- JSON Model Test ---");

    // 模拟: { "name": "Chrono", "id": 100 }
    var root: JObject* = new JObject();

    var nameVal: JString* = new JString("Chrono");
    root->put("name", nameVal);

    var idVal: JNumber* = new JNumber(100);
    root->put("id", idVal);

    // 读取
    var n: dyn = root->get("name");
    if (n) {
        // 必须强转回具体类型才能调用 asString (或者用虚函数)
        // 因为 JNode 是基类，我们可以 cast 为 JNode*
        var node: JNode* = n as JNode;
        @cpp std::cout << "Name: " << node->asString() << std::endl; @end
    }

    var i: dyn = root->get("id");
    if (i) {
        var node: JNode* = i as JNode;
        @cpp std::cout << "ID: " << node->asInt() << std::endl; @end
    }

    // 内存泄露注意：我们还没写 JObject 的析构函数来 release 成员
    // 暂时手动释放
    nameVal->release();
    idVal->release();
    root->release(); // root 引用了它们，但没自动释放，这里只是测试

    return 0;
}