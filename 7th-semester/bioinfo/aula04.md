## 1. Redes Complexas e Interação Proteína-Proteína (PPI)
A bioinformática utiliza grafos para modelar proteínas como nós e suas interações físicas ou funcionais como arestas.
* **Análise Topológica:** Focada na identificação de *hubs* (proteínas altamente conectadas, frequentemente essenciais ou associadas a patologias) e na detecção de comunidades (agrupamentos que indicam complexos proteicos ou vias metabólicas).
* **Algoritmos de Detecção de Comunidades:** * **Louvain:** Método hierárquico que particiona a rede iterativamente para maximizar a modularidade ($Q$), uma métrica que compara a densidade de conexões internas com uma distribuição aleatória.
    * **Leiden:** Uma evolução do Louvain que corrige problemas de instabilidade e otimização prematura. Ele exige que as comunidades tenham forte densidade de conectividade interna ($D(C_k)$) antes de fundir os nós, evitando partições desconectadas.
    * **Outros:** *PageRank*, Dijkstra, Adamic-Adar e *Graph Neural Networks* (GNNs), utilizando bibliotecas como NetworkX e DGL (*Deep Graph Library*).

## 2. Montagem e Anotação Genômica
* **Montagem de Genomas:** Reconstrução *in silico* do DNA completo a partir de fragmentos curtos (*reads*) oriundos do *Next-Generation Sequencing* (NGS). 
    * *Fluxo:* Pré-processamento (corte de adaptadores), alinhamento baseando-se em sobreposições e construção contínua (podendo ser *De novo* ou baseada em referência). Softwares como Pilon e Racon atuam na correção de erros (fechamento de *gaps*).
* **Anotação Genômica:** Conversão de dados brutos em conhecimento funcional. Divide-se em anotação estrutural (localização de genes e elementos regulatórios) e funcional (associação a processos metabólicos). Utiliza ferramentas como BLAST, Gene Ontology (GO) e modelos modernos de *Deep Learning* (como a arquitetura Transformer no DNABERT e redes RNNs/LSTMs) para predição contextual.

## 3. Análise de Expressão Gênica
Consiste em quantificar as cópias de transcritos de RNA mensageiro (mRNA) derivadas do DNA, revelando quais genes estão "ligados" ou "desligados" em condições fisiológicas específicas.
* **Técnicas de Leitura:** O RNA-Seq destaca-se por sequenciar diretamente o RNA, quantificando isoformas e descobrindo novos genes com alta precisão. Microarrays e qPCR também são utilizados. Bibliotecas como `scanpy` processam esses *datasets*.
* **Aplicações:** Vital na oncologia para verificar a inibição de crescimento tumoral pós-tratamento, na busca por biomarcadores de doenças e no melhoramento genético agropecuário (criação de cepas transgênicas mais resistentes).

## 4. Modelagem Estrutural de Proteínas
Predição da arquitetura tridimensional (3D) de uma proteína a partir da sua sequência linear de aminoácidos, contornando a lentidão e o alto custo das validações experimentais (Cristalografia de Raios-X e RMN).
* **Métodos Dependentes de Molde (Modelagem Comparativa):** Segue quatro etapas críticas: (1) Seleção da proteína-molde no PDB usando BLAST; (2) Alinhamento estrutural; (3) Construção do modelo adotando princípios de restrições espaciais e corpos rígidos; (4) Avaliação e refinamento do modelo.
* **Gráfico de Ramachandran:** Ferramenta termodinâmica e estérica mandatória para avaliação. Ele plota os ângulos diédricos de torção $\phi$ (phi) e $\psi$ (psi) formados pelas ligações peptídicas do esqueleto da molécula. Um modelo proteico confiável exige que no mínimo 90% dos seus resíduos situem-se nas zonas permitidas do gráfico (regiões equivalentes a hélices-$\alpha$ e folhas-$\beta$).

## 5. Metagenômica
Área voltada ao estudo integral de comunidades de microrganismos (microbiomas) sem a necessidade prévia de isolamento e cultura em placas de Petri.
* **Processamento:** O DNA ambiental total é extraído, fragmentado e sequenciado. Os algoritmos mapeiam as sequências contra genomas de referência para estabelecer Unidades Taxonômicas Operacionais (OTUs) e quantificar genes/vias metabólicas.
* **Classificação Ultrarrápida:** Uso do algoritmo **Kraken2**, que emprega correspondência exata de *k-mers* associados a tabelas de *hash* para varrer volumes massivos de dados ambientais de forma extremamente rápida.