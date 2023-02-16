#include <iostream>
#include "symbols.hpp"
#include <stdio.h>

// using namespace std;

extern FILE *yyin;
extern int yylex();
extern char *yytext;
extern int line;

int main(int argc, const char * argv[]){
	
	yyin = fopen("test.txt", "r");
	
	int token;
	
	do{
		token = yylex();
		switch(token){
			case _num: printf("numero [%s]\n", yytext); break;
			case _sum: printf("suma [%s]\n", yytext); break;
			case _resta: printf("resta [%s]\n", yytext); break;
			case _mult: printf("multiplicacion [%s]\n", yytext); break;
			case _div: printf("divicion [%s]\n", yytext); break;
			// error y fin de archivo
			case _error: printf("Error en la linea %i: Error [%s]\n", line, yytext);  break;
			case _fin: printf("Fin del analisis lexico ...\n"); break;
			default: printf("?\n");
		}
		
	}while(token != _error && token != _fin);
	
	fclose(yyin);
	system("PAUSE");
	
	return 0;
}
