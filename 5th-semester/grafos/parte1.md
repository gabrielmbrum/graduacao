[[graduacao/5th-semester/grafos/index|index]]
## 1. representação de grafos

a representação deve ser uma estrutura que:
- corresponde de forma única a um grafo dado
- pode ser armazedas e manipulada em um computador

a representação gráfica por um diagrama de pontos e linhas não satisfaz a segunda condição

### 1.1 matriz de adjacência

#### definição

considere um grafo G(V, A) com n vértices e m arestas
a matriz de adjacência é uma matriz n x n, denotada por 

$X = [x_{ij}]$ e $\begin{cases} x_{ij} = 1,\ se\ existe\ aresta\ entre\ i\ e\ j\ \\ x_{ij} = 0,\ caso\  contrário \end{cases}$

#### propriedadades

complexidade de memória é $O(n^2)$

**NÃO** são todos os tipos de grafos que podem ser representados assim, apenas aqueles que não possuem arestas paralelas

a diagonal principal de X qualquer é nula se, e somente se, não existir laços em G

se o grafo é simples (isto é, não possui laços e múltiplas arestas) o grau de um vértice é dado pela soma dos elementos de sua linha correspondente

dois grafos simples $G_1$ e $G_2$ são isomorfos (estruturalmente idênticos) se só se: $X(G_2) = R^{-1} X(G_1) R$
	tendo $X(G_1)$, aplicando a reodernação de linhas $R^{-1} X(G_1)$ e reordenação de colunas $X(G_1) R$
	caso exista R, entao eles são isomorfos

dado uma matriz qualquer M simétrica e binária, sempre é possível construir um grafo G com *n* vértices tal que X(G) = Q

um grafo G é disconexo com dois componentes $G_1$ e $G_2$ se, e somente se
$$
X(G) = \begin{bmatrix}
X(G_1) & 0 \\
0 & X(G_2)
\end{bmatrix}
$$

se X é a matriz de adjacência de um grafo simples e B = X², os elementos $b_{ij}$, $i \neq j$ , representam o número de caminhos distintos de comprimento 2 entre os vértices $v_i$ e $v_j$ 

>**teorema:** seja X a matriz de adjacência de um grafo simples G, então a ij-ésima entrada de $X^r$ é o número de passeios diferentes de comprimento r entre os vértices $v_i$ e $v_j$ 

>**corolário:** em um grafo conexo, a distância entre dois vértices $v_i$ e $v_j$, $i \neq j$ se, e somente se, k é o menor inteiro para o qual a ij-ésima entrada em $X^k$ é não-nula

>**corolário:** se X é a matriz de adjacência de um grafo com n vértices, e
>$$ Y = X + X² + X³ + ... + X^{n-1} $$
>então G é desconexo se, e somente se, existe ao menos uma entrada na matriz Y que é igual a zero

é possível utilizar esta estrutura para digrafos? sim!

a matriz de adjacência de um digrafo D (grafo direcionado) é denotada por $X = [x_{ij}]$ e $\begin{cases} x_{ij} = 1,\ se\ existe\ aresta\ direcionada\ de\ i\ para\ j\ \\ x_{ij} = 0,\ caso\  contrário \end{cases}$

observações
- neste caso a matriz só é simétrica se o digrafo for simétrico
- o grau de sáida do vértice $v_i$ é dado pela soma dos elementos da linha i
- o grau de entrada do vértice $v_i$ é dado pela soma dos elementos da coluna i
- com X de D, $X^{-1}$ é a matriz de adjacência obtida pela inversão da orientação das arestas de D

### 1.2 matriz de incidência

seja G um grafo com n vértices e m arestas, sua matriz de incidência é uma matriz n x m, denotada por
$$A = [a{ij}] = \begin{cases} a_{ij} = 1,\ se\ a\ aresta\ a_j\ é\ incidente\ no\ v_i\ \\ a_{ij} = 0,\ caso\  contrário \end{cases}$$
observações
- é necessário rotular os vértices e arestas de G
- a compelxidade para armazenar o grafo é $O(nm)$
- não pode-se armazenar grafos com arestas laço
- como cada aresta é incidente em exatamente dois vértices, cada coluna de A(G) possui exatamente dois 1's
- o número de 1's em cada linha é correspondente ao grau do vértice
- uma linha de 0's representa um vértice isolado
- arestas paralelas correspondem a colunas idênticas 
- um grafo G é um grafo desconexo se, e somente se:
	- $A(G) = \begin{bmatrix} A(G_1) & 0 \\ 0 & A(G_2) \end{bmatrix}$
	
- dois grafos são isomorfos se, e somente se,  suas matrizes de incidência diferem apenas por permutações de linhas ou colunas

**dígrafos**
são representáveis pela matriz de indicidência, porém com pequenas modificações, onde
$$A = [a{ij}] = \begin{cases} a_{ij} = 1,\ se\ a\ aresta\ a_j\ diverge\ de\ v_i\ \\ a_{ij} = -1,\ se\ a\ aresta\ a_j\ converge\ para\ v_i\ \\ a_{ij} = 0,\ caso\  contrário \end{cases}$$

