grammar ToxaLanguage;

// Начальное правило - программа
program: statement* EOF;

// Выражение может быть арифметическим выражением, операцией присваивания, оператором печати, if-else, for, while
statement: assignmentStatement
         | printStatement
         | ifStatement
         | ifElseStatement
         | whileStatement
         | forStatement
         | functionStatement
         | returnStatement
         | expression;

// Правило для операции присваивания
assignmentStatement: type ID EQ expression END_STATE;

// Правило для оператора печати
printStatement: 'print' LPAREN expression RPAREN END_STATE;

// Правило для if-else
ifStatement: 'if' LPAREN expression RPAREN RCORNER ifBlock LCORNER END_STATE;

ifBlock: statement*;

ifElseStatement: 'if' LPAREN expression RPAREN RCORNER ifBlock 'else' elseBlock LCORNER END_STATE;

elseBlock: statement*;

// Правило для оператора цикла for
forStatement: 'for' LPAREN forInitializer END_STATE (forCondition END_STATE?) forUpdate RPAREN RCORNER forBlock LCORNER END_STATE;

forBlock: statement*;

// Правило для инициализации цикла for
forInitializer: type ID EQ expression;

// Правило для условия цикла for
forCondition: expression;

// Правило для обновления цикла for
forUpdate: expression;

// Правило для оператора цикла while
whileStatement: 'while' LPAREN expression RPAREN RCORNER whileBlock LCORNER END_STATE;

whileBlock: statement*;

// Правило для функции
functionStatement: 'function' ID LPAREN params RPAREN RCORNER functionBlock LCORNER END_STATE;

functionBlock: statement*;

// Правило для оператора возврата
returnStatement: 'return' expression END_STATE;

// Вызов функции
functionCall: ID LPAREN params RPAREN;

// Параметры функции
params: expression? (',' expression)*;

// Правило для арифметического выражения
expression
    : operand
    | LPAREN expression RPAREN
    | expression (MUL | DIV | REM) expression
    | expression (PLUS | MINUS) expression
    | expression (GT | LT | GE | LE | EQ | EQEQ | NE) expression
    | expression (AND | OR) expression
    ;

operand
    : INT
    | FLOAT
    | ID
    | functionCall
    ;

// Типы данных
type: 'int' | 'float';

// Лексические правила (токены)
INT: DIGIT+;
FLOAT: DIGIT+ '.' DIGIT+;
ID: [a-zA-Z]+ DIGIT*;
MUL: '*';
REM: '%';
DIV: '/';
PLUS: '+';
MINUS: '-';
EQ: '=';
LPAREN: '(';
RPAREN: ')';
END_STATE: ';';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
EQEQ: '==';
NE: '!=';
AND: '&&';
OR: '||';
// Левая и правая фигурные скобки(Lexer Token)
RCORNER: '{';
LCORNER: '}';

// Пропускаем пробельные символы
WS: [ \t\r\n]+ -> skip;

fragment DIGIT: [0-9];
