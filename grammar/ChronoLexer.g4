// -----------------------------------------------------------------------------
// Chrono 词法分析器 (ChronoLexer.g4) - 最终修正版
// -----------------------------------------------------------------------------
lexer grammar ChronoLexer;

// --- 关键字 (必须在 IDENTIFIER 之前) ---
IMPORT  : 'import' ;
FUNC    : 'func' ;
LET     : 'let' ;
RETURN  : 'return' ;
CLASS   : 'class' ;
INIT    : 'init' ;    // <-- [ 新增 ]
DEINIT  : 'deinit' ; 
THIS    : 'this' ;   
STATIC  : 'static' ;
IF      : 'if' ;
ELSE    : 'else' ;
WHILE   : 'while' ;

PUBLIC  : 'public' ; // class attr access flag
// BOOL_LITERAL 必须在 IDENTIFIER 之前
BOOL_LITERAL    : 'true' | 'false' ;

// --- @cpp 模式切换 ---
AT_CPP  : '@cpp' -> pushMode(INSIDE_CPP_BLOCK);

// [ 关键修复 ] 
// 1. LT/GT/LTE/GTE 必须在 INCLUDE_PATH 之前
// 2. INCLUDE_PATH 规则现在限制性更强，
//    只匹配文件名中常见的字符 (字母, 数字, _, ., /)
//    这可以防止它错误地匹配 'if (x < 5)'

// 复杂操作符 (必须在简单操作符 = < > 之前)
EQ      : '==' ;
NEQ     : '!=' ;
LTE     : '<=' ; 
GTE     : '>=' ; 
ARROW   : '->' ;

// [ 新增 ] 算术运算符
PLUS    : '+' ;
MINUS   : '-' ;
STAR    : '*' ;
SLASH   : '/' ;

// 简单符号 (必须在 INCLUDE_PATH 之前)
LT      : '<' ; 
GT      : '>' ; 

// INCLUDE_PATH 现在在 LT/GT 之后，但只在 import 语句中使用
// 我们在 Parser 中处理这个上下文
INCLUDE_PATH
    : '<' [a-zA-Z_0-9./]+ '>'
    ;

SEMIC_TOKEN : ';' ;
LPAREN  : '(' ; 
RPAREN  : ')' ; 
LBRACE  : '{' ;
RBRACE  : '}' ;
COLON   : ':' ;
ASSIGN  : '=' ;
DOT     : '.' ;
COMMA   : ',' ;

// --- 通用规则 (必须在最后) ---
IDENTIFIER : [a-zA-Z_] [a-zA-Z0-9_]* ; 
INTEGER_LITERAL : [0-9]+ ;
STRING_LITERAL  : '"' ( ~["\\] | '\\' . )* '"' ; 

// --- 跳过 (Skipped) ---
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
WHITESPACE : [ \t\r\n\u00A0]+ -> skip ;

// --- 词法分析器模式 ---
mode INSIDE_CPP_BLOCK;
    AT_END : '@end' -> popMode;
    CPP_BODY : . ;