from Base import CodeGenerator


class Generator(CodeGenerator):
    def generate(self, context):
        prop_map = {}
        INDENT = "    "

        # 1. 收集 setXXX(String/Object)
        for name, symbol in context.symbols.items():
            methods = symbol.methods if hasattr(symbol, 'methods') else symbol.get('methods', {})

            for m_name, m_info in methods.items():
                info = self.get_method_info(m_name, m_info)

                # 筛选逻辑
                if info['access'] == 'public' and info['name'].startswith("set") and len(info['name']) > 3 and len(
                        info['args']) == 1:
                    arg_type = info['args'][0]['type']

                    # 过滤数字 (交给 IntInjector)
                    if arg_type in ["int", "i32", "int32_t", "long", "int64_t", "float", "f32"]:
                        continue

                    raw_prop = info['name'][3:]
                    prop_name = raw_prop[0].lower() + raw_prop[1:]
                    prop_map[prop_name] = {"method": info['name'], "type": arg_type}

        # 2. 生成 C++
        code = f"{INDENT}// --- @codegen(\"PropertyInjector\") Output ---\n"
        for prop, meta in prop_map.items():
            method = meta['method']
            type_name = meta['type']

            code += f"{INDENT}if (key == \"{prop}\") {{\n"
            code += f"{INDENT}{INDENT}using TargetType = {type_name};\n"
            code += f"{INDENT}{INDENT}if constexpr (CH::Converter<TargetType>::is_implemented) {{\n"
            code += f"{INDENT}{INDENT}{INDENT}auto val = CH::Converter<TargetType>::fromString(value);\n"
            code += f"{INDENT}{INDENT}{INDENT}obj->msgSend(_SEL(\"{method}\"), {{ val }});\n"
            code += f"{INDENT}{INDENT}{INDENT}return;\n"
            code += f"{INDENT}{INDENT}}} else {{\n"
            code += f"{INDENT}{INDENT}{INDENT}std::cerr << \"[Injector] No converter for {type_name}\" << std::endl;\n"
            code += f"{INDENT}{INDENT}{INDENT}return;\n"
            code += f"{INDENT}{INDENT}}}\n"
            code += f"{INDENT}}}\n"

        return code