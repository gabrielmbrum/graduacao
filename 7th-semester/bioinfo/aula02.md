## 1. Biologia Molecular e Genômica
* **Genoma e DNA:** O genoma representa o material genético completo de um organismo. O DNA é a molécula de fita dupla que armazena essas informações genéticas através da estrutura de nucleotídeos e bases nitrogenadas específicas (A-T, C-G).
* **Genes, RNA e Proteínas:** Genes são trechos de DNA contendo as instruções de codificação para a síntese proteica. O fluxo de informação biológica ocorre pela transcrição do gene em RNA mensageiro (mRNA) e sua posterior tradução no ribossomo, onde o RNA transportador (tRNA) encadeia aminoácidos para formar a proteína funcional.
* **Divisão Celular:** A mitose consiste na duplicação de células somáticas, resultando em células diplóides genotipicamente idênticas ($2n \rightarrow 2n$). A meiose, restrita às células germinativas, gera quatro células haplóides, introduzindo variabilidade genética através do processo de *crossing-over* ($2n \rightarrow n$).

## 2. Algoritmos Clássicos de Alinhamento
* **Programação Dinâmica:** Tratam-se de métodos matemáticos exatos que empregam matrizes de pontuação baseadas em pesos para *matches* (+1), *mismatches* (-1) e penalidades para lacunas (*gaps*).
  * **Needleman-Wunsch:** Executa o alinhamento global, forçando a correspondência por toda a extensão de duas sequências (ideal para pares de tamanho similar).
  * **Smith-Waterman:** Realiza o alinhamento local, focando na extração de sub-regiões (domínios) de maior similaridade evolutiva, ignorando extremidades que divergem.
* **FASTA:** Algoritmo pioneiro de natureza heurística estruturado para alinhamentos locais. Avalia similaridades usando estatísticas como o *E-value*, que quantifica a expectativa matemática de o alinhamento ocorrer de forma aleatória. O padrão correlato FASTQ armazena dados oriundos de sequenciadores com marcações ASCII denotando a qualidade da leitura.
* **BLAST (Basic Local Alignment Search Tool):** Otimizou drasticamente o custo computacional reduzindo o espaço de busca. O sistema particiona a sequência alvo em *word seeds* (palavras-chave curtas). Ao identificar um *match* preliminar da *seed* contra um banco de genomas, o BLAST expande a zona de alinhamento de forma heurística e bidirecional até a pontuação deixar de ser significativa. O pacote dispõe de variações de alvos, como BLASTn (nucleotídeo), BLASTp (proteína) e BLASTx (tradução cruzada).

## 3. Aplicações Práticas da Bioinformática
* **Diagnóstico e Genética:** Mapeamento de padrões de mutação tumoral e uso do sequenciamento de nova geração (NGS) na triagem genética pré-concepcional, permitindo antecipar predisposições ou distúrbios genéticos hereditários.
* **Medicina Personalizada:** Desenvolvimento de tratamentos direcionados às variações precisas mapeadas no perfil genômico individual do paciente.
* **Ciência Forense:** Rastreio e elucidação de investigações criminais com alta precisão a partir de vestígios e amostras biológicas.