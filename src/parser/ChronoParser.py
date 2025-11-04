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
        4,1,42,304,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,4,0,52,8,0,11,0,
        12,0,53,1,0,1,0,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,3,3,3,67,8,
        3,1,3,1,3,1,3,3,3,72,8,3,1,3,1,3,3,3,76,8,3,3,3,78,8,3,1,3,1,3,1,
        3,1,3,3,3,84,8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,92,8,4,10,4,12,4,95,
        9,4,1,4,1,4,1,5,3,5,100,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,109,
        8,5,1,5,1,5,5,5,113,8,5,10,5,12,5,116,9,5,1,5,1,5,1,6,1,6,1,6,5,
        6,123,8,6,10,6,12,6,126,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,3,8,135,
        8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,144,8,8,1,8,1,8,5,8,148,8,8,
        10,8,12,8,151,9,8,1,8,1,8,1,9,1,9,1,9,5,9,158,8,9,10,9,12,9,161,
        9,9,3,9,163,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,175,8,11,1,11,1,11,1,12,1,12,5,12,181,8,12,10,12,12,12,184,
        9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,5,15,200,8,15,10,15,12,15,203,9,15,1,16,1,16,1,16,1,16,
        1,16,1,16,5,16,211,8,16,10,16,12,16,214,9,16,1,16,1,16,1,16,1,16,
        1,16,5,16,221,8,16,10,16,12,16,224,9,16,1,16,3,16,227,8,16,3,16,
        229,8,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,237,8,17,10,17,12,17,
        240,9,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        3,18,253,8,18,1,19,1,19,1,19,3,19,258,8,19,1,20,1,20,1,20,1,20,1,
        20,3,20,265,8,20,1,20,3,20,268,8,20,5,20,270,8,20,10,20,12,20,273,
        9,20,1,20,3,20,276,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,
        285,8,21,1,22,1,22,1,22,3,22,290,8,22,1,22,1,22,1,23,1,23,1,23,5,
        23,297,8,23,10,23,12,23,300,9,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,4,
        2,0,26,26,38,38,2,0,7,7,36,36,2,0,15,18,20,25,2,0,13,13,37,38,324,
        0,51,1,0,0,0,2,61,1,0,0,0,4,63,1,0,0,0,6,83,1,0,0,0,8,85,1,0,0,0,
        10,99,1,0,0,0,12,119,1,0,0,0,14,129,1,0,0,0,16,134,1,0,0,0,18,162,
        1,0,0,0,20,164,1,0,0,0,22,168,1,0,0,0,24,178,1,0,0,0,26,187,1,0,
        0,0,28,191,1,0,0,0,30,196,1,0,0,0,32,204,1,0,0,0,34,230,1,0,0,0,
        36,252,1,0,0,0,38,254,1,0,0,0,40,275,1,0,0,0,42,284,1,0,0,0,44,286,
        1,0,0,0,46,293,1,0,0,0,48,301,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,
        0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,
        5,0,0,1,56,1,1,0,0,0,57,62,3,14,7,0,58,62,3,24,12,0,59,62,3,8,4,
        0,60,62,3,16,8,0,61,57,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,
        1,0,0,0,62,3,1,0,0,0,63,64,5,12,0,0,64,5,1,0,0,0,65,67,3,4,2,0,66,
        65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,84,3,22,11,0,69,71,5,8,
        0,0,70,72,3,4,2,0,71,70,1,0,0,0,71,72,1,0,0,0,72,78,1,0,0,0,73,75,
        3,4,2,0,74,76,5,8,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,
        77,69,1,0,0,0,77,73,1,0,0,0,78,79,1,0,0,0,79,84,3,10,5,0,80,84,3,
        10,5,0,81,84,3,12,6,0,82,84,3,24,12,0,83,66,1,0,0,0,83,77,1,0,0,
        0,83,80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,7,1,0,0,0,85,86,5,
        5,0,0,86,87,5,36,0,0,87,88,5,32,0,0,88,89,5,36,0,0,89,93,5,30,0,
        0,90,92,3,6,3,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,
        1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,31,0,0,97,9,1,0,0,0,
        98,100,3,4,2,0,99,98,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,
        102,5,2,0,0,102,103,5,36,0,0,103,104,5,28,0,0,104,105,3,18,9,0,105,
        108,5,29,0,0,106,107,5,19,0,0,107,109,5,36,0,0,108,106,1,0,0,0,108,
        109,1,0,0,0,109,110,1,0,0,0,110,114,5,30,0,0,111,113,3,36,18,0,112,
        111,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,
        117,1,0,0,0,116,114,1,0,0,0,117,118,5,31,0,0,118,11,1,0,0,0,119,
        120,5,6,0,0,120,124,5,30,0,0,121,123,3,36,18,0,122,121,1,0,0,0,123,
        126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,
        124,1,0,0,0,127,128,5,31,0,0,128,13,1,0,0,0,129,130,5,1,0,0,130,
        131,7,0,0,0,131,132,5,27,0,0,132,15,1,0,0,0,133,135,5,8,0,0,134,
        133,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,137,5,2,0,0,137,
        138,5,36,0,0,138,139,5,28,0,0,139,140,3,18,9,0,140,143,5,29,0,0,
        141,142,5,19,0,0,142,144,5,36,0,0,143,141,1,0,0,0,143,144,1,0,0,
        0,144,145,1,0,0,0,145,149,5,30,0,0,146,148,3,36,18,0,147,146,1,0,
        0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,152,1,0,
        0,0,151,149,1,0,0,0,152,153,5,31,0,0,153,17,1,0,0,0,154,159,3,20,
        10,0,155,156,5,35,0,0,156,158,3,20,10,0,157,155,1,0,0,0,158,161,
        1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,163,1,0,0,0,161,159,
        1,0,0,0,162,154,1,0,0,0,162,163,1,0,0,0,163,19,1,0,0,0,164,165,5,
        36,0,0,165,166,5,32,0,0,166,167,5,36,0,0,167,21,1,0,0,0,168,169,
        5,3,0,0,169,170,5,36,0,0,170,171,5,32,0,0,171,174,5,36,0,0,172,173,
        5,33,0,0,173,175,3,38,19,0,174,172,1,0,0,0,174,175,1,0,0,0,175,176,
        1,0,0,0,176,177,5,27,0,0,177,23,1,0,0,0,178,182,5,14,0,0,179,181,
        5,42,0,0,180,179,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,
        1,0,0,0,183,185,1,0,0,0,184,182,1,0,0,0,185,186,5,41,0,0,186,25,
        1,0,0,0,187,188,5,4,0,0,188,189,3,38,19,0,189,190,5,27,0,0,190,27,
        1,0,0,0,191,192,3,30,15,0,192,193,5,33,0,0,193,194,3,38,19,0,194,
        195,5,27,0,0,195,29,1,0,0,0,196,201,7,1,0,0,197,198,5,34,0,0,198,
        200,5,36,0,0,199,197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,
        202,1,0,0,0,202,31,1,0,0,0,203,201,1,0,0,0,204,205,5,9,0,0,205,206,
        5,28,0,0,206,207,3,38,19,0,207,208,5,29,0,0,208,212,5,30,0,0,209,
        211,3,36,18,0,210,209,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,
        213,1,0,0,0,213,215,1,0,0,0,214,212,1,0,0,0,215,228,5,31,0,0,216,
        226,5,10,0,0,217,227,3,32,16,0,218,222,5,30,0,0,219,221,3,36,18,
        0,220,219,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,
        0,223,225,1,0,0,0,224,222,1,0,0,0,225,227,5,31,0,0,226,217,1,0,0,
        0,226,218,1,0,0,0,227,229,1,0,0,0,228,216,1,0,0,0,228,229,1,0,0,
        0,229,33,1,0,0,0,230,231,5,11,0,0,231,232,5,28,0,0,232,233,3,38,
        19,0,233,234,5,29,0,0,234,238,5,30,0,0,235,237,3,36,18,0,236,235,
        1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,241,
        1,0,0,0,240,238,1,0,0,0,241,242,5,31,0,0,242,35,1,0,0,0,243,253,
        3,22,11,0,244,253,3,28,14,0,245,253,3,26,13,0,246,247,3,38,19,0,
        247,248,5,27,0,0,248,253,1,0,0,0,249,253,3,24,12,0,250,253,3,32,
        16,0,251,253,3,34,17,0,252,243,1,0,0,0,252,244,1,0,0,0,252,245,1,
        0,0,0,252,246,1,0,0,0,252,249,1,0,0,0,252,250,1,0,0,0,252,251,1,
        0,0,0,253,37,1,0,0,0,254,257,3,40,20,0,255,256,7,2,0,0,256,258,3,
        40,20,0,257,255,1,0,0,0,257,258,1,0,0,0,258,39,1,0,0,0,259,271,3,
        42,21,0,260,261,5,34,0,0,261,267,5,36,0,0,262,264,5,28,0,0,263,265,
        3,46,23,0,264,263,1,0,0,0,264,265,1,0,0,0,265,266,1,0,0,0,266,268,
        5,29,0,0,267,262,1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,260,
        1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,276,
        1,0,0,0,273,271,1,0,0,0,274,276,3,44,22,0,275,259,1,0,0,0,275,274,
        1,0,0,0,276,41,1,0,0,0,277,285,3,48,24,0,278,285,5,36,0,0,279,285,
        5,7,0,0,280,281,5,28,0,0,281,282,3,38,19,0,282,283,5,29,0,0,283,
        285,1,0,0,0,284,277,1,0,0,0,284,278,1,0,0,0,284,279,1,0,0,0,284,
        280,1,0,0,0,285,43,1,0,0,0,286,287,5,36,0,0,287,289,5,28,0,0,288,
        290,3,46,23,0,289,288,1,0,0,0,289,290,1,0,0,0,290,291,1,0,0,0,291,
        292,5,29,0,0,292,45,1,0,0,0,293,298,3,38,19,0,294,295,5,35,0,0,295,
        297,3,38,19,0,296,294,1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,0,298,
        299,1,0,0,0,299,47,1,0,0,0,300,298,1,0,0,0,301,302,7,3,0,0,302,49,
        1,0,0,0,34,53,61,66,71,75,77,83,93,99,108,114,124,134,143,149,159,
        162,174,182,201,212,222,226,228,238,252,257,264,267,271,275,284,
        289,298
    ]

