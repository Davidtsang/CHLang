import "jsonp/JsonParser"
import "jsonp/Json"
import "runtime/CH.h"
import <iostream>
import <string>
import <cctype>

@dynamic
implement JsonParser {
    init() {
        this->m_pos = 0;
        this->m_length = 0;
    }

    func parse(json: std::string) -> dyn {
        this->m_input = json;
        @cpp
        this->m_length = static_cast<int32_t>(json.length());
        @end

        this->m_pos = 0;
        this->skipWhitespace();
        return this->parseValue();
    }

    // --- 辅助方法 ---

    func peek() -> i8 {
        if (this->m_pos >= this->m_length) { return 0; }
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
            var is_sp: bool;
            @cpp is_sp = std::isspace(c); @end

            if (is_sp) {
                this->m_pos = this->m_pos + 1;
            } else {
                return;
            }
        }
    }

    // --- 核心递归逻辑 ---

    func parseValue() -> dyn {
        this->skipWhitespace();
        var c = this->peek();

        if (c == '{') { return this->parseObject(); }
        if (c == '[') { return this->parseArray(); }
        if (c == '"') { return this->parseString(); }

        var is_digit: bool;
        @cpp is_digit = std::isdigit(c) || c == '-'; @end
        if (is_digit) { return this->parseNumber(); }

        // [新增] Boolean & Null
        if (c == 't') { return this->parseTrue(); }
        if (c == 'f') { return this->parseFalse(); }
        if (c == 'n') { return this->parseNull(); }

        CH::Log("JsonParser Error: Unexpected char");
        return nullptr;
    }

    // [新增]
    func parseTrue() -> dyn {
        if (this->match('t') && this->match('r') && this->match('u') && this->match('e')) {
            return new JBool(true);
        }
        return nullptr;
    }

    // [新增]
    func parseFalse() -> dyn {
        if (this->match('f') && this->match('a') && this->match('l') && this->match('s') && this->match('e')) {
            return new JBool(false);
        }
        return nullptr;
    }

    // [新增]
    func parseNull() -> dyn {
        if (this->match('n') && this->match('u') && this->match('l') && this->match('l')) {
            return new JNode(); // 基类代表 Null
        }
        return nullptr;
    }

    func parseObject() -> dyn {
        var obj: JObject* = new JObject();
        this->match('{');

        while (true) {
            this->skipWhitespace();
            if (this->peek() == '}') { break; }

            var keyNode: JString* = this->parseString() as JString;
            if (keyNode == nullptr) {
                CH::Log("Error: Object key expected string");
                return nullptr;
            }

            var keyStr = keyNode->asString();
            keyNode->release();

            this->skipWhitespace();
            if (!this->match(':')) {
                CH::Log("Error: Expected ':'");
                return nullptr;
            }

            var valNode: dyn = this->parseValue();
            obj->put(keyStr, valNode);

            this->skipWhitespace();
            if (!this->match(',')) { break; }
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
            if (this->peek() == ']') { break; }

            var val: dyn = this->parseValue();
            arr->add(val);

            this->skipWhitespace();
            if (!this->match(',')) { break; }
        }

        if (!this->match(']')) {
            CH::Log("Error: Expected ']'");
            return nullptr;
        }
        return arr;
    }

    func parseString() -> dyn {
        this->match('"');
        var start = this->m_pos;

        while (this->m_pos < this->m_length) {
            var c = this->peek();
            if (c == '"') { break; }
            this->m_pos = this->m_pos + 1;
        }

        var len = this->m_pos - start;
        var s: std::string;
        s = this->m_input.substr(start, len);

        this->match('"');
        return new JString(s);
    }

    func parseNumber() -> dyn {
        var start = this->m_pos;
        while (this->m_pos < this->m_length) {
            var c = this->peek();
            var is_d: bool;
            @cpp is_d = std::isdigit(c) || c == '-'; @end
            if (!is_d) { break; }
            this->m_pos = this->m_pos + 1;
        }

        var len = this->m_pos - start;
        var s: std::string;
        s = this->m_input.substr(start, len);

        var val: i32 = 0;
        @cpp try { val = std::stoi(s); } catch(...) { val = 0; } @end

        return new JNumber(val);
    }
}