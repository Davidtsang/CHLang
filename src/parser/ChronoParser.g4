// -----------------------------------------------------------------------------
// Chrono Parser (ChronoParser.g4) - [已修复: simpleExpression 歧义]
// -----------------------------------------------------------------------------
parser grammar ChronoParser;
options { tokenVocab = ChronoLexer; }


// (在 ChronoParser.g4 中)
// (在 ChronoParser.g4 中)

// --- [ 1. 升级: 泛型/数组/函数 类型规则 ] ---
typeSpecifier
    : ( // 路径 A: C-Style 数组 [type; size]
        LBRACK typeSpecifier SEMIC_TOKEN expression RBRACK
      )
      ( (STAR | BIT_AND) )*

    | ( // 路径 B: 基础/泛型类型/C++函数类型
        baseType
        (LT typeList GT)?           // 泛型 <T>
        (LPAREN typeList? RPAREN)?  // [新增] C++函数类型 (Args...)，例如 void()
      )
      ( (STAR | BIT_AND) )* // 指针/引用后缀

    | ( // 路径 C: Chrono 闭包/函数指针类型 (Params) -> Ret
        LPAREN
        (
            (params=typeList? RPAREN ARROW returnType=typeSpecifier)
            | (nested=typeSpecifier RPAREN)
        )
      )
      ( (STAR | BIT_AND) )*
    ;

baseType
    : UNIQUE_KW
    | SHARED_KW
    | WEAK_KW
    // [修改] 允许 IDENTIFIER 后跟 . 或 ::
    // (为了兼容性保留 DOT，但推荐使用 COLON_COLON)
    | IDENTIFIER ( (DOT | COLON_COLON) IDENTIFIER )*
    ;

typeList
    : templateArgument (COMMA templateArgument)*
    ;

variableDeclaration
    : (EXTERN)? (CONST | VAR) name=IDENTIFIER       // 必须以 'const' 或 'var' 开头
      (COLON typeName=typeSpecifier)? // [修改] 类型 (e.g., : i32) 现在是可选的
      (ASSIGN expression)?            // [修改] 赋值 (e.g., = 10) 也是可选的
      SEMIC_TOKEN
    ;

templateArgument
    : typeSpecifier
    | literal
    ;

// 匹配: Framework, 或 Framework.UI, 或 Framework.UI.Window
qualifiedIdentifier
    : IDENTIFIER (DOT IDENTIFIER)*
    ;

// 匹配: namespace Framework.UI;
namespaceStatement
    : NAMESPACE name=qualifiedIdentifier SEMIC_TOKEN
    ;


// --- Top Level Rules ---
program : (topLevelImport)* (namespaceStatement)? topLevelStatement* EOF ;

topLevelImport
    : importDirective
    | CPP_DIRECTIVE
    ;

topLevelStatement
    : cppBlock
    | classDefinition
    | structDefinition
    | functionDefinition
    | enumDefinition
    | functionSignature
    | implementationBlock // [ [ [ 修正：添加此行 ] ] ]
    | interfaceDefinition
    | usingAlias
    | variableDeclaration
    | forwardDeclaration // [新增]
    | CPP_DIRECTIVE
    | endNamespaceStatement
    ;

// [新语法] 匹配: type Child : struct;
forwardDeclaration
    : TYPE name=IDENTIFIER COLON (kind=CLASS | kind=STRUCT) SEMIC_TOKEN
    ;

accessModifier : PUBLIC ;

endNamespaceStatement : END_NAMESPACE SEMIC_TOKEN ;

// 匹配: init(params);
initSignature
    : INIT LPAREN parameters RPAREN SEMIC_TOKEN
    ;

// 匹配: deinit;
deinitSignature
    : DEINIT SEMIC_TOKEN
    ;

classBodyStatement
    : (accessModifier)? variableDeclaration
    | (accessModifier)? enumDefinition
    | ( (accessModifier)? (STATIC)? | (STATIC)? (accessModifier)? ) functionSignature // 允许 'public static func'
    | (accessModifier)? initSignature
    | (accessModifier)? deinitSignature // <--- 修复 'publicdeinit' 错误
    | functionSignature   // (用于私有 func)
    | initSignature     // (用于私有 init)
    | deinitSignature   // (用于私有 deinit)
    | cppBlock
    | CPP_DIRECTIVE
    ;

classDefinition
    : CLASS name=IDENTIFIER
      (COLON base=IDENTIFIER)?      // [不变] 基类：可选，且只有一个
      (IMPL interfaces=typeList)? // [新增] 接口：可选，可以是一个列表
      LBRACE
          (classBodyStatement)*
      RBRACE
    ;

