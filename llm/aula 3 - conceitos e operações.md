
### conceitos básicos sobre LM

**montador**
relacionar o código desenvolvido com o hardware adjacente aplicado
de forma geral, é fornecido pelo fabricante

### operações lógicas

tabelas-verdade
portas lógicas

**definindo registradores**
endereços de 0x20 a 0x7F são frequentemente utilizados para..

**lógica AND**
a instrução *ANDWF* reliza uma operação lógica .and. bit a bit entre o conteúdo do registrador de trabalho *W* e o conteúdo de um registrador de arquivos espeficiado (exemplo: *f*), o resultado é armazenado no destino especificado (*W* ou *f*)


### operações aritméticas

*INC* -> incrementa um operando em uma unidade

```asm
; registrador AL é de uso geral
MOV AL, 1
INC AL
```

*DEC* -> decrementa um operando em uma unidade
```asm
MOV ECX, 10
DEC ECX
```

voce pode decrementar um valor armazenado em um endereço de memória
```
DATA_SEG    ;início da seção de dados
NUM DB 10   ;define var NUM com valor 10
DATA_END    ;fim da seção de dados

CODE_SEG
MOV AL, NUM ;move o valor de NUM para AL
DEC AL ;decrementa 1 em AL
MOV NUM, AL ;move AL para NUM
CODE_END
```

*ADD e SUB* -> adiciona/subtrai dados do tamanho em byte, word ou doubleword (8-bit, 16-bit ou 32-bit)
a instrução é usada para adicionar/subtrair dois operando e armazenar o resultado no primeiro operando
```
MOV EAX, 5
ADD EAX, 3

MOV EAX, 5
SUB EAX, 3
```

pode ser utilizado em endereço de memória também

*MUL/IMUL*

###### MUL trata de dados sem sinal

```
MOV AL, 10
MOV BL, 20
MUL BL ;multiplca AL por BL
```

**parte alta x parte baixa**
referem-se às divisões do resultado de uma multiplicação em Assembly, especialmente quando o produto é maior do que o tamnho dos operando originais

parte alta -> mais significativos
parte baixa -> menos significativos

exemplo
- AL = 5
- multiplicador = 3
- produto 15 (00000000 00001111)
	- AL = 15 (00001111)
	- AH = 0 (00000000)


###### IMUL trata de sinal

...

*DIV/IDIV*

realiza as operações de divisão

**overflow**
configura o código para verificar se houve alguma flag de estouro (overflow)