### 1.3 lista de arestas

dois vetores F e H, cada elemento recebe o rótulo de um vértice, de modo que a i-ésima aresta diverge de $f_i$ e converge para $h_i$
se o grafo não for direcionado, os vetores são definidos da mesma forma, desconsiderando "convergir" e "divergir"

>**complexidade:** $O(2m)$

### 1.4 lista de sucessores

quando a razao $m/n$ não é muito alta, é conveniente utilizar esta estrutura

definimos $n$ vetores, cada vetor é associado a um vértice

o primeiro elemento do vetor k é o elemento $v_k$, os demais elementos são os vértices adjacentes à $v_k$

supondo que $d_{med}$ é o grau médio do grafo G, a complexidade é $O(n \cdot d_{med})$ 

## 2. Grafos Eulerianos

	1) Algoritmo de Decomposição
	2) Algoritmo de Fleury
	3) Digrafos Eulerianos
	4) O Problema Chinês do Carteiro
		1) Algoritmo

**definições**
- um trajeto que inclua todas as arestas de um dado grafo G(V, A) é chamado de **trajeto Euleriano**
- seja G um grafo conexo, dizemos que ele é um **grafo Euleriano** se tiver um **trajeto euleriano fechado** (cada aresta é percorida uma unica vez)
- um grafo G não-Euleriano é dito ser **semi-Euleriano** se possui um trajeto euleriano

**lema**
- se G(V, A) é um grafo tal que d(v) >= 2 para todo v $\in$ V, então G contém um ciclo
- demonstração
	- se G possui laços ou arestas paralelas, não há o que provar
	- vamos supor que G é um grafo simples, seja $v_0 \in V$ um vértice arbitrário de G, como d(v) >= 2 para todo $v \in V$, podemos contruir um passeio $v_0 \rightarrow v_1 \rightarrow v_2 \dots$ indutivamente, escolhendo $v_{i+1}$ como sendo qualquer vértice adjacente a $v_i$ exceto $v_{i-1}$ 
	- como G possui uma quantidade finita de vértices, em algum momento escolheremos algum vértice, digamos $v_k$ , pela segunda vez
	- a parte do passeio entre a primeira e a segunda ocorrência de v_k constitui um ciclo

**teorema**
- um grafo conexo G(V, A) é Euleriano se, e somente se, o grau de cada vértice de G é par

**corolário**
- um grafo conexo é Euleriano se, e somente se, ele pode ser decomposto em circuitos disjuntos
- ![[Pasted image 20260419180610.png]]

**corolário**
- um grafo conexo é semi-Euleriamo se, e somente se, possui exatamente dois vértices de grau ímpar

### 2.1 algoritmo de decomposição (Hierholzer, 1873)

considere um grafo conexo G(V, A), onde d(v) é par para todo e qualquer v pertencente a V

**passo 1:** determine um circuito $C_1$ em G
- defina $T_1 = C_1$ e $G_1 = G$
- se $T_1$ possui todas as arestas de G, pare ($T_1$ é o trajeto procurado)
tome k = 1

**passo 2:**
- faça k = k + 1
- construa o subgrafo $G_k(\bar{V}_k, \bar{A}_k)$ removendo de $G_{k-1}$ as arestas pertencentes a $T_{k-1} (V_{k-1}, A_{k-1})$ 
- remova de $G_k$ os vértices isolados

**passo 3** 
- determine um vértice $v \in \bar{V}_k \cap V_{k-1}$ 
- a partir de v determine um circuito C_k em G_k

**passo 4:** determine $T_k = T_{k - 1} \cup C_k$
- se T_k possui todas as arestas de G, vá para o passo 5
- caso contrário, retorne ao passo 2

**passo 5:** pare
- o trajeto T_k é o trajeto procurado 

### 2.2 algoritmo de Fleury (Fleury, 1833)

considere um grafo conexo G(V, A) onde d(v) é par para todo e qualquer v pertencente a V

comece em qualquer vértice v e percora as arestas de forma aleatória, seguindo sempre as seguintes regras
- exclua as arestas depois de passar por elas
- exclua os vértices isolados, caso ocorram
- passe por uma ponte (aresta cuja remoção torna o grafo desconexo) somente se não houver outra alternativa

### 2.3 digrafos eulerianos

**definições:** 

um trajeto orientado que inclua todas as arestas de um dado digrafo G(V, A) é chamado de trajeto Euleriano

seja G um digrafo conexo, dizemos G é euleriano se possui um trajeo euleriano fechado

um digrafo G não-euleriano é dito ser semi-Euleriano se possui um trajeto Euleriano

**toerma de Euler para digrafos**

um digrafo D(V, A) é Euleriano se, e somente se, D é balanceado ($d_e(v) = d_s(v)$ para qualquer v pertencente a V)

**corolário**

