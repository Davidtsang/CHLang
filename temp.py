# src/ChronoVisitor.py

# ... (删除 _translate_type_string 方法) ...

# --- [ 1. 新增: 泛型 Vistor 方法 ] ---

def visitTypeSpecifier(self, ctx: ChronoParser.TypeSpecifierContext):
    """
    [新增] 访问 'typeSpecifier' 规则。
    将 'std.vector[i32]' 翻译为 'std::vector<int32_t>'
    """
    # 1. 翻译基础类型 (例如 "std.vector" -> "std::vector")
    base = self.visit(ctx.baseType())

    # 2. 如果有泛型参数
    if ctx.typeList():
        # 3. 翻译参数列表 (例如 "i32, $String" -> "int32_t, String*")
        args = self.visit(ctx.typeList())
        # 4. 组合 (例如 "std::vector<int32_t>")
        return f"{base}<{args}>"
    else:
        return base


def visitBaseType(self, ctx: ChronoParser.BaseTypeContext):
    """
    [新增] 访问 'baseType' 规则。
    处理:
    1. 命名空间: "std.string" -> "std::string"
    2. 别名: "Math.Type" -> "MyMath::Type"
    3. $类型: "$String" -> "String*"
    4. 基础类型: "i32" -> "int32_t"
    """
    raw_text = ctx.getText()  # (例如 "std.string", "$String", "i32")

    parts = raw_text.split('.')
    first_part = parts[0]

    # 1. 检查别名
    if first_part in self._alias_to_namespace_map:
        parts[0] = self._alias_to_namespace_map[first_part]

    cpp_namespace_type = "::".join(parts)  # (例如 "std::string", "$String")

    # 2. 检查 $ 标记 (用于泛型参数)
    if cpp_namespace_type.startswith('$'):
        base = cpp_namespace_type.lstrip('$')
        return f"{self._chrono_to_cpp_type(base)}*"  # (例如 "String*")

    # 3. 检查基础类型
    return self._chrono_to_cpp_type(cpp_namespace_type)  # (例如 "std::string", "int32_t")


def visitTypeList(self, ctx: ChronoParser.TypeListContext):
    """
    [新增] 访问 'typeList' 规则。
    将 'typeSpecifier' 列表翻译为逗号分隔的 C++ 字符串。
    """
    arg_list = [self.visit(t) for t in ctx.typeSpecifier()]
    return ", ".join(arg_list)


# --- [ 2. 替换: 引用新 Vistor 的方法 ] ---

def visitDeclaration(self, ctx: ChronoParser.DeclarationContext):
    var_name = ctx.variableName.text
    key = var_name
    cpp_name = var_name

    # --- [ 升级 ] ---
    # 之前的: base_type_cpp = self._translate_type_string(...)
    # 现在的: 我们访问新的 'typeSpecifier' 规则
    base_type_cpp = self.visit(ctx.typeName())
    # (例如 "std::vector<int32_t>" 或 "std::string")
    # --- [ 升级结束 ] ---

    accessor = "."
    is_pointer = False

    if var_name.startswith('$'):
        accessor = "->"
        is_pointer = True
        cpp_name = f"_{var_name.lstrip('$')}"
    else:
        accessor = "."
        is_pointer = False
        if base_type_cpp in _ACCESSOR_EXCEPTION_LIST or "::iterator" in base_type_cpp:
            accessor = "->"

    cpp_final_type = f"{base_type_cpp}*" if is_pointer else base_type_cpp

    self._add_variable(key, {
        "cpp_name": cpp_name,
        "accessor": accessor,
        "cpp_type": cpp_final_type
    })

    # ... (I. 局部变量 和 II. 类成员 逻辑不变) ...
    # I. 局部变量
    if not self._in_class or self._in_class_method:
        cpp_value = ""
        if is_pointer:
            cpp_value = " = nullptr"
        elif base_type_cpp == "bool":
            cpp_value = " = false"
        elif base_type_cpp in ("int32_t", "int64_t"):
            cpp_value = " = 0"
        # (std::string 和 std::vector 会被默认构造, 这是正确的)

        if ctx.expression():
            cpp_value = f" = {self.visit(ctx.expression())}"

        return f"{INDENT}{cpp_final_type} {cpp_name}{cpp_value};\n"

    # II. 类成员
    else:
        access = getattr(ctx, '_chrono_access', 'private')
        declaration_line = f"{INDENT}{cpp_final_type} {cpp_name};\n"
        self._class_sections[access] += declaration_line
        return ""


