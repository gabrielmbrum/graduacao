## enunciado

Implementar um analisador léxico usando o flex.
Entregar:
  1 - arquivo de entrada do flex
  2 - arquivo com o texto a ser analisado (entrada.txt).  Texto sem erros léxicos.
  3 - relatório (arquivo pdf contendo a decrição da linguagem regular E manual do usuário)

A linguagem regular deve conter, no mínimo:
- identificador
- números (inteiro, real)
- um caracter a ser utilizado para a atribuição
- operadores (+, - , *, )
- pontuação ,  .   ;  :
- {   }   (   )  [     ]
- pode usar o [ e ]   para delimitar comentários

Entrada: entrada.txt

Saída: imprimir na tela o token encontrado na linha x, se correto, se erro, imprimir erro léxico na linha x (por exemplo, caracter inválido).
