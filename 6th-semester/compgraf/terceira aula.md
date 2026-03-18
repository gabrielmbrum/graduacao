### Gŕaficos 3D

projeção geométrica
- visão humana
	- cada olho propicia uma cena de um ponto de vista diferente
	- o cérebro determina a profundidade, dada pela diferença entre as imagens fornecidas por cada olho
- projeções permitem visualizar objetos tridimensionais em um espaço bidimensional
	- R³ -> R²
- características
	- transformação geométrica específica
	- coordenadas homgêneas (uso de matrizes 4x4)
		- dado um ponto do espaço -. obter o ponto no plano equivalente
- elementos básicos
	- centro de projeção
	- raio projetante
	- plano de projeçaõ

tipos de projeção
- paralela
- perspectiva

### projeções paralelas

centro de projeção no infinito (não tem um ponto fixo - ex. de ponto fixo: camêra)

**ortográfica**
- multiplas vistas
	- mostra o objeto visto de topo, de frente e de lado
	- vejo uma face do objeto por vez
- axonométrica
	- representam mais de uma face do objeto
	- isométrica
		- todos os angulos no (x, y, z) são iguais
	- dimétrica
		- dois ângulos são iguais
	- trimétrica
		- três angulos são diferentes

**oblíqua**
- as linhas de projeção são paralelas entre si e constituem um determinado ângulo em relação ao plano de projeção
- cabinet
	- a linha perperndicular ao plano é meaded do comprimento que a linha em si
- cavaleira

### projeções em perspectivas

produz uma imagme realista do objeto
- não reproduz suas verdadeiras medidas
- não preserva ângulos
- não preserva escalas

 pontos de fuga
 - matrzes foram determinadas em relação aos cnetros de projeção
 - relação de cada matriz com o ponto de fuga