# Generated from src/parser/CHParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CHParser import CHParser
else:
    from CHParser import CHParser

# This class defines a complete generic visitor for a parse tree produced by CHParser.

class CHParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CHParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:CHParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#baseType.
    def visitBaseType(self, ctx:CHParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#typeList.
    def visitTypeList(self, ctx:CHParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:CHParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#templateArgument.
    def visitTemplateArgument(self, ctx:CHParser.TemplateArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:CHParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#namespaceStatement.
    def visitNamespaceStatement(self, ctx:CHParser.NamespaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#program.
    def visitProgram(self, ctx:CHParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#topLevelImport.
    def visitTopLevelImport(self, ctx:CHParser.TopLevelImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#topLevelStatement.
    def visitTopLevelStatement(self, ctx:CHParser.TopLevelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#forwardDeclaration.
    def visitForwardDeclaration(self, ctx:CHParser.ForwardDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#accessModifier.
    def visitAccessModifier(self, ctx:CHParser.AccessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#endNamespaceStatement.
    def visitEndNamespaceStatement(self, ctx:CHParser.EndNamespaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#initSignature.
    def visitInitSignature(self, ctx:CHParser.InitSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#deinitSignature.
    def visitDeinitSignature(self, ctx:CHParser.DeinitSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#classBodyStatement.
    def visitClassBodyStatement(self, ctx:CHParser.ClassBodyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#classDefinition.
    def visitClassDefinition(self, ctx:CHParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#implementationBlock.
    def visitImplementationBlock(self, ctx:CHParser.ImplementationBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#structDefinition.
    def visitStructDefinition(self, ctx:CHParser.StructDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#structBodyStatement.
    def visitStructBodyStatement(self, ctx:CHParser.StructBodyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#enumDefinition.
    def visitEnumDefinition(self, ctx:CHParser.EnumDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#enumBody.
    def visitEnumBody(self, ctx:CHParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#enumItem.
    def visitEnumItem(self, ctx:CHParser.EnumItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#functionSignature.
    def visitFunctionSignature(self, ctx:CHParser.FunctionSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#methodDefinition.
    def visitMethodDefinition(self, ctx:CHParser.MethodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#initDefinition.
    def visitInitDefinition(self, ctx:CHParser.InitDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#deinitBlock.
    def visitDeinitBlock(self, ctx:CHParser.DeinitBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#includeHeaderContent.
    def visitIncludeHeaderContent(self, ctx:CHParser.IncludeHeaderContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#importDirective.
    def visitImportDirective(self, ctx:CHParser.ImportDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#usingAlias.
    def visitUsingAlias(self, ctx:CHParser.UsingAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CHParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#parameters.
    def visitParameters(self, ctx:CHParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#parameter.
    def visitParameter(self, ctx:CHParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#cppBlock.
    def visitCppBlock(self, ctx:CHParser.CppBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#returnStatement.
    def visitReturnStatement(self, ctx:CHParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:CHParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#assignment.
    def visitAssignment(self, ctx:CHParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#assignableExpression.
    def visitAssignableExpression(self, ctx:CHParser.AssignableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#assignablePrimary.
    def visitAssignablePrimary(self, ctx:CHParser.AssignablePrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#ifStatement.
    def visitIfStatement(self, ctx:CHParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#ifBlock.
    def visitIfBlock(self, ctx:CHParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#elseBlock.
    def visitElseBlock(self, ctx:CHParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#whileStatement.
    def visitWhileStatement(self, ctx:CHParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#statement.
    def visitStatement(self, ctx:CHParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#blockStatement.
    def visitBlockStatement(self, ctx:CHParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#caseBlock.
    def visitCaseBlock(self, ctx:CHParser.CaseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#defaultBlock.
    def visitDefaultBlock(self, ctx:CHParser.DefaultBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#switchStatement.
    def visitSwitchStatement(self, ctx:CHParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#deleteStatement.
    def visitDeleteStatement(self, ctx:CHParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#forStatement.
    def visitForStatement(self, ctx:CHParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#forInit.
    def visitForInit(self, ctx:CHParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#forIncrement.
    def visitForIncrement(self, ctx:CHParser.ForIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#methodSignature.
    def visitMethodSignature(self, ctx:CHParser.MethodSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#interfaceDefinition.
    def visitInterfaceDefinition(self, ctx:CHParser.InterfaceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#variableDeclaration_no_semicolon.
    def visitVariableDeclaration_no_semicolon(self, ctx:CHParser.VariableDeclaration_no_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#assignment_no_semicolon.
    def visitAssignment_no_semicolon(self, ctx:CHParser.Assignment_no_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#baseInitializer.
    def visitBaseInitializer(self, ctx:CHParser.BaseInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#expression.
    def visitExpression(self, ctx:CHParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#unaryExpression.
    def visitUnaryExpression(self, ctx:CHParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#castExpression.
    def visitCastExpression(self, ctx:CHParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#simpleExpression.
    def visitSimpleExpression(self, ctx:CHParser.SimpleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#primary.
    def visitPrimary(self, ctx:CHParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#initializerList.
    def visitInitializerList(self, ctx:CHParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:CHParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#expressionList.
    def visitExpressionList(self, ctx:CHParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CHParser#literal.
    def visitLiteral(self, ctx:CHParser.LiteralContext):
        return self.visitChildren(ctx)



del CHParser