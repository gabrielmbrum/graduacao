
>04/03 e 11/03 e 18/03

### sistema visual
- visão
- onda eletromagnética
	- luz tem a cor definida pelo comprimento de onda
- o que é uma imagem?
	- fonte de luz -> incide nos objetos -> refletido nos olhos
- o que é uma imagem digital?
	- são imagens armazenadas em dispositivos digitais
	- é a representação numérica de imagem
	- é uma matriz

### percepção visual

15m / 100m = x / 17mm

qual tamanhao de um objeto de 15m visto a 100m de distancia??
2,55mm é o tamanho (resolvendo a eq acima)

### tipos de sinais
- um sinal é uma manifestação de um fenômeno, expresso de forma quantitativa
- meio de uma represetanação: função
	- variáveis independentes
		- definem informações da natureza ou comportamento do fenômeno
		- sinal de voz: função de uma variável (tempo)
		- imagem: pode ser definido por uma funçõa de duas variáveis


### vizinhança

existem alguns tipos de vizinhança:
- vizinhança de 4
- vizinhança de 8
- vizinhança de 16
...

pode ser explorada tanto em *n* dimensões, em 2D, a vizinhança de 4 é:

>vizinhanca_de_4 = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] = $N_4 (f)$

já a de 8 é

>vizinhanca_de_8 = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] $\cup$ $N_4 (f)$ = $N_8 (f)$ 

exemplo de vizinhança em 3D
![[Pasted image 20260318142217.png]]

---
### conectividade

são os elementos conexos (vizinhos) que atendem algum critério de similaridade
exemplo de critério de similaridade: mesmo valor numérico

---
### adjacência

dois elementos $f_1$ e $f_2$ são adjacentes se são conexos por alguma vizinhança

dois conjuntos $C_1$ e $C_2$ se pelo menos um elemento de $C_1$ for adjacente a um elemento de $C_2$

---
### caminho

sequencia de pixels entre $(x_0, y_0)$ e $(x_M, y_M)$: $(x_0, y_0)$, $(x_1, y_1)$, $\dots$ , $(x_N, y_N)$ tal que N é o comprimento do caminho e $(x_i, y_i)$ e $(x_{i+1}, y_{i+1})$ são adjacentes

caminho-4 utiliza um caminho da vizinhança-4, então caminho-N utiliza de vizinhança-N

---
### componentes conexos

>def.: subconjunto de elementos C da imagem que são conexos entre si

dois elementos são conexos se existir caminho entre eles que esteja contido em $C$ 

---
### borda e interior

dado um conjunto C, pontos no contorno do componente conexo C

---
### medidas de distância

**regras de distância**
qualquer métrica D precisa satisfazer:
1. $D(f_1, f_2) >= 0$ 
2. $D(f_1, f_2) = D(f_2, f_1)$
3. $D(f_1, f_3) <= D(f_1, f_2) + D(f_2, f_3)$

**distância euclidiana**
![[Pasted image 20260318143654.png]]

**city-block**
![[Pasted image 20260318143716.png]]

**chessboard**
![[Pasted image 20260318143734.png]]


