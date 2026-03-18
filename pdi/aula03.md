### vizinhança

existem alguns tipos de vizinhança:
- vizinhança de 4
- vizinhança de 8
- vizinhança de 16
...

pode ser explorada tanto em *n* dimensões

em 2D, a vizinhança de 4 é:

vizinhanca_de_4 = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

### conectividade

são os elementos conexos (vizinhos) que atendem algum critério de similaridade

### adjacência

dois elementos $f_1$ e $f_2$ são adjacentes se são conexos por alguma vizinhança

### caminho

sequencia de pixels entre $(x_0, y_0)$ e $(x_N, y_N)$, tal que N é o comprimento do caminho e $(x_P, y_i)$ e $(x_{1+P}, y_{1+i})$ são adjacentes

caminho-4 só utiliza um caminho da vizinhança-4, então caminho-N utiliza de vizinhança-N

### componentes conexos

>def.: subconjunto de elementos C da imagem que são conexos entre si


