
### sintetizando

**modelos de machine learning (ML)**
- melhora seu desempenbho por meio de experiência (dados)
- melhora execução de uma tarefa (T)
- com relação a uma medidade de desempenho (P)
- baseada na experiência (E)

**exemplo 1 - filtragem de mensagens de email**
- T: classificar mensagens de emali como spam ou legítima
- P: porcentagem de mensagens de spam e mensagens legítimas corretamente identificadas
- E: conjunto de emails apontados pelo usuário como spam/legítimos
- o modelo quer executar T visando maximar P por meio de E

### **ML x Inferência Indutiva**

**inferência**
- criar um raciocínio, para ter uma conclusão geral sobre todos os membros de uma classe por meio de análise de apenas alguns membros da classe
- de maneira geral: raciocínio do particular visando-se expandir para o geral

**exemplo de inferência indutiva**
- todos os pacientes com déficit de atenção anteiddos em 1986 sofriam de ansiedade
- todos os pacientes com déficit de atenção anteiddos em 1987 sofriam de ansiedade
- ...
- podemos inferir logicamente que todos os pacientes que sofrem de déficit de atenção também sofrem de ansiedade?
	- não!
	- isso pode ou não ser verdade, mas propicia uma boa generalização a partir do raciocínio indutivo

### tipos de aprendizado de máquina

>**modelos preditivos**
>- problema de classificação: o domínio é um conjunto de valores nominais ou valores discretos
	- dado um conjunto de observação $D = \{(X_i, y_i): X_i \in X; y_i \in Y; i = 1, \dots, N\}$
	- $f$ representa a função objetivo em que $y_i = f(X_i, \theta) + e_i$
	- essa $f$ mapeia as entradas $X_i$ nas saídas $y_i$
	- o algoritmo preditivo aprende uma aproximação para $f$ que permite estimar uma saída para novas entradas de X
	- classificação: $y_i \in Y = \{C_1, C_2, \dots, C_n\}$ (classes do problema)
	.
>- problema de regressão: o domínio é um conjunto infinito e ordenado de valores
	- dado um conjunto de observação $D = \{(X_i, y_i): X_i \in X; y_i \in Y; i = 1, \dots, N\}$
	- $f$ representa a função objetivo em que $y_i = f(X_i, \theta) + e_i$
	- essa $f$ mapeia as entradas $X_i$ nas saídas $y_i$
	- o algoritmo preditivo aprende uma aproximação para $f$ que permite estimar uma saída para novas entradas de X
	- regressão: $y_i \in Y = \mathbb{R}$

**aprendizado supervisionado**
- conjunto de dados com rótulos da classe-alvo conhecidos
- cada registro é descrito por um vetor de atributos e pelo rótulo da classe
- objetivo do indutor: construir um modelo que faça a inferência da classe de novos registros não-rotulados
	- a) para rótulos de classes discretas -> *problema de classificação*
	- b) para valores contínuos -> *problema de regressão*

**aprendizado não-supervisionado**
- conjunto de dados sem rótulos pré-definidos
- o indutor analisará os registros fornecidos, tentando agrupar os registror em *cluseters*
- após a determinação dos *clusters*, avalia os conjuntos formados

**aprendizado semi-supervisionado**
- mistura as ideias 
- este aprendizado, assume que, juntamente com o conjunto de treinamento com rótulos, há um segundo conjunto de registros não-rotualdos, também disponívem durante o treinamento
- permite unir dados pré-classificados com novos dados gerados, ainda não classificados

**aprendizado por reforço**
- estratégias de aprendizado por reforço tratam de situações onde um agente aprende por tentativa e erro ao atuar sobre um ambiente dinâmico
- não é necessária uma entidade externa que forneça instâncias de dadosm ou um modelo a respetio da rarefa a ser realizada: a unica fonte de aprendiazado é a própria experiência do agente junto ao ambiente
- o objetivo é adquirir um plano de ações que maiximize seu desempenho

