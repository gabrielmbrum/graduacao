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

---

# aula 02
### OpenGL

##### definição
- é uma API para aplicações gráficas 2D e 3D
- implementado em C
- são rotinas de baixo nível

##### pipeline
- descreve um processo que pode ter dois ou mais passos distintos
![[pipeline opengl.png]]

#### morfologia das funções
biblioteca + nome da função + número de variáveis + tipo de variáveis

### definições dos comandos

*glClear()*
- inicializa as combinações de matrizes para escrita com cores
- os componentes RGB são geralmente referenciados como color buffer ou pixel buffer

*glutSwapBuffers()*
- faz com que qualquer comando não executado seja executado

*glClearColor()*
- inicializa a cor de fundo
- parametro aplha define coisas como transparencia e tals (deixa "frufru")

*glutMainLoop()*

---

compilação dos códigos

■ sudo apt update
■ sudo apt install freeglut3-dev
○ gcc <fonte.c> -o <fonte> -lglut -lGL -lGLU –lm