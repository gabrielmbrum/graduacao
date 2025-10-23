
# aula 01
### linha do tempo

1886 - início do CRT (Cathode Ray Tube)

1929 - fotograma (24 FPS)

1927 - ENIAC dos cria

1938 - CRT colorido

1947 - invenção do transistor

1950 - Laposky cria obras de arte digitais

1955 - Sage (monitoramento aéreo)

 1959 - surge o termo Computer Graphics

1960 - primeiro computador comercial

 1961 - primeiro jogo com comp graf

1963 - sistema de desenho (Sutherland)

1963 - primeiro filme feito por computador (Zajac)

1964 - Boeing cria modelo computacional de um corpo humano

1966 - Odissey (primeiro video game)

1966 - MAGI (primeira empresa de produção computacional de animações e efeitos especiais)

1970 - algorimos para CG

1971 - tomografia computadorizada

1972 - Atari 

1975 - reconhecimento da CG como área (SIGGRAPH)

1977 - nova categoria no Oscar de efeitos especiais

1992 - padronização de pacotes gráficos (OpenGL)

---
### computação gráfica

é a interseção de três áreas:
- sintese de imagens
	- objetos criados pelo computador 
- processamento de imagens
	- visa melhorar as características visuais da imagem
- análise de imagens
	- obter características dos componentes de uma imagem

---
### OpenGL - Graphics LIbrary

a interface entre o software e o hardware gráfico é feita através de procedimentos e funções 

### sistemas e dispositivos gráficos

- vetoriais
	- x, y e z
	- noção de profundidade
	- ex.: blender, impressora 3D
	
- matriciais
	- somente x e y
	- ex.: paint

---
### tecnologia CRT

técnica da esquerda para direita e de cima para baixo, assim poderia se reduzir pela metade o FPS e o olho humano não perceberia a diferença

a quantidade de informação é medida em pixel

**pixel:** medida adimensional (sem tamanho físico definido, é definido pela resolução do dispositivo) -> isto afeta a qualidade da imagem

usando a resolução máxima -> um pixel é igual a uma unidade física do monitor
resolução menor que a máxima -> um pixel é composto por mais de uma unidade física do monitor

**qualidade da imagem:** influenciada pelo dot pitch (distância física entre os centros de um pixel), o qual, para manter a qualidade, deve ser no máximo de 0.28mm (mais pontos por polegada -> melhor a resolução)

---
### tecnologia LCD (Liquid Crystal Display)

duas lâminas polarizadas (uma na horizontal e outra na vertical) que tem uma camada de cristal líquido entre elas, para orientar a luz e definir as variações de intensidade

a cor final é criada pela mistura de quanta luz passa pelos subpixels R, G e B

a intensidade é controlada pela voltagem que a camada de transistor aplica, a qual faz os critais líquidos se alinharem de forma mais ou menos torcida, bloqueando mais ou menos luz

___
### tecnologia plasma

camada com cápsulas de fósforo vermelho, verde e azul (essas cápsulas contém ganes: neônio e xenônio)
eletrodos emites estímulos que transformar o gás em plasma

---
# aula 07

>aula de PI
### modelos de cores

**colorimetria**
- quantificação das cores e padronização de como enxergamos

**sistema CIE**
- utilizado para descrever a cor
- padronização de iluminantes e observadores
- fontes: luz incandescentes (A), luz solar (B) e luz do dia (C)

**cor**
- pode ser definida pela cromaticidade
- modelo XYZ ou CIE, desenvolvido pela CIE
	- baseado na resposta espectral
	- experimento com 20 indivíduos

**diagrama de cromaticidade**
- composição de cores em função de $x$ e $y$
- gama de cores "Gamut"

*resumindo*

distinção entre cores, considera:
- matiz: cor pura (comprimento de onda dominante)
- saturação: quantidade em que a cor pura é diluida na luz branca (pureza)
- cromaticidade: matiz e saturação tomadas juntas

percepção de cores
- brilho: quantidade de luz sobre a área
- luminância: medida para descrever o brilho percebido de uma cor

tipos de modelos de cores
- aditivos (luz)
	- a adição de luz em diferentes comprimentos de onda gera a mistura
	- exemplo: RGB, XYZ
	- aplicação: monitore, projetores e TVs
	
- subtrativo (luz)
	- gerada pela absorção da luz em diferentes comprimentos de onda
	- exemplo: CMY e CMYK
	- aplicação: impressão e tinta

### modelo RGB

é baseado em um sistema de coordenadas cartesianas, onde o espaço de cores é um cubo

![[cubo rgb.png]]

### modelo HSV ou HSB

matiz (H, hue), saturação (S, saturation) e luminância (V, value - brilho, qtd de luz na mistura)

é uma pirâmide de base hexagonal, representação gráfica:

![[modelo hsv.png]]


H está entre 0 e 360°

S está entre 0 e 1 

V entre 0 e 1

### conversão de RGB para HSV

$$
H = 
\begin{cases} 
60 \frac{(G - B)}{(M - m)}, & \text{se } M = R \\
60 \frac{(B - R)}{(M - m)} + 120, & \text{se } M = G \\
60 \frac{(R - G)}{(M - m)} + 240, & \text{se } M = B
\end{cases}
$$

