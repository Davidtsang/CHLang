// -----------------------------------------------------------------------------
// CH Parser (CHParser.g4) - [已修复: simpleExpression 歧义]
// -----------------------------------------------------------------------------
parser grammar CHParser;
options { tokenVocab = CHLexer; }


// (在 CHParser.g4 中)
// (在 CHParser.g4 中)

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

    | ( // 路径 C: CH 闭包/函数指针类型 (Params) -> Ret
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
    | DYN          // [新增] 允许 var x: dyn;
    // (为了兼容性保留 DOT，但推荐使用 COLON_COLON)
    | IDENTIFIER ( (DOT | COLON_COLON) IDENTIFIER )*
    ;

typeList
    : templateArgument (COMMA templateArgument)*
    ;

// 1. 变量声明 (支持 inline var/const)
variableDeclaration
    : (EXTERN)? (STATIC)? (INLINE)? (CONST | VAR) name=IDENTIFIER
      (COLON typeName=typeSpecifier)?
      (ASSIGN expression)?
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
    | codegenStatement  // <--- [新增] 允许在全局使用 @codegen
    ;

// [新语法] 匹配: type Child : struct;
forwardDeclaration
    : TYPEDECL name=IDENTIFIER COLON (kind=CLASS | kind=STRUCT) SEMIC_TOKEN
    ;

// [修改] 支持 public 或 protected
accessModifier
    : PUBLIC
    | PROTECTED
    ;

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
    : (AT_DYNAMIC)? // [新增] 允许 @dynamic class Name ...
     CLASS name=IDENTIFIER
      (COLON base=IDENTIFIER)?      // [不变] 基类：可选，且只有一个
      (IMPL interfaces=typeList)? // [新增] 接口：可选，可以是一个列表
      LBRACE
          (classBodyStatement)*
      RBRACE
    ;

// [ [ [ 1. 新增：实现块 (用于 .ch 文件) ] ] ]
implementationBlock
    : (AT_DYNAMIC)?
    IMPLEMENT name=IDENTIFIER LBRACE
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

// 3. 全局/类 函数声明 (用于 .h.ch)
functionSignature
    : (EXTERN)? (STATIC)? (INLINE)? (VIRTUAL)? (OVERRIDE)?
      FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)?
      SEMIC_TOKEN
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

// 4. 函数定义 (用于 .cpp.ch 或头文件内联实现)
functionDefinition
    : (EXTERN)? (STATIC)? (INLINE)?
      FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)?
      LBRACE
          statement* RBRACE ;

parameters : (parameter (COMMA parameter)*)? ;

parameter
    : name=IDENTIFIER COLON typeName=typeSpecifier
    ;

cppBlock : AT_CPP CPP_BODY* AT_END ;

returnStatement : RETURN expression? SEMIC_TOKEN ;

assignmentOperator
    : ASSIGN
    | PLUS_ASSIGN
    | MINUS_ASSIGN
    | STAR_ASSIGN
    | SLASH_ASSIGN
    | MOD_ASSIGN
    ;

assignment : assignableExpression assignmentOperator expression SEMIC_TOKEN ;

// (在 CHParser.g4 中替换 assignableExpression)
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
          | codegenStatement
          | CPP_DIRECTIVE
          ;
blockStatement : LBRACE statement* RBRACE ;  // <-- [新增]

// 语法规则: @codegen("PluginName");
codegenStatement
    : AT_CODEGEN LPAREN name=STRING_LITERAL RPAREN SEMIC_TOKEN
    ;

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

forRangeDeclaration
    : (CONST | VAR) name=IDENTIFIER (COLON typeName=typeSpecifier)?
    ;


// [修改] for 语句
forStatement
    : FOR LPAREN
      (
        // 路径 A: Range-based (新) -> for (var x in list)
        rangeDecl=forRangeDeclaration IN container=expression
        |
        // 路径 B: C-Style (旧) -> for (i=0; i<10; i++)
        init=forInit? SEMIC_TOKEN cond=expression? SEMIC_TOKEN incr=forIncrement?
      )
      RPAREN statement
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
    : (AT_OPTIONAL)? (accessModifier)?
     FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=typeSpecifier)? SEMIC_TOKEN
    ;

interfaceDefinition
    : INTERFACE name=IDENTIFIER
      LBRACE
          (methodSignature | cppBlock)*
      RBRACE
    ;

// 2. 变量声明 (无分号版，用于 for 循环等，通常不写 inline，但为了语法统一可以加上，或者忽略)
variableDeclaration_no_semicolon
    : (EXTERN)? (STATIC)? (INLINE)? (CONST | VAR) name=IDENTIFIER
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
    | castExpression   // 处理普通表达式
    ;

// 支持链式: obj as A as B (虽然很少用)
castExpression
    : simpleExpression (AS typeSpecifier)*
    ;

// --- [ 3. 升级: 'simpleExpression' 规则 ] ---
// [ [ 关键修复：已还原为无歧义的原始结构 ] ]
simpleExpression
    : ( primary | functionCallExpression )
      (
        // 路径 A: .foo / ->bar / ::baz
        (DOT | ARROW | COLON_COLON) IDENTIFIER (LT typeList GT)? (LPAREN expressionList? RPAREN)?

        // 路径 B: 数组索引 [i]
      | LBRACK expression RBRACK

        // 路径 C: [新增] 动态调用 ~>method(args)
        // 语法结构: ~> methodName ( args... )
      | TILDE_ARROW dynMethodName=IDENTIFIER LPAREN expressionList? RPAREN
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
    | closureExpression // [新增]
    ;

// 2. 定义闭包表达式
// 形式 A: (params) => { block }
// 形式 B: (params) => expression (单行隐式返回)
// 形式 C: { block } (简写，无参或尾随)
closureExpression
    : LPAREN parameters RPAREN ARROW_FUNC (blockStatement | expression)
    | blockStatement
    ;


initializerList
    : LBRACE expressionList? RBRACE
    ;

// 3. 修改函数调用，支持尾随闭包
// 原来: funcName LPAREN expressionList? RPAREN
// 现在: funcName LPAREN expressionList? RPAREN (closureExpression)?
functionCallExpression
    : funcName=(IDENTIFIER | AT_MOVE | AT_UNSAFE_MOVE)
      LPAREN expressionList? RPAREN
      (trailingClosure=closureExpression)? // [新增] 尾随闭包
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
    | C_STRING_LITERAL    // [新增] 代表 const char*
    | BOOL_LITERAL
    | CHAR_LITERAL
    | U8_STRING_LITERAL
    | U_STRING_LITERAL
    | U_STRING_LITERAL_CAP
    | L_STRING_LITERAL_CAP
    ;