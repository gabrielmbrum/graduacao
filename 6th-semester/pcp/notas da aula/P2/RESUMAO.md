
# intro a HPC

### a necessidade do paralelismo e o gargalo
- **O Problema:** Problemas complexos (como previsão do tempo) exigem trilhões de operações. Uma única CPU, mesmo rápida, levaria horas demais (o exemplo mostra 27,8 horas para algo que precisa ser feito em minutos).
    
- **A limitação física:** Não é só aumentar o clock da CPU. Existe um limite físico (velocidade da luz) no tempo que leva para buscar dados na memória. Isso cria uma latência inevitável.
    
- **Gargalo de Von Neumann:** A arquitetura clássica obriga o acesso sequencial a dados e instruções, o que trava o desempenho. A solução é usar paralelismo (múltiplas CPUs acessando memórias separadas/caches)

### taxonomia de Flynn
classifica o fluxo de instruções e dados em:
- **SISD (Single Instruction, Single Data):** O computador convencional (um processador, um dado por vez).
    
- **SIMD (Single Instruction, Multiple Data):** Computadores vetoriais ou GPUs. Uma ordem comanda vários dados ao mesmo tempo.
    
- **MIMD (Multiple Instruction, Multiple Data):** Paralelismo real. Vários processadores fazendo coisas diferentes com dados diferentes (clusters modernos)

### arquitetura de memória (UMA vs NUMA)
- **UMA (Uniform Memory Access):** O tempo para acessar qualquer dado é o mesmo para todos os processadores (todos "veem" a memória igual).
    
- **NUMA (Non-Uniform Memory Access):** O tempo muda. Se o dado está na memória "local" do processador, é rápido. Se está na memória de outro processador, é mais lento. É o padrão em grandes sistemas atuais.

---

# processadores HPC

### CISC x RISC
são formas de estrutura os conjuntos de instruções do processador, mudando seus padrões de codificação e execução

dificuldade inicial do RISC
- falta de 