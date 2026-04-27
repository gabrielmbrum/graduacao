## KNN

**k-vizinhos mais próximos**
- classifica um novo objeto com base nos registros do conjunto de treinamento que são próximos a ele
- não aprende um modelo compacto para os dados, apenas memoriza os dados de treinamento
- tem variações definidas com base eno n° de vizinhos a serem considerados
- vantagem: pode ser usado tanto para classificação quanto para regressão

**vizinhos mais próximos**
- parâmetro K -> se k = 1 então 1-vizinhos mais próximo
	- 1-NN, 1 - Nearest Neighbours
	- 2-NN, 2 - Neares Neighbours
- calcula a distância entre dois pontos (mais comum é a euclidiana)
- intuição:
	- ![[Pasted image 20260417201854.png]]

**complexidade**
- o algoritmo básico armazena todas as *n* instâncias de treinamento, logo:
	- complexidade para calcular as distâncias e encontrar o vizinho mais próximo -> $O(n)$
	- complexidade para selecionar as k amostras mais próximas -> $O(nk)$ = $O(n)$ 
		- k é muito menor que n, então pode-se simplificar

**predição**
- analisa-se os k mais próximos do ponto de teste z
- se for classificação, a inferência se baseia na MODA dos vizinhos
- se for regressão e minimizar o erro quadrático -> média
- se for regressão e minimizar o desvio absoluto -> mediana

**variação de k**
- ao variar o k, as inferências podem ser alteradas
- como escolher o melhor k? testando ;)
- proposta de encontrar o k ideal
	- validar o modelo com diferentes valroes de k
	- heurísticas
	- análise de viés-variância

## Regressão Logística

**motivação e definição**
- suponha que temos amostras de duas classes associadas aos números 1 (azul) e 0 (vermelhas)
- $Y  : \mathbb{R} \rightarrow {0, 1}$ com $Y = Y(x)$, sendo x o valor de uma feature
	- ![[Pasted image 20260418112136.png]]
-  fórmual geral é $Y = Y(x) = \beta_0 + \beta_1X_1 + \beta_2X_2 + \dots + \beta_dX_d = \beta^Tx$ 
	- com $x^T = [1, X_1, X_2, \dots, X_d]$ e $\beta^T = [\beta_0, \beta_1, \dots, \beta_d]$ $\in \mathbb{R}^{d+1}$ 
- usando a saída de Y em um valor inteiro, o modelo pode ser usado para classificação de dados
- a probabilidade para o caso de duas classes é $p(Y = 1| x)$ e $p(Y = 0|x)$

>**objetivo:** ajustar uma curva, em formato de S, aos valores das probabilidades e características (eixo x) dos dados
>![[Pasted image 20260418113021.png]]

**função sigmoide**
- para ajustar neste formato, utilizarem a função logística (função sigmoide): $$h(z) = \frac{e^z}{1 + e^z}$$
- esta função sempre retornará valores no intervalo [0, 1]

**regressão logística**
- tomando a probabilidade como sendo a função sigmoide, conseugimos definir uma probabilidade a partir dos atributos x:
$$p(y = 1|x) = \frac{e^{ \beta^Tx } }{ 1 + e^{ \beta^Tx } }$$
$$p(y = 0|x) = 1 - p(y = 1|x)= \frac{1}{ 1 + e^{ \beta^Tx } }$$
- neste caso, o aprendizado se resume a ajustar o vetor de parâmetros $\beta$ 
- este método é a regressão logística (RL)
- ![[Pasted image 20260418121124.png]]
- ![[Pasted image 20260418121141.png]]
- ![[Pasted image 20260418121150.png]]
- ![[Pasted image 20260418121203.png]]
- ![[Pasted image 20260418121217.png]]
- ![[Pasted image 20260418121238.png]]


## Teoria Bayesiana

**motivação e definição**
- dado M classes $w_1, \dots, w_m$ e uma observação $x = (x_1, \dots, x_n) \in \mathbb{R}^n
- determinar a probabilidade condicional $p(w_i | x)$ da observação pertencer a cada uma das classes $w_i$
	- $p(w_i | x)$ é a probabilidade de w_i dado x

- a ideia central é classificar novas observações de acordo com a classe mais provável
$$\hat{y} = arg  \space  max_{i \in \{1, \dots, M\}} p(w_i | x)$$
- a intuição é que a classe que a nova observação terá é aquela com maior probabilidade (esta probabildiade é calculada com base nos atributos da nova observação)

**classificador ótimo**
- se a probabilidade condicional for conhecida para todas as classes i, o erro obtido é o menor possível (classificador ótimo)
- porém na maioria das vezes a distribuição do modelo gerador dos dados não é conhecida, assim impossibilitando calcular as probabilidades condicionais explicitamente

**teoria da decisão bayesiana**
- dado M classes e uma observação x de n atributos, determinar a probabilidade condicional de x percenter a cada classe $w_i$ usando o teorema de bayes
$$p(w_i | x) = \frac{p(x|w_i)P(w_i)}{p(x)}$$
- ideia de uso como classificador (caso de duas classes)
	- assumindo $P(w_1) = P(w_2)$, temos:
		- $p(w_1 | x) \propto p(x | w_1)$

- a classificação de x será a classe com maior probabilidade condiocional de x

**classificador de naive bayes**
- assume-se que as variáveis que descrevem os atributos são independetes
- logo, a função de verosimilhança é o produto das marginais:
	- ![[Pasted image 20260418123332.png]]
- regra de bayes: classificar $x \in \mathbb{R}^d$ de acordo com a classe i mais provável
- caso com duas classes, se a probabilidade condicional de $w_1$ dado x for maior então é classificado como $w_1$, caso contrário é classificado como $w_2$ 
- fórmula geral é
	- ![[Pasted image 20260418123601.png]]

**exemplo via regra de bayes**
- ![[Pasted image 20260418153424.png]]
- ![[Pasted image 20260418153431.png]]
- ![[Pasted image 20260418153452.png]]
- ![[Pasted image 20260418153505.png]]
- ![[Pasted image 20260418153518.png]]
- ![[Pasted image 20260418153529.png]]
- ![[Pasted image 20260418153539.png]]
- ![[Pasted image 20260418153545.png]]

**classificação via regra de naive bayes**
- caso os atributos sejam contínuos, podemos assumir uma distribuição de probabilidade (geralmente Normal) e realizar a classificação maximizando a verossimilhança
- ![[Pasted image 20260418153700.png]]
- algoritmo
	- ![[Pasted image 20260418153723.png]]
- propriedades de naive bayes
	- ![[Pasted image 20260418153738.png]]

