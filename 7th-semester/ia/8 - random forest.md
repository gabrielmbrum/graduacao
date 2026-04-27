### motivação

usa um paradigma similar ao de árvores de decisão (AD), porém:
- são concebidas para suprir a limitação das ADs, a construção da árvore se baseia nos dados de treinamento, mas podem ser imprecisas na inferência de dados inéditos
- parte da ideia de que uma decisão tomada de forma coletiva é mais forte do que uma decisão individual

a ideia é gerar e combinar várias ADs

### definição

**random forest** é um algoritmo de AM voltado para classificação/regressão que usa várias ADs

**ideia central** é criar uma floresta (conjunto de ADs) sendo que cada AD será construída usando:
1. um subconjunto aleatório (*bootstrap*) amostrado dos dados de treinamento 
2. um subconjunto aleatório, amostrado dos atributos

**inferência** é feita a partir da combinação das previsões  de todas as ADs da floresta
- classificação: votação majoritária das previsões
- regressão: cálculo da média das previsões

### subconjunto bootstrapped

**passo 1)**
- criar um subconjunto aleatório a partir dos dados de treinamento
- estratégias bootstrap (*bootstrapped dataset* significa conjunto de dados com repetição)
	- **ideia básica** é cada árvore ser treinada com um subconjunto aleatório diferente dos dados de treinamento original, criado por amostragem com substituição
	- **diversidade:** como cada árvore vê diferentes subconjuntos dos dados, melhorando a generalização do modelo
- exemplo
	- dataset original a esquerda e bootstrapped a direita![[Pasted image 20260424153455.png]]
	- ![[Pasted image 20260424153715.png]]
	- ![[Pasted image 20260424153723.png]]
	- ![[Pasted image 20260424153752.png]]

então repetimos o passo 1 n vezes pra formar a RF

### como aplicar o RF para a predição?

o objetivo é inferir se o paciente tem ou não doença cardíaca usando o algoritmo RF

fazemos uma contagem da saída das $n$ ADs criadas, a saída que tiver mais contagens é a saída da RF

### avaliação do modelo RF

no momento da criação do subconjunto bootstrapped, utilizamos um esquema de reamostragem por repetição. desta forma, há amostrar que não foram utiliadas na construção do subconjunto bootstrapped, portanto não foram usadas no processo de treinamento da AD

a ideia para avalição é utilizar esses dados para validar a AD

o subconjunto das amostras não utilizadas na criação da AD é chamado de *Out-Of-Bag* (OOB) *dataset* 

**processo de avaliação:** passamos cada instância $x_i$ pertencente ao subconjunto OOB($AD_1$) na árvore de decisão $AD_1$

a instância $x_i$ é passada para todas as árvores que não a utilizaram no treinamento

a classificação de $x_i$ é realizada por votação de todas as saídas 

então compara-se a classificação com a esperada

é possível medir a acurácia por meio da proporção de instâncias OOB que foram corretamente classificadas

por outro lado, a proporção de amostrar incorretamente classificas constituem o *Out-of-Bag Error*, que pode ser utilizado para melhorar a RF

### melhorando a modelagem do RG

![[Pasted image 20260424155351.png]]

por exemplo, comparar o s = 2 com s = 3 (s sendo o n° de atributos analisados para escolha do atributo divisor da raíz das ADs)



