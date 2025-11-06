// -----------------------------------------------------------------------------
// Chrono Parser (ChronoParser.g4) - Final Correct Version
// -----------------------------------------------------------------------------
parser grammar ChronoParser;
options { tokenVocab = ChronoLexer; }

// --- Top Level Rules ---
program : topLevelStatement+ EOF ;

topLevelStatement
    : importDirective
    | cppBlock
    | classDefinition
    | functionDefinition
    ;

// --- 新增: 访问控制修饰符规则 ---
accessModifier : PUBLIC ;

// --- 新增: classBodyStatement 规则 (整合属性和方法) ---
classBodyStatement
    : (accessModifier)? declaration          // 属性声明接受可选的 public
    | ( // 允许修饰符的任意组合 (替代 )
        (STATIC (accessModifier)?) // 匹配: static, static public
    | (accessModifier (STATIC)?) // 匹配: public, public static
      ) methodDefinition
    |(accessModifier)? initDefinition     // <-- [ 新增 ]
    | methodDefinition // 匹配: (无修饰符)
    | deinitBlock
    | cppBlock
    ;

// --- 替换 classDefinition 规则 (使用新的 classBodyStatement) ---
classDefinition : CLASS name=IDENTIFIER (COLON base=IDENTIFIER)? LBRACE
                    (classBodyStatement)* RBRACE ;


// [NEW] 2. 类方法定义 (func foo()) - 接受 STATIC 和 Access Control
methodDefinition
    : FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=IDENTIFIER)? LBRACE
      statement* RBRACE ;

// [ 新增规则 ] initDefinition
// 它没有 'FUNC' 关键字，也没有 'returnType'
initDefinition
    : INIT LPAREN parameters RPAREN LBRACE statement* RBRACE ;

// [CRITICAL FIX] Must be statement*
deinitBlock : DEINIT LBRACE statement* RBRACE ; 

// [替换] importDirective 规则
importDirective
    : IMPORT path=(STRING_LITERAL | INCLUDE_PATH) (AS alias=IDENTIFIER)? SEMIC_TOKEN ;

// --- 修正 functionDefinition (移除 STATIC 和 accessModifier，因为它们在 classBodyStatement 中) ---
functionDefinition
    : (STATIC)? FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=IDENTIFIER)?
      LBRACE 
          statement* RBRACE ;

parameters : (parameter (COMMA parameter)*)? ;
parameter : name=IDENTIFIER COLON typeName=IDENTIFIER ;

//declaration : LET variableName=IDENTIFIER COLON typeName=IDENTIFIER (ASSIGN expression)? SEMIC_TOKEN ;
// --- 修正 declaration (移除 accessModifier，因为它在 classBodyStatement 中) ---
declaration : LET variableName=IDENTIFIER COLON typeName=IDENTIFIER (ASSIGN expression)? SEMIC_TOKEN ;

cppBlock : AT_CPP CPP_BODY* AT_END ;

returnStatement : RETURN expression SEMIC_TOKEN ;

assignment : assignableExpression ASSIGN expression SEMIC_TOKEN ;
assignableExpression
    : (IDENTIFIER | THIS) (DOT IDENTIFIER)*
    ;

// 使用新的命名规则 if_block 和 else_block
ifStatement
    : IF LPAREN expression RPAREN if_block=ifBlock // <-- [修改]
      ( ELSE
        ( else_if=ifStatement
        | else_block=elseBlock // <-- [修改]
        )
      )?
    ;

// [ 2. 添加新的辅助规则 ]
// 在这些规则中, "statement*" 是无歧义的
// 并且可以通过 ctx.statement() (默认访问器) 正确访问
ifBlock : LBRACE statement* RBRACE ;
elseBlock : LBRACE statement* RBRACE ;

// [CRITICAL FIX] Must be statement*
whileStatement
    : WHILE LPAREN expression RPAREN LBRACE statement* RBRACE
    ;

// --- Composite Rule ---
statement : declaration
          | assignment
          | returnStatement
          | expression SEMIC_TOKEN 
          | cppBlock
          | ifStatement
          | whileStatement
          | deleteStatement // <-- 引用新的专用规则
          ;
deleteStatement : DELETE expression SEMIC_TOKEN ;
// --- Expressions ---
expression
    : simpleExpression (
        (EQ | NEQ | LT | GT | LTE | GTE | PLUS | MINUS | STAR | SLASH) simpleExpression
      )?
    ;

simpleExpression
    : primary ( DOT IDENTIFIER (LPAREN expressionList? RPAREN)? )* | functionCallExpression 
    ;

primary
    : NEW IDENTIFIER LPAREN expressionList? RPAREN // <-- NEW 关键字创建对象
    | literal
    | IDENTIFIER
    | THIS
    | LPAREN expression RPAREN
    ;

functionCallExpression : name=IDENTIFIER LPAREN expressionList? RPAREN ;
expressionList : expression (COMMA expression)* ;

literal : INTEGER_LITERAL | STRING_LITERAL | BOOL_LITERAL ;