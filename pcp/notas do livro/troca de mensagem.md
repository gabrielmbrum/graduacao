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

#### 2.1 rede merge

a ideia é juntar duas listas ordenadas em uma lista única ordenada

cada filtro merge recebe valores de duas entradas ordenadas `in1` e `in2` e produz `out` 

o fim das streams de entrada são marcadas por um EOS (end of stream)

implementação:
![[fig 7.2.png]]

### 3. clientes e servidores

servidor é um processo que repetidamente lida com solicitações de processos clientes

#### 3.1 monitores ativos

monitor é um gerenciador de recursos

inicialmente, assume-se esta estrutura de monitor
```
monitor Mname {
	declaração de variáveis permanentes;
	inicialização do código;
	
	procedure op(formals) {
		body of op;
	}
}
```

$MI$ é a invariante do monitor (predicado que especifíca os estados das variávies permanentes quando nenhuma chamada está ativa)

para simular um monitor usando troca de mensagem, as variáveis viram as variáveis do server, ele inicializa elas e fica num loop servindo chamadas de `op`

![[fig 7.4.png]]

exemplo de cliente/servidor com múltiplas operações;
![[fig 7.5.png]]


### obs

o aleardo não passou tudo deste capítulo, então abaixo segue as implementações de exercícios que ele passou na aula (ao invés de dar o restante do conteúdo do capítulo)

---
### problema do barbeiro dorminhoco

versão assíncrona
```c

chan cli[N] (int clientId);
chan barber (int clienteId);
chan cadeira (int salve);

process Barber {
	int cliente_id;
	int buff;
	
	while (true) {
	
		while(empty(cli)) // espera ser acordado
			dorme();
			
		receive barber(cliente_id); //recebe cliente
		send cli[cliente_id](1); // chama para sentar
		
		receive cadeira(buff); //espera sentar
		
		corta_cabelo();
		
		send cli[cliente_id](1); //avisa que acabou corte
		receive cadeira(buff);
	
	}
	
	
}

process Client[i = 0 to N] {
	int salve;
	
	send barber(i); //avisa que chegou
	receive cli[i](salve); //espera ser chamado
	senta();
	send cadeira(salve); //avisa que sentou
	receive cli[i](salve);
	levanta();
	send cadeira(salve); //avisa que saiu da cadeira
	
	
}

```

versão síncrona
```c
chan cli(string msg);
chan bar(int buff);
chan cadeira(int buff);

#define CHEGUEI 1
#define LEVANTEI 2

process Barber() {
	int buff;
	while (true) {
		receive bar(buff); //espera um cliente chegar
		
		sync_send cli("senta aqui"); //avisa pra sentar e espera sentar
		corta();
		sync_send cli("cortei ja"); //avisa que cortou e espera o cliente ouvir
		
		receive cadeira(buff); //espera o cliente levantar
	}
}

process Client [i=0 to N] {
	string buff;
	while (true) {
		sync_send bar(CHEGUEI); //avisa que chegou e e espera ser recebido
		
		receive cli(buff); //espera ser chamado para sentar
		talk();
		receive cli(buff); //espera ser avisado que acabou o corte
	
		send cadeira(LEVANTEI); //avisa que levantou
	}
}

```
### problema do produtor consumidor

introdução de nova sintaxe -> `sync_send` -> faz envio sincrono

```c
chan market_place(string msg);

process Producer() {
	while (true) {
		sync_send market_place("me receba se quiser consumir algo");
		produz();
		sync_send market_place("ta feito meu campeão");
	}
}

process Consumer() {
	string buffer;
	while (true) {
		receive market_place(buffer);
		receive market_place(buffer);
		consome();
	}
}
```

agora, a versão assíncrona do problema
```c
chan prod(string), cons(string);

process Consumer() {
	string buff;
	while (true) {
		receive prod(buff);
		send cons("quero consumir");
		receive prod(buff);
		consome();
		send cons("esta consumido bb");
	}
}

process Producer() {
	string buff;
	while (true) {
		send prod("alguem quer consumir?");
		receive cons(buff);
		produz();
		send prod("ta pronto meu rei");
		receive cons(buff); //espera consumir o produto
	}
}
```

barbeiro dorminhoco com múltiplos barbeiros
```c

chan cli[N], bar[M], cadeira[M];

process Barber[id_barber=0 to M] {
	int who;
	while (true) {
		//precisa ser acordado por qualquer cliente
		receive bar[id_barber](who);
		sync_send cli[who](id_barber); //vem sentar

		receive cadeira[id_baber]
		
		corta();
		
		sync_send cli[who][id_barber]//sai da cadeira puta
		
		receive cadeira[id_barber] // ta livre dnv
	}
}

process Cliente[id_cli=0 to N] {
	int who;
	
	while (empty cli[id_cli]())
		for (int j = 0; j < M; j++)
			send bar[c];
	}
	receive cli[id_cli](who);
	
	sync_send cadeira[who]("vou sentar"); //espera o barbeiro deixar ele sentar
	
	receive cli[id_cli](who) // saindio
	
	sync_send cadeira[who](id_cli) // ta livre	
}

```

