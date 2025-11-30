import "jsonp/JsonParser"
import "jsonp/Json"
import "runtime/CH.h"
import <iostream>
import <string>
import <cctype> // 用于 isdigit, isspace

@dynamic
implement JsonParser {
    init() {
        this->m_pos = 0;
        this->m_length = 0;
    }

    func parse(json: std::string) -> dyn {
        this->m_input = json;

        // [标准库补全] std::string.length() 返回 size_t，强转为 i32
        @cpp
        this->m_length = static_cast<int32_t>(json.length());
        @end

        this->m_pos = 0;
        this->skipWhitespace();
        return this->parseValue();
    }

    // --- 辅助方法 ---

    func peek() -> i8 {
        if (this->m_pos >= this->m_length)
        {return 0;} // EOF
        // [语法] string[index] 访问
        return this->m_input[this->m_pos];
    }

    func next() -> i8 {
        var c = this->peek();
        this->m_pos = this->m_pos + 1;
        return c;
    }

    func match(expected: i8) -> bool {
        if (this->peek() == expected) {
            this->m_pos = this->m_pos + 1;
            return true;
        }
        return false;
    }

    func skipWhitespace() {
        while (this->m_pos < this->m_length) {
            var c = this->peek();
            // [C++ 互操作] 使用 isspace
            var is_sp: bool;
            @cpp is_sp = std::isspace(c); @end

            if (is_sp) {
                this->m_pos = this->m_pos + 1;
            } else {
                return; // 遇到非空白，退出
            }
        }
    }

    // --- 核心递归逻辑 ---

    func parseValue() -> dyn {
        this->skipWhitespace();
        var c = this->peek();

        // 1. Object
        if (c == '{') {return this->parseObject();}

        // 2. Array
        if (c == '[') {return this->parseArray();}

        // 3. String
        if (c == '"') {return this->parseString();}

        // 4. Number (简单判断：数字或负号)
        var is_digit: bool;
        @cpp is_digit = std::isdigit(c) || c == '-'; @end
        if (is_digit) {return this->parseNumber();}

        // TODO: true, false, null

        CH::Log("JsonParser Error: Unexpected char");
        return nullptr;
    }

    func parseObject() -> dyn {
        var obj: JObject* = new JObject();
        this->match('{'); // 吃掉 {

        while (true) {
            this->skipWhitespace();
            if (this->peek() == '}') {break;}

            // 1. Key (必须是字符串)
            var keyNode: JString* = this->parseString() as JString;
            if (keyNode == nullptr) {
                CH::Log("Error: Object key expected string");
                return nullptr;
            }

            // 转换 key 为 std::string
            // (注意：我们需要把 JString 转回 std::string，或者 JObject 直接接受 JString*)
            // 这里我们复用 asString()
            var keyStr = keyNode->asString();
            keyNode->release(); // 用完释放 keyNode，因为我们只存 string key

            this->skipWhitespace();
            if (!this->match(':')) {
                CH::Log("Error: Expected ':'");
                return nullptr;
            }

            // 2. Value
            var valNode: dyn = this->parseValue();
            obj->put(keyStr, valNode);

            this->skipWhitespace();
            if (!this->match(',')) {break; }// 如果没有逗号，说明结束了
        }

        if (!this->match('}')) {
             CH::Log("Error: Expected '}'");
             return nullptr;
        }
        return obj;
    }

    func parseArray() -> dyn {
        var arr: JArray* = new JArray();
        this->match('[');

        while (true) {
            this->skipWhitespace();
            if (this->peek() == ']'){ break;}

            var val: dyn = this->parseValue();
            arr->add(val);

            this->skipWhitespace();
            if (!this->match(',')) {break;}
        }

        if (!this->match(']')) {
            CH::Log("Error: Expected ']'");
            return nullptr;
        }
        return arr;
    }

    func parseString() -> dyn {
        this->match('"'); // 吃掉左引号

        var start = this->m_pos;

        // 寻找右引号 (简化版，暂不支持转义字符 \" )
        while (this->m_pos < this->m_length) {
            var c = this->peek();
            if (c == '"') {break;}
            this->m_pos = this->m_pos + 1;
        }

        // 截取字符串
        var len = this->m_pos - start;
        var s: std::string;
        s = this->m_input.substr(start, len);

        this->match('"'); // 吃掉右引号

        return new JString(s);
    }

    func parseNumber() -> dyn {
        var start = this->m_pos;

        // 吞掉所有数字
        while (this->m_pos < this->m_length) {
            var c = this->peek();
            var is_d: bool;
            is_d = std::isdigit(c) || c == '-';

            if (!is_d) {break;}
            this->m_pos = this->m_pos + 1;
        }

        var len = this->m_pos - start;
        var s: std::string;
        s = this->m_input.substr(start, len);

        // 转为 int
        var val: i32 = 0;
        @cpp
        try { val = std::stoi(s); } catch(...) { val = 0; }
        @end

        return new JNumber(val);
    }
}