um digrafo D(V, A) é semi-Euleriano se, e somente se, existem dois vértices x, y pertencen a V tais que

$d_s(x) - d_e(x) = 1,\: \: \: \: d_e(y) - d_s(y) = 1$ 

e

$d_e(v) = d_s(v) \ \forall v \in V \: com \: exceção \: de \: \{x, y\}$  

### 2.4 o problema chinês do carteiro

considere um grafo valorado G tal que os pesos das arestas são não-negativos, encontre um passeio fechado que percorra todas as arestas de G com peso total mínimo

**algoritmo**

considere um grafo valorado conexo G em que o conjunto de vértices de grau ímpar é $V_{impar} = \{v_1, \dots, v_{2k}\}$ onde $k \geq 1$ 

1. para cada par $(v_i, v_j) \in V_{impar} \ X \ V_{impar}$ com $v_i \neq v_j$ encontre o caminho mínimo $P_{i, j}$ entre v_i e v_j
2. construa um grafo completo com os 2k vértices de $V_{impar}$ em que o peso da aresta $(v_i, v_j)$ é o peso do caminho mínimo $P_{i, j}$ 
3. determine o conjunto $E = \{e_1, e_2, \dots, e_k \}$ de k arestas do grafo completo, duas a duas não-adjacentes, tal que a soma de seus pesos seja mínima
4. para cada aresta $e = (v_i, v_j) \in E$, duplique as arestas de $P_{i, j}$ em G

## 3. Grafos Hamiltonianos

3) Grafos Hamiltonianos:
	1) O Problema do Caixeiro Viajante
	2) Digrafos Hamiltonianos

**definições**
- um circuito Hamiltoniano em um grafo conexo é um circuito que contém todos os vértices do grafo, podendo repetir as arestas, que inicia e termina no mesmo vértice 
- um grafo é chamado de grafo Hamiltoniano se possui um circuito Hamiltoniano
- um grafo não-Hamiltoniano é semi-Hamiltoniano se possui um caminho que contém todos os seus vértices

**condições necessárias e suficientes para definir um grafo hamiltoniano**
1. arestas paralelas e laços não podem pertencer a um circuito Hamiltoniano
2. se um vértice possui grau 2, as arestas a ele incidentes deve, pertencer ao circuito hamiltoniano
3. nenhum subcircuito próprio, isto é, um circuito que não possui todos os vértices de G, pode ser formado durante a construção do circuito hamiltoniano
4. um vez incluído um vértice, todas as arestas e ele incidentes e que não foram inseridas no circuito podem ser desconsideradas

pra que tipo de grafo podemos garantir a existência de um circuito hamiltoniano?

>grafo completo: grafo simples tal que existe uma aresta entre cada par de vértice

**teorema:** em um grafo compelto com n vértices, existem (n - 1)/2 circuitos hamiltonianos aresta-disjuntos, se n >= 3 é impar

**teorema de Ore:** se G(V, A) é um grafo simples com n >= 3 vértices e se $$d(v) + d(w) \geq n$$ para cada par de vértice não-ajdacentes $v$ e $w$ então G é hamiltoniano

**teorema de Dirac:** se G é um grafo simples com n >= 3 vértices e se $$d(v) \geq \frac{n}{2}$$
para cada vértice v, então G é hamiltoniano

**teorema:** se G(V, A) é um grafo hamiltoniano, então para todo subconjunto não-vazio, $S \subseteq V$, o grafo G - S possui no máximo |S| componentes

### 3.1 o problema do caixeiro viajante

um viajante necessita visita rum certo número de cidades durante uma viagem e retornar ao lugar de origem de tal maneira que cada cidade é visitada exatamemte uma vez e que a distância total percorrida seja a menor possível. dada a distância entre as cidades, que rota ele deve escolher?

como resolver?
- em princípio, este problema pode ser resolvido determinando todas as rotas possíveis e escolhendo a melhor
- o problema é falta de eficiência, a qual no caso de $n$ cidades, são possíveis (n - 1)! rotas

### 3.2 digrafos hamiltonianos

**definições**
- um digrafo D é dito hamiltoniano se possuir um circuito orientado que inclua todos os seus vértices
- um digrafo não-hamiltoniano é dito ser semi-hamiltoniano se possuir um caminho orientado que inclua todos os seus vértices

**teorema de Ghouilà-Houri:** seja D um digrafo simples com n vértices
- se $d_s(v) \geq \frac{n}{2}$ e $d_e(v) \geq \frac{n}{2}$
- para todo vértice v de D, então D é hamiltoniano

**teorema de Woodall:** seja D um digrafo simples com n vértices
- se $d_s(v) + d_e(w) \geq n$
- para todo par de vértice não-ajacentes v e w de D, então D é hamiltoniano

**teorema de Meyniel:** seja D um digrafo simples e fortemente conexo com n vértices
- se $d(v) + d(w) \geq 2n - 1$ 
- para todo par de ǘertices não-ajdacentes v e w de D, então D é Hamiltoniano
