# src/TypemapScanner.py
from parser.ChronoParserVisitor import ChronoParserVisitor


class TypemapScanner(ChronoParserVisitor):
    """
    轻量级扫描器。
    只遍历语法树以查找 'typemap' 定义，并将它们注册到全局上下文。
    不生成任何 C++ 代码。
    """

    def __init__(self, context):
        self.context = context

    def visitTypemapDefinition(self, ctx):
        name = ctx.name.text
        # 提取字符串值 (去除引号)
        # 假设 value 是 STRING_LITERAL (e.g., "int WINAPI")
        raw_val = ctx.value.text
        if raw_val.startswith('"') and raw_val.endswith('"'):
            value = raw_val[1:-1]
        else:
            value = raw_val

        self.context.register_typemap(name, value)
        return None

    # --- 遍历逻辑 ---
    # 我们必须确保访问到所有可能包含 typemap 的层级

    def visitProgram(self, ctx):
        # 遍历所有子节点 (Import, Namespace, TopLevelStatement)
        for child in ctx.children:
            if hasattr(child, 'accept'):
                child.accept(self)
        return None

    def visitNamespaceStatement(self, ctx):
        # typemap 通常不在 namespace 内部定义 (它是全局宏替换)，
        # 但如果语法允许，我们也应该扫描它。
        return None

    def visitTopLevelStatement(self, ctx):
        # topLevelStatement 可能包含 typemapDefinition
        # 或者其他包含子节点的结构 (虽然目前 typemap 是顶层的)
        if ctx.typemapDefinition():
            return self.visitTypemapDefinition(ctx.typemapDefinition())
        return None

    # 忽略所有其他节点