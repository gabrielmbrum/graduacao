### a era dos dados
- a cada 20 meses, dobra-se a quantidade de dados no mundo
- 10 ~ 20% dados estruturados
	- abstração do mundo físico em um conjunto de atributos
	- cada **objeto** é uma instação
	- cada **atributo** é uma propriedade do objeto
	
- 80 ~ 90% dados não estruturados
	- textos, arquivos, imagens...

- dados semi-estruturados
	- XML, JSON ....

- tabela de atrivutos
	- matrix **n x d**
	- n -> n° de objetos
	- d -> número de atributos de cada objeto, isto representa também a **dimensionalidade** dos objetos
	- esses objetos podem ter associado a eles uma **classe**, que é um metadado do conjunto
```
df = pd.read_csv('hospital.csv', delimiter = ";")
```
 
- tipos de atributos
	- quantitativa
		- discreto
			- número de valores finito ou qtd enumerável
			- ex.: contagem de defeitos, n° de clientes...
		- contínuo
			- resultam de infinitos valores possíveis que correspondem a alguma escala contínua
			- ex.: pressão, temperatura...
	- qualitativo
		- nominal
			- consistem em nomes, rótulos ou categorias
			- os dados não podem ser ordenados
			
		- ordinal
			- podem ser arranjados em alguma ordem
			- ex.: estatura (baixo, médio, alto); nível de febre (alto, médio, baixo)...

- escala dos dados
	- grau de significância 
	- qualitativo
		- nominais
			- constituidos por nomes, carregando poucas informações
			- **não há relação de ordem definida**
			- **operações admitidas:** =, <>
			- ex.: IDs, cores, sexo...
			- representação
				- gráfica -> diagrama de barra, de linhas e de pizza
				- medidas -> moda
				- dispersão -> 
			
		- ordinais
			- valores refletem a *ordem das categorias*
			- operações admitidas: =, <>, <, >, <=, >= 
			- ex.: nível de febre, grau de escolaridade...
			- representações
				- gráfica -> boxplot
				- medidas -> mediana
				- dispersão -> interval o interquartílico
			
	- quantitativo
		- intervalares
			- variam em determinado intervalo, com intervalos iguais entre os valores
			- pode-se definir uma reçaõ de ordem, e/ou soma/diferença de magnitudes
			- nõa há zero absoluto
			- operações admitidas: =, <>, <, >, <=, >=, +, -
			- ex.: datas, temperaturas, tamanho roupa
			- representações
				- gráfica -> histograma, políno de frequências
				- medidas -> média
				- dispersão -> desvio padrão
			
		- racional/razão
			- n° são arbitrários, sem escopo de limitação
			- operações admitidas: =, <>, <, >, <=, >=, +, -, produto, quociente
			- há um zero absoluto, que repsenta ausência total da característica medida
			- ex.: distância, peso, salário, n° de votos
			- representações
				- gráfica -> 
				- medidas -> média geométrica
				- dispersão -> coeficiente de variação
	- ![[Pasted image 20260316162329.png]]

### análise e exploração de dados

- estatística descritiva
	- medidas de localidade
	- espalhamento e distribuição
	- outras medidas...

- visualização
	- gráficos de barras, dispersão, boxplots
	- técnicas de visualização específicas (ilustração com grafos, treempas, stacked maps, KDE, PCA...)

### pré-processamento

- etapa de pré-processamento
	- visa melhorar a qualidade dos dados
	- eliminam/reduzem os *outliers*
	1. remoção de atributos
	2. integração dos dados
	3. amostragem de dados
	4. balanceamento de dados
	5. limpeza de dados/remoção de outliers
	6. redução de dimensionalidade
	7. conversão de dados

- removendo atributos
	- quando um atributo não contribui para as análises de dados, ou não impactam na tarefa-alvo

- integração de dados
	- busca por atributos comuns nos conjutnos para serem unidos

- amostragem de dados
	- algoritmos de AM podem ter dificuldades com grandes quantidades de objetos
	- *trade-off* entre eficiencia computacional x acurácia
	- a amostra deve representar todo o conjunto
	- amostragem aleatória simples
		- sem reposição de exemplos: são extraídas do conjunto original para o cojunto de amostras
		- cada amostra pode ser selecionada apenas uma vez
		
	- amostragem progressiva
		- inicia com amostragem pequena e ir aumentando progressivamente
		
	- amostragem estratificada
		- usada quando há classes distintas e classes desbalanceadas

- limpeza de dados 
	- dados com ruído: valores distintos do esperado
	- dados inconsistentes: não estão de acordo com as regras, expectativas ou padrões estabelecidos
		- ex.: dois registros identicos porém com um atributo divergente
		- como lidar
			- remoção 
			- análise de contexto
			- atribuir maior peso aos registros com base na frequência de ocorrência
			- criação de nova classe, ou substituiçõa, com base na média/mediana
			- predição via ML
			
	- dados incompletos
		- ausencia de valores para alguns dos atributos
		- como lidar
			- eliminar os objetos com valores ausentes
			- preencher manualmente 
			- empregar algoritmo de AM que lidam internamente com valores ausentes
			- usar alguma heurística para preencher automaticamente
			
	- dados com redundância
		- quando dois ou mais objetos/colunas tem os mesmos valores 
			- como lidar
				- eliminar os objetos/colunas
				- agrupar em um único registro
				- empregar algoritmo de agrupamento
				- usar redução de dimensionalidade
				- uso de técnicas de *Feature Selection*
				
	- outliers

- transformação de dados
	- conversão simbólico-numérico
		- ex.: ausente = 0 | presente = 1
	- *label encoding*
		- converter dados qualitativos em quantitativos
		- cada categoria deve ser convertida para um número
			- ex.: febre (alta, média, baixa) -> febre (2, 1, 0)
		- geralmente, a conversão é feita em qualitativos ordinais
		- quando é qualitativo nominal, pode-se empregar uma transformação manual
		
	- *one-hot encoding*
		- visa converter dados qualitativos nominais/outros em formato adequado para aprendizado de máquina
		- cria colunas binárias separadas para cada categoria única
		- exemplo:
			- dado original (coluna cor)
				- cor = vermelho
				- cor = verde
			- *one-hot encoded*
				- coluna cor_vermelho recebe 0 ou 1 
				- coluna cor_verde recebe 0 ou 1
				- ...
			- útil para datas
				- ex.: muito assalto nas quartas e domingos, em que ocorria jogo do brasileirao, entao cria-se colunas para os dias e horários
				
	- técnicas de reescalonamento
		- converter os atributos para uma escala adequada
		- ex.: idade e salário estão em escalas muito diferentes, neste caso, o salário teria um peso EXTREMAMENTE maior que idade, pois varia muito mais do que a idade na escala original
		- três propostas
			- escalonamento via mediana + IQR
			- padronização (standarlization)
			- normalização min-max