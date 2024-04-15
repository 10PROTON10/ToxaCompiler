grammar ToxaLanguage;

// Начальное правило - программа
program: statement* EOF;

// Выражение может быть арифметическим выражением, операцией присваивания, оператором печати, if-else, for, while
statement: assignmentStatement
         | printStatement
         | ifStatement
         | whileStatement
         | forStatement
         | functionDeclaration
         | returnStatement
         | expression;

// Правило для операции присваивания
assignmentStatement: ID EQ expression END_STATE;

// Правило для оператора печати
printStatement: 'print' LPAREN expression RPAREN END_STATE;

// Правило для if-else
ifStatement: 'if' LPAREN expression RPAREN 'then' block ( elseStatement )? 'endif' END_STATE;

// Правило для elseStatement
elseStatement: 'else' block;

block: statement*;

// Правило для оператора цикла for
forStatement: 'for' LPAREN forInitializer? ';' forCondition? ';' forUpdate? RPAREN 'then' block 'endfor' END_STATE;

// Правило для оператора цикла while
whileStatement: 'while' LPAREN expression RPAREN 'then' block 'endwhile' END_STATE;

// Правило для функции
functionDeclaration: 'function' ID LPAREN params RPAREN 'begin' statement* 'end' END_STATE;

// Правило для оператора возврата
returnStatement: 'return' expression END_STATE;

// Правило для инициализации цикла for
forInitializer: assignmentStatement | expression;

// Правило для условия цикла for
forCondition: expression;

// Правило для обновления цикла for
forUpdate: expression;

// Вызов функции
functionCall: ID LPAREN params RPAREN;

// Параметры функции
params: expression? (',' expression)*;

// Правило для арифметического выражения
expression
    : '(' expression ')'                      #expressionNested
    | expression POW expression              #expressionPow
    | expression (MUL | DIV | REM) expression  #expressionMulDivRem
    | expression (PLUS | MINUS) expression     #expressionAddSub
    | operand                                  #expressionOperand
    | expression (GT | LT | GE | LE | EQ | EQEQ | NE) expression        #expressionComparison
    | expression (AND | OR) expression        #expressionAndOr
    ;

// Правило для операнда
operand
    : INT                                     #operandInt
    | FLOAT                                   #operandFloat
    | ID                                      #operandId
    | functionCall                            #operandFunctionCall
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
POW: '^';
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

// Пропускаем пробельные символы
WS: [ \t\r\n]+ -> skip;

fragment DIGIT: [0-9];