// [ [ [ 1. 新增：实现块 (用于 .ch 文件) ] ] ]
implementationBlock
    : IMPLEMENT name=IDENTIFIER LBRACE
        ( methodDefinition  // 方法实现
        | initDefinition    // 构造函数实现
        | deinitBlock       // 析构函数实现
        // | rawCppDirective   // (如果我们保留了 # 指令)
        )*
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
    | (accessModifier)? enumDefinition
    | (accessModifier)? functionSignature // (Struct 不支持 static func)
    | (accessModifier)? initSignature
    | (accessModifier)? deinitSignature // <--- 修复 'publicdeinit' 错误
    | functionSignature   // (用于私有 func)
    | initSignature     // (用于私有 init)
    | deinitSignature   // (用于私有 deinit)
    | cppBlock
    | CPP_DIRECTIVE
    ;

// [新增] 枚举定义规则
// 匹配:
// 1. enum Color { Red, Blue }
// 2. enum class State : u8 { OK = 0, Error = 1 }
enumDefinition
    : ENUM (CLASS)? name=IDENTIFIER
      (COLON typeSpecifier)? // 可选底层类型
      LBRACE enumBody? RBRACE SEMIC_TOKEN?
    ;

enumBody
    : enumItem (COMMA enumItem)* (COMMA)? // 允许尾部逗号
    ;

enumItem
    : name=IDENTIFIER (ASSIGN expression)?
    ;

// [ [ [ 1. 新增：全局/类 函数声明 (用于 .h.ch) ] ] ]
functionSignature
    : (EXTERN)? (STATIC)?
    FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)?
    SEMIC_TOKEN // <-- 关键区别：分号，而不是 LBRACE ... RBRACE
    ;

methodDefinition
    : FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)?
    LBRACE
      statement* RBRACE ;

initDefinition
    : INIT LPAREN parameters RPAREN
      (COLON baseInit=baseInitializer)? // <-- [ [ [ 新增 ] ] ]
      LBRACE statement* RBRACE
    ;

deinitBlock : DEINIT LBRACE statement* RBRACE ;

includeHeaderContent
    : (IDENTIFIER | DOT | SLASH | MINUS | PLUS | DECIMAL_LITERAL)+
    ;

// 2. 修改 importDirective
// 以前是: IMPORT path=(STRING_LITERAL | INCLUDE_PATH) ...
// 现在改为:
importDirective
    : IMPORT
      ( pathStr=STRING_LITERAL              // 匹配 "path/to/file.ch"
      | (LT pathSeq=includeHeaderContent GT) // 匹配 <vector> 或 <sys/stat.h>
      )
      (AS alias=IDENTIFIER)?
    ;

usingAlias
    : USING name=IDENTIFIER ASSIGN typeName=typeSpecifier SEMIC_TOKEN ;

functionDefinition
    : (EXTERN)? (STATIC)?
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
    : assignablePrimary
      ( // 循环处理链
        DOT IDENTIFIER                      // 路径 A: .foo
      | ARROW IDENTIFIER                    // 路径 B: ->foo
      | COLON_COLON IDENTIFIER              // 路径 C: ::foo [新增]
      | LBRACK expression RBRACK            // 路径 D: [i]
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
          | switchStatement
          | CPP_DIRECTIVE
          ;
blockStatement : LBRACE statement* RBRACE ;  // <-- [新增]

// 匹配: case 1 { ... }
caseBlock
    : CASE expression LBRACE statement* RBRACE ;

// 匹配: default { ... }
defaultBlock
    : DEFAULT LBRACE statement* RBRACE ;

// 匹配: switch (expr) { case... default... }
switchStatement
    : SWITCH LPAREN expression RPAREN
      LBRACE
          ( caseBlock )* // 0 个或多个 case 块
          ( defaultBlock )?   // 0 或 1 个 default 块
      RBRACE
    ;


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
    : (EXTERN)? (CONST | VAR) name=IDENTIFIER
      (COLON typeName=typeSpecifier)?
      (ASSIGN expression)?
    ;

assignment_no_semicolon
    : assignableExpression assignmentOperator expression
    ;

// [ [ [ 新增：基类初始化器规则 ] ] ]
// 匹配: Window(arg1, arg2)
baseInitializer
    : name=IDENTIFIER LPAREN args=expressionList? RPAREN
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
    : ( primary | functionCallExpression )
      (
        // [修改] 显式匹配三种访问符
        (DOT | ARROW | COLON_COLON) IDENTIFIER (LT typeList GT)? (LPAREN expressionList? RPAREN)?

      | LBRACK expression RBRACK
      )* ;

primary
    : NEW baseType LPAREN expressionList? RPAREN

    // [关键修改] @make<T>(...)
    | (AT_MAKE_UNIQUE | AT_MAKE_SHARED) LT typeSpecifier GT LPAREN expressionList? RPAREN

    // [关键修改] static_cast<T>(...)
    | ( AT_MAKE_UNIQUE
      | AT_MAKE_SHARED
      | STATIC_CAST
      | REINTERPRET_CAST
      | CONST_CAST
      )
      LT typeSpecifier GT LPAREN expressionList? RPAREN

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