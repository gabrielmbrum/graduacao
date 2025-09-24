
algoritmos iterativos são utilizados para computar melhores aproximações a respostas, esses métodos normalmente utilizam estruturas como vetores, iterando sobre todas as suas posições

pensnado na paralelização de processos assim, é importante a sincronização, pois cada iteração depende do resultado das iterações anteriores

```
process Worker[i  = 1 to n] {
	while (true) {
		code to implement task i;
	wait for all n tasks to complete;
	}	
}
```

### 1. contador compartilhado

assuma que tem-se $n$ processos de trabalhadores que precisam se encontrar numa barreira, quando um processo chega na barreira, incrementa $count$ 

```
int count = 0;

process Worker[i  = 1 to n] {
	while (true) {
		code to implement task i;
	< count++; >
	< await (count == n); >
	}	
}
```

count precisa ser resetado para 0 toda vez que todos os processos passam pela barreira
quando atinge-se o limiar $count == n$ precisa-se garantir que ninguém incremente antes de resetar o contador

a solução é ter um coordenador, o trabalhador vai sinalizar que chegou `arrive[i] = 1` e vai ficar esperando `await(continue[i] == n)` 

o array continue fica de responsabilidade do coordenador, que setará como 1 toda as posições assim que todos os trabalhadores tiverem chego

### 2 flags e coordenadores

variáveis flags: *arrive* e *continue* são exemplo delas

**princípios de flags**
- o processo que espera pela flag de sincronização é quem deveria limpar ela
- uma flag não deve ser setada até que saiba que foi limpa

```c
process Worker[i=1 to N] {
	while (true) {
		...
		arrive[i] = 1;
		<await(continue[i]==1);>
		continue[i] = 0;
	}
}

process Coordinator {
	while (true) {
		for (j = 1; j <= N; j++)
			<await(arrive[j]==0) arrive[j] = 0;>
			
		for (j = 1; j <= N; j++)
			continue[j]=1;
	}
}
```

**contras** dessa implementação
- requer um processo extra
- sincronização por espera-ocupada é não desejada (o processador que faz o papel de coordenador seria melhor utilizado por outro trabalhador)

#### 2.1 combinando barreiras com árvores

a solução é transformar o trabalhador em um coordenador também, organizando os trabalhadores em uma árvore

um nó trabalhador espera seus filhos chegarem, então avisa os nós pais que ele chegou

quando a raiza aprende que seus filhos chegaram, ela sabe que todos os trabalhadores chegarem e pode dizer pros seus filhos continuarem

![[fig 3.13.png]]

![[fig 3.14.png]]

é mais eficiente que a implementação anterior para grandes $n$, pois a altura é proporcional a $log_{2}^{n}$  
### 3. barreiras simétricas

todos os processos executam o mesmo algoritmo, cada um em seu próprio processador, assim, a chegada na barreira é sincronizada

uma barreira simétrica para n-processos é criada a partide de barreiras de dois-processos

por exemplo, deixemos cada processo ter uma flag que seta quando chega na barreira, então espera que outro processo sete a flag e limpe a flag do outro

considerando W[i] e W[j] dois processos
```c
/* barreira para o trabalhador W[i]*/
<await (arrive[i] == 0);>
arrive[i] = 1;
<await (arrive[j] == 1); >
arrive[j] = 0;

/* barreira para o trabalhador W[j] */
<await (arrive[j] == 0);>
arrive[j] = 1;
<await (arrive[i] == 1); >
arrive[i] = 0;
```

#### 3.1 barreira de borboleta

se $n$ é potência de 2 pode-se utilizá-la

![[fig 3.15.png]]

na etapa $s$ o trabalhador sincroniza com um trabalhador numa distância de $2^{s-1}$ 

##### exemplo de problema

utilizando apenas uma flag pro processo pode ocorrer o seguinte:
1. processo 1 chega no primeiro estagio e seta a flag arrive[1] 
2. processo 2 não chegou ainda
3. processo 3 e 3 chegaram no primeiro estágio, set e espera pelas flags um dos outros, limpa eles e continua pro segunda estagio
4. no segundo estágio, 3 <-> 1, como 1 ja chegou, processo 3 continua pro terceiro estagio

**problema** -> alguns processos saem antes da barreira e outros esperam pra sempre pra chegar no próximo estágio (isto tb ocorrre com o item 3.2)

```
// barrier code for worker process i
for [s = 1 to num_stages] {
	arrive[i] = arrive[i] + 1;
	// determine neighbor j for stage s
	while (arrive[j] < arrive[i]) skip;
}
```


#### 3.2 barreira de disseminação


![[fig 3.16.png]]

```c
BARREIRA_SIMETRICA:
	// solução errada
	for (num = 1 to num_estagios) {
		j = para_quem_envio(i, num);
		V(s[i]);
		P(s[j]);
	}

	// solução correta
	for (s = 1 to num_estagios) {
		j = para_quem_envio(i, s);
		V(s[i][s])
		P(s[j][s])
	}
```