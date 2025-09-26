### 0. intro

troca de mensagens pode ser utilizadao para clientes e servidores (assim como visto em [[troca de mensagem]]), porém exige muitos canais

neste capítulo vemos duas notações adicionais, RPC e rendezvous, que são ideais para programação de interações no estilo clientes/servidores, pois combinam aspectos de monitores e troca de mensagem síncrona

a novidade desses métodos é que uma operação é um canal de comunicação de duas-vias, a partir do "chamador" até o processo que serve essa chamada e de volta para o "chamador" 

o invocador ("chamador") fica em espera até a operação ser executada e os resultados serem retornados

**RPC x rendezvous *(diferenças)***
a diferença é na maneira em que as chamadas aos procesos são servidas, uma delas é declarar um procedimento para cada operação e criar um novo processo para cada chamada (*remote procedure call* -> este nome é devido a possibilidade de o invocador e o corpo do procedimento estarem em máquinas diferentes), já a outra é servida por meio de uma expressão de entrada que espera por uma chamada, processa ela e retorna os resultados (*rendezvous*)

---

### 1. remote procedure call

em monitores, existiam dois componentes: processos e monitores

aqui, existe apenas um que encapsula processos e procedimentos -> **módulos**

estrutura de um módulo:
```
module mname
	headers of exported operations;
body
	variable declarations;
	initialization code;
	procedures for exported operations;
	local procedures and processes;
end mname
```

o header de um operação é declarado assim:
>op opname(formals) [returns result]

formals e returns -> especificam o tipo das variáveis

uma operação é implementada por um proc:
```
proc opname (formal identifires) returns result identifier
	declarations of local variables;
	statements
end
```

a chamada de um procedimento em outro módulo é feita:
>call mname.opname(args)

#### 1.1 sincronização em módulos

existem duas abordagens:
1. assumir que todos os processos no mesmo módulo executam com exclusão mútua (no máximo um de cada vez), caso deseje ter sincronização condicional, usa-se variáveis de condições ou semáforos
2. assume-se que os processos executam concorrentemente, assim programa-se exclusão mútua e condições de sincronização 

a primeira coisa a ser executada em um programa com módulos é o código de inicialização

iremos assumir a `opção 2` pois é a mais útil

#### 1.2 time server

o problema é criar um servidor relógio, em que um modulo fornece serviço de tempo para processos clientes em outro módulos, o servidor define duas operações:
1. get_time -> pega o horário do dia
2. delay -> bloqueia por *interval* unidades de tempo

o servidor tem um processo itnerno que continuamente começa um timer no hardware

```
module TimeServer
	op get_time() returns int;
	op delay(int interval);
body
	int tod = 0;  # TimeOfDay, its shared var
	sem m = 1;
	sem d[n] = ([n] 0)
	queue of (int waketime, int process_id) napQ;
	
	proc get_time() returns time {
		time = tod;
	}
	
	proc delay(interval) {
		int waketime = tod + interval;
		P(m);
		insert (waketime, myid);
		V(m);
		P(d[myid]);
	}
	
	process Clock {
		start hardware timer;
		while (true) {
			wait for interrupt, then restart hardware timer;
			tod = tod + 1;
			P(m);
			while (tod >= smallest waketime on napQ) {
				int id = id of the smallest waketime no napQ 
				remove (waketime, id) from napQ;
				V(d[id]);
			}
			V(m);
		}
	}
end TimeServer
```

#### 1.4 uma rede de ordenação merge 

RPC é esquisito para filtros ou *interacting peers*

um filtro merge consome dois fluxos de entradas e produz um fluxo de saída, cada entrada já está organizada, a tarefa do filtro é juntar os valores das entradas para produzir uma única saída ordenada

RPC não suporta uma comunicação direta entre processos, 

```c
optype stream = (int); 

module Merge[i = 1 to n]
	op in1 stream, in2 stream;
	op initialize(cap stream);
body
	int v1, v2;
	cap stream out;
	sem empty1 = 1, full1 = 0, empty2 = 1, full2 = 0;
	
	proc initialize(output) {
		out = output;
	}
	
	proc in1(value1) {
		P(empty1); v1 = value1; V(full1);
	}
	
	proc in2(value2) {
		P(empty2), v2 = value2; V(full2);
	}
	
	process M {
		P(full1); P(full2);
		while (v1 != EOS and v2 != EOS)
			if (v1 <= v2)
				{ call out(v1); V(empty1); P(full1);}
			else 
				{ call out(v2); V(empty2); P(full2);}
				
		if (v1 == EOS)
			while (v2 != EOS)
				{ call out(v2); V(empty2); P(full2); }
		else
			while (v1 != EOS)
				{ call out(v1); V(empty1); P(full1);}
		call out(EOS);
	}
end Merge
```

