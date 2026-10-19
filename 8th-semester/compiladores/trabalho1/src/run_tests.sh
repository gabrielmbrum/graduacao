#!/bin/bash

for i in {1..5}
do
    echo "=============================="
    echo "Rodando teste: input${i}.txt"
    echo "=============================="
    
    if [ -f "input${i}.txt" ]; then
        ./lexer input${i}.txt
    else
        echo "Arquivo input${i}.txt não encontrado."
    fi
    
    echo -e "\n"
done