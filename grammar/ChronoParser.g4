// -----------------------------------------------------------------------------
// Chrono 解析器 (ChronoParser.g4)
// -----------------------------------------------------------------------------
parser grammar ChronoParser;

// 关键：导入所有来自 ChronoLexer 的词法规则 (Tokens)
options { tokenVocab = ChronoLexer; }

// --- 解析器规则 (Parser Rules) ---

// 顶层规则
program : globalStatement* functionDefinition+ EOF ;

// [ 新规则 ] globalStatement 是一个包装器
// 它允许 import 或 cppBlock 以任何顺序出现
globalStatement : importDirective | cppBlock ;

// --- 基础规则 (必须在 'statement' 之前定义) ---

// import 规则现在接受 "..." (STRING_LITERAL) 或 <...> (INCLUDE_PATH)
importDirective : IMPORT path=(STRING_LITERAL | INCLUDE_PATH) SEMIC_TOKEN ;

functionDefinition : FUNC name=IDENTIFIER LPAREN RPAREN ARROW returnType=IDENTIFIER LBRACE statement* RBRACE ;

declaration : LET variableName=IDENTIFIER COLON typeName=IDENTIFIER ASSIGN expression SEMIC_TOKEN ;

methodCall : methodCallExpression SEMIC_TOKEN ;

cppBlock : AT_CPP CPP_BODY* AT_END ;

//printCall : PRINT LPAREN expression RPAREN SEMIC_TOKEN ;

returnStatement : RETURN expression SEMIC_TOKEN ;

// [新] 全局函数调用 (C-style function call)
// (我们还必须允许它作为一个语句存在)
// [新] 全局函数调用的表达式形式
functionCallExpression : name=IDENTIFIER LPAREN expressionList? RPAREN ;

functionCall : functionCallExpression SEMIC_TOKEN ;

// --- 复合规则 ---

statement : declaration
          | methodCall
          | cppBlock
          | functionCall
          | returnStatement
          ;

expression
    : literal
    | IDENTIFIER
    | methodCallExpression
    ;

methodCallExpression : receiver=IDENTIFIER DOT methodName=IDENTIFIER LPAREN expressionList? RPAREN ;

expressionList : expression (COMMA expression)* ;

literal : INTEGER_LITERAL | STRING_LITERAL ;