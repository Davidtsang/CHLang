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
        4,1,27,206,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,4,0,40,8,0,
        11,0,12,0,41,1,0,1,0,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,2,1,3,1,3,
        1,3,5,3,71,8,3,10,3,12,3,74,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,3,5,
        83,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,92,8,5,1,5,1,5,5,5,96,8,5,
        10,5,12,5,99,9,5,1,5,1,5,1,6,1,6,1,6,5,6,106,8,6,10,6,12,6,109,9,
        6,3,6,111,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,123,8,
        8,1,8,1,8,1,9,1,9,5,9,129,8,9,10,9,12,9,132,9,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,3,11,143,8,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,5,13,155,8,13,10,13,12,13,158,9,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,167,8,14,1,15,1,15,1,15,1,15,
        1,15,3,15,174,8,15,1,15,3,15,177,8,15,5,15,179,8,15,10,15,12,15,
        182,9,15,1,15,3,15,185,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,
        16,194,8,16,1,17,1,17,1,17,5,17,199,8,17,10,17,12,17,202,9,17,1,
        18,1,18,1,18,0,0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,0,3,2,0,21,21,23,23,2,0,7,7,20,20,1,0,22,23,216,0,39,1,0,0,
        0,2,49,1,0,0,0,4,51,1,0,0,0,6,67,1,0,0,0,8,77,1,0,0,0,10,82,1,0,
        0,0,12,110,1,0,0,0,14,112,1,0,0,0,16,116,1,0,0,0,18,126,1,0,0,0,
        20,135,1,0,0,0,22,139,1,0,0,0,24,146,1,0,0,0,26,151,1,0,0,0,28,166,
        1,0,0,0,30,184,1,0,0,0,32,193,1,0,0,0,34,195,1,0,0,0,36,203,1,0,
        0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,43,1,0,0,0,43,44,5,0,0,1,44,1,1,0,0,0,45,50,3,8,4,0,46,
        50,3,18,9,0,47,50,3,4,2,0,48,50,3,10,5,0,49,45,1,0,0,0,49,46,1,0,
        0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,3,1,0,0,0,51,52,5,5,0,0,52,53,
        5,20,0,0,53,54,5,15,0,0,54,55,5,20,0,0,55,62,5,13,0,0,56,61,3,16,
        8,0,57,61,3,10,5,0,58,61,3,6,3,0,59,61,3,18,9,0,60,56,1,0,0,0,60,
        57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,
        0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,14,0,0,66,5,
        1,0,0,0,67,68,5,6,0,0,68,72,5,13,0,0,69,71,3,28,14,0,70,69,1,0,0,
        0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,
        1,0,0,0,75,76,5,14,0,0,76,7,1,0,0,0,77,78,5,1,0,0,78,79,7,0,0,0,
        79,80,5,10,0,0,80,9,1,0,0,0,81,83,5,8,0,0,82,81,1,0,0,0,82,83,1,
        0,0,0,83,84,1,0,0,0,84,85,5,2,0,0,85,86,5,20,0,0,86,87,5,11,0,0,
        87,88,3,12,6,0,88,91,5,12,0,0,89,90,5,17,0,0,90,92,5,20,0,0,91,89,
        1,0,0,0,91,92,1,0,0,0,92,93,1,0,0,0,93,97,5,13,0,0,94,96,3,28,14,
        0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,
        1,0,0,0,99,97,1,0,0,0,100,101,5,14,0,0,101,11,1,0,0,0,102,107,3,
        14,7,0,103,104,5,19,0,0,104,106,3,14,7,0,105,103,1,0,0,0,106,109,
        1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,111,1,0,0,0,109,107,
        1,0,0,0,110,102,1,0,0,0,110,111,1,0,0,0,111,13,1,0,0,0,112,113,5,
        20,0,0,113,114,5,15,0,0,114,115,5,20,0,0,115,15,1,0,0,0,116,117,
        5,3,0,0,117,118,5,20,0,0,118,119,5,15,0,0,119,122,5,20,0,0,120,121,
        5,16,0,0,121,123,3,30,15,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,
        1,0,0,0,124,125,5,10,0,0,125,17,1,0,0,0,126,130,5,9,0,0,127,129,
        5,27,0,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,133,1,0,0,0,132,130,1,0,0,0,133,134,5,26,0,0,134,19,
        1,0,0,0,135,136,5,4,0,0,136,137,3,30,15,0,137,138,5,10,0,0,138,21,
        1,0,0,0,139,140,5,20,0,0,140,142,5,11,0,0,141,143,3,34,17,0,142,
        141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,5,12,0,0,145,
        23,1,0,0,0,146,147,3,26,13,0,147,148,5,16,0,0,148,149,3,30,15,0,
        149,150,5,10,0,0,150,25,1,0,0,0,151,156,7,1,0,0,152,153,5,18,0,0,
        153,155,5,20,0,0,154,152,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,
        156,157,1,0,0,0,157,27,1,0,0,0,158,156,1,0,0,0,159,167,3,16,8,0,
        160,167,3,24,12,0,161,167,3,20,10,0,162,163,3,30,15,0,163,164,5,
        10,0,0,164,167,1,0,0,0,165,167,3,18,9,0,166,159,1,0,0,0,166,160,
        1,0,0,0,166,161,1,0,0,0,166,162,1,0,0,0,166,165,1,0,0,0,167,29,1,
        0,0,0,168,180,3,32,16,0,169,170,5,18,0,0,170,176,5,20,0,0,171,173,
        5,11,0,0,172,174,3,34,17,0,173,172,1,0,0,0,173,174,1,0,0,0,174,175,
        1,0,0,0,175,177,5,12,0,0,176,171,1,0,0,0,176,177,1,0,0,0,177,179,
        1,0,0,0,178,169,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,
        1,0,0,0,181,185,1,0,0,0,182,180,1,0,0,0,183,185,3,22,11,0,184,168,
        1,0,0,0,184,183,1,0,0,0,185,31,1,0,0,0,186,194,3,36,18,0,187,194,
        5,20,0,0,188,194,5,7,0,0,189,190,5,11,0,0,190,191,3,30,15,0,191,
        192,5,12,0,0,192,194,1,0,0,0,193,186,1,0,0,0,193,187,1,0,0,0,193,
        188,1,0,0,0,193,189,1,0,0,0,194,33,1,0,0,0,195,200,3,30,15,0,196,
        197,5,19,0,0,197,199,3,30,15,0,198,196,1,0,0,0,199,202,1,0,0,0,200,
        198,1,0,0,0,200,201,1,0,0,0,201,35,1,0,0,0,202,200,1,0,0,0,203,204,
        7,2,0,0,204,37,1,0,0,0,21,41,49,60,62,72,82,91,97,107,110,122,130,
        142,156,166,173,176,180,184,193,200
    ]

