
### sistemas de coordenadas

sistemas de coordenadas -> sistema de referência
- define a unidade de referência básica
- determina limites extremos para descrever o objeto

SRU (Sistema de Referência do Universo)
SRD (Sistema de Refrência do Dispositivo)

### transformação janela | porta de visão | window-to-viewport

### clipping

recorte de segmentos de retas
- para cada x e y, deve-se verificar se ele está entre $x_{min}$ e $x_{max}$ 

cohen-sutherland
- classificaçaõ dos segmentos
- vérticies do segmento -> classificados com base em cada semiplano que delimita a janela
- **plano dividido em 9 regiões**
	- 1° bit -> semiplano acima da aresta superior y > y_{max}
	- 2° bit -> semimplano abaixo da aresta inferior y < y_{min}
	- 3° bit -> semiplano à diretira da aresta direita x > x_{max}
	- 4° bit -> semiplano à esquerda da aresta esquerda x < x_{min}
- teste de aceitação ou rejeição
	- rejeita -> codigo(P1) .and. codigo(P2) != 0
	- aceita -> codigo(P1) .== 0 and. codigo(P2) == 0
	- avaliar -> caso contrário -> **clipping!!!!**

como encontrar os pontos de corte?
- encontrar o *coeficiente anguar*
	- a = (y1 - y0)/(x1 - x0)
- aplicar na equação
	- y = (y1 - y0)/(x1 - x0) * (xmin - x0) + y0
	- x = (y1 - y0)/(x1 - x0) * (ymin - y0) + x0

recortes de polígonos
- 