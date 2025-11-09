// -----------------------------------------------------------------------------
// Chrono Parser (ChronoParser.g4) - [已修复: assignableExpression]
// -----------------------------------------------------------------------------
parser grammar ChronoParser;
options { tokenVocab = ChronoLexer; }

// --- [ 1. 升级: 泛型/数组类型规则 ] ---
typeSpecifier
    : ( // 路径 A: 泛型/基础 (std.vector[i32] or i32)
        baseType (LBRACK typeList RBRACK)?
      )
    | ( // 路径 B: C-Style 数组 (递归)
        LBRACK typeSpecifier SEMIC_TOKEN expression RBRACK // [关键修改] baseType -> typeSpecifier
      )
    ;

baseType
    : IDENTIFIER (DOT IDENTIFIER)*
    ;

// typeList 现在是 'templateArgument' 的列表
typeList
    : templateArgument (COMMA templateArgument)*
    ;

// templateArgument (C++ 模板参数)
// 可以是一个 '类型' (std.string) 或一个 '值' (5)
templateArgument
    : typeSpecifier
    | literal
    ;


// --- Top Level Rules ---
program : topLevelStatement+ EOF ;
// ... (topLevelStatement, classDefinition 等保持不变) ...
topLevelStatement
    : importDirective
    | cppBlock
    | classDefinition
    | structDefinition // <-- [新增]
    | functionDefinition
    | interfaceDefinition // <-- [新增]
    ;
accessModifier : PUBLIC ;
classBodyStatement
    : (accessModifier)? declaration
    | ( (STATIC (accessModifier)?)
      | (accessModifier (STATIC)?)
      ) methodDefinition
    | (accessModifier)? initDefinition
    | methodDefinition
    | deinitBlock
    | cppBlock
    ;

classDefinition
    : CLASS name=IDENTIFIER
      (COLON base=IDENTIFIER)?      // [不变] 基类：可选，且只有一个
      (IMPL interfaces=typeList)? // [新增] 接口：可选，可以是一个列表
      LBRACE
          (classBodyStatement)*
      RBRACE
    ;

// structDefinition 规则
// 注意：它故意不允许 ':', 'impl' (无继承)
structDefinition
    : STRUCT name=IDENTIFIER
      LBRACE
          (structBodyStatement)*
      RBRACE
    ;

// structBodyStatement 规则
// 故意不允许 'STATIC'
structBodyStatement
    : (accessModifier)? declaration
    | (accessModifier)? methodDefinition
    | (accessModifier)? initDefinition
    | deinitBlock // deinit 总是 public
    | cppBlock
    ;

methodDefinition
    : FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)?
    LBRACE
      statement* RBRACE ;
initDefinition
    : INIT LPAREN parameters RPAREN LBRACE statement* RBRACE ;
deinitBlock : DEINIT LBRACE statement* RBRACE ;
importDirective
    : IMPORT path=(STRING_LITERAL | INCLUDE_PATH) (AS alias=IDENTIFIER)? SEMIC_TOKEN ;
functionDefinition
    : (STATIC)?
    FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)?
      LBRACE
          statement* RBRACE ;
parameters : (parameter (COMMA parameter)*)? ;
parameter
    : name=IDENTIFIER COLON typeName=typeSpecifier
    ;
declaration
    : LET variableName=IDENTIFIER COLON typeName=typeSpecifier (ASSIGN expression)? SEMIC_TOKEN
    ;
cppBlock : AT_CPP CPP_BODY* AT_END ;
returnStatement : RETURN expression SEMIC_TOKEN ;
// [ 新增 ] 辅助规则，用于所有赋值操作
assignmentOperator
    : ASSIGN
    | PLUS_ASSIGN
    | MINUS_ASSIGN
    | STAR_ASSIGN
    | SLASH_ASSIGN
    | MOD_ASSIGN
    ;

// [ 修改 ] assignment 规则
assignment : assignableExpression assignmentOperator expression SEMIC_TOKEN ;

// --- [ 2. 升级: 'assignableExpression' 规则 ] ---
// [修改] 使其支持 '.' 和 '[]' 链 (例如 numbers[3])
assignableExpression
    : (IDENTIFIER | THIS)
      ( // 循环处理链
        DOT IDENTIFIER                      // 路径 A: .foo
      | LBRACK expression RBRACK            // 路径 B: [i] (数组索引)
      )*
    ;

