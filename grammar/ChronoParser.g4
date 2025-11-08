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
    | functionDefinition
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
classDefinition : CLASS name=IDENTIFIER (COLON base=IDENTIFIER)?
    LBRACE
        (classBodyStatement)* RBRACE ;
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
assignment : assignableExpression ASSIGN expression SEMIC_TOKEN ;

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
          ;
deleteStatement : DELETE expression SEMIC_TOKEN ;

// --- Expressions ---
expression
    : unaryExpression (
        (EQ | NEQ | LT | GT | LTE | GTE | PLUS | MINUS | STAR | SLASH) unaryExpression
      )*
    ;

unaryExpression
    : (PLUS | MINUS) unaryExpression
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