
antes de falarmos de CUDA, vamos falar de GPU de maneira geral primeiro

### introdução

começou com o desenvolvimento de APIs que permitissem a programação das placas gráficas em alto nível

a dificuldade era desenvolver os programas em DirectX (já utilizado em GPU) para fazer o processamento de calculos númericos pesados

### bibliotecas
desenvolvidas para trabalhar com GPU
- CUDA
- OpenCL
- OpenACC

### arquitetura de GPUs

arquitetura massivamente paralela

os núcleos de processamento são direcionados a operações aritméticas

um alto grau de paralelismo aumenta desempenho

### Graphical Processing Units

iniciaram a lançar familias de GPUs com enfoque para processamento aritmético SEM saída para tela (processamento gráfico nõa era o principal objetivo)

séries da NVIDIA:
- Tesla (2008)
- Fermi (2011)
- Kepler (2012)
- Ampere (2020)
- Hopper (2022)

### programação

as diferenças de arquitetura tornam a programação sensível ao contexto, um programa otimizado para uma GPU pode não funcionar bem em outra

CPU acessa a memória principal, por meio de transferencia para a cache

a GPU também possui cache, mas ela não faz acesso a memória principal, pois o acesso é muito mais lento do que a CPU, então deve-se evitar ao máximo a transferência de dados entre memória principal e GPU. para isso, deve-se transferir o máximo de volume de dados por vez.