class ChronoParser ( Parser ):

    grammarFileName = "ChronoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'func'", "'let'", "'return'", 
                     "'class'", "'deinit'", "'this'", "'static'", "'if'", 
                     "'else'", "'while'", "'public'", "<INVALID>", "'@cpp'", 
                     "'=='", "'!='", "'<='", "'>='", "'->'", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'>'", "<INVALID>", "';'", "'('", 
                     "')'", "'{'", "'}'", "':'", "'='", "'.'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'@end'" ]

    symbolicNames = [ "<INVALID>", "IMPORT", "FUNC", "LET", "RETURN", "CLASS", 
                      "DEINIT", "THIS", "STATIC", "IF", "ELSE", "WHILE", 
                      "PUBLIC", "BOOL_LITERAL", "AT_CPP", "EQ", "NEQ", "LTE", 
                      "GTE", "ARROW", "PLUS", "MINUS", "STAR", "SLASH", 
                      "LT", "GT", "INCLUDE_PATH", "SEMIC_TOKEN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "COLON", "ASSIGN", "DOT", 
                      "COMMA", "IDENTIFIER", "INTEGER_LITERAL", "STRING_LITERAL", 
                      "LINE_COMMENT", "WHITESPACE", "AT_END", "CPP_BODY" ]

    RULE_program = 0
    RULE_topLevelStatement = 1
    RULE_accessModifier = 2
    RULE_classBodyStatement = 3
    RULE_classDefinition = 4
    RULE_methodDefinition = 5
    RULE_deinitBlock = 6
    RULE_importDirective = 7
    RULE_functionDefinition = 8
    RULE_parameters = 9
    RULE_parameter = 10
    RULE_declaration = 11
    RULE_cppBlock = 12
    RULE_returnStatement = 13
    RULE_assignment = 14
    RULE_assignableExpression = 15
    RULE_ifStatement = 16
    RULE_whileStatement = 17
    RULE_statement = 18
    RULE_expression = 19
    RULE_simpleExpression = 20
    RULE_primary = 21
    RULE_functionCallExpression = 22
    RULE_expressionList = 23
    RULE_literal = 24

    ruleNames =  [ "program", "topLevelStatement", "accessModifier", "classBodyStatement", 
                   "classDefinition", "methodDefinition", "deinitBlock", 
                   "importDirective", "functionDefinition", "parameters", 
                   "parameter", "declaration", "cppBlock", "returnStatement", 
                   "assignment", "assignableExpression", "ifStatement", 
                   "whileStatement", "statement", "expression", "simpleExpression", 
                   "primary", "functionCallExpression", "expressionList", 
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
    IF=9
    ELSE=10
    WHILE=11
    PUBLIC=12
    BOOL_LITERAL=13
    AT_CPP=14
    EQ=15
    NEQ=16
    LTE=17
    GTE=18
    ARROW=19
    PLUS=20
    MINUS=21
    STAR=22
    SLASH=23
    LT=24
    GT=25
    INCLUDE_PATH=26
    SEMIC_TOKEN=27
    LPAREN=28
    RPAREN=29
    LBRACE=30
    RBRACE=31
    COLON=32
    ASSIGN=33
    DOT=34
    COMMA=35
    IDENTIFIER=36
    INTEGER_LITERAL=37
    STRING_LITERAL=38
    LINE_COMMENT=39
    WHITESPACE=40
    AT_END=41
    CPP_BODY=42

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
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.topLevelStatement()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16678) != 0)):
                    break

            self.state = 55
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
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.importDirective()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.cppBlock()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.classDefinition()
                pass
            elif token in [2, 8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
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


    class AccessModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(ChronoParser.PUBLIC, 0)

        def getRuleIndex(self):
            return ChronoParser.RULE_accessModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessModifier" ):
                listener.enterAccessModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessModifier" ):
                listener.exitAccessModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessModifier" ):
                return visitor.visitAccessModifier(self)
            else:
                return visitor.visitChildren(self)




    def accessModifier(self):

        localctx = ChronoParser.AccessModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_accessModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ChronoParser.PUBLIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ChronoParser.DeclarationContext,0)


        def accessModifier(self):
            return self.getTypedRuleContext(ChronoParser.AccessModifierContext,0)


        def methodDefinition(self):
            return self.getTypedRuleContext(ChronoParser.MethodDefinitionContext,0)


        def STATIC(self):
            return self.getToken(ChronoParser.STATIC, 0)

        def deinitBlock(self):
            return self.getTypedRuleContext(ChronoParser.DeinitBlockContext,0)


        def cppBlock(self):
            return self.getTypedRuleContext(ChronoParser.CppBlockContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_classBodyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBodyStatement" ):
                listener.enterClassBodyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBodyStatement" ):
                listener.exitClassBodyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBodyStatement" ):
                return visitor.visitClassBodyStatement(self)
            else:
                return visitor.visitChildren(self)




    def classBodyStatement(self):

        localctx = ChronoParser.ClassBodyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classBodyStatement)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 65
                    self.accessModifier()


                self.state = 68
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 69
                    self.match(ChronoParser.STATIC)
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        self.state = 70
                        self.accessModifier()


                    pass
                elif token in [12]:
                    self.state = 73
                    self.accessModifier()
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 74
                        self.match(ChronoParser.STATIC)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 79
                self.methodDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.methodDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.deinitBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.cppBlock()
                pass


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

        def classBodyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.ClassBodyStatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.ClassBodyStatementContext,i)


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
        self.enterRule(localctx, 8, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(ChronoParser.CLASS)
            self.state = 86
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 87
            self.match(ChronoParser.COLON)
            self.state = 88
            localctx.base = self.match(ChronoParser.IDENTIFIER)
            self.state = 89
            self.match(ChronoParser.LBRACE)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 20812) != 0):
                self.state = 90
                self.classBodyStatement()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(ChronoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDefinitionContext(ParserRuleContext):
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

        def accessModifier(self):
            return self.getTypedRuleContext(ChronoParser.AccessModifierContext,0)


        def ARROW(self):
            return self.getToken(ChronoParser.ARROW, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def getRuleIndex(self):
            return ChronoParser.RULE_methodDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDefinition" ):
                listener.enterMethodDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDefinition" ):
                listener.exitMethodDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDefinition" ):
                return visitor.visitMethodDefinition(self)
            else:
                return visitor.visitChildren(self)




    def methodDefinition(self):

        localctx = ChronoParser.MethodDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_methodDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 98
                self.accessModifier()


            self.state = 101
            self.match(ChronoParser.FUNC)
            self.state = 102
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 103
            self.match(ChronoParser.LPAREN)
            self.state = 104
            self.parameters()
            self.state = 105
            self.match(ChronoParser.RPAREN)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 106
                self.match(ChronoParser.ARROW)
                self.state = 107
                localctx.returnType = self.match(ChronoParser.IDENTIFIER)


            self.state = 110
            self.match(ChronoParser.LBRACE)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481304799896) != 0):
                self.state = 111
                self.statement()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
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
        self.enterRule(localctx, 12, self.RULE_deinitBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(ChronoParser.DEINIT)
            self.state = 120
            self.match(ChronoParser.LBRACE)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481304799896) != 0):
                self.state = 121
                self.statement()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
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
        self.enterRule(localctx, 14, self.RULE_importDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ChronoParser.IMPORT)
            self.state = 130
            localctx.path = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==26 or _la==38):
                localctx.path = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
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
        self.enterRule(localctx, 16, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 133
                self.match(ChronoParser.STATIC)


            self.state = 136
            self.match(ChronoParser.FUNC)
            self.state = 137
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 138
            self.match(ChronoParser.LPAREN)
            self.state = 139
            self.parameters()
            self.state = 140
            self.match(ChronoParser.RPAREN)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 141
                self.match(ChronoParser.ARROW)
                self.state = 142
                localctx.returnType = self.match(ChronoParser.IDENTIFIER)


            self.state = 145
            self.match(ChronoParser.LBRACE)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481304799896) != 0):
                self.state = 146
                self.statement()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
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
        self.enterRule(localctx, 18, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 154
                self.parameter()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 155
                    self.match(ChronoParser.COMMA)
                    self.state = 156
                    self.parameter()
                    self.state = 161
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
        self.enterRule(localctx, 20, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 165
            self.match(ChronoParser.COLON)
            self.state = 166
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
        self.enterRule(localctx, 22, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ChronoParser.LET)
            self.state = 169
            localctx.variableName = self.match(ChronoParser.IDENTIFIER)
            self.state = 170
            self.match(ChronoParser.COLON)
            self.state = 171
            localctx.typeName = self.match(ChronoParser.IDENTIFIER)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 172
                self.match(ChronoParser.ASSIGN)
                self.state = 173
                self.expression()


            self.state = 176
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
        self.enterRule(localctx, 24, self.RULE_cppBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ChronoParser.AT_CPP)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 179
                self.match(ChronoParser.CPP_BODY)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
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
        self.enterRule(localctx, 26, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ChronoParser.RETURN)
            self.state = 188
            self.expression()
            self.state = 189
            self.match(ChronoParser.SEMIC_TOKEN)
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
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.assignableExpression()
            self.state = 192
            self.match(ChronoParser.ASSIGN)
            self.state = 193
            self.expression()
            self.state = 194
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
        self.enterRule(localctx, 30, self.RULE_assignableExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==7 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 197
                self.match(ChronoParser.DOT)
                self.state = 198
                self.match(ChronoParser.IDENTIFIER)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.if_statements = None # StatementContext
            self.else_if = None # IfStatementContext
            self.else_statements = None # StatementContext

        def IF(self):
            return self.getToken(ChronoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.LBRACE)
            else:
                return self.getToken(ChronoParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ChronoParser.RBRACE)
            else:
                return self.getToken(ChronoParser.RBRACE, i)

        def ELSE(self):
            return self.getToken(ChronoParser.ELSE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChronoParser.StatementContext,i)


        def ifStatement(self):
            return self.getTypedRuleContext(ChronoParser.IfStatementContext,0)


        def getRuleIndex(self):
            return ChronoParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = ChronoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ChronoParser.IF)
            self.state = 205
            self.match(ChronoParser.LPAREN)
            self.state = 206
            self.expression()
            self.state = 207
            self.match(ChronoParser.RPAREN)
            self.state = 208
            self.match(ChronoParser.LBRACE)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481304799896) != 0):
                self.state = 209
                localctx.if_statements = self.statement()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 215
            self.match(ChronoParser.RBRACE)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 216
                self.match(ChronoParser.ELSE)
                self.state = 226
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9]:
                    self.state = 217
                    localctx.else_if = self.ifStatement()
                    pass
                elif token in [30]:
                    self.state = 218
                    self.match(ChronoParser.LBRACE)
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481304799896) != 0):
                        self.state = 219
                        localctx.else_statements = self.statement()
                        self.state = 224
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 225
                    self.match(ChronoParser.RBRACE)
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


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.statements = None # StatementContext

        def WHILE(self):
            return self.getToken(ChronoParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(ChronoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ChronoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ChronoParser.RPAREN, 0)

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
            return ChronoParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = ChronoParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ChronoParser.WHILE)
            self.state = 231
            self.match(ChronoParser.LPAREN)
            self.state = 232
            self.expression()
            self.state = 233
            self.match(ChronoParser.RPAREN)
            self.state = 234
            self.match(ChronoParser.LBRACE)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481304799896) != 0):
                self.state = 235
                localctx.statements = self.statement()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
            self.match(ChronoParser.RBRACE)
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


        def ifStatement(self):
            return self.getTypedRuleContext(ChronoParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(ChronoParser.WhileStatementContext,0)


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
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.expression()
                self.state = 247
                self.match(ChronoParser.SEMIC_TOKEN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 249
                self.cppBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 250
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 251
                self.whileStatement()
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

        def simpleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChronoParser.SimpleExpressionContext)
            else:
                return self.getTypedRuleContext(ChronoParser.SimpleExpressionContext,i)


        def EQ(self):
            return self.getToken(ChronoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ChronoParser.NEQ, 0)

        def LT(self):
            return self.getToken(ChronoParser.LT, 0)

        def GT(self):
            return self.getToken(ChronoParser.GT, 0)

        def LTE(self):
            return self.getToken(ChronoParser.LTE, 0)

        def GTE(self):
            return self.getToken(ChronoParser.GTE, 0)

        def PLUS(self):
            return self.getToken(ChronoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ChronoParser.MINUS, 0)

        def STAR(self):
            return self.getToken(ChronoParser.STAR, 0)

        def SLASH(self):
            return self.getToken(ChronoParser.SLASH, 0)

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
        self.enterRule(localctx, 38, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.simpleExpression()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66551808) != 0):
                self.state = 255
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66551808) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 256
                self.simpleExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleExpressionContext(ParserRuleContext):
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
            return ChronoParser.RULE_simpleExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpression" ):
                listener.enterSimpleExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpression" ):
                listener.exitSimpleExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpression" ):
                return visitor.visitSimpleExpression(self)
            else:
                return visitor.visitChildren(self)




    def simpleExpression(self):

        localctx = ChronoParser.SimpleExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_simpleExpression)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.primary()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 260
                    self.match(ChronoParser.DOT)
                    self.state = 261
                    self.match(ChronoParser.IDENTIFIER)
                    self.state = 267
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==28:
                        self.state = 262
                        self.match(ChronoParser.LPAREN)
                        self.state = 264
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 481304780928) != 0):
                            self.state = 263
                            self.expressionList()


                        self.state = 266
                        self.match(ChronoParser.RPAREN)


                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
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
        self.enterRule(localctx, 42, self.RULE_primary)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 37, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.literal()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(ChronoParser.IDENTIFIER)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.match(ChronoParser.THIS)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.match(ChronoParser.LPAREN)
                self.state = 281
                self.expression()
                self.state = 282
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
        self.enterRule(localctx, 44, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            localctx.name = self.match(ChronoParser.IDENTIFIER)
            self.state = 287
            self.match(ChronoParser.LPAREN)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 481304780928) != 0):
                self.state = 288
                self.expressionList()


            self.state = 291
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
        self.enterRule(localctx, 46, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.expression()
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 294
                self.match(ChronoParser.COMMA)
                self.state = 295
                self.expression()
                self.state = 300
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

        def BOOL_LITERAL(self):
            return self.getToken(ChronoParser.BOOL_LITERAL, 0)

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
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 412316868608) != 0)):
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





