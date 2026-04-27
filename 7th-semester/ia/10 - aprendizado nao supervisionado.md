
### agrupamento de dados
- **técnicas de agrupamento** (*clustering*)
	- encontram um conjunto de cluster (grupos) dentro dos dados  
	
- instâncias que pertencem à um mesmo cluster compartilham características similares em termos de certos aspectos específicos, atributos, ou critérios
- **objetivo:** dado um conjunto de dados, agrupar seus elementos em clusters a partir da escolha de um **critério de similaridade** entre eles
	- temos diferentes critérios de agrupamento, por exemplo para os animais, pode-se agrupar em: água x terra | ave x mamífero | com bico x sem bico
	
- classificação x agrupamento
	- ![[Pasted image 20260424082513.png]]

- **ideia (abstrata) de cluster**
	- coleção de objetos próximos 
	- ![[Pasted image 20260424082654.png]]
	- neste exemplo, parecem existir 3 clusters
	- porém, podemos ter uma ambiguidade, como neste exemplo
	- ![[Pasted image 20260424082848.png]]
	- podemos dividir em várias quantidades de calsses diferentes, como exemplo:
	- ![[Pasted image 20260424082858.png]]

### definições básicas: agrupamento
1. **clusters bem divididos:** grupo de objetos em que os elementos dentro de um mesmo cluster são mais semelhantes entre si do que em relação aos objetos de outros clusters
		![[Pasted image 20260424083412.png]]
		
2. **cluster baseado no centro:** grupo de objetos tal que qualquer objeto em um dado cluster está mais próximo ao centro do referido cluster do que do centro de outros clusters
	- centro de um cluster: pode ser definido em termos de seu centróide, obtido a partir do cálculo da média aritmética dos objetos do cluster
		![[Pasted image 20260424083446.png]]
		
3. **cluster contínuo:** grupo de objetos tal que qualquer objeto em um dado cluster está mais próximo de um ou mais objetos desses cluster do que a qualquer objeto que não pertence a ele
		![[Pasted image 20260424083923.png]]
		
4. **cluster hierárquico:** grupod e objetos onde há uma hierarquia definida entre seus objetos
		![[Pasted image 20260424083958.png]]

#### aspectos importantes

1. o ajuste de parâmetros, por exemplo, o número de clusters
	- a etapa de avaliação auxilia tanto na escolha do algoritmo mais apropriado como também no ajuste dos parâmetros
	
2. existe a possibilidade de que mais de uma estrutura relevante esteja presente nos dados
		![[Pasted image 20260424084220.png]]

### etapas da análise de agrupamento
![[Pasted image 20260424084449.png]]

1. **preparação dos dados**
	- conversão dos tipso de dados
	- normalização
	- redução do número de atributos por meio de seleção, ou via reduçaõ de dimensionalidade
	
2. uso de EDs para calcular proximidade entre objetos
	- matriz dos objetos
	- matriz e grafo de similaridade (ou dissimilaridade)
	
#### proximidade via matriz de similaridade
- representa a similaridade entre cada par de objetos
- cada elemento da matriz $S_{m\ x\ n}$ é definido pela distância $d(x_i, x_j)$ ou similaridade $s(x_i, x_j)$ entre os objetos $x_i$ e $x_j$ 

#### conceitos de proximidade
- definição de medidas de proximidade ao domínio da aplicação e tipo de informaçõa que se deseja extrair dos dados
- três tipos básicos:
	1. proximidade entre objetos
	2. proximidade entre objeto e grupod e objetos
	3. proximidade entre dois grupos de objetos

1. **medida de dissimilaridade:** $d(x_i, x_j)$ é máxima (exemplo: distância euclidiana)
2. **medida de similaridade:** $d(x_i, x_j) = 0$ (exemplo: correlação)

	- **medida de dissimilaridade (propriedades)**
		- $d(x, y) \geq 0$ para tod x e y, e  $d(x, y) = 0$, se, e somente se, $x = y$
		- $d(x, y) = d(y, x)$ para todo x e y
		- $d(x, z) \leq d(x, y) + d(y, z)$ para todo x, y e z
	
	- **medida de similaridade (propriedade)**
		- $s(x, y) = 1$ (ou o valor máximo de similaridade) se x = y (aqui supomos $0 \leq s(x, y) \leq 1$)
		- $s(x, y) = s(y,x)$ para todo x e y
		
		
		![[Pasted image 20260424085947.png]]

3. **etapa de agrupamento:** utilização de alguma estratégia/técnica de agrupamento 
4. **etapa de validação:**
	- determina-se se os cluster são significativos (solução obtida é representativa para o conjunto de dados analisado)
	- visa veriticar se o número de cluster é apropriado para o conjunto de dados 

		![[Pasted image 20260424090254.png]]
		![[Pasted image 20260424090306.png]]
		![[Pasted image 20260424090320.png]]

5. **etapa de interpretação:** 
	- examina cada cluster com relação a seus obhetos para, enfim, rotulá-los 
	- identifica/atribui significado para os clusters
	- geralmente feito com auxílio do especialista no domínio do negócio

