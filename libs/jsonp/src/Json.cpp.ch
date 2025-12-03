import "jsonp/Json"

// --- JNode Base ---
@dynamic
implement JNode {
    init() {}
    func getType() -> JType { return JType::J_NULL; }
    func asString() -> std::string { return "null"; }
    func asInt() -> i32 { return 0; }
    func asBool() -> bool { return false; } // [新增]
}

// --- JBool [新增] ---
@dynamic
implement JBool {
    init(v: bool) { this->m_val = v; }
    func getType() -> JType { return JType::J_BOOL; }
    func asBool() -> bool { return this->m_val; }

    func asString() -> std::string {
        if (this->m_val) { return "true"; }
        return "false";
    }
}

// --- JString ---
@dynamic
implement JString {
    init(v: std::string) { this->m_val = v; }
    func getType() -> JType { return JType::J_STRING; }
    func asString() -> std::string { return this->m_val; }
}

// --- JNumber ---
@dynamic
implement JNumber {
    init(v: i32) { this->m_val = v; }
    func getType() -> JType { return JType::J_NUMBER; }
    func asInt() -> i32 { return this->m_val; }
}

// --- JObject ---
@dynamic
implement JObject {
    init() {}
    func getType() -> JType { return JType::J_OBJECT; }

    func put(key: std::string, val: dyn) {
        if (val) { val->retain(); }
        this->m_map[key] = val;
    }

    func get(key: std::string) -> dyn {
        if (this->m_map.count(key) > 0) {
            return this->m_map[key];
        }
        return nullptr;
    }

    func getKeys() -> std::vector<std::string> {
        var keys: std::vector<std::string>;
        for (var kv in this->m_map) {
            keys.push_back(kv.first);
        }
        return keys;
    }
}

// --- JArray ---
@dynamic
implement JArray {
    init() {}
    func getType() -> JType { return JType::J_ARRAY; }

    func add(val: dyn) {
        if (val) { val->retain(); }
        this->m_list.push_back(val);
    }

    func get(index: i32) -> dyn {
        if (index >= 0) {
            @cpp
            if (index < this->m_list.size())
             {return this->m_list[index];}
            @end
        }
        return nullptr;
    }

    func size() -> i32 {
        @cpp return (int32_t)this->m_list.size(); @end
    }
}