# Generated from src/parser/ChronoParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChronoParser import ChronoParser
else:
    from ChronoParser import ChronoParser

# This class defines a complete listener for a parse tree produced by ChronoParser.
class ChronoParserListener(ParseTreeListener):

    # Enter a parse tree produced by ChronoParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:ChronoParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by ChronoParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:ChronoParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by ChronoParser#baseType.
    def enterBaseType(self, ctx:ChronoParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by ChronoParser#baseType.
    def exitBaseType(self, ctx:ChronoParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by ChronoParser#typeList.
    def enterTypeList(self, ctx:ChronoParser.TypeListContext):
        pass

    # Exit a parse tree produced by ChronoParser#typeList.
    def exitTypeList(self, ctx:ChronoParser.TypeListContext):
        pass


    # Enter a parse tree produced by ChronoParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:ChronoParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by ChronoParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:ChronoParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by ChronoParser#templateArgument.
    def enterTemplateArgument(self, ctx:ChronoParser.TemplateArgumentContext):
        pass

    # Exit a parse tree produced by ChronoParser#templateArgument.
    def exitTemplateArgument(self, ctx:ChronoParser.TemplateArgumentContext):
        pass


    # Enter a parse tree produced by ChronoParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:ChronoParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by ChronoParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:ChronoParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by ChronoParser#namespaceStatement.
    def enterNamespaceStatement(self, ctx:ChronoParser.NamespaceStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#namespaceStatement.
    def exitNamespaceStatement(self, ctx:ChronoParser.NamespaceStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#program.
    def enterProgram(self, ctx:ChronoParser.ProgramContext):
        pass

    # Exit a parse tree produced by ChronoParser#program.
    def exitProgram(self, ctx:ChronoParser.ProgramContext):
        pass


    # Enter a parse tree produced by ChronoParser#topLevelImport.
    def enterTopLevelImport(self, ctx:ChronoParser.TopLevelImportContext):
        pass

    # Exit a parse tree produced by ChronoParser#topLevelImport.
    def exitTopLevelImport(self, ctx:ChronoParser.TopLevelImportContext):
        pass


    # Enter a parse tree produced by ChronoParser#topLevelStatement.
    def enterTopLevelStatement(self, ctx:ChronoParser.TopLevelStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#topLevelStatement.
    def exitTopLevelStatement(self, ctx:ChronoParser.TopLevelStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#accessModifier.
    def enterAccessModifier(self, ctx:ChronoParser.AccessModifierContext):
        pass

    # Exit a parse tree produced by ChronoParser#accessModifier.
    def exitAccessModifier(self, ctx:ChronoParser.AccessModifierContext):
        pass


    # Enter a parse tree produced by ChronoParser#endNamespaceStatement.
    def enterEndNamespaceStatement(self, ctx:ChronoParser.EndNamespaceStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#endNamespaceStatement.
    def exitEndNamespaceStatement(self, ctx:ChronoParser.EndNamespaceStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#initSignature.
    def enterInitSignature(self, ctx:ChronoParser.InitSignatureContext):
        pass

    # Exit a parse tree produced by ChronoParser#initSignature.
    def exitInitSignature(self, ctx:ChronoParser.InitSignatureContext):
        pass


    # Enter a parse tree produced by ChronoParser#deinitSignature.
    def enterDeinitSignature(self, ctx:ChronoParser.DeinitSignatureContext):
        pass

    # Exit a parse tree produced by ChronoParser#deinitSignature.
    def exitDeinitSignature(self, ctx:ChronoParser.DeinitSignatureContext):
        pass


    # Enter a parse tree produced by ChronoParser#classBodyStatement.
    def enterClassBodyStatement(self, ctx:ChronoParser.ClassBodyStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#classBodyStatement.
    def exitClassBodyStatement(self, ctx:ChronoParser.ClassBodyStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#classDefinition.
    def enterClassDefinition(self, ctx:ChronoParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by ChronoParser#classDefinition.
    def exitClassDefinition(self, ctx:ChronoParser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by ChronoParser#implementationBlock.
    def enterImplementationBlock(self, ctx:ChronoParser.ImplementationBlockContext):
        pass

    # Exit a parse tree produced by ChronoParser#implementationBlock.
    def exitImplementationBlock(self, ctx:ChronoParser.ImplementationBlockContext):
        pass


    # Enter a parse tree produced by ChronoParser#structDefinition.
    def enterStructDefinition(self, ctx:ChronoParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by ChronoParser#structDefinition.
    def exitStructDefinition(self, ctx:ChronoParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by ChronoParser#structBodyStatement.
    def enterStructBodyStatement(self, ctx:ChronoParser.StructBodyStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#structBodyStatement.
    def exitStructBodyStatement(self, ctx:ChronoParser.StructBodyStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#functionSignature.
    def enterFunctionSignature(self, ctx:ChronoParser.FunctionSignatureContext):
        pass

    # Exit a parse tree produced by ChronoParser#functionSignature.
    def exitFunctionSignature(self, ctx:ChronoParser.FunctionSignatureContext):
        pass


    # Enter a parse tree produced by ChronoParser#methodDefinition.
    def enterMethodDefinition(self, ctx:ChronoParser.MethodDefinitionContext):
        pass

    # Exit a parse tree produced by ChronoParser#methodDefinition.
    def exitMethodDefinition(self, ctx:ChronoParser.MethodDefinitionContext):
        pass


    # Enter a parse tree produced by ChronoParser#initDefinition.
    def enterInitDefinition(self, ctx:ChronoParser.InitDefinitionContext):
        pass

    # Exit a parse tree produced by ChronoParser#initDefinition.
    def exitInitDefinition(self, ctx:ChronoParser.InitDefinitionContext):
        pass


    # Enter a parse tree produced by ChronoParser#deinitBlock.
    def enterDeinitBlock(self, ctx:ChronoParser.DeinitBlockContext):
        pass

    # Exit a parse tree produced by ChronoParser#deinitBlock.
    def exitDeinitBlock(self, ctx:ChronoParser.DeinitBlockContext):
        pass


    # Enter a parse tree produced by ChronoParser#includeHeaderContent.
    def enterIncludeHeaderContent(self, ctx:ChronoParser.IncludeHeaderContentContext):
        pass

    # Exit a parse tree produced by ChronoParser#includeHeaderContent.
    def exitIncludeHeaderContent(self, ctx:ChronoParser.IncludeHeaderContentContext):
        pass


    # Enter a parse tree produced by ChronoParser#importDirective.
    def enterImportDirective(self, ctx:ChronoParser.ImportDirectiveContext):
        pass

    # Exit a parse tree produced by ChronoParser#importDirective.
    def exitImportDirective(self, ctx:ChronoParser.ImportDirectiveContext):
        pass


    # Enter a parse tree produced by ChronoParser#usingAlias.
    def enterUsingAlias(self, ctx:ChronoParser.UsingAliasContext):
        pass

    # Exit a parse tree produced by ChronoParser#usingAlias.
    def exitUsingAlias(self, ctx:ChronoParser.UsingAliasContext):
        pass


    # Enter a parse tree produced by ChronoParser#typemapDefinition.
    def enterTypemapDefinition(self, ctx:ChronoParser.TypemapDefinitionContext):
        pass

    # Exit a parse tree produced by ChronoParser#typemapDefinition.
    def exitTypemapDefinition(self, ctx:ChronoParser.TypemapDefinitionContext):
        pass


    # Enter a parse tree produced by ChronoParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:ChronoParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by ChronoParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:ChronoParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by ChronoParser#parameters.
    def enterParameters(self, ctx:ChronoParser.ParametersContext):
        pass

    # Exit a parse tree produced by ChronoParser#parameters.
    def exitParameters(self, ctx:ChronoParser.ParametersContext):
        pass


    # Enter a parse tree produced by ChronoParser#parameter.
    def enterParameter(self, ctx:ChronoParser.ParameterContext):
        pass

    # Exit a parse tree produced by ChronoParser#parameter.
    def exitParameter(self, ctx:ChronoParser.ParameterContext):
        pass


    # Enter a parse tree produced by ChronoParser#cppBlock.
    def enterCppBlock(self, ctx:ChronoParser.CppBlockContext):
        pass

    # Exit a parse tree produced by ChronoParser#cppBlock.
    def exitCppBlock(self, ctx:ChronoParser.CppBlockContext):
        pass


    # Enter a parse tree produced by ChronoParser#returnStatement.
    def enterReturnStatement(self, ctx:ChronoParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#returnStatement.
    def exitReturnStatement(self, ctx:ChronoParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:ChronoParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by ChronoParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:ChronoParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by ChronoParser#assignment.
    def enterAssignment(self, ctx:ChronoParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ChronoParser#assignment.
    def exitAssignment(self, ctx:ChronoParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ChronoParser#assignableExpression.
    def enterAssignableExpression(self, ctx:ChronoParser.AssignableExpressionContext):
        pass

    # Exit a parse tree produced by ChronoParser#assignableExpression.
    def exitAssignableExpression(self, ctx:ChronoParser.AssignableExpressionContext):
        pass


    # Enter a parse tree produced by ChronoParser#assignablePrimary.
    def enterAssignablePrimary(self, ctx:ChronoParser.AssignablePrimaryContext):
        pass

    # Exit a parse tree produced by ChronoParser#assignablePrimary.
    def exitAssignablePrimary(self, ctx:ChronoParser.AssignablePrimaryContext):
        pass


    # Enter a parse tree produced by ChronoParser#ifStatement.
    def enterIfStatement(self, ctx:ChronoParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#ifStatement.
    def exitIfStatement(self, ctx:ChronoParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#ifBlock.
    def enterIfBlock(self, ctx:ChronoParser.IfBlockContext):
        pass

    # Exit a parse tree produced by ChronoParser#ifBlock.
    def exitIfBlock(self, ctx:ChronoParser.IfBlockContext):
        pass


    # Enter a parse tree produced by ChronoParser#elseBlock.
    def enterElseBlock(self, ctx:ChronoParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by ChronoParser#elseBlock.
    def exitElseBlock(self, ctx:ChronoParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by ChronoParser#whileStatement.
    def enterWhileStatement(self, ctx:ChronoParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#whileStatement.
    def exitWhileStatement(self, ctx:ChronoParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#statement.
    def enterStatement(self, ctx:ChronoParser.StatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#statement.
    def exitStatement(self, ctx:ChronoParser.StatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#blockStatement.
    def enterBlockStatement(self, ctx:ChronoParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#blockStatement.
    def exitBlockStatement(self, ctx:ChronoParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#caseBlock.
    def enterCaseBlock(self, ctx:ChronoParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by ChronoParser#caseBlock.
    def exitCaseBlock(self, ctx:ChronoParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by ChronoParser#defaultBlock.
    def enterDefaultBlock(self, ctx:ChronoParser.DefaultBlockContext):
        pass

    # Exit a parse tree produced by ChronoParser#defaultBlock.
    def exitDefaultBlock(self, ctx:ChronoParser.DefaultBlockContext):
        pass


    # Enter a parse tree produced by ChronoParser#switchStatement.
    def enterSwitchStatement(self, ctx:ChronoParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#switchStatement.
    def exitSwitchStatement(self, ctx:ChronoParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#deleteStatement.
    def enterDeleteStatement(self, ctx:ChronoParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#deleteStatement.
    def exitDeleteStatement(self, ctx:ChronoParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#forStatement.
    def enterForStatement(self, ctx:ChronoParser.ForStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#forStatement.
    def exitForStatement(self, ctx:ChronoParser.ForStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#forInit.
    def enterForInit(self, ctx:ChronoParser.ForInitContext):
        pass

    # Exit a parse tree produced by ChronoParser#forInit.
    def exitForInit(self, ctx:ChronoParser.ForInitContext):
        pass


    # Enter a parse tree produced by ChronoParser#forIncrement.
    def enterForIncrement(self, ctx:ChronoParser.ForIncrementContext):
        pass

    # Exit a parse tree produced by ChronoParser#forIncrement.
    def exitForIncrement(self, ctx:ChronoParser.ForIncrementContext):
        pass


    # Enter a parse tree produced by ChronoParser#methodSignature.
    def enterMethodSignature(self, ctx:ChronoParser.MethodSignatureContext):
        pass

    # Exit a parse tree produced by ChronoParser#methodSignature.
    def exitMethodSignature(self, ctx:ChronoParser.MethodSignatureContext):
        pass


    # Enter a parse tree produced by ChronoParser#interfaceDefinition.
    def enterInterfaceDefinition(self, ctx:ChronoParser.InterfaceDefinitionContext):
        pass

    # Exit a parse tree produced by ChronoParser#interfaceDefinition.
    def exitInterfaceDefinition(self, ctx:ChronoParser.InterfaceDefinitionContext):
        pass


    # Enter a parse tree produced by ChronoParser#variableDeclaration_no_semicolon.
    def enterVariableDeclaration_no_semicolon(self, ctx:ChronoParser.VariableDeclaration_no_semicolonContext):
        pass

    # Exit a parse tree produced by ChronoParser#variableDeclaration_no_semicolon.
    def exitVariableDeclaration_no_semicolon(self, ctx:ChronoParser.VariableDeclaration_no_semicolonContext):
        pass


    # Enter a parse tree produced by ChronoParser#assignment_no_semicolon.
    def enterAssignment_no_semicolon(self, ctx:ChronoParser.Assignment_no_semicolonContext):
        pass

    # Exit a parse tree produced by ChronoParser#assignment_no_semicolon.
    def exitAssignment_no_semicolon(self, ctx:ChronoParser.Assignment_no_semicolonContext):
        pass


    # Enter a parse tree produced by ChronoParser#baseInitializer.
    def enterBaseInitializer(self, ctx:ChronoParser.BaseInitializerContext):
        pass

    # Exit a parse tree produced by ChronoParser#baseInitializer.
    def exitBaseInitializer(self, ctx:ChronoParser.BaseInitializerContext):
        pass


    # Enter a parse tree produced by ChronoParser#expression.
    def enterExpression(self, ctx:ChronoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ChronoParser#expression.
    def exitExpression(self, ctx:ChronoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ChronoParser#unaryExpression.
    def enterUnaryExpression(self, ctx:ChronoParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by ChronoParser#unaryExpression.
    def exitUnaryExpression(self, ctx:ChronoParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by ChronoParser#simpleExpression.
    def enterSimpleExpression(self, ctx:ChronoParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by ChronoParser#simpleExpression.
    def exitSimpleExpression(self, ctx:ChronoParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by ChronoParser#primary.
    def enterPrimary(self, ctx:ChronoParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ChronoParser#primary.
    def exitPrimary(self, ctx:ChronoParser.PrimaryContext):
        pass


    # Enter a parse tree produced by ChronoParser#initializerList.
    def enterInitializerList(self, ctx:ChronoParser.InitializerListContext):
        pass

    # Exit a parse tree produced by ChronoParser#initializerList.
    def exitInitializerList(self, ctx:ChronoParser.InitializerListContext):
        pass


    # Enter a parse tree produced by ChronoParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:ChronoParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by ChronoParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:ChronoParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by ChronoParser#expressionList.
    def enterExpressionList(self, ctx:ChronoParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by ChronoParser#expressionList.
    def exitExpressionList(self, ctx:ChronoParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by ChronoParser#literal.
    def enterLiteral(self, ctx:ChronoParser.LiteralContext):
        pass

    # Exit a parse tree produced by ChronoParser#literal.
    def exitLiteral(self, ctx:ChronoParser.LiteralContext):
        pass



del ChronoParser