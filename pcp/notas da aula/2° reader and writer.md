### assuntos da aula
- await
- semáforos
- monitor
### comando *await*

utilizado para abstrair condições de exclusão mútuae sincronismo, ele não existe de fato em alguma linguagem de programação, é apenas uma abstração.
em sua forma mais simples temos:

`<S;>` => indica que S é executado de modo exclusivo

temos também a forma que indica sincronismo simples:

`<await(B);>`=> indica que o próximo comando será executado quando B for verdade 

temos finalmente, a combinação, dada por:

`<await(B) S;>`-

### *múltiplos leitores e escritores*

```c
int nr = 0;
sem rw = 1;

process Writer[j=1 to N] {
	while (true) {
		...
		
		P(rw);
		escreve;
		V(rw);
	}
}

process Reader [i=1 to M] {
	while (true) {
		...
		
		<	nr = nr + 1;
			if (nr == 1) P(rw); >
		leitura;
		<   nr = nr - 1;
		    if (nr == 0) V(rw); >	
	}
}
```

como await é uma abstração, precisamos implementá-lo de alguma forma, neste caso usaremos semáforos

```c
int nr = 0;
sem rw = 1;
sem mutex = 1;

process Writer[j=1 to N] {
	while (true) {
		...
		
		P(rw);
		escreve;
		V(rw);
	}
}

process Reader [i=1 to M] {
	while (true) {
		...
		
		P(mutex);
		nr = nr + 1;
		if (nr == 1) P(rw);
		V(mutex);
		
		leitura;
		
		P(mutex)
		nr = nr - 1;
		if (nr == 0) V(rw);
		V(mutex);
	}
}
```

esta solução possui o problema de **starvation** (writer fica de xereca kk)
então, quando um escritor quer escrever, não entra mais leitores

```c
int nr = 0, nw = 0, dr = 0, dw = 0;
sem e = 1, r = 0, w = 0;

process Writer[j = 1 to N] {
	while (true) {
		<	await (nr == 0 and nw == 0)
			nw = nw + 1; >
		escreve;
		<   nw = nw - 1;
			SIGNAL; >
	}
}

process Reader[i = 1 to M] {
	while (true) {
		<   await (nw == 0) nr = nr + 1; >
		leitura;
		<   nr = nr - 1;
			SIGNAL; >		
    }
}

SIGNAL:
	if(nw == 0 and dr > 0) {
		dr = dr - 1; 
		V(r);
	}
	else if (nr == 0 and nw == 0 and dw > 0) {
		dw = dw - 1;
		V(w);
	}
	else {
		V(e);
	}
```

não se pode utilizar apenas um mutex no reader (como foi feito anteriormente), pois precisa-se ter um mutex para entrada de leitores e outro para saída de leitores, pois se usasse o mesmo, caso ficasse um leitor esperando pois houve solicitação de escrita, não seria possível liberar os leitores que já estavam lendo, pois o mutex estaria com o leitor que foi bloqueado na entrada

logo, a solução é esta:
```c
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

ai que não sei oq não sei oq lá, linha pra cacete e bla bla bla

simplesmente
**receba**
os
**monitores**

```
monitor RW_Controller{
	int nr = 0, nw = 0;
	cond OK to read, OK to write;
	
	procedure request_read() {
			while (nw > 0)
				wait(OK to read);
			nr = nr + 1;
	}
	
	procedure release_read() {
		nr = nr - 1;
		if (nr == 0) signal(OK to write);	
	}
	
	procedure request_write() {
		while (nr > 0 || nw > 0)
			wait(OK to write);
		nw = nw + 1;	
	}

	procedure release_write() {
		nw = nw - 1;
		signal(OK to write);
		signal_all(OK to read);
	}
}
```

esta solução ainda está com starvation, porém é bem mais simples a adaptação do que com semáforos

dependendo da política, SC ou SW, as coisas mudam...