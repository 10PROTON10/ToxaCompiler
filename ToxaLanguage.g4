grammar ToxaLanguage;

// Определение лексем

INT : [0-9]+ ;
FLOAT : [0-9]+'.'[0-9]+ ;

// Арифметические операторы(Lexer Token)
PLUS : '+' ; // Сложение
MINUS : '-' ; // Вычитание
MULT : '*' ; // Умножение
DIV : '/' ; // Деление

// Скобки(Lexer Token)
LPAREN : '(' ; // Левая круглая скобка
RPAREN : ')' ; // Правая круглая скобка

// Пропуск пробелов и переводов строк
WS : [ \t\r\n]+ -> skip ;

// Правила синтаксиса
expr : expr (MULT | DIV) expr
     | expr (PLUS | MINUS) expr
     | INT
     | FLOAT
     | LPAREN expr RPAREN
     ;




