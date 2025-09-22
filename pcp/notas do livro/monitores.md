
### 0. intro

monitores são módulos de programas que proporciona mais estruturas do que semáforos 

monitores são mecanismos de abstração de dados

um monitor contém variáveis que armazenam estados de objetos e procedimentos que implementam operações no objeto

**exclusão mútua** é adquirida implicitamente, pela garantia de que os procedimentos no mesmo monitor não são executados concorrentemente

exisrtem dois tipos de módulos: processos ativos e monitores pacivos

assume-se todas as variáveis dentro dos monitores, logo dois processos interagem no mesmo monitor

essa modularização traz dois benefícios:
1. um processo que chama um procedimento de monitor pode ignorar como o procedimento é implementado
2. o programador do monitor pode ignorar como ou onde os procedimentos do monitor são usados e pode mudar a implementação do monitor 

esses benfícios permitem um design individual para cada monitor, facilitando o desenvolvimento e compreensão de tal

### 1. sintaxe e semântica

um monitor tem uma interface (especifíca os métodos) e um corpo (contém as variáveis que representam o estado dos recursos e procedimentos)

declaração assumida
```
monitor mname {
	declarations of permanent variables
	initilization statements
	procedures
}
```

procedures -> implementam as operações visíveis
perm var -> compartilhadas por todos os procedimentos dentro do corpo do monitor

##### propriedades

**1° propriedade**

como somente os procedimentos são visíveis externamente, para alterar os estados das variáveis permanentes, uma chamada a um procedimento tem que ser feita, a sintaxe é:

>call mname.opname(arguments)

opname é o nome da operação

**2° propriedade**

declarações dentro do monitor (declarção de inicialização e internas aos procedimentos) podem não acessar variáveis declaradas fora do monitor

**3° propriedade **

variáveis permanentes são inicializadas antes de que qualquer procedimento ser chamado, logo, a inicialização é feita assim que o monitor é criado

##### atributos

um monitor pode ser desenvolvido em um isolamento relativo, o programador não sabe a ordem que os procedimentos serão chamados, logo não se pode desenvolver algo que dependa da ordem de execução

um monitor invariante é um predicato que especifica estados razoáveis para as variáveis permanentes quando nenhum processo está acessando elas (um código de inicializaçaõ precisa definir um invariante)


#### 1.1 exclusão mútua

a exclusão mútua em monitores é gerada implicitamente e sincronização condiionalç é programada por variávies de condições

`processo`
- um processo de um montor é chamado por um processo externo
- ele é ativo caso algum processo esteja executando um procedimento
- no máximo uma instância de monitor está ativa por vez 

#### 1.2 variáveis de condição

é utilizada para atrasar um processo que não pode continuar a executar seguramente, e também para acordar um processo atrasado quando a condição for verdadeira. declaração:

>cond cv;

podem ser declaradas e utilizadas dentro de monitores

o valor de tal é uma fila de processos atrasados, inicialmente é vazia 

pode-se checar o estado de uma variável de condição

>empty(cv);                                        // T -> fila 'cv' vazia

um processo é bloqueado em uma variável de condição por:

>wait(cv);                                         // o processo em execução vai pra o final da fila cv

processos bloqueados são acordados pela seguinte chamada:

>signal(cv);                                      

`wait()` e `signal()` trabalham com FIFO

#### 1.3 regras de sinalização

quando um processo executa um `signal()`, ele tem o controle do lock implicitamente associado ao monitor, logo, ele pode decidir se quem segue com a execução é ele mesmo OU o processo acordado

*Signal and Continue (SC)*: o sinalizador continua e o processo acordado é executado depois

*Signal and Wait (SW)*: o sinalizador aguarda e o processo acordado é executado

SC é não-preemptivo e SW é preemptivo

![[figure5.1 book.png]]

**implementação de um semáforo**

![[figure 5.2 book.png]]

o inteiro $s$ representa o valor do semáforo

$Psem$ -> espera até que $s$ seja positivo, então decrementa de $s$ 
o loop $while$ faz esparar na variável de condição $pos$ se $s$ é 0

$Vsem$ -> incrementa no valor de $s$ e sinaliza $pos$ 

*problema com SC* 

o processo acordado precisa checar novamente se $s$ continua positivo, algum outro processo esperando na fila de entrada e executou $Psem$ antes e decrementou $s$, então o FIFO não é respeitado para SC

**semáforo com *condição de passagem***

muda-se a antiga para que:
1. funcione corretamente para SC e SW
2. não utilize um loop while
3. implemente um semáforo com FIFO

>quando faz um Vsem, se há um processo esperando, sinaliza na variável de condição mas NÃO incrementa o semáforo, caso contrário, pode incrementar

![[fig 5.3 livro.png]]

*exemplo*
ini -> s = 1

P1 -> Psem -> s = s - 1 -> s = 0

P2 -> Psem -> wait (pos)

P1 -> Vsem -> singal(pos)

P3 -> Psem -> wait(pos) {ele fica depois do P2 na fila}

P4 -> Psem -> wait(pos)

P2 -> awakened -> faz oq precisa -> V(sem)

### 2. técnicas de sincronização

#### 2.1 bounded buffers: sincronização de condição básica

dois processos -> produtor e consumidor
eles se comunicam compartilhando um buffer com $n$ slots, este contém uma fila de mensagens

o produtor envia no uma mensagem para o consumidor no final da fila
o consumidor recebe a mensagem procurando a mensagem na frente da fila

a sincronização proíbe um depósito em uma fila cheia e uma busca em fila vazia

![[fig 5.4 book.png]]

#### 2.2 readers and writers: broadcast signal

escritores precisam de acesso exclusivo

**signal_all(cond)**
essa função sinaliza a todos que esperavam a condicional 

```
monitor RW_Controller () {

	int nr = nw = 0;
	cond oktoread, oktowrite;
	
	procedure request_read() {
		while (nw > 0) await(oktoread);
		nr++;
	}
	
	procedure request_write() {
		while (nr > 0 || nw > 0) await(oktowrite);
		nw++;
	}
	
	procedure release_read() {
		nr--;
		if (nr == 0) signal(oktowrite);
	}
	
	procedure release_write() {
		nw = nw - 1;
		signal(oktowrite);
		signal_all(oktoread);
	}

}
```

#### 2.3 Shortest-Job-Next Allocation: priority way

**wait(cv, rank)**
atrasa processos em uma ordem ascendente ao rank (do menor pro maior)
![[fig 5.6 book.png]]


