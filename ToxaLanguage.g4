grammar ToxaLanguage;
// Определение лексем

INT : [0-9]+ ;
PLUS : '+' ;
MULT : '*' ;
OPEN_PAREN : '(' ;
CLOSE_PAREN : ')' ;

// Пропуск пробелов и переводов строк
WS : [ \t\r\n]+ -> skip ;

// Правила синтаксиса
expression : INT
| expression PLUS expression
| expression MULT expression
| OPEN_PAREN expression CLOSE_PAREN
;



