
>*Support Vector Machine*

### introdução

SVM é um algoritmo de aprendizado de máquina supervisionado, que calcula um hiperplano ótimo para classificar novas amostras

ideia-chave
- construir hiperplanos de decisão, que definem limites de decisão no espaço de atributos
- modelar o problema de classificação como um problema de otimização matemática, visando encontrar o "melhor hiperplano"

inicialmente, vamos considerar um problema de classificação binário, que pode ser modelado como um problema de separação de classes no espaço de atributos de entrada, $X \subset \mathbb{R}^m$

>qual é a melhor escolha de reta divisora?

### conceitos

**margem máxima**
- intuição: quanto mais longe uma instância de dados estiver do limite de decisão, maior será seu grau de confiabilidade na predição
- ![[Pasted image 20260417082118.png]]
- distância da instância $x^{(i)}$ até o hiperplano separador é $r = \frac{ |w^T x^{(i)} + b| }{ ||w|| }$
- as instâncias mais próximas do separador são os vetores de suporte (pontos circulados na imagem acima)
- margem $p$ do separador: é a distância entre os dois hiperplanos de suporte (linhas tracejadas paralelas a fronteira de decisão)
- proposta: maximizar $p$

### modelagem matemática

![[Pasted image 20260417083017.png]]
![[Pasted image 20260417083419.png]]
![[Pasted image 20260417083745.png]]
![[Pasted image 20260417084054.png]]
![[Pasted image 20260417084459.png]]
![[Pasted image 20260417084807.png]]
![[Pasted image 20260417085001.png]]
![[Pasted image 20260417085553.png]]
![[Pasted image 20260417091421.png]]
![[Pasted image 20260417091436.png]]
![[Pasted image 20260417091451.png]]

#### modelagem rígida
![[Pasted image 20260417091537.png]]
![[Pasted image 20260417091614.png]]

#### modelagem suave
![[Pasted image 20260417091710.png]]
![[Pasted image 20260417091755.png]]
![[Pasted image 20260417092800.png]]

### SVM não linear

![[Pasted image 20260417095039.png]]
![[Pasted image 20260417095051.png]]
![[Pasted image 20260417095232.png]]

#### o truque do kernel
![[Pasted image 20260417095251.png]]
![[Pasted image 20260417095300.png]]
![[Pasted image 20260417095308.png]]
![[Pasted image 20260417095320.png]]
![[Pasted image 20260425094620.png]]
![[Pasted image 20260425094636.png]]
![[Pasted image 20260425094646.png]]
![[Pasted image 20260425094654.png]]
![[Pasted image 20260425094709.png]]

### conclusão
![[Pasted image 20260425094751.png]]
![[Pasted image 20260425094759.png]]
