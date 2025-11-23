# Generated from src/parser/CHParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CHParser import CHParser
else:
    from CHParser import CHParser

# This class defines a complete listener for a parse tree produced by CHParser.
class CHParserListener(ParseTreeListener):

    # Enter a parse tree produced by CHParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CHParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CHParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CHParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CHParser#baseType.
    def enterBaseType(self, ctx:CHParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by CHParser#baseType.
    def exitBaseType(self, ctx:CHParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by CHParser#typeList.
    def enterTypeList(self, ctx:CHParser.TypeListContext):
        pass

    # Exit a parse tree produced by CHParser#typeList.
    def exitTypeList(self, ctx:CHParser.TypeListContext):
        pass


    # Enter a parse tree produced by CHParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:CHParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by CHParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:CHParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by CHParser#templateArgument.
    def enterTemplateArgument(self, ctx:CHParser.TemplateArgumentContext):
        pass

    # Exit a parse tree produced by CHParser#templateArgument.
    def exitTemplateArgument(self, ctx:CHParser.TemplateArgumentContext):
        pass


    # Enter a parse tree produced by CHParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:CHParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by CHParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:CHParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by CHParser#namespaceStatement.
    def enterNamespaceStatement(self, ctx:CHParser.NamespaceStatementContext):
        pass

    # Exit a parse tree produced by CHParser#namespaceStatement.
    def exitNamespaceStatement(self, ctx:CHParser.NamespaceStatementContext):
        pass


    # Enter a parse tree produced by CHParser#program.
    def enterProgram(self, ctx:CHParser.ProgramContext):
        pass

    # Exit a parse tree produced by CHParser#program.
    def exitProgram(self, ctx:CHParser.ProgramContext):
        pass


    # Enter a parse tree produced by CHParser#topLevelImport.
    def enterTopLevelImport(self, ctx:CHParser.TopLevelImportContext):
        pass

    # Exit a parse tree produced by CHParser#topLevelImport.
    def exitTopLevelImport(self, ctx:CHParser.TopLevelImportContext):
        pass


    # Enter a parse tree produced by CHParser#topLevelStatement.
    def enterTopLevelStatement(self, ctx:CHParser.TopLevelStatementContext):
        pass

    # Exit a parse tree produced by CHParser#topLevelStatement.
    def exitTopLevelStatement(self, ctx:CHParser.TopLevelStatementContext):
        pass


    # Enter a parse tree produced by CHParser#forwardDeclaration.
    def enterForwardDeclaration(self, ctx:CHParser.ForwardDeclarationContext):
        pass

    # Exit a parse tree produced by CHParser#forwardDeclaration.
    def exitForwardDeclaration(self, ctx:CHParser.ForwardDeclarationContext):
        pass


    # Enter a parse tree produced by CHParser#accessModifier.
    def enterAccessModifier(self, ctx:CHParser.AccessModifierContext):
        pass

    # Exit a parse tree produced by CHParser#accessModifier.
    def exitAccessModifier(self, ctx:CHParser.AccessModifierContext):
        pass


    # Enter a parse tree produced by CHParser#endNamespaceStatement.
    def enterEndNamespaceStatement(self, ctx:CHParser.EndNamespaceStatementContext):
        pass

    # Exit a parse tree produced by CHParser#endNamespaceStatement.
    def exitEndNamespaceStatement(self, ctx:CHParser.EndNamespaceStatementContext):
        pass


    # Enter a parse tree produced by CHParser#initSignature.
    def enterInitSignature(self, ctx:CHParser.InitSignatureContext):
        pass

    # Exit a parse tree produced by CHParser#initSignature.
    def exitInitSignature(self, ctx:CHParser.InitSignatureContext):
        pass


    # Enter a parse tree produced by CHParser#deinitSignature.
    def enterDeinitSignature(self, ctx:CHParser.DeinitSignatureContext):
        pass

    # Exit a parse tree produced by CHParser#deinitSignature.
    def exitDeinitSignature(self, ctx:CHParser.DeinitSignatureContext):
        pass


    # Enter a parse tree produced by CHParser#classBodyStatement.
    def enterClassBodyStatement(self, ctx:CHParser.ClassBodyStatementContext):
        pass

    # Exit a parse tree produced by CHParser#classBodyStatement.
    def exitClassBodyStatement(self, ctx:CHParser.ClassBodyStatementContext):
        pass


    # Enter a parse tree produced by CHParser#classDefinition.
    def enterClassDefinition(self, ctx:CHParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by CHParser#classDefinition.
    def exitClassDefinition(self, ctx:CHParser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by CHParser#implementationBlock.
    def enterImplementationBlock(self, ctx:CHParser.ImplementationBlockContext):
        pass

    # Exit a parse tree produced by CHParser#implementationBlock.
    def exitImplementationBlock(self, ctx:CHParser.ImplementationBlockContext):
        pass


    # Enter a parse tree produced by CHParser#structDefinition.
    def enterStructDefinition(self, ctx:CHParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by CHParser#structDefinition.
    def exitStructDefinition(self, ctx:CHParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by CHParser#structBodyStatement.
    def enterStructBodyStatement(self, ctx:CHParser.StructBodyStatementContext):
        pass

    # Exit a parse tree produced by CHParser#structBodyStatement.
    def exitStructBodyStatement(self, ctx:CHParser.StructBodyStatementContext):
        pass


    # Enter a parse tree produced by CHParser#enumDefinition.
    def enterEnumDefinition(self, ctx:CHParser.EnumDefinitionContext):
        pass

    # Exit a parse tree produced by CHParser#enumDefinition.
    def exitEnumDefinition(self, ctx:CHParser.EnumDefinitionContext):
        pass


    # Enter a parse tree produced by CHParser#enumBody.
    def enterEnumBody(self, ctx:CHParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by CHParser#enumBody.
    def exitEnumBody(self, ctx:CHParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by CHParser#enumItem.
    def enterEnumItem(self, ctx:CHParser.EnumItemContext):
        pass

    # Exit a parse tree produced by CHParser#enumItem.
    def exitEnumItem(self, ctx:CHParser.EnumItemContext):
        pass


    # Enter a parse tree produced by CHParser#functionSignature.
    def enterFunctionSignature(self, ctx:CHParser.FunctionSignatureContext):
        pass

    # Exit a parse tree produced by CHParser#functionSignature.
    def exitFunctionSignature(self, ctx:CHParser.FunctionSignatureContext):
        pass


    # Enter a parse tree produced by CHParser#methodDefinition.
    def enterMethodDefinition(self, ctx:CHParser.MethodDefinitionContext):
        pass

    # Exit a parse tree produced by CHParser#methodDefinition.
    def exitMethodDefinition(self, ctx:CHParser.MethodDefinitionContext):
        pass


    # Enter a parse tree produced by CHParser#initDefinition.
    def enterInitDefinition(self, ctx:CHParser.InitDefinitionContext):
        pass

    # Exit a parse tree produced by CHParser#initDefinition.
    def exitInitDefinition(self, ctx:CHParser.InitDefinitionContext):
        pass


    # Enter a parse tree produced by CHParser#deinitBlock.
    def enterDeinitBlock(self, ctx:CHParser.DeinitBlockContext):
        pass

    # Exit a parse tree produced by CHParser#deinitBlock.
    def exitDeinitBlock(self, ctx:CHParser.DeinitBlockContext):
        pass


    # Enter a parse tree produced by CHParser#includeHeaderContent.
    def enterIncludeHeaderContent(self, ctx:CHParser.IncludeHeaderContentContext):
        pass

    # Exit a parse tree produced by CHParser#includeHeaderContent.
    def exitIncludeHeaderContent(self, ctx:CHParser.IncludeHeaderContentContext):
        pass


    # Enter a parse tree produced by CHParser#importDirective.
    def enterImportDirective(self, ctx:CHParser.ImportDirectiveContext):
        pass

    # Exit a parse tree produced by CHParser#importDirective.
    def exitImportDirective(self, ctx:CHParser.ImportDirectiveContext):
        pass


    # Enter a parse tree produced by CHParser#usingAlias.
    def enterUsingAlias(self, ctx:CHParser.UsingAliasContext):
        pass

    # Exit a parse tree produced by CHParser#usingAlias.
    def exitUsingAlias(self, ctx:CHParser.UsingAliasContext):
        pass


    # Enter a parse tree produced by CHParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CHParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CHParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CHParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CHParser#parameters.
    def enterParameters(self, ctx:CHParser.ParametersContext):
        pass

    # Exit a parse tree produced by CHParser#parameters.
    def exitParameters(self, ctx:CHParser.ParametersContext):
        pass


    # Enter a parse tree produced by CHParser#parameter.
    def enterParameter(self, ctx:CHParser.ParameterContext):
        pass

    # Exit a parse tree produced by CHParser#parameter.
    def exitParameter(self, ctx:CHParser.ParameterContext):
        pass


    # Enter a parse tree produced by CHParser#cppBlock.
    def enterCppBlock(self, ctx:CHParser.CppBlockContext):
        pass

    # Exit a parse tree produced by CHParser#cppBlock.
    def exitCppBlock(self, ctx:CHParser.CppBlockContext):
        pass


    # Enter a parse tree produced by CHParser#returnStatement.
    def enterReturnStatement(self, ctx:CHParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CHParser#returnStatement.
    def exitReturnStatement(self, ctx:CHParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CHParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:CHParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by CHParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:CHParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by CHParser#assignment.
    def enterAssignment(self, ctx:CHParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CHParser#assignment.
    def exitAssignment(self, ctx:CHParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CHParser#assignableExpression.
    def enterAssignableExpression(self, ctx:CHParser.AssignableExpressionContext):
        pass

    # Exit a parse tree produced by CHParser#assignableExpression.
    def exitAssignableExpression(self, ctx:CHParser.AssignableExpressionContext):
        pass


    # Enter a parse tree produced by CHParser#assignablePrimary.
    def enterAssignablePrimary(self, ctx:CHParser.AssignablePrimaryContext):
        pass

    # Exit a parse tree produced by CHParser#assignablePrimary.
    def exitAssignablePrimary(self, ctx:CHParser.AssignablePrimaryContext):
        pass


    # Enter a parse tree produced by CHParser#ifStatement.
    def enterIfStatement(self, ctx:CHParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CHParser#ifStatement.
    def exitIfStatement(self, ctx:CHParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CHParser#ifBlock.
    def enterIfBlock(self, ctx:CHParser.IfBlockContext):
        pass

    # Exit a parse tree produced by CHParser#ifBlock.
    def exitIfBlock(self, ctx:CHParser.IfBlockContext):
        pass


    # Enter a parse tree produced by CHParser#elseBlock.
    def enterElseBlock(self, ctx:CHParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by CHParser#elseBlock.
    def exitElseBlock(self, ctx:CHParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by CHParser#whileStatement.
    def enterWhileStatement(self, ctx:CHParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CHParser#whileStatement.
    def exitWhileStatement(self, ctx:CHParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CHParser#statement.
    def enterStatement(self, ctx:CHParser.StatementContext):
        pass

    # Exit a parse tree produced by CHParser#statement.
    def exitStatement(self, ctx:CHParser.StatementContext):
        pass


    # Enter a parse tree produced by CHParser#blockStatement.
    def enterBlockStatement(self, ctx:CHParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by CHParser#blockStatement.
    def exitBlockStatement(self, ctx:CHParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by CHParser#caseBlock.
    def enterCaseBlock(self, ctx:CHParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by CHParser#caseBlock.
    def exitCaseBlock(self, ctx:CHParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by CHParser#defaultBlock.
    def enterDefaultBlock(self, ctx:CHParser.DefaultBlockContext):
        pass

    # Exit a parse tree produced by CHParser#defaultBlock.
    def exitDefaultBlock(self, ctx:CHParser.DefaultBlockContext):
        pass


    # Enter a parse tree produced by CHParser#switchStatement.
    def enterSwitchStatement(self, ctx:CHParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by CHParser#switchStatement.
    def exitSwitchStatement(self, ctx:CHParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by CHParser#deleteStatement.
    def enterDeleteStatement(self, ctx:CHParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by CHParser#deleteStatement.
    def exitDeleteStatement(self, ctx:CHParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by CHParser#forStatement.
    def enterForStatement(self, ctx:CHParser.ForStatementContext):
        pass

    # Exit a parse tree produced by CHParser#forStatement.
    def exitForStatement(self, ctx:CHParser.ForStatementContext):
        pass


    # Enter a parse tree produced by CHParser#forInit.
    def enterForInit(self, ctx:CHParser.ForInitContext):
        pass

    # Exit a parse tree produced by CHParser#forInit.
    def exitForInit(self, ctx:CHParser.ForInitContext):
        pass


    # Enter a parse tree produced by CHParser#forIncrement.
    def enterForIncrement(self, ctx:CHParser.ForIncrementContext):
        pass

    # Exit a parse tree produced by CHParser#forIncrement.
    def exitForIncrement(self, ctx:CHParser.ForIncrementContext):
        pass


    # Enter a parse tree produced by CHParser#methodSignature.
    def enterMethodSignature(self, ctx:CHParser.MethodSignatureContext):
        pass

    # Exit a parse tree produced by CHParser#methodSignature.
    def exitMethodSignature(self, ctx:CHParser.MethodSignatureContext):
        pass


    # Enter a parse tree produced by CHParser#interfaceDefinition.
    def enterInterfaceDefinition(self, ctx:CHParser.InterfaceDefinitionContext):
        pass

    # Exit a parse tree produced by CHParser#interfaceDefinition.
    def exitInterfaceDefinition(self, ctx:CHParser.InterfaceDefinitionContext):
        pass


    # Enter a parse tree produced by CHParser#variableDeclaration_no_semicolon.
    def enterVariableDeclaration_no_semicolon(self, ctx:CHParser.VariableDeclaration_no_semicolonContext):
        pass

    # Exit a parse tree produced by CHParser#variableDeclaration_no_semicolon.
    def exitVariableDeclaration_no_semicolon(self, ctx:CHParser.VariableDeclaration_no_semicolonContext):
        pass


    # Enter a parse tree produced by CHParser#assignment_no_semicolon.
    def enterAssignment_no_semicolon(self, ctx:CHParser.Assignment_no_semicolonContext):
        pass

    # Exit a parse tree produced by CHParser#assignment_no_semicolon.
    def exitAssignment_no_semicolon(self, ctx:CHParser.Assignment_no_semicolonContext):
        pass


    # Enter a parse tree produced by CHParser#baseInitializer.
    def enterBaseInitializer(self, ctx:CHParser.BaseInitializerContext):
        pass

    # Exit a parse tree produced by CHParser#baseInitializer.
    def exitBaseInitializer(self, ctx:CHParser.BaseInitializerContext):
        pass


    # Enter a parse tree produced by CHParser#expression.
    def enterExpression(self, ctx:CHParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CHParser#expression.
    def exitExpression(self, ctx:CHParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CHParser#unaryExpression.
    def enterUnaryExpression(self, ctx:CHParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by CHParser#unaryExpression.
    def exitUnaryExpression(self, ctx:CHParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by CHParser#castExpression.
    def enterCastExpression(self, ctx:CHParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by CHParser#castExpression.
    def exitCastExpression(self, ctx:CHParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by CHParser#simpleExpression.
    def enterSimpleExpression(self, ctx:CHParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by CHParser#simpleExpression.
    def exitSimpleExpression(self, ctx:CHParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by CHParser#primary.
    def enterPrimary(self, ctx:CHParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CHParser#primary.
    def exitPrimary(self, ctx:CHParser.PrimaryContext):
        pass


    # Enter a parse tree produced by CHParser#initializerList.
    def enterInitializerList(self, ctx:CHParser.InitializerListContext):
        pass

    # Exit a parse tree produced by CHParser#initializerList.
    def exitInitializerList(self, ctx:CHParser.InitializerListContext):
        pass


    # Enter a parse tree produced by CHParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:CHParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by CHParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:CHParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by CHParser#expressionList.
    def enterExpressionList(self, ctx:CHParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by CHParser#expressionList.
    def exitExpressionList(self, ctx:CHParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by CHParser#literal.
    def enterLiteral(self, ctx:CHParser.LiteralContext):
        pass

    # Exit a parse tree produced by CHParser#literal.
    def exitLiteral(self, ctx:CHParser.LiteralContext):
        pass



del CHParser