
### OpenGL - rasterização

GL_POINTS -> cada vértice é um ponto

GL_LINES -> cada par de vértices gera um segmento de linha independente

GL_LINE_LOOP -> desenha um grupo de segmentos de linhas, conectando o primeiro ao último vértice

GL_LINE_STRIP -> desenha um grupo de segmentos de linhas conectados do primeiro ao último vértice

---
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
		- ![[formula_rotacao_2D.png]]
		- ![[rotacao_formula_3D.png]]
		- 
