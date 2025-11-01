# Generated from grammar/ChronoParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,191,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,4,0,45,8,0,11,0,12,0,46,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,5,1,59,8,1,10,1,12,1,62,9,1,1,1,1,1,1,2,1,2,1,2,5,
        2,69,8,2,10,2,12,2,72,9,2,1,2,1,2,1,3,1,3,3,3,78,8,3,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,93,8,5,10,5,12,5,96,
        9,5,1,5,1,5,1,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,3,6,108,8,
        6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,120,8,8,1,8,1,8,1,
        9,1,9,5,9,126,8,9,10,9,12,9,129,9,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,3,11,140,8,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,
        148,8,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,161,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,170,8,14,1,
        15,1,15,1,15,1,15,1,15,3,15,177,8,15,1,15,1,15,1,16,1,16,1,16,5,
        16,184,8,16,10,16,12,16,187,9,16,1,17,1,17,1,17,0,0,18,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,0,3,2,0,20,20,22,22,2,0,7,
        7,19,19,1,0,21,22,197,0,39,1,0,0,0,2,50,1,0,0,0,4,65,1,0,0,0,6,77,
        1,0,0,0,8,79,1,0,0,0,10,83,1,0,0,0,12,107,1,0,0,0,14,109,1,0,0,0,
        16,113,1,0,0,0,18,123,1,0,0,0,20,132,1,0,0,0,22,136,1,0,0,0,24,147,
        1,0,0,0,26,160,1,0,0,0,28,169,1,0,0,0,30,171,1,0,0,0,32,180,1,0,
        0,0,34,188,1,0,0,0,36,38,3,6,3,0,37,36,1,0,0,0,38,41,1,0,0,0,39,
        37,1,0,0,0,39,40,1,0,0,0,40,44,1,0,0,0,41,39,1,0,0,0,42,45,3,2,1,
        0,43,45,3,10,5,0,44,42,1,0,0,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,
        1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,
        51,5,5,0,0,51,52,5,19,0,0,52,53,5,14,0,0,53,54,5,19,0,0,54,60,5,
        12,0,0,55,59,3,16,8,0,56,59,3,10,5,0,57,59,3,4,2,0,58,55,1,0,0,0,
        58,56,1,0,0,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,
        0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,13,0,0,64,3,1,0,0,0,65,
        66,5,6,0,0,66,70,5,12,0,0,67,69,3,26,13,0,68,67,1,0,0,0,69,72,1,
        0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,0,73,
        74,5,13,0,0,74,5,1,0,0,0,75,78,3,8,4,0,76,78,3,18,9,0,77,75,1,0,
        0,0,77,76,1,0,0,0,78,7,1,0,0,0,79,80,5,1,0,0,80,81,7,0,0,0,81,82,
        5,9,0,0,82,9,1,0,0,0,83,84,5,2,0,0,84,85,5,19,0,0,85,86,5,10,0,0,
        86,87,3,12,6,0,87,88,5,11,0,0,88,89,5,16,0,0,89,90,5,19,0,0,90,94,
        5,12,0,0,91,93,3,26,13,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,
        0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,13,0,0,98,11,
        1,0,0,0,99,104,3,14,7,0,100,101,5,18,0,0,101,103,3,14,7,0,102,100,
        1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,108,
        1,0,0,0,106,104,1,0,0,0,107,99,1,0,0,0,107,108,1,0,0,0,108,13,1,
        0,0,0,109,110,5,19,0,0,110,111,5,14,0,0,111,112,5,19,0,0,112,15,
        1,0,0,0,113,114,5,3,0,0,114,115,5,19,0,0,115,116,5,14,0,0,116,119,
        5,19,0,0,117,118,5,15,0,0,118,120,3,28,14,0,119,117,1,0,0,0,119,
        120,1,0,0,0,120,121,1,0,0,0,121,122,5,9,0,0,122,17,1,0,0,0,123,127,
        5,8,0,0,124,126,5,26,0,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,
        5,25,0,0,131,19,1,0,0,0,132,133,5,4,0,0,133,134,3,28,14,0,134,135,
        5,9,0,0,135,21,1,0,0,0,136,137,5,19,0,0,137,139,5,10,0,0,138,140,
        3,32,16,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,
        5,11,0,0,142,23,1,0,0,0,143,144,5,7,0,0,144,145,5,17,0,0,145,148,
        5,19,0,0,146,148,5,19,0,0,147,143,1,0,0,0,147,146,1,0,0,0,148,149,
        1,0,0,0,149,150,5,15,0,0,150,151,3,28,14,0,151,152,5,9,0,0,152,25,
        1,0,0,0,153,161,3,16,8,0,154,161,3,24,12,0,155,161,3,20,10,0,156,
        157,3,28,14,0,157,158,5,9,0,0,158,161,1,0,0,0,159,161,3,18,9,0,160,
        153,1,0,0,0,160,154,1,0,0,0,160,155,1,0,0,0,160,156,1,0,0,0,160,
        159,1,0,0,0,161,27,1,0,0,0,162,170,3,34,17,0,163,170,5,19,0,0,164,
        170,3,30,15,0,165,170,3,22,11,0,166,167,5,7,0,0,167,168,5,17,0,0,
        168,170,5,19,0,0,169,162,1,0,0,0,169,163,1,0,0,0,169,164,1,0,0,0,
        169,165,1,0,0,0,169,166,1,0,0,0,170,29,1,0,0,0,171,172,7,1,0,0,172,
        173,5,17,0,0,173,174,5,19,0,0,174,176,5,10,0,0,175,177,3,32,16,0,
        176,175,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,179,5,11,0,0,
        179,31,1,0,0,0,180,185,3,28,14,0,181,182,5,18,0,0,182,184,3,28,14,
        0,183,181,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,
        0,186,33,1,0,0,0,187,185,1,0,0,0,188,189,7,2,0,0,189,35,1,0,0,0,
        18,39,44,46,58,60,70,77,94,104,107,119,127,139,147,160,169,176,185
    ]

