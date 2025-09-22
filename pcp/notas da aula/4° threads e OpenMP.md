
### threads

são processos que executam sem a carga de gerenciamento normal.
permite a construção de programas paralelos, mesmo em uma única máquina.

uso de threads
```c
#include <pthread.h>

pthread_attr_t atrib; 
pthread_t ident; // descritor do thread

pthread_attr_init(atrib);

/*
o escopo pode ser:
	SYSTEM -> disputa com todos os threads do sistema
	PROCESS -> disputa apenas com threads do mesmo processo
*/
pthread_attr_setscope(&atrib, PTHREAD_SCOPE_SYSTEM);

/*
	retorna 0 se a criação for bem sucedida
*/
pthread_create(&ident, &atrib, start_func, arg..);

pthread_exit(atrib);
// pthread_join(ident, ptr_valor); # espera outra thread terminar
```

a thread pode ser vista como uma função, se diferenciando pelo tratamento recebido pelo SO

entram em atividade pela execução de *pthread_create* e podem se comunicar e controlar sua execução por primitivas próprias

*pthread_exit(valor)* é a forma amigável e sinalizada, em que valor é um ponteiro para o retorno de algum valor ao processo pai

*pthread_join(ident, ptr_valor)* faz o processo pai esperar pelo processo de seu filho

### semáforos

```c
sem_t mutex; // declara o semáforo mutex

/*
	faz mutex = 1
*/
sem_init(&mutex, SHARED, 1);

// P(mutex) (bloqueia se mutex == 0 || libera e faz mutex-- caso mutex>0)
sem_wait(&mutex);
 
// V(mutex) (faz mutex++ e libera algum processo bloqueado)
sem_post(&mutex);
```

---

### OpenMP

##### introdução

é uma API portável para threads em sistemas multiprocessadores de memória compartilhada

padroniza paralelismo em grão fino (laços) -> "dividir $x$ laço em $n$ threads"

suporta também algoritmos de grão grosso

não faz paralelização automática

#### modelo de uso em C

```c
main() {
#pragma omp parallel for 

	shared(A); //A é o vetor compartilhado
	private(i);
	
	for (i = 1, i <= 12, i++) {
		...
	}
}
```

#### modelo de paralelização

programa OpenMP começa com uma thread sequencial

para criar novos threads o usuário define uma região paralela
- threads trabalhadores são disparados
- metstre é parte dos trheads
- threads saem ao final da região paralela
- modelo fork-join 

#### criação de threads

```c
#pragma omp parallel
{
	//code to be executed by each thread
}
```

a diretiva *parallel* pode receber cláusulas de execução, as quais podem definir o número de threads ou quais variáveis serão compartilahdas entre threads

```c
#pragma omp parallel num_threads (quantity)
{
	//code to be ececuted by each thread
}

#pragma omp parallel shared(A) private(i) 
{
	// code to be executed by each thread
}
```

#### variáveis nos threads

OpenMP trabalha com memória compartilahda, logo todas as threads vão acessar a mesma memória

pode-se criar áreas de memória privativas

podem ter valor inicial comum (firstprivate) ou valor final comum (lastprivate)

#### exclusão mútua

pode ser implementada de duas formas
- região crítica
- execução atômica

**região crítica**

podem ser nomeadas e esses nomes são globais (não podem conflitar com nomes de funções/entidades)
```c
#pragma omp parallel
{
	...
	#pragma omp critical(left)
	A[i] += Alocal
	...
}
```

**execução atômica**

não são estruturáveis

é aplicada apenas ao comando seguinte

otmizam a exclusão mútua (se o hardware permitir)

```c
#pragma omp parallel
{
	...
	#pragma omp atomic
	A[i] += Alocal
	...
}
```

#### outros elementos

**execução sequencial**

utilizada para o controle de laços de repetição

além da exclusão mútua, obriga a execução sequencial do laço

```
#pragma omp parallel
{
	...
	#pragma omp ordered
	printf("%d\n", i);
	...
}
```

**barreira de sincronismo**

therads esperam chegada de todos

barreira implícita ao final de cada região paralela

```c
#pragma omp parallel
{
	...
	#pragma omp barrier
	...
}
```

**laços de repetição**

diretiva *do* (*for* em C)

deve estar dentro de um trecho paralelo, divide as iterações entre os threads

pode ser estático, dinamico ou runtime

```c
#pragma omp parallel shared(a,b,c,chunk) private(i)
{
	#pragma omp for schedule(dynamic, chunk) nowait
	for (i=0; i < N; i++)
		c[i] = a[i] + b[i];
} 
```

**atributo *schedule***

escalonamento estático 
- divisão sequencial entre as threads (não tem parâmetros)
	- vetor.size = 10 e n = 5
	- T1 fica com 0, 1
	- T2 fica com 2, 3
	- ...
	- T5 fica com 8, 9
- divisão por chunk (possui 1 parâmetro)
	- (static, $x$) -> x é o tanto de iterações para cada thread
	- divide tamanhos fixos menores
	- deixa em ordem as threads

escalonamento dinâmico
- (dynamic, $x$)
	- ao terminar já pega outra região para trabalhar
	- é um estático por chunk sem ordenação
	- entrega $x$ iterações para cada thread

- (guided, $x$)
	- evita troca de informação com muita frequência (a troca de informaçõa é informar à thread o que ele deve fazer)
	- "começa de sola, entrega varias coisas pro primeiro, e vai diminuindo a carga pra cada thread na esperança de que consiga terminar logo as iterações"

- runtime
	- ele decide em tempo de execução

**primitiva section**

```c
// isto está dentro de um parallel

#pragma omp sections nowait
{
	#pragma omp section
		do_a_section
	#pragma omp section
		do_another_section
}
```

**diretiva master**

trecho executado apenas pelo thread principal

```c
#pragma omp parallel
{
	...
	#pragma omp master
	printf("so o principal executa");
	...
}
```

**diretiva single**

```c
#pragma omp parallel
{
	...
	#pragma omp single
	printf("o primeiro a chegar faz, de resto tmj sextou bb");
	...
}
```

**diretiva task**

é a forma de criar seções sem ter que conhecer antecipadamente quanas seções serão necessárias, nem quais threads executarão

```c
#pragma omp parallel default(none)
{
	...
	#pragma omp task
	printf("gera isso e entrega pra outro thread");
	
	#prgama omp task
	printf("gera isso e entrega pra outro thread");
	...
}
```
#### exemplo

`src/hello.c` -> faz um hello world com threads

`src/trap.c` -> calcula área de determinada função pelos trapézios aproximados