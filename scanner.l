%{
// codigo c
// #include "y.tab.h"
#include "symbols.hpp"
#include <stdio.h>
#include <math.h> // se necesita esto para la funcion atof
int line = 1;
%}

digit	[0-9]
numero	{digit}+"."{digit}+
nl		\n

%%

{numero}	return _num;
"+"			return _sum;
"-"			return _resta;
"*"			return _mult;
"/"			return _div;

{nl}		line++;
<<EOF>>		return _fin;

.			return _error;

%%

int yywrap() { return 1; }
