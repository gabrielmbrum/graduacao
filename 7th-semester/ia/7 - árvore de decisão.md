### árvores de decisão
- AD é um algoritmo de aprendizado de máquina superviosionado
- fáceis de serem implementadas e versáteis
- exemplos na literatura: CART (Classificaiton and Regression Trees)
- estratégia de "dividir e conquistar", particionando o espaço de atributos em regiões menores
- a ideia é decompor um problema complexo em sub-problemas
- recursivamente, a mesma estratégia é aplicada a cada sub-problema

### exemplo - base "Iris"
![[Pasted image 20260424125005.png]]
![[Pasted image 20260424125014.png]]

### nomenclatura
1. **Nó raiz**: é o nó de partida, contém uma decisão/teste para o atributo de maior importância para a primeira divisão dos dados
2. **Nó de decisão:** são os nós internos da árvore, eles contém um teste/decisão para um atributo
3. **Nó folha:** são os nós terminais da árvore, que representam as classes de saída ou as previsões finais do modelo
4. ![[Pasted image 20260424125225.png]]

### propriedades
- cada nó de decisão contém um teste em um atributo
- cada nó folha contém uma classe
- para cada valor de corte de um atributo, existe um ramo para outra sub-árvore
- cada percurso corresponde à uma regra específica de classificação

### algoritmo

**ideia do algoritmo**
1. selecionar um atributo $x_i$ 
2. adicionar ramos a partir do atributo $x_i$ e do valor de corte $a_i$ 
3. passar as instâncias de treinamento para as folhas
4. para cada folha
	1. se todas as instâncias são da mesma classe, associar essa classe à folha
	2. se não, repetir os passos 1 ~ 4

>como selecionar o melhor atributo?

**escolha do melhor atributo**
- exemplo
	- ![[Pasted image 20260424125945.png]]
	- ![[Pasted image 20260424130058.png]]
	- como medir a capacidade de segmentação do atributo?
		- uma divisão que preserve as proporções de classes entre os ramos **não** é desejável
		- uma divisão em que cada ramo todas as instâncias são da mesma classe tem **utilidade máxima**
		- a ideia é aplicar uma medida de qualidade para avaliar o poder discriminatório de um dado atributo

### medidas em árvore de decisão

- medidas são calculadas nos dados de treinamento
- medidas clássicas da literatura
	1. **coeficiente de gini:** mede a probabilidade de uma amostra ser incorretamente classificada antes vs depois da divisão
	2. **ganho de informação:** avaliar a entropia antes e depois da divisão dos dados
	
- **coeficiente de gini
	- medida de impureza
	- máxima se as classes estão perfeitamente misturadas
	- mínima se for perfeitamente pura
	- ![[Pasted image 20260424131420.png]]
	- notação -> S:[9+, 5-] significa que o conjunto S de entrada é formado por 14 instâncias, sendo 9 instâncias da classe positiva (+) e 5 da negativa (-)
	- $Gini(S) = 1 - \sum_{j=1}^{c}P_{j}^2 = 1 - (\frac{5}{14}) +(\frac{9}{14}) = 0.7142$ 
	
- **ganho de informação**
	- **entropia**
		- entropia é a medida que avaliar desordem, isto é, mede nível de incerteza de um conjunto de dados
			- entropia alta: conjunto de dados é mais imprevisível ou misturado, com maior incerteza
			- entropia baixa: conjunto de dados mais homogêneo, mais certeza
			
		- seja S o subconjunto de instâncias de treinamento
		- P(x) é a proporção de exemplos da classe x em S
			- se P(x) = 0 ou 1, então é mínima
			- se P(x) = 0,5, então é máxima
		- $Entropia = H(S) = -P(+)log_2 P(+) - P(-)log_2 P(-)$
		- $H([9+, 5-]) = -(\frac{9}{14})log_2(\frac{9}{14}) - (\frac{5}{14})log_2(\frac{5}{14}) = 0.94$
		- multiclasse
			- $H(S) = - \sum_{i=1}^{c} P_i log_2 P_i$ 
			- ![[Pasted image 20260424134223.png]]
		
	- **fórmula de ganho de informação**
		- mede a redução da entropia causada pelo particionamento das instâncias mediante os atributos e suas categorias (quanto maior, melhor)
		- mede a diferença entre a entropia antes e a entropia depois da divisão referente ao atributo A
		- ![[Pasted image 20260424134515.png]]

### aplicação das medidas

- exemplo de uso do IG para variáveis categóricas
- ![[Pasted image 20260424141456.png]]
- ![[Pasted image 20260424141533.png]]
- ![[Pasted image 20260424141548.png]]
- ![[Pasted image 20260424141558.png]]
- ![[Pasted image 20260424141649.png]]
- ![[Pasted image 20260424141708.png]]
- ![[Pasted image 20260424142312.png]]

#### IG para variáveis numéricas
- diferente dos atributos categóricos, variáveis numéricas necessitam de um **ponto de corte** (threshold)
- partição binária nos dados
	- instância que tem atributo < ponto de referência
	- instância que tem atributo >= ponto de referência
	
- para escolher o ponto de corte do atributo, procede-se da seguinte forma
	1. ordena as instâncias por odem crescente dos valores do atributo numérico
	2. qualquer ponto intermediário no conjunto de treinamento pode ser usado como possível ponto de referência
- exemplo
	- ![[Pasted image 20260424143922.png]]
	- ![[Pasted image 20260424143935.png]]
	- ![[Pasted image 20260424144046.png]]

### critério de parada na divisão
- se todas as instâncias pertencem a mesma classe, então situação ideal
- precisa-se decidir entre
	- quando aceitamos um novo ramo, ou
	- inserimos um nó folha definitivo
- duas estratégias
	1. parar o crescimento da árvore mais cedo (*pré-pruning*)
	2. construir uma árvore completa e, em seguida, podar a árvore (*pós-tuning*)

- **pós-pruning**
	- percore a árovre em profundidade para cada nó de decisão e calcula
		- o erro do nó (ex.: proporção de previsões incorretas)
		- a soma dos erros de seus nós descendentes
	- critério de pruning
		- se o erro do nó for <= soma dos erros de todos os nós descendentes, então
			- este nó pode ser transformado em um nó-folha atribuindo a classe majoritária dos exemplos que chegam até ele
			- todos os nós descendentes são truncados
		
	- algoritmo básico de pós-pruning
		- erro na classificação (erro de Laplace)
		- $E(S) = (N - n + k - 1) / (N + k)$
			- S: conjunto de instâncias retidas no nó em análilse
			- N: n° de instâncias em S
			- n: das N instâncias em S, quantoas fazem parte da classe majoritária em S
			- k: n° de classes
	- ![[Pasted image 20260424145937.png]]
	- ![[Pasted image 20260424145954.png]]
	- 

