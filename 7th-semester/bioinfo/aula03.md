## 1. Genômica e Dogma Central da Biologia Molecular
* **Projeto Genoma Humano:** Mapeamento de 3,3 bilhões de pares de nucleotídeos, processo que demandou e impulsionou o desenvolvimento de algoritmos de armazenamento, alinhamento e predição de genes.
* **Dogma Central (Crick, 1958):** Estabelece o fluxo da informação genética em três processos:
  1. **Replicação:** Duplicação do DNA mediada pela DNA polimerase.
  2. **Transcrição:** Síntese de RNA mensageiro (mRNA) a partir de um molde de DNA, catalisada pela RNA polimerase.
  3. **Tradução:** Decodificação do mRNA pelos ribossomos para a síntese de cadeias polipeptídicas (proteínas).
* **Exceção (Retrovírus/HIV):** O vírus HIV burla o dogma ao utilizar a enzima *transcriptase reversa* para transcrever seu RNA viral em DNA (*cDNA*), que é posteriormente integrado ao genoma da célula hospedeira.

## 2. Biologia Celular e Homeostase
* **Homeostase:** Manutenção do equilíbrio termodinâmico e químico interno (como pH e glicemia) mediante sistemas de controle por retroalimentação negativa (*feedback* negativo).
* **Impacto da Bioinformática:** Fornece ferramentas para a modelagem in silico e simulação de vias metabólicas, processamento de dados ômicos para descoberta de biomarcadores e fundamentação da medicina personalizada baseada em perfis genéticos.

## 3. Algoritmos de Alinhamento de Sequências
* **Modelos de Programação Dinâmica (Métodos Exatos):** * **Needleman-Wunsch (1970):** Algoritmo de alinhamento **global** de complexidade $O(mn)$. Computa uma matriz de transição aplicando pontuações para *matches*, *mismatches* e penalidades de *gap*, definindo o alinhamento ótimo através de *backtracking*.
  * **Smith-Waterman (1981):** Algoritmo de alinhamento **local**. Diferencia-se do alinhamento global ao impedir a propagação de pontuações negativas na matriz (valores $< 0$ são substituídos por $0$), forçando o algoritmo a extrair exclusivamente as sub-regiões de maior homologia.
* **Modelos Heurísticos:**
  * **BLAST (1990):** Otimiza o custo computacional particionando a sequência de consulta em fragmentos curtos chamados *word seeds* (*k-mers*). Ao rastrear correspondências no banco de dados, o BLAST realiza uma extensão bidirecional da semente até que o *score* limite seja atingido. O resultado é validado estatisticamente pelo *E-value*.

## 4. Predição Estrutural e Ferramentas Computacionais
* **Bancos de Dados Operacionais:** Repositórios de nucleotídeos (GenBank, ENA, DDBJ), proteínas (UniProt, PDB) e classificadores funcionais/famílias (Pfam, KEGG).
* **Estrutura de Proteínas:** Historicamente dependente de métodos experimentais demorados, como a Cristalografia de Raios-X e a Criomicroscopia Eletrônica. 
* **AlphaFold / ColabFold:** Abordagem computacional baseada em *Deep Learning* que prevê a estrutura terciária e quaternária de proteínas a partir da sequência primária, utilizando *Multiple Sequence Alignments* (MSA) e extração de covariância evolutiva.
* **Biopython:** Biblioteca Python dedicada à bioinformática, permitindo a automação do *parsing* de arquivos (ex: FASTA, A3M) e execução de alinhamentos diretos em servidores remotos (ex: API `NCBIWWW.qblast`).