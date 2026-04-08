>25/03
### operações lógicas e aritméticas

adição e subtração
- soma/subtrai os valores de cada pixel

multiplicação ou divisão
- utilizada para ajuste de brilho após o processo de aquisição
- filtragem de imagens 

operações lógicxas
- OR
- AND
- NOT
- XOR

### transformações geométricas

modificam a relação espacial entre os pixels de uma imagem
$$
(x, y) = T{(v, w)}
$$
-> (v, w) são coordenadas de um pixel na imagem original
-> (x, y) são as coodenadas do pixel correspodente na imagem transformada

### métricas de qualidade de imagens

resolução: quantidade de pixel (M x N)

quantização: quantidade de bits para representar cada pixel

a qualidade de uma imagem pode ser avaliada via métricas

as avaliações objetivas mais comuns sõa baseadas em medidas de similaridades ou diferenças entre as imagens

considere as imagens $f$ e $g$ com dimensões MxN pixels
- erro máximo (*Maximum Error - ME*)
	$ME = max |f(x, y) - g(x, y)|$

- erro médio absoluto (*Mean Absolute Error - MAE*) 
	$MAE = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{n-1} |f(x, y) - g(x, y)|$

- raiz do erro médio quadrático (*Root Mean Square Error - RMSE*)
	$RMSE = \sqrt{MAE} = \sqrt{\frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{n-1} |f(x, y) - g(x, y)|}$

- coeficiente de jaccard 
$$
J = \frac{\sum_{x=0}^{M-1} \sum_{y=0}^{n-1} 
\begin{cases}
= 1, & \text{se } f(x, y) = g(x, y) \\
= 0, & \text{caso contrario}
\end{cases}}
	{MN}
$$
	- pode-se ter uma tolerância, em que não necessariamente precisam ser iguais, podem estar em um intervalo

---

## ruídos

### restauração

principais fontes de ruído em imagens digitais
- durante a aquisição
- transmissão

sensores afetados por condições
- ambientais
- qualidades dos sensores