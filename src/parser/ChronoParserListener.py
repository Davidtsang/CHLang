# Generated from grammar/ChronoParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChronoParser import ChronoParser
else:
    from ChronoParser import ChronoParser

# This class defines a complete listener for a parse tree produced by ChronoParser.
class ChronoParserListener(ParseTreeListener):

    # Enter a parse tree produced by ChronoParser#program.
    def enterProgram(self, ctx:ChronoParser.ProgramContext):
        pass

    # Exit a parse tree produced by ChronoParser#program.
    def exitProgram(self, ctx:ChronoParser.ProgramContext):
        pass


    # Enter a parse tree produced by ChronoParser#topLevelStatement.
    def enterTopLevelStatement(self, ctx:ChronoParser.TopLevelStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#topLevelStatement.
    def exitTopLevelStatement(self, ctx:ChronoParser.TopLevelStatementContext):
        pass


    # Enter a parse tree produced by ChronoParser#classDefinition.
    def enterClassDefinition(self, ctx:ChronoParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by ChronoParser#classDefinition.
    def exitClassDefinition(self, ctx:ChronoParser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by ChronoParser#deinitBlock.
    def enterDeinitBlock(self, ctx:ChronoParser.DeinitBlockContext):
        pass

    # Exit a parse tree produced by ChronoParser#deinitBlock.
    def exitDeinitBlock(self, ctx:ChronoParser.DeinitBlockContext):
        pass


    # Enter a parse tree produced by ChronoParser#importDirective.
    def enterImportDirective(self, ctx:ChronoParser.ImportDirectiveContext):
        pass

    # Exit a parse tree produced by ChronoParser#importDirective.
    def exitImportDirective(self, ctx:ChronoParser.ImportDirectiveContext):
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


    # Enter a parse tree produced by ChronoParser#declaration.
    def enterDeclaration(self, ctx:ChronoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ChronoParser#declaration.
    def exitDeclaration(self, ctx:ChronoParser.DeclarationContext):
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


    # Enter a parse tree produced by ChronoParser#ifStatement.
    def enterIfStatement(self, ctx:ChronoParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ChronoParser#ifStatement.
    def exitIfStatement(self, ctx:ChronoParser.IfStatementContext):
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


    # Enter a parse tree produced by ChronoParser#expression.
    def enterExpression(self, ctx:ChronoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ChronoParser#expression.
    def exitExpression(self, ctx:ChronoParser.ExpressionContext):
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