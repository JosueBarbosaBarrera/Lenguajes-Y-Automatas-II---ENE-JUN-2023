%{

#include <stdio.h>
#include "symbols.hpp"

extern int line;
extern int yylex();
int yyerror(const char *);

%}

%token _num
%start Inicio
%left "+" "-"
%left "*" "/"

%%
Inicio: Exp { $$ = $1; };
Exp:
_num "+" _num		{ $$ = $1 + $3; } |
_num "-" _num		{ $$ = $1 - $3; } |
_num "*" _num		{ $$ = $1 * $3; } |
_num "/" _num		{ $$ = $1 / $3; } |
_num				{ $$ = $1; };

%%


int yyerror(const char *){
	printf("Error en linea %i\n", line);
	return 0;
}