### algoritmos de agrupamento

1. algoritmo hierárquico
2. k-means
3. mean shift

#### agrupamento hierárquico
- envolvem a construçaõ de hierarquia de cluster
	- estratégia 1: aglomerativo
		- ligação individual/simples
		- ligação completa
		- ligação média
		
	- estratégia 2: divisivo
	
- **aglomerativo**
	- cada objeto começa com seu próprio grupo
	- em passo seguitnes, os dois grupos mais similares são combinados em um novo grupo
	- o número de grupos é reduzido em uma unidade a cada passo
	- ao final, todos os elementos são reunidos em um único grupo
	- **ligação individual**
		- a similaridade entre dois grupos quaisquer é a menor distância de qualquer objeto de um grupo até qualquer objeto do outro
		- ![[Pasted image 20260424091003.png]]
		- características
			- geram longas cadeias e todos objetos são colocados em um único grupo alongado
			- os objetos em extremos opostos de uma cadeia podem ser muito distintos, mas o método considera sendo da mesma classe
			- ![[Pasted image 20260424091400.png]]

	- ligação completa
		- critério de agrupameto: maior distância de todos os objetos em um grupo para os demais em outro
		- ![[Pasted image 20260424091559.png]]
		
	- ligação média
		- o critério de agrupamento utilizada a distância média
		- tendmem a combinar grupos com pequena variação interna
		- tendem a produzir grupos com aproximadamente a mesma variância
		- ![[Pasted image 20260424091715.png]]
		
	- exemplo de ligação simples
		- ![[Pasted image 20260424091851.png]]
		- ![[Pasted image 20260424091904.png]]
		- ![[Pasted image 20260424091957.png]]
		- ![[Pasted image 20260424092737.png]]
		- ![[Pasted image 20260424092752.png]]
		- ![[Pasted image 20260424092804.png]]
		- ![[Pasted image 20260424092830.png]]
		- ![[Pasted image 20260424092913.png]]
		- ![[Pasted image 20260424092928.png]]
		- ![[Pasted image 20260424092942.png]]
		- ![[Pasted image 20260424093228.png]]
		- ![[Pasted image 20260424093243.png]]
		
	- características do aglomerativo
		- preserva hierarquia
		- é determinístico
		- produz uma ordem para objetos - informativo para a exibição de dados
	- limitações
		- embora os usuário indiquem um número desejado de cluster como condição de término, os objetos só podem ser agrupados baseando-se em decisções locais, as quais, uma vez tomadas, não podem ser revertidas

### k-means

- agrupamento baseado em centroide
- centroide é utilziado para representar o cluster
- a qualdiade do agrupamento pode ser medido pela variância intracluster
- produz clusters mais compactos e separados possíveis
- o número de cluster (k) precisa ser definido, a priori...

#### algoritmo k-means
1. os primeiros k centros dos aglomerados são escolhidos aleatoriamente
2. cada objeto é atribuído ao grupo associado com o centro mais próximo
3. um novo centro para cada grupo é calculado pela média dos valores de todos objetos (centroide)
4. o passo 2 e passo 3 são repetidos até que não haja mudança nos centros

- exemplo
	- aplicar k-means com k = 2, usando dist euclidiana como medida de dissimilaridade
	- ![[Pasted image 20260424093942.png]]
	- ![[Pasted image 20260424094034.png]]
	- ![[Pasted image 20260424094200.png]]
	- ![[Pasted image 20260424094652.png]]
	- ![[Pasted image 20260424094939.png]]
	- ![[Pasted image 20260424094952.png]]
	- ![[Pasted image 20260424095027.png]]
	- ![[Pasted image 20260424095124.png]]
	- ![[Pasted image 20260424095139.png]]
	- ![[Pasted image 20260424095336.png]]
	
- limitação: sensibildiade à escolha inicial dos centróides
	- ![[Pasted image 20260424095433.png]]
	- ![[Pasted image 20260424095446.png]]
	
- características do k-means
	- pode ser aplicado apenas quando a média do conjunto é definida
	- pode não ser o caso de algumas aplicações com atributos nominais (solução: k-modas)
	- sensível a outliers, pois distorcem drasticamente o valor médio do cluster (solução: k-medoids)
	- particional
	- varia de acordo com a escolha inicial dos centróides
		- pode ser não-determinístico, se adotado inicializações aleatórias para os centróides
	- grupos (clusters) tendem a ser esféricos
	- o n° de grupos deve ser definido a priori!!!1!!1!1!!!

#### quantos clusters utilizar? método do cotovelo
- empregado para estmiar o melhor valor de k
- o método adota a distância média dentro de um cluster até o seu centróide (*Within-cluster Sum of Squares*) para diferentes valores k
- ![[Pasted image 20260424095951.png]]
- ![[Pasted image 20260424100114.png]]
- ![[Pasted image 20260424100125.png]]

### avaliação de agrupamentos

medidas para avliar agrupamentos podem ser utilziados em diferentes casos
![[Pasted image 20260424100237.png]]
![[Pasted image 20260424100254.png]]
![[Pasted image 20260424100304.png]]
