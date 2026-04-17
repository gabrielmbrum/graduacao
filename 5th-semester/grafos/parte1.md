[[graduacao/5th-semester/grafos/index|index]]
## 1. representação de grafos

a representação deve ser uma estrutura que:
- corresponde de forma única a um grafo dado
- pode ser armazedas e manipulada em um computador

a representação gráfica por um diagrama de pontos e linhas não satisfaz a segunda condição

### 1.1 matriz de adjacência

#### definição

considere um grafo G(V, A) com n vértices e m arestas
a matriz de adjacência é uma matriz n x n, denotada por $X = [x_{ij}]$ e $\begin{cases} x_{ij} = 1,\ se\ existe\ aresta\ entre\ i\ e\ j\ \\ x_{ij} = 0,\ caso\  contrário \end{cases}$

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
