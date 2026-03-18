### agentes

![[Pasted image 20260315212130.png]]

agente humano
- sensores: olhes, ouvidos...
- atuadores: mãos, pés, boca...

agente robo
- sensores: câmeras, localizadores, infravermelhos...
- atuadores: motores, engrenagens, sintetizadores de voz...

### agentes racionais

o que é?
- quando é capaz de realizar "o correto" para atingir o objetivo
- no contexto de IA, fazer a coisa certa é ter sucesso em uma tarefa
- ex.: avaliação do sucesso de melhor caminho
	- caminho A é mais curto, porem congestionado
	- caminho B é médio, normalmente livre
	- caminho C é longo, mas livre
	- ter sucesso seria se o agente, com o tempo, escolhesse o caminho que minimiza o tempo médio para o caminho

função utilidade (U)
- um agente racional é aquele que realiza ações que maximizam sua função utilidade
- função utilidadedescreve os objetivos do agente
- exemplos
	- sistemas de recomendação
		- U = relevância x probabilidade
		- objetivo é maximizar a satisfação do usuário
	
	- chatbots
		- U = Relevância da resposta - Tempo de processamento
		- objetivo é fornecer respostas precisas e rápidas

	- modelos de aprendizado de máquina
		- U = -Erro
		- objetivo é maximizar o negativo do erro de predição do modelo

pac-man
- diante de um objetivo a ser alcançado, um agente deve buscar um plano para atinigir seu objetivo
- **plano:** é uma sequência de ações que o agente deve executar para que ele alcance seu objetivo
- **problema de busca:** problema em que um agente precisa encontrar um plano que leva de um estado inicial para um estado objetivo
- ![[Pasted image 20260315213843.png]]

espaço de estados
- conjunto de todos os possíveis estados que podem ocorrer na resolução do problema
- ![[Pasted image 20260315214011.png]]
- espaço de estados formam um grafo direcionado, em que
	- estados são nós
	- arestas são ações
- ![[Pasted image 20260315214619.png]]
- 

conjunto de ações
- no pacman, ações = {"up", "down", "left", "right"}
- as ações podem ter custos, ou não

teste de objetivo
- chegou no estado objetivo?
	- se não, continua
	- se sim, para

árvore de busca
- ED em que cada nó tem um elemento do espaço de estados e a raiz é o estado inicial
- nós filhos são geardos pelas ações em estados pais
- cada aresta representa uma ação

nós x estados
- estado: é uma representação de uma configuração específica do sistema "agente-ambiente"
- nó: inclui estado, nó pai, ação e custo do caminho

estratégias de busca
- são algoritmos para buscar um plano, a partir da formulação de um problema de busca
- **ideia geral**
	- percorrer o espaço de estados com o auxílio de uma árvore de busca
	- durante a execução, a árvore de busca vai sendo expandida gradativamente
	- expandir => aplicar o modelo de transição para gerar novos nós
	
- **froteira/borda:** conjunto de nós folha disponíveis para expansão em um dado momento
- **busca:** seguir um caminho, guardando os outros para tentar depois
