$$
S =
\begin{cases}
\frac{(M - m)}{M}, & \text{se } M = B
0, & \text{caso contrário}
\end{cases}
$$
$$
V = \frac{M}{255}
$$
em que $m = min(R, G, B)$ e $M = max(R, G, B)$

### modelo HSI

definidos por: matiz (H), saturação (S) e intensidade (I - luminância)

representação gráfica:
![[modelo HSI.png]]

variávies:
- H entre 0 e 360°
- S entre 0 e 1
- intensidade entre 0 e 1 

modelo de interesse em visão computacional
![[exemplo HSI.png]]

equalização do histograma (aplicado sobre o componente *i*)
![[equalizacao hsi.png]]

# aula 03

### transformações geométricas no plano e no espaço

#### conceitos que vão ser explorados
- transformação de escala
- transformação de rotação
- transformação de translação
- transformação de reflexão
- composição de transformações
- coordenadas homgêneas

#### conceitos iniciais
- representação vetorial
	- vetor: segmento de reta orientado (módulo, direção e sentido)
	- direção: ângulo formado ($\theta$)
	- sentido: de A para B
	- módulo ou intensidade: |v| = $\sqrt{a² + b²}$
	- esta representação é utilizada para 3D (como no blender)
![[compontentes_de_v.png]]

- representação matricial
	- planificaçaõ
	- renderização de objeto 3D em uma imagem

#### transformações geométricas
- operações que podem ser aplciadas para alterar posição, orientação, forma ou tamanho de um objeto
	- envolvem operações de aritmética simples
	- uso de matrizes
- podem ser representadas na forma de equações
- considere um sistema de coordenadas cartesianas
	- translação
		- dado um ponto $P$ caso seja 2D [x y] e caso seja 3D [x y z]
		- uma transformação geométrica $T$ seria em 2D $[d_x \space d_y]$  e em 3D $[d_x \space d_y \space d_z]$ 
		- então a transformação pode ser definida como $P' = P + T$
	- transformação de escala (S)
		- 2D $$ P' = S*P = \begin{pmatrix} S_x & 0 \\ 0 & S_y \end{pmatrix} * \begin{pmatrix} x \\ y \end{pmatrix} $$
		- 3D $$ P' = S*P = \begin{pmatrix} S_x & 0 & 0\\ 0 & S_y & 0 \\ 0 & 0 & S_z \end{pmatrix} * \begin{pmatrix} x \\ y \\ z \end{pmatrix} $$
	- cisalhamento (c)
		- distorce o formato de um objeto considerando um ponto P
		- uma coordenada é deslocada segundo um valor proporcional à sua distância em relação ao eixo tomado como referência
		- ![[formulas_cisalhamento.png]]
		- ![[exemplo_cisalhamento.png]]
	- espelhamento
		- em um espaço euclidiano, espelhar um objeto em relação a
			- uma reta -> nomerado como eixo de reflexão ou de simetria
			- um plano -> nomeado como plano de reflexão ou de simetria
			- ![[eixo_de_simetria.png]]
			- ![[formulas_espalhamento.png]]
	- rotação
		- girar em torno da origem, um objeto
		- considerando um ângulo $\theta$ qualquer em suas coordendas
		- objeto original -> translação do ponto pivo a origem -> rotação -> translação para a posição inicial
		- ![[formula_rotacao_2D.png]]
		- ![[rotacao_formula_3D.png]]
- adaptação para normaalização das operações
	- rotação e escala são feitas por meio de multiplicação
	- translação é feita por soma
	- para facilitar a combinação das operações, precisamos transformar a translação em multiplicação
	- **coordenadas homogêneas**
		- translação por produto matricial
		- transição entre sistemas de coordenadas
		- utiliza quatro valores para definir um ponto $P \begin{pmatrix} x \\ y \\ z \\ M \end{pmatrix}$ , com M = 1
		- ![[coord_homo_M1.png]]


# aula 04

### projeções geométricas

- visão humana
	- cada olho propicia uma cena de um ponto de vista diferente
	- o cérebro determina a profundidade, dada pela diferença entre as imagens fornecidas por cada olho
- projeções permitem visualizar objetos tridimensionais em um espaço bidimensional
	- R³ -> R²
	- resultando em uma planificação do objeto em uma posiçaõ específica
- definição
	- transformação geométrica específica
	- coordenadas homgêneas (uso de matrizes 4x4)
		- dado um ponto do espaço -> obter o ponto no plano equivalente
- elementos básicos
	- centro de projeção: origem dos raios de projeção
	- raio projetante: retas (virtuais) utilizadas para definir o que será interceptado
	- plano de projeção: superfície utilizada para representar o objeto (deve ser perpendicular ao eixo de direção do sistema de coordendas do ponto)
- classificação
	- a classificação depende das relações entre o centro de projeção, o plano de projeção e a inclinação das projetantes
	- podem ser paralelas ou perspectivas

![[classificao_de_projecoes.png]]

### projeções paralelas

centro de projeção no infinito (não tem um ponto fixo - ex. de ponto fixo: camêra)

