### introdução

FPGA
- é um circuito integrado
- possui uma matriz de portas programáveis em campo (após ser fabricado)

ASIC
- application specific integrated circuit
- é customizado para uma aplicação específica, visando otimização

### problema

> por que trabalhar com software híbrido envolvendo à integração de linguagens de alto nível com linguagens de montagem?

por otimização, desemepenho e acesso a baixo nivel

### lm - linguagem de montagem

assembly ou linguagem de montagem é uma notaçaõ legível para o código de máquina

utilizada para dispositivos como microprocessadores e microcontroladores

linguagem assembly x assembler
- um é a linguagem, o outro é o tradutor para código de máquina

há diferenteças entre a sintaxe da Intel e AT&T

### montador x compilador

montador tem a arquitetura adjacente do hardware onde o código irá ser executado

é diferente do executável do compilador, que é utilizavel em qualquer grupo de arquitetura do hardware


### hardware adjacente - Intel 80386

para LM, o programador precisa conhecer o *hw* da máquina, por exemplo o INtel 80386 tem 8 registradores

- **ESP e EBP:** usados para pilha, ESP fica com o topo e EBP é usado para andar sobre ela
- **EAX (acumulador):** utilizado em operações aritméticas, acesso de portas de entrada e saída, transferência de dados...
- **EBX (base):** utilizado como ponteiro de acesso à memória, índice e auxiliar às operações aritméticas do registrador EAX
- **ECX (contador):** servir de contador para os laços de repetição
- **EDX (dados):** usado em operações aritméticas, junto do EAD, recebe o resto da divisão e o produto da multiplicação, acesso de portas de I/O...
- **ESI e EDI:** movimentação de dados, guardando o endereço fonte de uma variável (ESI) e guardando o endereço do destino (EDI)
