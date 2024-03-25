grammar ToxaLanguage;

// Определение лексем
INT : [0-9]+ ;
FLOAT : [0-9]+'.'[0-9]+ ;
PLUS : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
OPEN_PAREN : '(' ;
CLOSE_PAREN : ')' ;

// Пропуск пробелов и переводов строк
WS : [ \t\r\n]+ -> skip ;

// Правила синтаксиса
expression : multExpr
           | expression PLUS multExpr
           | expression MINUS multExpr
           ;

multExpr : atom
         | multExpr MULT atom
         | multExpr DIV atom
         ;

atom : INT
     | FLOAT
     | OPEN_PAREN expression CLOSE_PAREN
     ;