def visitParameter(self, ctx: ChronoParser.ParameterContext):
    var_name = ctx.name.text
    key = var_name
    cpp_name = var_name

    # --- [ 升级 ] ---
    # 现在的: 我们访问新的 'typeSpecifier' 规则
    base_type_cpp = self.visit(ctx.typeName())
    # --- [ 升级结束 ] ---

    accessor = "."
    is_pointer = False

    if var_name.startswith('$'):
        accessor = "->"
        is_pointer = True
        cpp_name = f"_{var_name.lstrip('$')}"
    elif base_type_cpp in _ACCESSOR_EXCEPTION_LIST or "::iterator" in base_type_cpp:
        accessor = "->"
        is_pointer = False

    cpp_final_type = f"{base_type_cpp}*" if is_pointer else base_type_cpp

    self._add_variable(key, {
        "cpp_name": cpp_name,
        "accessor": accessor,
        "cpp_type": cpp_final_type
    })

    return f"{cpp_final_type} {cpp_name}"


def visitMethodDefinition(self, ctx: ChronoParser.MethodDefinitionContext):
    self._in_class_method = True
    self._enter_scope()

    self._add_variable("this", {
        "cpp_name": "this",
        "accessor": "->",
        "cpp_type": f"{self._current_class_name}*"
    })

    func_name = ctx.name.text
    params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

    statements = self._safe_iterate_statements(ctx.statement())
    body_code = "".join(self.visit(s) for s in statements)

    is_static = getattr(ctx, '_chrono_static', False)
    access = getattr(ctx, '_chrono_access', 'private')

    if ctx.returnType:
        # --- [ 升级 ] ---
        # 现在的: 我们访问新的 'typeSpecifier' 规则
        return_type_cpp = self.visit(ctx.returnType)
        # (例如 "std::vector<int32_t>" 或 "String*")
        # --- [ 升级结束 ] ---

        # (注意: _chrono_to_cpp_type 已在 visitBaseType 中处理)
        if "::" in return_type_cpp or "<" in return_type_cpp or return_type_cpp in ("int32_t", "int64_t", "bool"):
            cpp_return_type = return_type_cpp
        else:
            cpp_return_type = f"{return_type_cpp}"  # 'String*' 已经是 '*'

        cpp_func_name = func_name.lstrip('$')
    else:
        cpp_return_type = "void"
        cpp_func_name = func_name.lstrip('$')

    static_prefix = "static " if is_static else ""

    func_def_code = (
        f"\n{INDENT}{static_prefix}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
        f"{body_code}"
        f"{INDENT}// --- Method End ---\n"
        f"{INDENT}}}\n"
    )
    self._class_sections[access] += func_def_code
    self._exit_scope()
    self._in_class_method = False
    return ""


def visitFunctionDefinition(self, ctx: ChronoParser.FunctionDefinitionContext):
    self._enter_scope()

    func_name = ctx.name.text
    params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

    statements = self._safe_iterate_statements(ctx.statement())
    body_code = "".join(self.visit(s) for s in statements)

    is_static = False
    if hasattr(ctx, 'STATIC') and ctx.STATIC():
        is_static = True

    if ctx.returnType:
        # --- [ 升级 ] ---
        return_type_cpp = self.visit(ctx.returnType)
        # --- [ 升级结束 ] ---

        if func_name == "main":  # 'main' 必须返回 'int'
            cpp_return_type = "int"
            cpp_func_name = "main"
        else:
            if "::" in return_type_cpp or "<" in return_type_cpp or return_type_cpp in ("int32_t", "int64_t", "bool"):
                cpp_return_type = return_type_cpp
            else:
                cpp_return_type = f"{return_type_cpp}"
            cpp_func_name = func_name.lstrip('$')
    else:
        cpp_return_type = "void"
        cpp_func_name = func_name.lstrip('$')

    static_prefix = "static " if is_static else ""
    self._exit_scope()
    return (
        f"\n{static_prefix} {cpp_return_type} {cpp_func_name}({params_code}) {{\n"
        f"{body_code}"
        "}\n"
    )


def visitPrimary(self, ctx: ChronoParser.PrimaryContext):
    if ctx.NEW():
        # --- [ 升级 ] ---
        # 之前的: class_name = self._chrono_to_cpp_type(ctx.IDENTIFIER().getText())
        # 现在的: 访问 'baseType' 规则
        class_name = self.visit(ctx.baseType())
        # (注意: 'new' 不支持泛型参数, 'new std.vector[i32]()' 语法无效)
        # (我们的语法 只支持 'new baseType()')
        # --- [ 升级结束 ] ---

        args = self.visit(ctx.expressionList()) if ctx.expressionList() else ""
        return f"new {class_name}({args})"

    if ctx.literal():
        return self.visit(ctx.literal())

    if ctx.IDENTIFIER():
        primary_text = ctx.IDENTIFIER().getText()
        variable_info = self._find_variable(primary_text)
        if variable_info:
            return variable_info["cpp_name"]
        else:
            # (处理 "String.create()" 中的 "String")
            return self._chrono_to_cpp_type(primary_text.lstrip('$'))

    if ctx.THIS():
        return "this"

    if ctx.LPAREN():
        return f"({self.visit(ctx.expression())})"

    return ""