// -----------------------------------------------------------------------------
// Chrono Parser (ChronoParser.g4) - [已修复: simpleExpression 歧义]
// -----------------------------------------------------------------------------
parser grammar ChronoParser;
options { tokenVocab = ChronoLexer; }


// (在 ChronoParser.g4 中)
// (在 ChronoParser.g4 中)

// --- [ 1. 升级: 泛型/数组/函数 类型规则 ] ---
typeSpecifier
    : ( // 路径 A: C-Style 数组 (e.g., [char; 20])
        LBRACK typeSpecifier SEMIC_TOKEN expression RBRACK
      )
      ( (STAR | BIT_AND) )* // 数组的后缀

    | ( // 路径 B: 基础/泛型类型 (e.g., std.vector[i32] or i32)
        baseType (LBRACK typeList RBRACK)?
      )
      ( (STAR | BIT_AND) )* // 基础类型的后缀

    | ( // [ [ [ 关键修复: 路径 C/D 合并 ] ] ]
        //   处理所有以 '(' 开头的类型
        LPAREN
        (
            // 选项 1 (Path C): 这是一个函数类型
            // [ [ 关键变更 ] ]
            // 现在使用 'typeList?' (只匹配类型, e.g., 'i32, i32' 或 '()')
            (params=typeList? RPAREN ARROW returnType=typeSpecifier)

            // 选项 2 (Path D): 这是一个带括号的类型
            | (nested=typeSpecifier RPAREN)
        )
      )
      ( (STAR | BIT_AND) )* // 函数/带括号类型的后缀
    ;

baseType
    : (IDENTIFIER (DOT IDENTIFIER)*)
    | UNIQUE_KW   // [新增]
    | SHARED_KW   // [新增]
    | WEAK_KW     // [新增]
    ;

typeList
    : templateArgument (COMMA templateArgument)*
    ;

variableDeclaration
    : (CONST | VAR) name=IDENTIFIER       // 必须以 'const' 或 'var' 开头
      (COLON typeName=typeSpecifier)? // [修改] 类型 (e.g., : i32) 现在是可选的
      (ASSIGN expression)?            // [修改] 赋值 (e.g., = 10) 也是可选的
      SEMIC_TOKEN
    ;

templateArgument
    : typeSpecifier
    | literal
    ;


// --- Top Level Rules ---
program : topLevelStatement+ EOF ;

topLevelStatement
    : importDirective
    | cppBlock
    | classDefinition
    | structDefinition // <-- [新增]
    | functionDefinition
    | interfaceDefinition // <-- [新增]
    | usingAlias
    | typemapDefinition
    ;

accessModifier : PUBLIC ;

classBodyStatement
    : (accessModifier)? variableDeclaration // <-- [修改]
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
structDefinition
    : STRUCT name=IDENTIFIER
      LBRACE
          (structBodyStatement)*
      RBRACE
    ;

// structBodyStatement 规则
structBodyStatement
    : (accessModifier)? variableDeclaration
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
    : IMPORT path=(STRING_LITERAL | INCLUDE_PATH) (AS alias=IDENTIFIER)?;

usingAlias
    : USING name=IDENTIFIER ASSIGN typeName=typeSpecifier SEMIC_TOKEN ;

// 语法: typemap <NewName> [: <HintType>] = "<LiteralString>"
typemapDefinition
    : TYPEMAP name=IDENTIFIER (COLON hint=typeSpecifier)? ASSIGN value=STRING_LITERAL SEMIC_TOKEN ;

functionDefinition
    : (STATIC)?
    FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)?
      LBRACE
          statement* RBRACE ;

parameters : (parameter (COMMA parameter)*)? ;

parameter
    : name=IDENTIFIER COLON typeName=typeSpecifier
    ;

cppBlock : AT_CPP CPP_BODY* AT_END ;

returnStatement : RETURN expression SEMIC_TOKEN ;

assignmentOperator
    : ASSIGN
    | PLUS_ASSIGN
    | MINUS_ASSIGN
    | STAR_ASSIGN
    | SLASH_ASSIGN
    | MOD_ASSIGN
    ;

assignment : assignableExpression assignmentOperator expression SEMIC_TOKEN ;

// (在 ChronoParser.g4 中替换 assignableExpression)
assignableExpression
    : assignablePrimary      // 路径 A: 标识符, this, 或解引用/取地址的一元表达式
      ( // 循环处理链
        DOT IDENTIFIER                      // 路径 B: .foo
      | LBRACK expression RBRACK            // 路径 C: [i] (数组索引)
      | ARROW IDENTIFIER                    // 路径 D: ->foo 
      )*
    ;

