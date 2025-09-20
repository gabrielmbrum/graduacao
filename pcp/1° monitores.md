
dado um monitor X, só existe uma entrada para o monitor, logo, só um processo consegue acessar o monitor por vez (uma requisição por vez)

dentro do monitor existem *N* funções

### qual é a sintaxe?

> ref.: livro do andrews

```pseudoaleardo
monitor mname {
	- declaração de variáveis permanentes
	- comandos de inicialização
	- procedimentos do monitor
}
```

### características

apenas os **nomes** dos procedimentos são visíveis externamente

comandos de inicialização e dos procedimentos não podem acessar variáveis externas ao monitor

variáveis permanentes são inicializadas antes de executar a primeira chamada ao monitor

os procedimentos do monitor são chamados assim: `call mname.opname(args)`

> 17996675069 me liga bb

por definição, procedimentos são executados em exclusão mútua, obtida implicitamente na implementação do TAD (Tipo Abstrato de Dados) monitor

### funções implícitas 

interações entre processos, providas pelo monitor, são controladasd por meio de <u>variáveis condicionais</u>, acessadas por funções específicas

declaração de variável condicional: `cond cv;`

funções sobre variáveis condicionais:
```c
empty(cv);            // retorna zero se existe processo esperando cv
wait(cv);             // bloqueia processo faz a chamada, liberando o acesso
																  ao monitor

wait(cv, rank);       // bloqueia o processo, usando o valor de rank para 
															inserir na fila

signal(cv);          // libera processo na frente da fila de cv

signal_all(cv);      // libera todos os processo na fila de cv

minrank(cv);         // retorna o rank do processo na frente da fila
```

### políticas de liberação (*signal*)

***Signal and Continue (SC)***
- o procedimento que fez a chamada continua a ser executado (processo não sofre preempção - troca de proc. na CPU feita pelo SO)

***Signal and Wait (SW)***
- o procedimento que fez a chamada cede a execução para o processo que foi liberado

### exemplo: implementação das primitivas de semáforo usando monitores

```
// implementação boa para política SW

monitor Semaphore{
	int s = 0;
	cond pos;
	
	procedure Psem(){
		while(s == 0)
			wait(pos);
		s = s - 1;
	}
	
	procedure Vsem(){
		s = s + 1;
		signal(pos);
	}
}
```

esta solução, apesar de correta, não garante o melhor atendimento numa política SC. para também obter isso podemos modificar o monitor para:
```
monitor FIFOSemaphore{
	int s = 0;
	cond pos;
	
	procedure Psem(){
		if (s == 0)
			wait(pos);
		else
			s = s - 1;
	}
	
	procedure Vsem(){
		if (empty(pos))
			s = s + 1;
		else
			signal(pos);
	}
}
```

