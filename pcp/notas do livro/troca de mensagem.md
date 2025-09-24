### "intro da parte 2 do livro"

a sincronização que examinamos até então, é baseada em leitura e escrita em variáveis compartilhadas

consequentemente, para programas concorrentes, os programas eram executados com processadores compartilhanado memória

implica em mecanismo em cima de comunicação disponível pela rede, ao invés de compartilhar memória em si

para isso ser possível, os processos vão ser comunicar por mensagens

implica em IPC (Interprocess Comunication)
- troca de mensagens 
- RPC (Remote Procedure Call)
- Roudevous

---

###  intro de troca de mensagem

este capítulo foca em troca de mensagem *assíncrona*

canais são como semáforos que carregam informações, e `send` e `receive` são primitivas como `V` e `P` (respectivamente)

### 1. trocando mensagens assíncronas

em trocas de mensagens assíncronas, um canal é uma fila de mensagens que foram enviadas mas não recebidas. declaração:

```
chan ch(type1 id1, ..., typeN idN)
```

ch -> nome do canal

para enviar/receber mensagens é da seguinte forma:

```
send ch(expr1, ..., exprN)

receive ch(var1, ..., varN)
```

tanto as expressões enviadas `expr` quanto as variáveis que recebem os dados `var` devem ser dos mesmos tipos estipulados na declaração do canal

a função receive faz com que o "recebedor" espere até que tenha ao menos uma mensagem no canal

checa se a fila do canal está vazia:
```
empty ch()
```


### 2. filtros: uma rede de ordenação

um filtro é um predicato que relaciona o valor das mensagens enviadas em um canal de saída com os valores de mensagens recebidas no canal de entrada

para ilustrar, pode-se criar um filtro organizador

`input` é o canal de entrada
`output` é o canal de saída

os $n$ valores a serem ordenados são enviados por $input$ 

```
process Sort {
	receive all number from channel input;
	sort the number;
	send the sortede numbers to channel output;
}
```

#### rede merge

a ideia é juntar duas listas ordenadas em uma lista única ordenada

cada filtro merge recebe valores de duas entradas ordenadas `in1` e `in2` e produz `out` 

o fim das streams de entrada são marcadas por um EOS (end of stream)

primeira implementação:
![[fig 7.2.png]]










