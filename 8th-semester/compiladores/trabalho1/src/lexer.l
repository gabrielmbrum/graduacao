%{
#include <stdio.h>
int linha = 1;
%}

%option noyywrap

/* Definições Regulares */
DIGITO      [0-9]
LETRA       [a-zA-Z_]
ID          {LETRA}({LETRA}|{DIGITO})*
INTEIRO     {DIGITO}+
REAL        {DIGITO}+\.{DIGITO}+

%%

\n                      { linha++; }
[ \t\r]+                { /* Ignora espaços em branco e tabulações */ }

\[[^\]]*\]              { printf("Comentario ignorado na linha %d\n", linha); /* Comentários delimitados por [ ] */ }

{REAL}                  { printf("Token: NUM_REAL (%s) encontrado na linha %d\n", yytext, linha); }
{INTEIRO}               { printf("Token: NUM_INTEIRO (%s) encontrado na linha %d\n", yytext, linha); }
{ID}                    { printf("Token: IDENTIFICADOR (%s) encontrado na linha %d\n", yytext, linha); }

"="                     { printf("Token: ATRIBUICAO (%s) encontrado na linha %d\n", yytext, linha); }
"+"                     { printf("Token: OP_SOMA (%s) encontrado na linha %d\n", yytext, linha); }
"-"                     { printf("Token: OP_SUB (%s) encontrado na linha %d\n", yytext, linha); }
"*"                     { printf("Token: OP_MULT (%s) encontrado na linha %d\n", yytext, linha); }
"/"                     { printf("Token: OP_DIV (%s) encontrado na linha %d\n", yytext, linha); }

","                     { printf("Token: VIRGULA (%s) encontrado na linha %d\n", yytext, linha); }
"."                     { printf("Token: PONTO (%s) encontrado na linha %d\n", yytext, linha); }
";"                     { printf("Token: PONTO_VIRGULA (%s) encontrado na linha %d\n", yytext, linha); }
":"                     { printf("Token: DOIS_PONTOS (%s) encontrado na linha %d\n", yytext, linha); }

"{"                     { printf("Token: ABRE_CHAVE (%s) encontrado na linha %d\n", yytext, linha); }
"}"                     { printf("Token: FECHA_CHAVE (%s) encontrado na linha %d\n", yytext, linha); }
"("                     { printf("Token: ABRE_PARENTESE (%s) encontrado na linha %d\n", yytext, linha); }
")"                     { printf("Token: FECHA_PARENTESE (%s) encontrado na linha %d\n", yytext, linha); }

.                       { printf("Erro lexico: caractere invalido '%s' na linha %d\n", yytext, linha); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            printf("Erro ao abrir o arquivo %s\n", argv[1]);
            return 1;
        }
    } else {
        printf("Uso: ./lexer input1.txt\n");
        return 1;
    }
    
    yylex();
    fclose(yyin);
    return 0;
}
