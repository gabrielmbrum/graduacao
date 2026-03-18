
### conteúdo
- rasterização
- antialiasing
- poligonos

### rasterização

gráficos
dispositivos gráficos
rasterização

representação matricial, tem quatro formas
1. seleção de pixels imediatamente acima e abaixo (linhas densas)
2. pixels obtidos pelo arredondamento de valores (problema do 45°)
3. cada linha vertical, seleção dos pixels mais próximos do ponto de intersecção
4. mesmo critério de 3, porém nas linhas horizontais

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