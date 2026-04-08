
## realce de imagens

objetiva melhoras a aparência de características
deve-se aplicar devido a:
 - perda de contraste
 - introdução de ruídos
 - borramento
### fenômenos

**bandas de mach**
é a tendência do olho humano de ver faixas brilhantes ou escuras perto dos limites entre áreas de iluminação nitidamente diferentes

**contraste simultâneo**
brilho aparente depende da intensidade do fundo
![[Pasted image 20260401103613.png]]

### contraste

intensidade luminosa por unidade de área

lei de Weber-Fechner
- a resposta do sistema visual humano depende de variações locais de luminânciia -> em vez da luminância absoluta
### transformações de contrates

melhorar a qualidade

aplicando sobre o intervalo de contraste $I_c$
$$Ic = L_{max} - L_{min}$$
onde L é um nível de cinza na imagem

**histograma**
permite avaliar o contraste de uma imagem

uma função T de níveis de cinza pode ser descrita como $g = T(f)$ 
- $f$ representa níveis de cinza em uma imagem dada como entrada
- $g$ representa níveis de cinza após processo de transformação
![[Pasted image 20260408082706.png]]


#### **transformações de contraste lineares**

cada ponto na imagem de entrada gera um ponto na imagem de saída
$$g = c \cdot f + b$$

em que
$$c = \frac{g_{max} - g_{min}}{f_{max} - f_{min}}$$

![[Pasted image 20260408082936.png]]

**negativo**
$$T[f(x, y)] = g(x, y) = w - f(x, y)$$
$w$ é a intensidade máxima presente na imagem

a intensidade de $g$ diminui a medida que $f$ aumenta

**alargamento de contraste**

com dois thresholds

![[Pasted image 20260408083430.png]]

**binarização**
![[Pasted image 20260408083458.png]]

#### transformações de constraste não-lineares

![[Pasted image 20260408083557.png]]

![[Pasted image 20260408083609.png]]

**correção gama**
![[Pasted image 20260408083721.png]]


### equalização de histograma

imagem original $f$ -> transformada -> $g$ -> distribuição mais uniforme

**1° etapa**
$$p_f(f_i) = \frac{n(i)}{n}$$
- distribuição discreta de probabilidade
	- $n(i)$ é número de ocorrências do nível de cinza *i*
	- $n$ é o total de pixels da imagem
	- $p_f(f_i)$ é a probabilidade do i-ésimo nível de cinza

- medidas estatísticas dos níveis de cinza
	- valor min e max
	- valor médio
	- variância
	- desvio padrão

**2° etapa**
- considerede uma imagem composta por $n = M \cdot N$  pixels
	- níveis de cinza $k = 0, 1, \dots, L - 1$
	- equalizar um histograma via $FDA(g_k)$
	- $g_k = T(f_k) = \sum_{i = 0}^{k} p_f(f_i) = \sum_{i = 0}^{k} \frac{n_i}{n}$ 

**3° etapa**
- cada valor $g_k$ é substituído pelo nível mais próximo
- ![[Pasted image 20260408090838.png]]
- ![[Pasted image 20260408090909.png]]
