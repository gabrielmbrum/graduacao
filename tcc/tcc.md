
## 1. starter pack do lipai

coletanea de técnicas de processamento de imagens
- source
- exemplos
- utilização
- referências

coletanea de modelos classificatórios (várias arq)
- inicialmente, seriam poucas
- source
- exemplos
- utilização / motivação
- referências

datasets
- source (k-fold por exemplo)
- imagens
- propriedades e resultados parecidos

## 2.  aprofundamento nas imagens geradas artificialmente

qual maneira de avaliar?
- entropias
- estatísticos
- probabilísticos
- resultado em classificações
- análise de textura?

quais técnicas de aumento?
- GAN
- DDPM
- CN

## 3. RNN 

m modelo híbrido de dupla via (_Two-Stream Network_ com _Late Fusion_). Além disso, essa abordagem nos permite aproveitar o embasamento teórico sobre arquiteturas de Redes Neurais Recorrentes (RNRs) que venho construindo recentemente para a redação do artigo da minha disciplina, otimizando nosso tempo e aprofundando a pesquisa.

1. Via Deep Learning (Semântica Visuais): Manteríamos o uso da arquitetura híbrida combinando CNNs e Transformers (como a CoAtNet) para processar a imagem original, extraindo as características locais e globais. Isso geraria nosso primeiro vetor de _embedding_ profundo.

2. Via Topológica (Redes Complexas + RNA): Em vez de mapearmos as medidas topológicas de volta para o espaço da imagem para gerar dados sintéticos, extrairíamos os descritores diretamente do grafo. Ao variarmos o raio de conexão da rede complexa, extraímos sequencialmente métricas como o grau de saída e métricas ponderadas dos vértices. A grande inovação aqui é tratar esse aumento paramétrico do raio como uma "série temporal" da expansão espacial da textura. Esse vetor sequencial alimentaria uma Rede Neural Recorrente (como uma LSTM ou GRU). A RNA processaria a dinâmica de como as micro e macroestruturas se relacionam, gerando nosso segundo vetor de _embedding_ topológico.

3. Fusão Tardia (Late Fusion): Por fim, os vetores de saída da CoAtNet e da RNA seriam concatenados antes de passarem por uma camada densa (_Fully Connected_) final de classificação. Dessa forma, a decisão do modelo é fundamentada tanto no aprendizado semântico automático da IA quanto na exatidão da modelagem matemática da textura extraída pela Rede Complexa. Acredito que essa abordagem não só aproveita grande parte da revisão bibliográfica e implementação que já fizemos, mas também eleva a complexidade técnica para o nível de um excelente TCC, explorando um conceito moderno de aprendizado multimodal.

