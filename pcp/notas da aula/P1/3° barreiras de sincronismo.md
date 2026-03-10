
#### primeira solução
```c
process Worker[i=1 to N] {
	while (true) {
		...
		<arrive++;>
		<await(arrive == N);>
	}
}
```

acima temos uma solução simples e ruim, pois, primeiramente tem o problema de que o arrive não é resetado, ent, caso chegue algum processo que faça arrive chegar a N+1, nunca saíra mais do await todos os processos

#### solução com coordenador

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

**hotspot:** área com muito acesso e concorrência, esta segunda solução retira o hotspot da primeira (que ocorria na variável arrive)

#### princípio de sincronização por flags

> problema da última solução: "quem sinaliza, não é quem limpa"

- o processo que espera por uma flag é o processo que deve "limpar" essa flag
- uma flag não pode ser sinalizada se não tiver sido limpa antes

#### solução com barreira em árvore

```c
// se inicializa todas as flags como zero
process Worker[i=1 to N] {
	while (true) {
		...
		BARREIRA
	}
}

processo folha
	BARREIRA:
		arrive[i] = 1;
		<await(continue[i]==1) continue[i] = 0;>

processo raiz
	BARREIRA:
		<await(arrive[esq]==1) arrive[esq] = 0;>
		<await(arrive[dir]==1) arrive[dir] = 0;>
		continue[esq]=1;
		continue[dir]=1;

processo intermediario
	BARREIRA:
		<await(arrive[esq]==1) arrive[esq] = 0;>
		<await(arrive[dir]==1) arrive[dir] = 0;>
		arrive[i]=1;
		<await(continue[i]==1) continue[i]=0;>
		continue[esq]=1;
		continue[dir]=1;

```

#### solução com barreira simétricas

- barreira borboleta
- barreira por dissemincação

#### barreira borboleta

![[barreiraborboleta.png]]

```c
// código da barreira borboleta

BARREIRA_BORBOLETA:
	for (s = 1 to num_estagios) {
		arrive[i] = arrive[i] + 1;
		// determina vizinho 'j'
		while (arrive[j] < arrive[i]) skip;
	}
```

#### barreira por disseminação

![[barreirasimetrica.png]]

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
