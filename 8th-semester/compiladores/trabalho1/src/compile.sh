#!/bin/bash

echo "Gerando o código C com o Flex..."
flex lexer.l

if [ $? -ne 0 ]; then
    echo "Erro ao executar o Flex."
    exit 1
fi

echo "Compilando com o GCC..."
gcc lex.yy.c -o lexer

if [ $? -ne 0 ]; then
    echo "Erro na compilação."
    exit 1
fi

echo "Sucesso! O analisador léxico está pronto."
echo "Para testar, execute: ./lexer entrada.txt"