ifStatement
    : IF LPAREN expression RPAREN if_block=ifBlock
      ( ELSE
        ( else_if=ifStatement
        | else_block=elseBlock
        )
      )?
    ;
ifBlock : LBRACE statement* RBRACE ;
elseBlock : LBRACE statement* RBRACE ;
whileStatement
    : WHILE LPAREN expression RPAREN LBRACE statement* RBRACE
    ;
statement : declaration
          | assignment
          | returnStatement
          | expression SEMIC_TOKEN
          | cppBlock
          | ifStatement
          | whileStatement
          | deleteStatement
          | forStatement // <-- [新增]
          ;

deleteStatement : DELETE expression SEMIC_TOKEN ;

// [新增] C-Style For 循环
// [修改] C-Style For 循环
forStatement
    : FOR LPAREN init=forInit? SEMIC_TOKEN cond=expression? SEMIC_TOKEN incr=forIncrement? RPAREN
      LBRACE
          statement*
      RBRACE
    ;

// 'forInit' 规则允许两种形式的初始化：
// 1. let i: i32 = 0 (一个*无分号*的声明)
// 2. i = 0 (一个*无分号*的赋值)
forInit
    : declaration_no_semicolon
    | assignment_no_semicolon
    ;

// [ [ 新增 ] ]
// 'forIncrement' 规则
// 允许增量部分是 'i = i + 1' (赋值) 或 'myFunc()' (表达式)
forIncrement
    : assignment_no_semicolon
    | expression
    ;

// [新增] 接口中的方法签名
// (注意：没有 'public' 或 'static'，接口方法默认是 public virtual)
methodSignature
    : FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)? SEMIC_TOKEN
    ;

// [新增] 接口定义
interfaceDefinition
    : INTERFACE name=IDENTIFIER
      LBRACE
          (methodSignature | cppBlock)* // 接口只能包含方法签名或 @cpp 块
      RBRACE
    ;
    
// 我们需要复制 'declaration' 和 'assignment' 规则，
// 但移除它们末尾的 SEMIC_TOKEN。

declaration_no_semicolon
    : LET variableName=IDENTIFIER COLON typeName=typeSpecifier (ASSIGN expression)?
    ;

// [ 修改 ] assignment_no_semicolon 规则
assignment_no_semicolon
    : assignableExpression assignmentOperator expression
    ;
// --- Expressions ---
expression
    : unaryExpression (
        (EQ | NEQ | LT | GT | LTE | GTE | PLUS | MINUS | STAR | SLASH
        | MODULO | AND_OP | OR_OP
        | BIT_AND | BIT_OR | BIT_XOR | LSHIFT | RSHIFT) unaryExpression // <-- [修改]
      )*
    ;

unaryExpression
    : (PLUS | MINUS | NOT_OP | BIT_NOT) unaryExpression // <-- [修改]
    | simpleExpression
    ;

// --- [ 3. 升级: 'simpleExpression' 规则 ] ---
// [修改] 将 primary/functionCall 移到链的开头
simpleExpression
    : ( primary | functionCallExpression )
      ( // 循环处理链式调用
        DOT IDENTIFIER (LPAREN expressionList? RPAREN)? // 路径 A: .foo() 或 .foo
      | LBRACK expression RBRACK                      // 路径 B: [i] (数组索引)
      )* ;

primary
    : NEW baseType LPAREN expressionList? RPAREN
    | literal
    | initializerList // <-- 支持 {...} 作为值
    | IDENTIFIER
    | THIS
    | LPAREN expression RPAREN
    ;

// [新增] initializerList 规则 (例如 {1, 2, 3})
initializerList
    : LBRACE expressionList? RBRACE
    ;

functionCallExpression : name=IDENTIFIER LPAREN expressionList? RPAREN ;
expressionList : expression (COMMA expression)* ;

// [修改] literal 规则 (以匹配 Lexer)
literal
    : DECIMAL_LITERAL
    | HEX_LITERAL
    | BINARY_LITERAL
    | OCTAL_LITERAL
    | FLOAT_LITERAL
    | BYTE_LITERAL
    | STRING_LITERAL
    | BOOL_LITERAL
    | CHAR_LITERAL
    ;