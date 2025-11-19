# Generated from src/parser/ChronoParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChronoParser import ChronoParser
else:
    from ChronoParser import ChronoParser

# This class defines a complete generic visitor for a parse tree produced by ChronoParser.

class ChronoParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ChronoParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:ChronoParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#baseType.
    def visitBaseType(self, ctx:ChronoParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#typeList.
    def visitTypeList(self, ctx:ChronoParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:ChronoParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#templateArgument.
    def visitTemplateArgument(self, ctx:ChronoParser.TemplateArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:ChronoParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#namespaceStatement.
    def visitNamespaceStatement(self, ctx:ChronoParser.NamespaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#program.
    def visitProgram(self, ctx:ChronoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#topLevelImport.
    def visitTopLevelImport(self, ctx:ChronoParser.TopLevelImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#topLevelStatement.
    def visitTopLevelStatement(self, ctx:ChronoParser.TopLevelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#forwardDeclaration.
    def visitForwardDeclaration(self, ctx:ChronoParser.ForwardDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#accessModifier.
    def visitAccessModifier(self, ctx:ChronoParser.AccessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#endNamespaceStatement.
    def visitEndNamespaceStatement(self, ctx:ChronoParser.EndNamespaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#initSignature.
    def visitInitSignature(self, ctx:ChronoParser.InitSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#deinitSignature.
    def visitDeinitSignature(self, ctx:ChronoParser.DeinitSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#classBodyStatement.
    def visitClassBodyStatement(self, ctx:ChronoParser.ClassBodyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#classDefinition.
    def visitClassDefinition(self, ctx:ChronoParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#implementationBlock.
    def visitImplementationBlock(self, ctx:ChronoParser.ImplementationBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#structDefinition.
    def visitStructDefinition(self, ctx:ChronoParser.StructDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#structBodyStatement.
    def visitStructBodyStatement(self, ctx:ChronoParser.StructBodyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#enumDefinition.
    def visitEnumDefinition(self, ctx:ChronoParser.EnumDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#enumBody.
    def visitEnumBody(self, ctx:ChronoParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#enumItem.
    def visitEnumItem(self, ctx:ChronoParser.EnumItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#functionSignature.
    def visitFunctionSignature(self, ctx:ChronoParser.FunctionSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#methodDefinition.
    def visitMethodDefinition(self, ctx:ChronoParser.MethodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#initDefinition.
    def visitInitDefinition(self, ctx:ChronoParser.InitDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#deinitBlock.
    def visitDeinitBlock(self, ctx:ChronoParser.DeinitBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#includeHeaderContent.
    def visitIncludeHeaderContent(self, ctx:ChronoParser.IncludeHeaderContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#importDirective.
    def visitImportDirective(self, ctx:ChronoParser.ImportDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#usingAlias.
    def visitUsingAlias(self, ctx:ChronoParser.UsingAliasContext):
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


    # Visit a parse tree produced by ChronoParser#cppBlock.
    def visitCppBlock(self, ctx:ChronoParser.CppBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#returnStatement.
    def visitReturnStatement(self, ctx:ChronoParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:ChronoParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#assignment.
    def visitAssignment(self, ctx:ChronoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#assignableExpression.
    def visitAssignableExpression(self, ctx:ChronoParser.AssignableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#assignablePrimary.
    def visitAssignablePrimary(self, ctx:ChronoParser.AssignablePrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#ifStatement.
    def visitIfStatement(self, ctx:ChronoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#ifBlock.
    def visitIfBlock(self, ctx:ChronoParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#elseBlock.
    def visitElseBlock(self, ctx:ChronoParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#whileStatement.
    def visitWhileStatement(self, ctx:ChronoParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#statement.
    def visitStatement(self, ctx:ChronoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#blockStatement.
    def visitBlockStatement(self, ctx:ChronoParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#caseBlock.
    def visitCaseBlock(self, ctx:ChronoParser.CaseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#defaultBlock.
    def visitDefaultBlock(self, ctx:ChronoParser.DefaultBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#switchStatement.
    def visitSwitchStatement(self, ctx:ChronoParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#deleteStatement.
    def visitDeleteStatement(self, ctx:ChronoParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#forStatement.
    def visitForStatement(self, ctx:ChronoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#forInit.
    def visitForInit(self, ctx:ChronoParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#forIncrement.
    def visitForIncrement(self, ctx:ChronoParser.ForIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#methodSignature.
    def visitMethodSignature(self, ctx:ChronoParser.MethodSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#interfaceDefinition.
    def visitInterfaceDefinition(self, ctx:ChronoParser.InterfaceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#variableDeclaration_no_semicolon.
    def visitVariableDeclaration_no_semicolon(self, ctx:ChronoParser.VariableDeclaration_no_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#assignment_no_semicolon.
    def visitAssignment_no_semicolon(self, ctx:ChronoParser.Assignment_no_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#baseInitializer.
    def visitBaseInitializer(self, ctx:ChronoParser.BaseInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#expression.
    def visitExpression(self, ctx:ChronoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#unaryExpression.
    def visitUnaryExpression(self, ctx:ChronoParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#simpleExpression.
    def visitSimpleExpression(self, ctx:ChronoParser.SimpleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#primary.
    def visitPrimary(self, ctx:ChronoParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#initializerList.
    def visitInitializerList(self, ctx:ChronoParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:ChronoParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#expressionList.
    def visitExpressionList(self, ctx:ChronoParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChronoParser#literal.
    def visitLiteral(self, ctx:ChronoParser.LiteralContext):
        return self.visitChildren(ctx)



del ChronoParser