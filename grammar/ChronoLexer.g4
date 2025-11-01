// -----------------------------------------------------------------------------
// Chrono 词法分析器 (ChronoLexer.g4) - 已修正顺序
// -----------------------------------------------------------------------------
lexer grammar ChronoLexer;

// --- 默认模式 (DEFAULT_MODE) ---
// 关键字
IMPORT  : 'import' ;
FUNC    : 'func' ;
LET     : 'let' ;
RETURN  : 'return' ;
//PRINT   : 'print' ;
CLASS   : 'class' ;  // [ 新增 ]
DEINIT  : 'deinit' ; // [ 新增 ]
THIS    : 'this' ;   // [ 新增 ]
STATIC  : 'static' ;
// 关键：遇到 @cpp 时，切换到 INSIDE_CPP_BLOCK 模式
// (INSIDE_CPP_BLOCK 在文件末尾定义)
AT_CPP  : '@cpp' -> pushMode(INSIDE_CPP_BLOCK);

// 符号
SEMIC_TOKEN : ';' ;
LPAREN  : '(' ; // 修正：之前是 '()'
RPAREN  : ')' ; // 修正：之前是 ')'
LBRACE  : '{' ;
RBRACE  : '}' ;
COLON   : ':' ;
ASSIGN  : '=' ;
ARROW   : '->' ;
DOT     : '.' ;
COMMA   : ',' ;

// 标识符
IDENTIFIER : [a-zA-Z_] [a-zA-Z0-9_]* ;

// --- 修正顺序 ---


// Import 路径 (现在只匹配 <...>)
INCLUDE_PATH
    : '<' ( ~[>] )* '>'
    ;

// 字面量 (Literals)
INTEGER_LITERAL : [0-9]+ ;
STRING_LITERAL  : '"' ( ~["\\] | '\\' . )* '"' ; // <-- 在 INCLUDE_PATH 之后

// 注释
LINE_COMMENT : '//' ~[\r\n]* -> skip ;

// 空格
WHITESPACE : [ \t\r\n]+ -> skip ; // 跳过所有空格、制表符和换行

// --- 词法分析器模式 (Lexer Modes) ---
// 模式: 捕获 @cpp 和 @end 之间的所有内容
// (必须在所有 DEFAULT_MODE 规则之后定义)
mode INSIDE_CPP_BLOCK;
    AT_END : '@end' -> popMode; // 优先级最高
    CPP_BODY : . ;             // 捕获所有其他字符