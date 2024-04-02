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

// Присвоение и вывод
ASSIGN : '=' ;
PRINT : 'print' ;

// Типы данных переменных
TYPE_INT : 'int' ;
TYPE_FLOAT : 'float' ;

// Идентификатор
ID : [a-zA-Z]+ ; // Переменные и имена функций состоят из букв.

// Пропуск пробелов и переводов строк
WS : [ \t\r\n]+ -> skip ;

// Добавленный токен
END_STATE : ';' ;

// Правила синтаксиса
prog : (assignStatement | printStatement | expr) ;

printStatement : PRINT LPAREN expr RPAREN END_STATE ;

// Правила для выражений
expr : term ((PLUS | MINUS) term)* ;

term : factor ((MULT | DIV) factor)* ;

factor : INT
       | FLOAT
       | LPAREN expr RPAREN
       | ID
       ;

// Правило для объявления переменной
assignStatement : type ID (ASSIGN expr)? END_STATE ;

type : TYPE_INT | TYPE_FLOAT ;