**ortográfica**
- ortográfica (multiplas vistas)
	- as linhas de projeção são paralelas entre si e perperndiculares ao plano de projeção
	- mostra o objeto visto de topo, de frente e de lado
	- ![[projecao ortografica.png]] 
- axonométrica
	- representam mais de uma face do objeto
	- isométrica
		- todos os angulos no (x, y, z) são iguais
	- dimétrica
		- dois ângulos são iguais
	- trimétrica
		- três angulos são diferentes

- oblíqua
	- as linhas de projeção são paralelas entre si e constituem um determinado ângulo em relação ao plano de projeção
	- cabinet: a projeção de uma linha perperndicular ao plano é metade do comprimento que a linha em si
		- ![[obliqua cabinet.png]]
	- cavaleira: a projeção de uma linha perpendicular ao plano é de mesmo comprimento que a linha em si
		- ![[obliqua cavaleira.png]]

### projeções em perspectivas

- produz uma imagem realista do objeto
	- não reproduz suas verdadeiras medidas
	- não preserva ângulos
	- não preserva escalas
- característiacs
	- objetos mais distantes parecem menores
	- retas paralelas provocam a ilusaão que se encontram em um ponto no horizonte: ponto de fuga
- projeção de um ponto P
	- projetante (reta) é traçada ligando P ao centro de projeçaõ C
	- o ponto de projeção é a intersecção entre a projetante e o plano
- projeção de um segmento de reta definido por P e Q
	- traça a projetante dos dois pontos limitantes da reta e pega a intersecção de ambos no plano
-  pontos de fuga
	- ![[pontos de fuga.png]]

# aula 05

### rasterização: convertendo formas geométricas em pixels numa matriz
- gráficos
	- definidos por meio de primitivas geométricas
	- ponto, segmento de reta, arco de circunferência, polígonos
- dispositivos gráficos
	- matrizes de pixels
- rasterização
	- converter uma representação vetorial para matricial

algoritmos para segmento de reta -> representação matricial, tem quatro formas
1. seleção de pixels imediatamente acima e abaixo (linhas densas)
2. pixels obtidos pelo arredondamento de valores (problema do 45°)
3. cada linha vertical, seleção dos pixels mais próximos do ponto de intersecção
4. mesmo critério de 3, porém nas linhas horizontais
![[representacoes de segmentos.png]]

##### tipos de algoritmos
- algoritmo para segmentos de reta
	- dada a equação da reduzida da reta $y \space = \space y_1 \space + \space a(x\space-\space x_1)$ 
	- 
##### conversão matricial
- algoritmos para semgnetos de retas
- características desejáveis
	- linearidade
	- precisão (início e fim nos pontos especificados)
	- densidade uniforme (pixels igualmente espaçados)
	- intensidade independente da inclinação
	- continuidade
	- rapidez no traçado

##### tipos de algoritmo - algoritmos para segmentos de retas
- método incremental
	- idei básica
		- decidir se o próximo pixel terá coordenadas
		- ($x_p + 1, y$) ou 
		- algoritmo do ponto médio

##### algoritmo do "ponto médio" para segmentos de reta
- decisão central: dado um pixel o algoritmo precisa decidir qual será o próximo pixel na coluna $x_p$ + 1 
	- PI -> ($x_p$ + 1, $y_p$)
	- PS -> ($x_p$ + 1, $y_p$ + 1)
- o algoritmo calcula o ponto médio M ($x_p$ + 1, $y_p$ + 1/2)
- a variável de decisão (d): o algoritmo verifica se a linha ideal passa acima ou abaixo de M, isto é feito calculando o valor da função no ponto M
	- se d > 0 então PS
	- se d <= então PI
- a eficiência é que ele não recalcula d do zero a cada passo, ele atualiza de forma incremental usando apenas adições
	-  se $d_{anterior}$ for PI, então $d_{novo}$  é = dy
	-  se $d_{anterior}$ for PS, então $d_{novo}$  é = dy - dx

##### algoritmo do "ponto médio" para circunferências
- se d > 0 então é fora circunferência
- se d < 0 então dentro circunferência
- se d = 0 então sobre



### aliasing

efeito aliasing -> aparência serrilhada ou efeito escada
![[aliasing.png]]

#### preenchimento de polígonos

em muitos casos rasterizar não é suficiente, é necessário preeencher

**preenchimento em pares**
- usar a regra daparidade
	- paridade inicial é par (0 ou falso)
	- encontrou ponto -> inverte paridade
- como tratar vértices que são compartilhados por mais de uma aresta do polígono?
	- verifique se o pixel é um vértice
	- determine o tipo de vértice ($y_{min}$ e/ou $y_{min}$)
	- se for min e max inverte paridade e pinta o pixel
- se houver apenas um vértice na aresta
	- se for min e max -> não inverte e pinta o pixel

# aula 06

### recorte de primitivas 2D - clipping

recorte de segmentos de retas - algoritmo de cohen-sutherland

![[cohen_sutherland_segmentos.png]]

![[classificacao dos segmentos.png]]

![[teste_de_aceitacao.png]]

![[exemplo_de_recorte.png]]

