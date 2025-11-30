import "jsonp/Json"
import "jsonp/JsonParser" // 引入解析器
import "runtime/CH.h"
import <iostream>

func main() -> int {
    CH::Log("--- Testing Json Parser ---");

    // 待解析的 JSON
    var jsonText = "{ \"name\": \"Chrono\", \"id\": 123, \"list\": [ 1, 2 ] }";
    CH::Log("Input: " + jsonText);

    var parser: JsonParser* = new JsonParser();

    // 解析 (返回 dyn)
    var result: dyn = parser->parse(jsonText);

    if (result) {
        CH::Log("Parse Success!");

        // 转换为 JObject
        var root: JObject* = result as JObject;

        if (root) {
            // 1. 验证 String
            var nameNode: dyn = root->get("name");
            if (nameNode) {
                var s: JString* = nameNode as JString;
                CH::Log("name: " + s->asString());
            }

            // 2. 验证 Number
            var idNode: dyn = root->get("id");
            if (idNode) {
                var n: JNumber* = idNode as JNumber;
                @cpp std::cout << "id: " << n->asInt() << std::endl; @end
            }

            // 3. 验证 Array
            var listNode: dyn = root->get("list");
            if (listNode) {
                var arr: JArray* = listNode as JArray;
                var size: i32 = arr->size();
                @cpp std::cout << "list size: " << size << std::endl; @end

                var item0: dyn = arr->get(0);
                var num0: JNumber* = item0 as JNumber;
                @cpp std::cout << "list[0]: " << num0->asInt() << std::endl; @end
            }
        }

        result->release(); // 释放整个树
    } else {
        CH::Log("Parse Failed!");
    }

    parser->release();
    return 0;
}