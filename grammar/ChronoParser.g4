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


classDefinition : CLASS name=IDENTIFIER COLON base=IDENTIFIER LBRACE
                    (declaration | functionDefinition | deinitBlock | cppBlock)*
                  RBRACE ;

// [CRITICAL FIX] Must be statement*
deinitBlock : DEINIT LBRACE statement* RBRACE ; 

// --- Basic Rules ---
importDirective : IMPORT path=(STRING_LITERAL | INCLUDE_PATH) SEMIC_TOKEN ;

// [CRITICAL FIX] Must be statement*
functionDefinition 
    : (STATIC)? FUNC name=IDENTIFIER LPAREN parameters RPAREN (ARROW returnType=IDENTIFIER)? 
      LBRACE 
          statement* RBRACE ;

parameters : (parameter (COMMA parameter)*)? ;
parameter : name=IDENTIFIER COLON typeName=IDENTIFIER ;

declaration : LET variableName=IDENTIFIER COLON typeName=IDENTIFIER (ASSIGN expression)? SEMIC_TOKEN ;

cppBlock : AT_CPP CPP_BODY* AT_END ;

returnStatement : RETURN expression SEMIC_TOKEN ;

assignment : assignableExpression ASSIGN expression SEMIC_TOKEN ;
assignableExpression
    : (IDENTIFIER | THIS) (DOT IDENTIFIER)*
    ;

// --- Flow Control ---
// [CRITICAL FIX] Must be statement*
ifStatement
    : IF LPAREN expression RPAREN LBRACE if_statements=statement* RBRACE 
      ( ELSE 
        ( else_if=ifStatement 
        | LBRACE else_statements=statement* RBRACE 
        )
      )? 
    ;

// [CRITICAL FIX] Must be statement*
whileStatement
    : WHILE LPAREN expression RPAREN LBRACE statements=statement* RBRACE 
    ;

// --- Composite Rule ---
statement : declaration
          | assignment
          | returnStatement
          | expression SEMIC_TOKEN 
          | cppBlock
          | ifStatement
          | whileStatement
          ;

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
    : literal
    | IDENTIFIER
    | THIS
    | LPAREN expression RPAREN 
    ;

functionCallExpression : name=IDENTIFIER LPAREN expressionList? RPAREN ;
expressionList : expression (COMMA expression)* ;

literal : INTEGER_LITERAL | STRING_LITERAL | BOOL_LITERAL ;