// -----------------------------------------------------------------------------
// Chrono 词法分析器 (ChronoLexer.g4) - 最终修正版
// -----------------------------------------------------------------------------
lexer grammar ChronoLexer;

// --- 关键字 (必须在 IDENTIFIER 之前) ---
IMPORT  : 'import' ;
FUNC    : 'func' ;
// [ [ 修改 ] ]
VAR     : 'var';     // <-- [新增]
CONST   : 'const';   // <-- [新增]

RETURN  : 'return' ;
CLASS   : 'class' ;
IMPLEMENT: 'implement'; //
STRUCT  : 'struct' ; // <-- [新增]
INIT    : 'init' ;    // <-- [ 新增 ]
DEINIT  : 'deinit' ; 
THIS    : 'this' ;   
STATIC  : 'static' ;
IF      : 'if' ;
ELSE    : 'else' ;
WHILE   : 'while' ;
FOR     : 'for' ;   // <-- [新增]
PUBLIC  : 'public' ; // class attr access flag
INTERFACE: 'interface' ; // <-- [新增]
IMPL    : 'impl' ;      // <-- [新增]
AS      : 'as' ;     // [新增] 用于 import 别名
USING   : 'using' ;
TYPEMAP : 'typemap' ;
NAMESPACE : 'namespace';
SWITCH  : 'switch' ;
CASE    : 'case' ;
DEFAULT : 'default' ;

HASH_LBRACK : '#[';
HASH : '#';

UNIQUE_KW : 'unique' ;     // [新增]
SHARED_KW : 'shared' ;     // [新增]
WEAK_KW   : 'weak' ;       // [新增]

AT_MAKE_UNIQUE : '@make' ;        // [新增] 对应 @make[T]
AT_MAKE_SHARED : '@make_shared' ; // [新增] 对应 @make_shared[T] (修正了你的 @make_shread 拼写)
AT_MOVE        : '@move' ;       // [新增] 对应 @move(a)

STATIC_CAST      : 'static_cast' ;
REINTERPRET_CAST : 'reinterpret_cast' ;
CONST_CAST       : 'const_cast' ;

// BOOL_LITERAL 必须在 IDENTIFIER 之前
BOOL_LITERAL    : 'true' | 'false' ;
// [新增] new / delete 关键字
NEW     : 'new' ;
DELETE  : 'delete' ;
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
AND_OP  : '&&' ; // <-- [新增]
OR_OP   : '||' ; // <-- [新增]

// [ 新增 ] 位移运算符 (必须在 LT/GT 之前)
LSHIFT  : '<<' ;
RSHIFT  : '>>' ;

// [ 新增 ] 算术运算符
PLUS    : '+' ;
MINUS   : '-' ;
STAR    : '*' ;
SLASH   : '/' ;
MODULO  : '%' ; // <-- [新增]

// [ 新增 ] 复合赋值运算符
// [ 关键 ] 必须在 ASSIGN (=) 之前定义
PLUS_ASSIGN   : '+=' ;
MINUS_ASSIGN  : '-=' ;
STAR_ASSIGN   : '*=' ;
SLASH_ASSIGN  : '/=' ;
MOD_ASSIGN    : '%=' ;

// 简单符号 (必须在 INCLUDE_PATH 之前)
LT      : '<' ; 
GT      : '>' ; 
NOT_OP  : '!' ; // <-- [新增] (注意: '!=' 必须在此之前定义)

// [ 新增 ] 位运算符 (必须在 AND_OP/OR_OP 之后)
BIT_AND : '&' ;
BIT_OR  : '|' ;
BIT_XOR : '^' ;
BIT_NOT : '~' ;

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
LBRACK  : '[' ;
RBRACK  : ']' ;
COLON   : ':' ;
ASSIGN  : '=' ;
DOT     : '.' ;
COMMA   : ',' ;

// [修改] 1. 优先级最高的数字字面量
// 必须在 DECIMAL_LITERAL 之前
HEX_LITERAL     : '0' [xX] [0-9a-fA-F]+ ;
BINARY_LITERAL  : '0' [bB] [01]+ ;
OCTAL_LITERAL   : '0' [oO] [0-7]+ ;

// [新增] 2. FLOAT_LITERAL (例如 3.14)
// 必须在 DECIMAL_LITERAL 之前
FLOAT_LITERAL   : [0-9]+ '.' [0-9]+ ;

// [修改] 2. DECIMAL_LITERAL (之前是 INTEGER_LITERAL)
// 必须在 Hex/Binary/Octal 之后
DECIMAL_LITERAL : [0-9]+ ;

// [新增] 3. BYTE_LITERAL (例如 b'A')
// 必须在 CHAR_LITERAL 之前
BYTE_LITERAL    : 'b' '\'' ( ~['\\] | '\\' . ) '\'' ;

// C++11 UTF-8 string (e.g., u8"hello")
U8_STRING_LITERAL : 'u8' '"' ( ~["\\] | '\\' . )* '"' ;

// C++11 UTF-16 string (e.g., u"hello")
U_STRING_LITERAL  : 'u'  '"' ( ~["\\] | '\\' . )* '"' ;

// C++11 UTF-32 string (e.g., U"hello")
U_STRING_LITERAL_CAP : 'U'  '"' ( ~["\\] | '\\' . )* '"' ;

// Win32 Wide string (e.g., L"hello")
L_STRING_LITERAL_CAP : 'L'  '"' ( ~["\\] | '\\' . )* '"' ;

// --- 通用规则 (必须在最后) ---
IDENTIFIER : [a-zA-Z_] [a-zA-Z0-9_]* ;
//INTEGER_LITERAL : [0-9]+ ;
STRING_LITERAL  : '"' ( ~["\\] | '\\' . )* '"' ; 
CHAR_LITERAL    : '\'' ( ~['\\] | '\\' . ) '\'' ; // 匹配单引号字符 (例如 'a', '\n')

// --- 跳过 (Skipped) ---
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
WHITESPACE : [ \t\r\n\u00A0]+ -> skip ;
NEWLINE: ('\r' '\n'? | '\n') -> skip;
// --- 词法分析器模式 ---
mode INSIDE_CPP_BLOCK;
    AT_END : '@end' -> popMode;
    CPP_BODY : . ;