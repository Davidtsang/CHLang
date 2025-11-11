# [ [ 1. 替换 ] ]
# 'visitMethodDefinition' 必须移除 lstrip('$')
#
def visitMethodDefinition(self, ctx: ChronoParser.MethodDefinitionContext):
    self._in_class_method = True
    self._enter_scope()

    # 'this' 永远是一个指针, 无论在 class 还是 struct 中
    accessor = "->"
    cpp_type = f"{self._current_class_name}*"

    self._add_variable("this", {
        "cpp_name": "this",
        "accessor": accessor,
        "cpp_type": cpp_type
    })

    func_name = ctx.name.text
    params_code = self.visit(ctx.parameters()) if ctx.parameters() else ""

    statements = self._safe_iterate_statements(ctx.statement())
    body_code = "".join(self.visit(s) for s in statements)

    is_static = getattr(ctx, '_chrono_static', False)
    access = getattr(ctx, '_chrono_access', 'private')

    if ctx.returnType:
        cpp_return_type = self.visit(ctx.returnType)
        cpp_func_name = func_name
    else:
        cpp_return_type = "void"
        cpp_func_name = func_name

    static_prefix = "static " if is_static else ""

    func_def_code = (
        f"\n{INDENT}{static_prefix}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
        f"{body_code}"
        f"{INDENT}// --- Method End ---\n"
        # [ [ 关键修复 ] ]
        # 之前是: f"{INDENT}}}}\n" (4个括号, 错误地输出 '}}')
        # 或者是 (如你的日志所示) 3个括号 (语法错误)
        # 正确的: f"{INDENT}}}\n" (2个括号, 输出 '}')
        f"{INDENT}}}\n"
    )

    self._class_sections[access] += func_def_code

    self._exit_scope()
    self._in_class_method = False
    return ""


# [ [ 2. 替换 ] ]
# 'visitFunctionDefinition' 必须移除 lstrip('$')
#
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
        cpp_return_type = self.visit(ctx.returnType)

        if func_name == "main":  # 'main' 必须返回 'int'
            cpp_return_type = "int"
            cpp_func_name = "main"
        else:
            cpp_func_name = func_name
    else:
        cpp_return_type = "void"
        cpp_func_name = func_name

    static_prefix = "static " if is_static else ""
    self._exit_scope()
    return (
        f"\n{static_prefix}{cpp_return_type} {cpp_func_name}({params_code}) {{\n"
        f"{body_code}"
        # [ [ 关键修复 ] ]
        # 之前可能是 f"}}\n" (2个括号, 输出 '}')
        # (这个之前可能是对的，但为了保持一致性，我们确保它是 2 个)
        f"}}\n"
    )