grammar ToxaLanguage;

// Начальное правило - программа - конечное правило
program: statement* EOF;

// Выражение может быть арифметическим выражением, операцией присваивания, оператором печати, if-else, for, while
statement: assignmentStatement
         | printStatement
         | ifStatement
         | ifElseStatement
         | whileStatement
         | forStatement
         | functionStatement
         | functionCall
         | returnStatement
         | expression;

// Правило для операции присваивания
assignmentStatement: type ID EQ expression END_STATE;

// Правило для оператора печати
printStatement: 'print' LPAREN expression RPAREN END_STATE;

// Правило для if-else
ifStatement: 'if' LPAREN expression RPAREN THEN ifBlock ENDIF END_STATE;

ifBlock: statement*;

ifElseStatement: 'if' LPAREN expression RPAREN THEN ifBlock 'else' elseBlock ENDIF END_STATE;

elseBlock: statement*;

forStatement: 'for' LPAREN forInitializer END_STATE forCondition END_STATE forUpdate RPAREN THEN forBlock ENDFOR END_STATE;

forBlock: statement*;

// Правило для инициализации цикла for
forInitializer: type ID EQ expression;

// Правило для условия цикла for
forCondition: expression;

// Правило для обновления цикла for
forUpdate: ID incrementOrDecrement;

incrementOrDecrement: INCREMENT | DECREMENT;

// Правила для инкремента и декремента
INCREMENT: PLUS PLUS;
DECREMENT: MINUS MINUS;

// Правило для оператора цикла while
whileStatement: 'while' LPAREN expression RPAREN THEN whileBlock ENDWHILE END_STATE;

whileBlock: statement*;

// Правило для функции
functionStatement: 'function' ID LPAREN params? RPAREN THEN functionBlock ENDFUNCTION END_STATE;

functionBlock: statement*;

// Правило для оператора возврата
returnStatement: 'return' expression END_STATE;

// Вызов функции
functionCall: ID LPAREN paramsCall RPAREN;

paramsCall: operand (',' operand)*;

// Параметры функции
params: type operand (',' type operand)*;

// Правило для арифметического выражения
expression
    : arithmetic
    | comparison
    | logical
    | operand
    | functionCall
    ;

comparison: operand (GT | LT | GE | LE | EQ | EQEQ | NE) operand;

arithmetic: operand ((MUL | DIV | REM | PLUS | MINUS) operand)*;

logical: operand (AND | OR) operand;

operand
    : INT
    | FLOAT
    | ID
    | functionCall
    | LPAREN expression RPAREN
    ;

// Типы данных
type: 'int' | 'float';

// Лексические правила (токены)
THEN: 'then';
ENDIF: 'endif';
ENDFOR: 'endfor';
ENDWHILE: 'endwhile';
ENDFUNCTION: 'endfunction';
INT: DIGIT+;
FLOAT: DIGIT+ '.' DIGIT+;
ID: [a-zA-Zа-яА-Я]+ DIGIT*;
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


// Пропускаем пробельные символы
WS: [ \t\r\n]+ -> skip;

fragment DIGIT: [0-9];