class ChronoParser ( Parser ):

    grammarFileName = "ChronoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'func'", "'let'", "'return'", 
                     "'class'", "'deinit'", "'this'", "'static'", "'@cpp'", 
                     "';'", "'('", "')'", "'{'", "'}'", "':'", "'='", "'->'", 
                     "'.'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'@end'" ]

    symbolicNames = [ "<INVALID>", "IMPORT", "FUNC", "LET", "RETURN", "CLASS", 
                      "DEINIT", "THIS", "STATIC", "AT_CPP", "SEMIC_TOKEN", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "ASSIGN", 
                      "ARROW", "DOT", "COMMA", "IDENTIFIER", "INCLUDE_PATH", 
                      "INTEGER_LITERAL", "STRING_LITERAL", "LINE_COMMENT", 
                      "WHITESPACE", "AT_END", "CPP_BODY" ]

    RULE_program = 0
    RULE_topLevelStatement = 1
    RULE_classDefinition = 2
    RULE_deinitBlock = 3
    RULE_importDirective = 4
    RULE_functionDefinition = 5
    RULE_parameters = 6
    RULE_parameter = 7
    RULE_declaration = 8
    RULE_cppBlock = 9
    RULE_returnStatement = 10
    RULE_functionCallExpression = 11
    RULE_assignment = 12
    RULE_assignableExpression = 13
    RULE_statement = 14
    RULE_expression = 15
    RULE_primary = 16
    RULE_expressionList = 17
    RULE_literal = 18

    ruleNames =  [ "program", "topLevelStatement", "classDefinition", "deinitBlock", 
                   "importDirective", "functionDefinition", "parameters", 
                   "parameter", "declaration", "cppBlock", "returnStatement", 
                   "functionCallExpression", "assignment", "assignableExpression", 
                   "statement", "expression", "primary", "expressionList", 
                   "literal" ]

    EOF = Token.EOF
    IMPORT=1
    FUNC=2
    LET=3
    RETURN=4
    CLASS=5
    DEINIT=6
    THIS=7
    STATIC=8
    AT_CPP=9
    SEMIC_TOKEN=10
    LPAREN=11
    RPAREN=12
    LBRACE=13
    RBRACE=14
    COLON=15
    ASSIGN=16
    ARROW=17
    DOT=18
    COMMA=19
    IDENTIFIER=20
    INCLUDE_PATH=21
    INTEGER_LITERAL=22
    STRING_LITERAL=23
    LINE_COMMENT=24
    WHITESPACE=25
    AT_END=26
    CPP_BODY=27

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

        def topLevelStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.TopLevelStatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.TopLevelStatementContext,i)


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
            while True:
                self.state = 38
                self.topLevelStatement()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 806) != 0)):
                    break

            self.state = 43
            self.match(ChronoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importDirective(self):
            return self.getTypedRuleContext(ChronoParser.ImportDirectiveContext,0)


        def cppBlock(self):
            return self.getTypedRuleContext(ChronoParser.CppBlockContext,0)


        def classDefinition(self):
            return self.getTypedRuleContext(ChronoParser.ClassDefinitionContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(ChronoParser.FunctionDefinitionContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_topLevelStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelStatement" ):
                listener.enterTopLevelStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelStatement" ):
                listener.exitTopLevelStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelStatement" ):
                return visitor.visitTopLevelStatement(self)
            else:
                return visitor.visitChildren(self)




    def topLevelStatement(self):

        localctx = ChronoParser.TopLevelStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topLevelStatement)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.importDirective()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.cppBlock()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.classDefinition()
                pass
            elif token in [2, 8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.functionDefinition()
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


        def cppBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.CppBlockContext)
            else:
                return self.getTypedRuleContext(ChronoParser.CppBlockContext,i)


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
        self.enterRule(localctx, 4, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(ChronoParser.CLASS)
            self.state = 52
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 53
            self.match(ChronoParser.COLON)
            self.state = 54
            localctx.base = self.match(ChronoParser.IDENTIFIER)
            self.state = 55
            self.match(ChronoParser.LBRACE)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 844) != 0):
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 56
                    self.declaration()
                    pass
                elif token in [2, 8]:
                    self.state = 57
                    self.functionDefinition()
                    pass
                elif token in [6]:
                    self.state = 58
                    self.deinitBlock()
                    pass
                elif token in [9]:
                    self.state = 59
                    self.cppBlock()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
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
        self.enterRule(localctx, 6, self.RULE_deinitBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ChronoParser.DEINIT)
            self.state = 68
            self.match(ChronoParser.LBRACE)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13634200) != 0):
                self.state = 69
                self.statement()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(ChronoParser.RBRACE)
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
            self.state = 77
            self.match(ChronoParser.IMPORT)
            self.state = 78
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==21 or _la==23):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 79
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

        def LBRACE(self):
            return self.getToken(ChronoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChronoParser.RBRACE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def STATIC(self):
            return self.getToken(ChronoParser.STATIC, 0)

        def ARROW(self):
            return self.getToken(ChronoParser.ARROW, 0)

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
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 81
                self.match(ChronoParser.STATIC)


            self.state = 84
            self.match(ChronoParser.FUNC)
            self.state = 85
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 86
            self.match(ChronoParser.LPAREN)
            self.state = 87
            self.parameters()
            self.state = 88
            self.match(ChronoParser.RPAREN)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 89
                self.match(ChronoParser.ARROW)
                self.state = 90
                localctx.returnType = self.match(ChronoParser.IDENTIFIER)


            self.state = 93
            self.match(ChronoParser.LBRACE)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13634200) != 0):
                self.state = 94
                self.statement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
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
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 102
                self.parameter()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
                    self.state = 103
                    self.match(ChronoParser.COMMA)
                    self.state = 104
                    self.parameter()
                    self.state = 109
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
            self.state = 112
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 113
            self.match(ChronoParser.COLON)
            self.state = 114
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
            self.state = 116
            self.match(ChronoParser.LET)
            self.state = 117
            localctx.variableName = self.match(ChronoParser.IDENTIFIER)
            self.state = 118
            self.match(ChronoParser.COLON)
            self.state = 119
            localctx.typeName = self.match(ChronoParser.IDENTIFIER)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 120
                self.match(ChronoParser.ASSIGN)
                self.state = 121
                self.expression()


            self.state = 124
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
            self.state = 126
            self.match(ChronoParser.AT_CPP)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 127
                self.match(ChronoParser.CPP_BODY)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
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
            self.state = 135
            self.match(ChronoParser.RETURN)
            self.state = 136
            self.expression()
            self.state = 137
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
            self.state = 139
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 140
            self.match(ChronoParser.LPAREN)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 13633664) != 0):
                self.state = 141
                self.expressionList()


            self.state = 144
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

        def assignableExpression(self):
            return self.getTypedRuleContext(ChronoParser.AssignableExpressionContext,0)


        def ASSIGN(self):
            return self.getToken(ChronoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def SEMIC_TOKEN(self):
            return self.getToken(ChronoParser.SEMIC_TOKEN, 0)

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
            self.state = 146
            self.assignableExpression()
            self.state = 147
            self.match(ChronoParser.ASSIGN)
            self.state = 148
            self.expression()
            self.state = 149
            self.match(ChronoParser.SEMIC_TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignableExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def THIS(self):
            return self.getToken(ChronoParser.THIS, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.DOT)
            else:
                return self.getToken(ChronoParser.DOT, i)

        def getRuleIndex(self):
            return ChronoParser.RULE_assignableExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignableExpression" ):
                listener.enterAssignableExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignableExpression" ):
                listener.exitAssignableExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignableExpression" ):
                return visitor.visitAssignableExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignableExpression(self):

        localctx = ChronoParser.AssignableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignableExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not(_la==7 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 152
                self.match(ChronoParser.DOT)
                self.state = 153
                self.match(ChronoParser.IDENTIFIER)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.expression()
                self.state = 163
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
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

        def primary(self):
            return self.getTypedRuleContext(ChronoParser.PrimaryContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.DOT)
            else:
                return self.getToken(ChronoParser.DOT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.IDENTIFIER)
            else:
                return self.getToken(ChronoParser.IDENTIFIER, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.LPAREN)
            else:
                return self.getToken(ChronoParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.RPAREN)
            else:
                return self.getToken(ChronoParser.RPAREN, i)

        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ExpressionListContext,i)


        def functionCallExpression(self):
            return self.getTypedRuleContext(ChronoParser.FunctionCallExpressionContext,0)


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
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.primary()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 169
                    self.match(ChronoParser.DOT)
                    self.state = 170
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 176
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 171
                        self.match(ChronoParser.LPAREN)
                        self.state = 173
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 13633664) != 0):
                            self.state = 172
                            self.expressionList()


                        self.state = 175
                        self.match(ChronoParser.RPAREN)


                    self.state = 182
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.functionCallExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ChronoParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(ChronoParser.IDENTIFIER, 0)

        def THIS(self):
            return self.getToken(ChronoParser.THIS, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = ChronoParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_primary)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.literal()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.match(ChronoParser.THIS)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.match(ChronoParser.LPAREN)
                self.state = 190
                self.expression()
                self.state = 191
                self.match(ChronoParser.RPAREN)
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
        self.enterRule(localctx, 34, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.expression()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 196
                self.match(ChronoParser.COMMA)
                self.state = 197
                self.expression()
                self.state = 202
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
        self.enterRule(localctx, 36, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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





