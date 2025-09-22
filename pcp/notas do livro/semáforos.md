### 1. sintaxe e semântica

um semáforo é um tipo especial de uma variável compartilhada que é manipulado por duas operações atômicas, *P* e *V*

o valor do semáforo é *não negativo*

*V* -> usado para sinalizar a ocorrência de um evento, incrementa o semáforo

*P* -> usado para atrasar um processo até que certo evento ocorra, espera até que o semáforo seja positivo para então decrementar dele

declaração
```
// o valor inicial padrão é 0
sem s; 

sem lock = 1; // inicializado com 1

sem forrks[5] = ([5] 1);
```

**P(s): <await (s > 0) s = s - 1;>
V(s): <s = s + 1>**

### 2. problemas e técnicas básicos

semáforos suportam a implementação de exclusão mútua, em regiões críticas, e também de sincronização condicional, então podem ser utilizados em vários problemas

#### 2.1 região crítica: exclusão mútua

![[fig 4.1 book.png]]

#### 2.3 produtor e consumidor: semáforos binários divididos

sem estoque
- empty e full são semáforos binários
- os dois nunca são igual a 1 ao mesmo tempo

```c
// sem estoque
sem oktoconsume = 0, oktoproduce = 1;

process Consumer() {
	while (true) {
		P(oktoconsume);
		consume();
		V(oktoproduce);
	}
}

process Producer() {
	while (true) {
		P(oktoproduce);
		produz();
		V(oktoconsume);
	}
}

// com estoque de N produtos
sem pode_produzir = 10, pode_consumir = 0;

process Producer() {
	while (true) {
		P(pode_produzir);
		produz();
		V(pode_consumir);
	}
}

process Consumer() {
	while (true) {
		P(pode_consumir);
		consome;
		V(pode_produzir);
	}
}
```

#### 2.4 bounded buffers: contando recursos

seguindo o exemplo anterior, utilizar um buffer para armazenar mais itens produzidos aumenta a performance

um *bounded buffer* é um buffer de comunicação com vários slots

definições
- buf[n] -> buffer com n posições
- front -> index da mensagem da frente da fila
- rear -> index do primeiro slot vazio 

![[fig 4.4 book.png]]

o código acima não protege contra or risco de dois produtores depositarem seus dados na mesma posição, assim sobreescrevendo dados (o mesmo ocorre para os consumidores)

a solução é criar um mutex para cada processo:
![[fig 4.5.png]]

### 4. readers and writers

```
int nr = 0, nw = 0, dr = 0, dw = 0;

// dr = delayed reader || dw = delayed writer

sem e = 1, r = 0, w = 0;

process Writer[j=1 to N] {
	while(true) {
		P(e);
		if (nr > 0 or nw > 0) {
			dw = dw + 1;
			V(e);
			P(e);
		}
		nw = nw + 1;
		V(e);

		escreve;

		P(e);
		nw = nw - 1;
		if (dr > 0) {
			dr = dr - 1;
			V(r);
		}
		else if (dw > 0) {
			dw = dw - 1;
			V(w);
		}
		else
			V(e);
	}
}

process Reader[i=1 to M] {
	while (true) {
		P(e);
		if (nw > 0) {
			dr = dr + 1;
			V(e);
			P(r);
		}
		nr = nr + 1;
		if (dr > 0) {
			dr = dr - 1;
			V(r);
		}
		else {
			V(e);
		}

		leitura;

		P(e);
		nr = nr - 1;
		if (nr == 0 and dw > 0) {
			dw = dw - 1;
			V(w);
		}
		else {
			V(e);
		}
	}
}
```

com monitores é bem mais simples, a implementação está aqui -> [[monitores]]