---

### 2. rendezvous

rpc é um mecanismo de comunicação entre módulos

rendezvous combina comunicação e sincronização

um processo clietne chama uma operaçõa por meio de um expressão `call`, porém a aoperação é servida por um processo existente, e NÃO por um processo recem criado (como no RPC)

as operações são servidas uma de cada vez, pois o processo servidor usa uma *input statement* para esperar uma chamada e então agir pra atende-la

#### 2.1 expressões de entrada

suponha um módulo que exporte a operação `op opname(types of formals);`, o processo servidor realiza um rendezvous com a chama de opname executando uma empressão de entrada, a sua forma mais simples é:

>in opname (formal identifiers) -> S; ni

a região entre `in` e `ni` é chamada de **operação guardada**
S é a lista de expressões que serve uma chamada da operação

uma expressão de entrada faz o server esperar até que exista pelo menos uma chamada de *opname* pendente, quando tiver, o processo seleciona a chamada mais antiga, copia os valores de argumentos, executa $S$ e retorna os resultados

em rendezvous, o server é um processo ativo que executa antes e depois de uma chamada remota

$S$ pode ter várias expressões, como em
```
in op1 (formals1) and B1 by e1 -> S1;
[] ...
[] opN (formalsN) and BN by eN -> SN;
ni
```

o **guarda** é a parte antes de '->', cada guarda contém o nome de uma operação e seus formais (expressão de sincronização opcional) que seria o `and Bi` e também uma expressão de escalonamento, que seria `by ei` 

#### 2.2 exemplos de cliente/servidor

##### bounded buffer
deseja-se um processo que tenha um buffer local de $n$ items de dados e que serve duas operações `deposit` e `fetch` 

```c
module BoundedBuffer
	op deposit(typeT);
	op fetch(result typeT);

body
	process Buffer {
		typeT buf[n];
		int front = 0, //primeira posição com item
			 rear = 0, //primeira posição vazia
			 count = 0; //qtd de items produzidos
		while (true) {
			/*
			switch case(op) {
				case deposit:
					
			}
			*/
			in deposit(item) and count < n ->
				buf[rear] = item;
				rear = (rear+1) % n;
				count++;
			[] fetch(item) and count > 0 ->
				item = buf[front];
				front = (front+1) % n;
				count--;
			ni
		}
	}
end BoundedBuffer
```

comparando com a implementação de monitores ([[fig 5.4 book.png]]), os procedimentos de monitores viraram expressões contidas dentro do `in ... ni` 

##### filósofos famintos

```c
module Table
	op getforks(int), relforks(int);
	
body
	process Waiter {
		bool eating[5] = ([5] false);
		while (true) {
			in getforks(i) and (not eating[left(i)] and not eating[right(i)]) -> eating[i] = true;
			[] relforks(i) -> eating[i] = false;
			ni
		}
	}
end Table

process Philosopher[i = 0 to N] {
	while (true) {
		call getforks(i);
		eat;
		call relforks(i);
		think;
	}
}
```

##### time server

```c
module TimeServer
	op get_time(int) returns int;
	op delay(int), tick();

body
	process Timer {
		int tod = 0;
		while (true) {
			// tod++;
			in get_time(time) returns time -> time = tod;
			[] delay(waketime) and waketime <= tod -> skip;
			[] tick() -> {tod++; restart timer;}
			ni
		}
	}
end TimeServer
```

tick() é chamada pelo *clock interrupter handler*

get_time e delay é chamda pelos clientes

##### allocador SJN (Shortest Job Next)
 
```c
module SJN_Allocator
	op request(int time), release();

body
	process SJN {
		bool free = true;
		while (true) {
			in request(time) and free by time -> free = false;
			[] release() -> free = true;
			ni
		}
	}
end SJN_Allocator
```

### merge
```c
optype stream=(int)
module Merge[i=1 to N]
	op in1 stream, in2 stream;
	op initialize(cap stream); // link stream saída
body
	process Filter{
		int v1,v2;
		cap stream out;
		in initialize(c)->out=c; ni
		in in1(v)->v1=v; ni
		in in2(v)->v2=v; ni
		while(v1 != EOS and v2 != EOS)
			if(v1<=v2){
				call out(v1)
				in in1(v)->v1=v; ni
			}
			else{
				call out(v2)
				in in2(v)->v2=v; ni
			}
		if(v1 == EOS){
			while(v2!=EOS){
				call out(v2); 
				in in2(v)->v2=v; ni
			}
		}
		else{
			while(v1!=EOS){
				call out(v1); 
				in in1(v)->v1=v; ni
			}
		}
		call out(EOS);
		end Merge	
```
