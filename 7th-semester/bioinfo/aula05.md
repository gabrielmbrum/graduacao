## 1. Alinhamento de Sequências
* **Alinhamento Global (Needleman-Wunsch):** Baseado em programação dinâmica, cria uma matriz de pontuação (considerando *matches*, *mismatches* e penalidades de *gap*) para alinhar sequências inteiras. O *traceback* reconstrói o alinhamento ótimo.
* **Alinhamento Local (Smith-Waterman):** Ideal para achar sub-regiões de similaridade em sequências longas.
* **Alinhamento Múltiplo (MSA - Clustal Omega):** Usa heurísticas de *k-tuple* para gerar matrizes de distância e árvores guias (*guide trees*), realizando alinhamentos progressivos e baseados em Modelos Ocultos de Markov (HMM).
* **Heurísticos (BLAST):** Divide a *query* em *k-mers* (*seeds*), filtra pontuações promissoras e estende os alinhamentos bidirecionalmente, gerando *High-scoring Segment Pairs* (HSPs) avaliados estatisticamente pelo *E-value*.
* **Probabilísticos (HMMER):** Utiliza Modelos Ocultos de Markov para detectar padrões evolutivos complexos (substituições, inserções, deleções) e buscar domínios proteicos conservados.

## 2. Interação Proteína-Proteína (PPI)
* Modela proteínas como nós e interações como arestas para detecção de módulos funcionais ou vias metabólicas.
* **Algoritmo de Louvain:** Método hierárquico voltado para a detecção de comunidades através da otimização da modularidade da rede.
* **Algoritmo de Leiden:** Uma evolução do Louvain que corrige problemas de instabilidade e otimização prematura, evitando a fusão inadequada de comunidades.

## 3. Montagem de Genomas
Reconstrução de sequências completas a partir de *reads* curtos.
* **Montagem *De Novo* (SPAdes):** Não exige genoma de referência. Utiliza **Grafos de De Bruijn**, onde vértices são *k-mers* sobrepostos e arestas são as transições. O algoritmo lida com hibridização de dados (leituras curtas e longas) e otimiza a formação de *contigs* e *scaffolds*.
* **Baseada em Referência (BWA):** O *Burrows-Wheeler Aligner* mapeia *reads* curtos contra um genoma conhecido. Constrói um índice eficiente via transformação de Burrows-Wheeler e exporta as coordenadas de alinhamento em formatos padronizados (SAM/BAM).

## 4. Anotação Genômica
Identificação estrutural e funcional de genes (códons de início, parada e *Open Reading Frames* - ORFs).
* **Glimmer:** Voltado para procariotos, utiliza Modelos de Markov Interpolados (IMM) para identificar ORFs e refina predições resolvendo sobreposições de sequências.
* **GeneMark:** Utiliza Modelos de Markov (e HMMs em versões avançadas) treinados para distinguir estatisticamente regiões codificantes de não codificantes, considerando a probabilidade de transição entre os nucleotídeos.

## 5. Análise de Expressão Gênica
Focada em quantificar transcritos (mRNA via RNA-Seq) e achar Genes Diferencialmente Expressos (DEGs).
* **DESeq2:** Algoritmo de normalização e modelagem estatística. Como dados de RNA-Seq são contagens discretas altamente variáveis, o DESeq2 utiliza uma regressão baseada na **Distribuição Binomial Negativa** para lidar com a superdispersão dos dados de forma robusta e extrair significância biológica (ex: vias de apoptose, proliferação).