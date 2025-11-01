# Generated from grammar/ChronoParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChronoParser import ChronoParser
else:
    from ChronoParser import ChronoParser

# This class defines a complete generic visitor for a parse tree produced by ChronoParser.

class ChronoParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ChronoParser#program.
    def visitProgram(self, ctx:ChronoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#topLevelStatement.
    def visitTopLevelStatement(self, ctx:ChronoParser.TopLevelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#classDefinition.
    def visitClassDefinition(self, ctx:ChronoParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#deinitBlock.
    def visitDeinitBlock(self, ctx:ChronoParser.DeinitBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#importDirective.
    def visitImportDirective(self, ctx:ChronoParser.ImportDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:ChronoParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#parameters.
    def visitParameters(self, ctx:ChronoParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#parameter.
    def visitParameter(self, ctx:ChronoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#declaration.
    def visitDeclaration(self, ctx:ChronoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#cppBlock.
    def visitCppBlock(self, ctx:ChronoParser.CppBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#returnStatement.
    def visitReturnStatement(self, ctx:ChronoParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:ChronoParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#assignment.
    def visitAssignment(self, ctx:ChronoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#assignableExpression.
    def visitAssignableExpression(self, ctx:ChronoParser.AssignableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#statement.
    def visitStatement(self, ctx:ChronoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#expression.
    def visitExpression(self, ctx:ChronoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#primary.
    def visitPrimary(self, ctx:ChronoParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#expressionList.
    def visitExpressionList(self, ctx:ChronoParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#literal.
    def visitLiteral(self, ctx:ChronoParser.LiteralContext):
        return self.visitChildren(ctx)



del ChronoParser