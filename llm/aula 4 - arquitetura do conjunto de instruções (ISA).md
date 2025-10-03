
### hierarquia
1. físico
2. dispositivos
3. portas/registradores
4. micro arquitetura
5. **ISA**
6. linguage de máquina
7. linguagem assembly
8. linguagem de programação
9. algoritmo
10. aplicação

### base de funcionamento

a ISA corresponde aos níveis de linguagem de montagem e de linguagem de máquina

o compilador traduz uma linguagem de alto nível, que é independente de arquitetura, na linguagem assembly, que é dependente da arquitetura

o assembler traduz programas em linguagem assembly em códigos binários executáveis

a ISA é a interface entre o software e o hardware, os compiladores transformam uma linguagem de alto nível para uma linguagem de nível ISA

quais instruções o ISA disponibiliza?
1. quais as instruções disponíveis
2. qual modelo de memória utilizado
3. quais e quantos registradores existem
4. quais os ipos de dados suportados

### compiladores

a ISA fornece elementos essenciais para os compiladores, como os modos de endereçamento, conjunto de instruções e registradores de propósito geral

### montadores

o montador deve compreender total a ISA do processador alvo

mapeamento de símbolos: tradução de símbolos (como rótulos e variáveis) em endereços de memória ou registradores corretos

otimização de código, assim como o compilador faz, para manter o código eficiente

### compilador x interpretador


| Tradutor   | Vantagens                         | Desvantagens                           |
| ---------- | --------------------------------- | -------------------------------------- |
| compilador | execução veloz                    | várias etapas de tradução              |
|            | programas mais complexos          | maior consumo de memória para execução |
|            | permite otmização de código fonte | ....                                   |
|            |                                   |                                        |
|            |                                   |                                        |
|            |                                   |                                        |
|            |                                   |                                        |
### tipos de isntruções

o conjutno de instruões são as operações que um processador (microprocessador, microcontrolador, CPU ...) fornece para o programador, é a representação em mnemônicos do código de máquina

os elementos mais usados no projeto de instruçoes são:
- repertório de operações
- tipos de dados
- formato das instruções
- registradores
- modos de endereçamento

---

# Simulador x86

simulador EMU8086






