class ChronoParser ( Parser ):

    grammarFileName = "ChronoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'func'", "'let'", "'return'", 
                     "'class'", "'deinit'", "'this'", "'@cpp'", "';'", "'('", 
                     "')'", "'{'", "'}'", "':'", "'='", "'->'", "'.'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'@end'" ]

    symbolicNames = [ "<INVALID>", "IMPORT", "FUNC", "LET", "RETURN", "CLASS", 
                      "DEINIT", "THIS", "AT_CPP", "SEMIC_TOKEN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "COLON", "ASSIGN", "ARROW", 
                      "DOT", "COMMA", "IDENTIFIER", "INCLUDE_PATH", "INTEGER_LITERAL", 
                      "STRING_LITERAL", "LINE_COMMENT", "WHITESPACE", "AT_END", 
                      "CPP_BODY" ]

    RULE_program = 0
    RULE_classDefinition = 1
    RULE_deinitBlock = 2
    RULE_globalStatement = 3
    RULE_importDirective = 4
    RULE_functionDefinition = 5
    RULE_parameters = 6
    RULE_parameter = 7
    RULE_declaration = 8
    RULE_cppBlock = 9
    RULE_returnStatement = 10
    RULE_functionCallExpression = 11
    RULE_assignment = 12
    RULE_statement = 13
    RULE_expression = 14
    RULE_methodCallExpression = 15
    RULE_expressionList = 16
    RULE_literal = 17

    ruleNames =  [ "program", "classDefinition", "deinitBlock", "globalStatement", 
                   "importDirective", "functionDefinition", "parameters", 
                   "parameter", "declaration", "cppBlock", "returnStatement", 
                   "functionCallExpression", "assignment", "statement", 
                   "expression", "methodCallExpression", "expressionList", 
                   "literal" ]

    EOF = Token.EOF
    IMPORT=1
    FUNC=2
    LET=3
    RETURN=4
    CLASS=5
    DEINIT=6
    THIS=7
    AT_CPP=8
    SEMIC_TOKEN=9
    LPAREN=10
    RPAREN=11
    LBRACE=12
    RBRACE=13
    COLON=14
    ASSIGN=15
    ARROW=16
    DOT=17
    COMMA=18
    IDENTIFIER=19
    INCLUDE_PATH=20
    INTEGER_LITERAL=21
    STRING_LITERAL=22
    LINE_COMMENT=23
    WHITESPACE=24
    AT_END=25
    CPP_BODY=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ChronoParser.EOF, 0)

        def globalStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.GlobalStatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.GlobalStatementContext,i)


        def classDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ClassDefinitionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ClassDefinitionContext,i)


        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.FunctionDefinitionContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ChronoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==8:
                self.state = 36
                self.globalStatement()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 42
                    self.classDefinition()
                    pass
                elif token in [2]:
                    self.state = 43
                    self.functionDefinition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==5):
                    break

            self.state = 48
            self.match(ChronoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.base = None # Token

        def CLASS(self):
            return self.getToken(ChronoParser.CLASS, 0)

        def COLON(self):
            return self.getToken(ChronoParser.COLON, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ChronoParser.DeclarationContext,i)


        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.FunctionDefinitionContext,i)


        def deinitBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.DeinitBlockContext)
            else:
                return self.getTypedRuleContext(ChronoParser.DeinitBlockContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_classDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefinition" ):
                listener.enterClassDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefinition" ):
                listener.exitClassDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDefinition" ):
                return visitor.visitClassDefinition(self)
            else:
                return visitor.visitChildren(self)




    def classDefinition(self):

        localctx = ChronoParser.ClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ChronoParser.CLASS)
            self.state = 51
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 52
            self.match(ChronoParser.COLON)
            self.state = 53
            localctx.base = self.match(ChronoParser.IDENTIFIER)
            self.state = 54
            self.match(ChronoParser.LBRACE)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 76) != 0):
                self.state = 58
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 55
                    self.declaration()
                    pass
                elif token in [2]:
                    self.state = 56
                    self.functionDefinition()
                    pass
                elif token in [6]:
                    self.state = 57
                    self.deinitBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeinitBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEINIT(self):
            return self.getToken(ChronoParser.DEINIT, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_deinitBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeinitBlock" ):
                listener.enterDeinitBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeinitBlock" ):
                listener.exitDeinitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeinitBlock" ):
                return visitor.visitDeinitBlock(self)
            else:
                return visitor.visitChildren(self)




    def deinitBlock(self):

        localctx = ChronoParser.DeinitBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_deinitBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ChronoParser.DEINIT)
            self.state = 66
            self.match(ChronoParser.LBRACE)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6816152) != 0):
                self.state = 67
                self.statement()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importDirective(self):
            return self.getTypedRuleContext(ChronoParser.ImportDirectiveContext,0)


        def cppBlock(self):
            return self.getTypedRuleContext(ChronoParser.CppBlockContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_globalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalStatement" ):
                listener.enterGlobalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalStatement" ):
                listener.exitGlobalStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalStatement" ):
                return visitor.visitGlobalStatement(self)
            else:
                return visitor.visitChildren(self)




    def globalStatement(self):

        localctx = ChronoParser.GlobalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_globalStatement)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.importDirective()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.cppBlock()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.path = None # Token

        def IMPORT(self):
            return self.getToken(ChronoParser.IMPORT, 0)

        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def STRING_LITERAL(self):
            return self.getToken(ChronoParser.STRING_LITERAL, 0)

        def INCLUDE_PATH(self):
            return self.getToken(ChronoParser.INCLUDE_PATH, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_importDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDirective" ):
                listener.enterImportDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDirective" ):
                listener.exitImportDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDirective" ):
                return visitor.visitImportDirective(self)
            else:
                return visitor.visitChildren(self)




    def importDirective(self):

        localctx = ChronoParser.ImportDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_importDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ChronoParser.IMPORT)
            self.state = 80
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==20 or _la==22):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 81
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.returnType = None # Token

        def FUNC(self):
            return self.getToken(ChronoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(ChronoParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(ChronoParser.ARROW, 0)

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = ChronoParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ChronoParser.FUNC)
            self.state = 84
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 85
            self.match(ChronoParser.LPAREN)
            self.state = 86
            self.parameters()
            self.state = 87
            self.match(ChronoParser.RPAREN)
            self.state = 88
            self.match(ChronoParser.ARROW)
            self.state = 89
            localctx.returnType = self.match(ChronoParser.IDENTIFIER)
            self.state = 90
            self.match(ChronoParser.LBRACE)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6816152) != 0):
                self.state = 91
                self.statement()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ParameterContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.COMMA)
            else:
                return self.getToken(ChronoParser.COMMA, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = ChronoParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 99
                self.parameter()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 100
                    self.match(ChronoParser.COMMA)
                    self.state = 101
                    self.parameter()
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.typeName = None # Token

        def COLON(self):
            return self.getToken(ChronoParser.COLON, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ChronoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 110
            self.match(ChronoParser.COLON)
            self.state = 111
            localctx.typeName = self.match(ChronoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variableName = None # Token
            self.typeName = None # Token

        def LET(self):
            return self.getToken(ChronoParser.LET, 0)

        def COLON(self):
            return self.getToken(ChronoParser.COLON, 0)

        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def ASSIGN(self):
            return self.getToken(ChronoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ChronoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ChronoParser.LET)
            self.state = 114
            localctx.variableName = self.match(ChronoParser.IDENTIFIER)
            self.state = 115
            self.match(ChronoParser.COLON)
            self.state = 116
            localctx.typeName = self.match(ChronoParser.IDENTIFIER)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 117
                self.match(ChronoParser.ASSIGN)
                self.state = 118
                self.expression()


            self.state = 121
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CppBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_CPP(self):
            return self.getToken(ChronoParser.AT_CPP, 0)

        def AT_END(self):
            return self.getToken(ChronoParser.AT_END, 0)

        def CPP_BODY(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.CPP_BODY)
            else:
                return self.getToken(ChronoParser.CPP_BODY, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_cppBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCppBlock" ):
                listener.enterCppBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCppBlock" ):
                listener.exitCppBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCppBlock" ):
                return visitor.visitCppBlock(self)
            else:
                return visitor.visitChildren(self)




    def cppBlock(self):

        localctx = ChronoParser.CppBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cppBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ChronoParser.AT_CPP)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 124
                self.match(ChronoParser.CPP_BODY)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(ChronoParser.AT_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ChronoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = ChronoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ChronoParser.RETURN)
            self.state = 133
            self.expression()
            self.state = 134
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def expressionList(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_functionCallExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpression" ):
                listener.enterFunctionCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpression" ):
                listener.exitFunctionCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpression" ):
                return visitor.visitFunctionCallExpression(self)
            else:
                return visitor.visitChildren(self)




    def functionCallExpression(self):

        localctx = ChronoParser.FunctionCallExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 137
            self.match(ChronoParser.LPAREN)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6815872) != 0):
                self.state = 138
                self.expressionList()


            self.state = 141
            self.match(ChronoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ChronoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def THIS(self):
            return self.getToken(ChronoParser.THIS, 0)

        def DOT(self):
            return self.getToken(ChronoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ChronoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 143
                self.match(ChronoParser.THIS)
                self.state = 144
                self.match(ChronoParser.DOT)
                self.state = 145
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [19]:
                self.state = 146
                self.match(ChronoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 149
            self.match(ChronoParser.ASSIGN)
            self.state = 150
            self.expression()
            self.state = 151
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ChronoParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ChronoParser.AssignmentContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ChronoParser.ReturnStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

        def cppBlock(self):
            return self.getTypedRuleContext(ChronoParser.CppBlockContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ChronoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.expression()
                self.state = 157
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.cppBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ChronoParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def methodCallExpression(self):
            return self.getTypedRuleContext(ChronoParser.MethodCallExpressionContext,0)


        def functionCallExpression(self):
            return self.getTypedRuleContext(ChronoParser.FunctionCallExpressionContext,0)


        def THIS(self):
            return self.getToken(ChronoParser.THIS, 0)

        def DOT(self):
            return self.getToken(ChronoParser.DOT, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ChronoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(ChronoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.methodCallExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.functionCallExpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.match(ChronoParser.THIS)
                self.state = 167
                self.match(ChronoParser.DOT)
                self.state = 168
                self.match(ChronoParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.receiver = None # Token
            self.methodName = None # Token

        def DOT(self):
            return self.getToken(ChronoParser.DOT, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def THIS(self):
            return self.getToken(ChronoParser.THIS, 0)

        def expressionList(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_methodCallExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCallExpression" ):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCallExpression" ):
                listener.exitMethodCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallExpression" ):
                return visitor.visitMethodCallExpression(self)
            else:
                return visitor.visitChildren(self)




    def methodCallExpression(self):

        localctx = ChronoParser.MethodCallExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_methodCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            localctx.receiver = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==7 or _la==19):
                localctx.receiver = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self.match(ChronoParser.DOT)
            self.state = 173
            localctx.methodName = self.match(ChronoParser.IDENTIFIER)
            self.state = 174
            self.match(ChronoParser.LPAREN)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6815872) != 0):
                self.state = 175
                self.expressionList()


            self.state = 178
            self.match(ChronoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.COMMA)
            else:
                return self.getToken(ChronoParser.COMMA, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = ChronoParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.expression()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 181
                self.match(ChronoParser.COMMA)
                self.state = 182
                self.expression()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(ChronoParser.INTEGER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(ChronoParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ChronoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