// [新增] 允许作为赋值左值的一元表达式
assignablePrimary
    : IDENTIFIER 
    | THIS
    | STAR assignablePrimary   // [关键新增] 允许 * 解引用作为左值 (例如: **p2)
    | BIT_AND assignablePrimary // [新增] & 操作也允许，但实际 C++ 中无效（除非用于引用）
    | LPAREN assignableExpression RPAREN // 允许括号
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

statement : variableDeclaration
          | assignment
          | returnStatement
          | expression SEMIC_TOKEN
          | cppBlock
          | ifStatement
          | whileStatement
          | deleteStatement
          | forStatement
          | blockStatement  // <-- [新增]
          ;
blockStatement : LBRACE statement* RBRACE ;  // <-- [新增]
deleteStatement : DELETE expression SEMIC_TOKEN ;

forStatement
    : FOR LPAREN init=forInit? SEMIC_TOKEN cond=expression? SEMIC_TOKEN incr=forIncrement? RPAREN
      LBRACE
          statement*
      RBRACE
    ;

forInit
    : variableDeclaration_no_semicolon
    | assignment_no_semicolon
    ;

forIncrement
    : assignment_no_semicolon
    | expression
    ;

methodSignature
    : FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)? SEMIC_TOKEN
    ;

interfaceDefinition
    : INTERFACE name=IDENTIFIER
      LBRACE
          (methodSignature | cppBlock)*
      RBRACE
    ;

variableDeclaration_no_semicolon
    : (CONST | VAR) name=IDENTIFIER
      (COLON typeName=typeSpecifier)?
      (ASSIGN expression)?
    ;

assignment_no_semicolon
    : assignableExpression assignmentOperator expression
    ;

// --- Expressions ---
expression
    : unaryExpression (
        (EQ | NEQ | LT | GT | LTE | GTE | PLUS | MINUS | STAR | SLASH
        | MODULO | AND_OP | OR_OP
        | BIT_AND | BIT_OR | BIT_XOR | LSHIFT | RSHIFT) unaryExpression
      )*
    ;

unaryExpression
    : (PLUS | MINUS | NOT_OP | BIT_NOT) unaryExpression  // 处理 +, -, !, ~
    | BIT_AND unaryExpression // [新增] BIT_AND (& 取地址操作符)
    | STAR unaryExpression // [关键] STAR (* 解引用操作符)
    | simpleExpression   // 处理普通表达式
    ;

// --- [ 3. 升级: 'simpleExpression' 规则 ] ---
// [ [ 关键修复：已还原为无歧义的原始结构 ] ]
simpleExpression
    : ( primary | functionCallExpression )  // <-- [已还原]
      ( // 循环处理链式调用

        // 路径 A: .foo, .foo(), .foo[int], .foo[int]()
        DOT IDENTIFIER (LBRACK typeList RBRACK)? (LPAREN expressionList? RPAREN)?

      | LBRACK expression RBRACK            // 路径 B: [i] (数组索引)

      // 路径 C: ->foo() 或 ->foo
      | ARROW IDENTIFIER (LPAREN expressionList? RPAREN)? // <-- [ -> 支持已保留]

      )* ;

primary
    : NEW baseType LPAREN expressionList? RPAREN
    // [ [ 新增 ] ] @make[T](args) 和 @make_shared[T](args)
    | (AT_MAKE_UNIQUE | AT_MAKE_SHARED) LBRACK typeSpecifier RBRACK LPAREN expressionList? RPAREN
    | ( AT_MAKE_UNIQUE
      | AT_MAKE_SHARED
      | STATIC_CAST         // <-- [新增]
      | REINTERPRET_CAST    // <-- [新增]
      | CONST_CAST          // <-- [新增]
      )
      LBRACK typeSpecifier RBRACK LPAREN expressionList? RPAREN
    | literal
    | initializerList
    | IDENTIFIER
    | THIS
    | LPAREN expression RPAREN
    ;

initializerList
    : LBRACE expressionList? RBRACE
    ;

// (在 ChronoParser.g4 中替换 functionCallExpression)
functionCallExpression
    : funcName=(IDENTIFIER | AT_MOVE) // [修改] 允许 @move 作为函数名
    LPAREN expressionList? RPAREN
    ;

expressionList : expression (COMMA expression)* ;

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
    | U8_STRING_LITERAL
    | U_STRING_LITERAL
    | U_STRING_LITERAL_CAP
    | L_STRING_LITERAL_CAP
    ;