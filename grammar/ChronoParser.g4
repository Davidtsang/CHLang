// -----------------------------------------------------------------------------
// Chrono 解析器 (ChronoParser.g4) - 已修正
// -----------------------------------------------------------------------------
parser grammar ChronoParser;

// 关键：导入所有来自 ChronoLexer 的词法规则 (Tokens)
options { tokenVocab = ChronoLexer; }

// --- 解析器规则 (Parser Rules) ---

// 顶层规则
program : globalStatement* (classDefinition | functionDefinition)+ EOF ;

// [ 新增 ] 'class' 规则
classDefinition : CLASS name=IDENTIFIER COLON base=IDENTIFIER LBRACE
                    (declaration | functionDefinition | deinitBlock)* // 允许成员, 方法, 和 deinit
                  RBRACE ;

// [ 新增 ] 'deinit' 规则
deinitBlock : DEINIT LBRACE statement* RBRACE ;

// [ 新规则 ] globalStatement 是一个包装器
globalStatement : importDirective | cppBlock ;

// --- 基础规则 ---

importDirective : IMPORT path=(STRING_LITERAL | INCLUDE_PATH) SEMIC_TOKEN ;

// [ 已修正 ] 
// 'functionDefinition' 现在可以接受 'parameters'
functionDefinition : FUNC name=IDENTIFIER LPAREN parameters RPAREN ARROW returnType=IDENTIFIER LBRACE statement* RBRACE ;

// [ 新增 ] 'parameters' 规则
// (允许 0 个或多个参数, 例如 'title: String, x: i32')
parameters : (parameter (COMMA parameter)*)? ;

// [ 新增 ] 'parameter' 规则
parameter : name=IDENTIFIER COLON typeName=IDENTIFIER ;

// [ 已修正 ] 
// 赋值 (ASSIGN expression) 现在是可选的 '?'
// 这允许 'let title: String;' 这样的类成员
declaration : LET variableName=IDENTIFIER COLON typeName=IDENTIFIER (ASSIGN expression)? SEMIC_TOKEN ;

cppBlock : AT_CPP CPP_BODY* AT_END ;

returnStatement : RETURN expression SEMIC_TOKEN ;

functionCallExpression : name=IDENTIFIER LPAREN expressionList? RPAREN ;

// [ 新增 ] 赋值语句
assignment : (THIS DOT IDENTIFIER | IDENTIFIER) ASSIGN expression SEMIC_TOKEN ;

// --- 复合规则 ---

// [ 已修正 ]
// 'methodCall' 和 'functionCall' 是多余的
// 'expression SEMIC_TOKEN' 已经处理了 'myFunc();' 和 'myObj.method();'
statement : declaration
          | assignment
          | returnStatement
          | expression SEMIC_TOKEN // 表达式语句 (例如一个函数调用)
          | cppBlock
          ;

// [ 已修正 ]
// 1. 添加了 'functionCallExpression' (允许 'let x = myFunc()')
// 2. 'THIS DOT IDENTIFIER' 保持不变 (用于 'this.title')
expression
    : literal
    | IDENTIFIER
    | methodCallExpression
    | functionCallExpression // [ 修正 1 ]
    | THIS DOT IDENTIFIER
    ;

// [ 已修正 ] 
// 'receiver' 现在可以是 'THIS' 或 'IDENTIFIER'
methodCallExpression : receiver=(THIS | IDENTIFIER) DOT methodName=IDENTIFIER LPAREN expressionList? RPAREN ;

expressionList : expression (COMMA expression)* ;

literal : INTEGER_LITERAL | STRING_LITERAL ;