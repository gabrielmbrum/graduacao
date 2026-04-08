# Classificação de Imagens via Fusão de Deep Learning e Redes Complexas utilizando Redes Neurais Recorrentes

um modelo híbrido de dupla via (_Two-Stream Network_ com _Late Fusion_)

1. Deep Learning - Semântica Visuais: manter arquitetura híbrida para processar a imagem original, extraindo as características locais e globais -> 1° vetor de _embedding_ profundo.

2. Redes Complexas + RRN: extrair os descritores diretamente do grafo, variando o raio de conexão da rede complexa, extraímos sequencialmente métricas como o grau de saída e métricas ponderadas dos vértices, explorar a variação de raio como "série temporal" da expansão espacial da textura, isso alimentaria uma Rede Neural Recorrente (como uma LSTM ou GRU), processando a dinâmica de como as micro e macroestruturas se relacionam, gerando nosso segundo vetor de _embedding_.

3. Fusão Tardia (Late Fusion): Por fim, os vetores de saída da CoAtNet e da RNA seriam concatenados antes de passarem por uma camada densa (_Fully Connected_) final de classificação

---

## extração de características


A teoria dos grafos foi fundamentada por [Solutio problematis], sendo até hoje uma estrutura de dados utilizada em diversas áreas, pois é possível mapear problemas reais e complexos dentro de um grafo. A rede complexa é fruto da abstração de conceitos como redes sociais, internet, redes genéticas, redes de proteína, redes de proteína e entre outros problemas que necessitam ser estruturados para que o estudo deles se torne possível [complex networks: strucutre and dynamics]. Neste trabalho, as redes complexas serão utilizadas para análise de textura de imagens, assim como foi feito em [Texture analysis and classification], em que a imagem tem sua textura avaliada com base em um *r* escolhido, o qual pode variar para assim poder ter várias representações de uma mesma imagem. Em [Texture analysis and classification], cada pixel da imagem é mapeada como um vértice, onde a existência de uma aresta entre dois vértices é definida caso os pixels estejam há uma distância euclidiana menor que um raio *r*. No trabalho [Texture analysis and classification] apenas o grau de conectividade foi calculado, em que representa a quantidade de arestas que um vértice possui, porém outras métricas podem ser inferidas a partir desse mapeamento. Um exemplo é a medida do peso da aresta, em que [Fusion of complex networks and randomized] de acordo com o raio calculava o peso de uma aresta com base na diferença de intensidade e/ou distância dos vértices.

```
@article{euler1736solutio,
  title={Solutio problematis ad geometriam situs pertinentis},
  author={Euler, Leonhard},
  journal={Commentarii academiae scientiarum imperialis Petropolitanae},
  volume={8},
  pages={128--140},
  year={1736}
}

###

@article{BOCCALETTI2006175,
title = {Complex networks: Structure and dynamics},
journal = {Physics Reports},
volume = {424},
number = {4},
pages = {175-308},
year = {2006},
issn = {0370-1573},
doi = {https://doi.org/10.1016/j.physrep.2005.10.009},
url = {https://www.sciencedirect.com/science/article/pii/S037015730500462X},
author = {S. Boccaletti and V. Latora and Y. Moreno and M. Chavez and D.-U. Hwang},
abstract = {Coupled biological and chemical systems, neural networks, social interacting species, the Internet and the World Wide Web, are only a few examples of systems composed by a large number of highly interconnected dynamical units. The first approach to capture the global properties of such systems is to model them as graphs whose nodes represent the dynamical units, and whose links stand for the interactions between them. On the one hand, scientists have to cope with structural issues, such as characterizing the topology of a complex wiring architecture, revealing the unifying principles that are at the basis of real networks, and developing models to mimic the growth of a network and reproduce its structural properties. On the other hand, many relevant questions arise when studying complex networks’ dynamics, such as learning how a large ensemble of dynamical systems that interact through a complex wiring topology can behave collectively. We review the major concepts and results recently achieved in the study of the structure and dynamics of complex networks, and summarize the relevant applications of these ideas in many different disciplines, ranging from nonlinear science to biology, from statistical mechanics to medicine and engineering.}
}

###

@article{BACKES2013168,
title = {Texture analysis and classification: A complex network-based approach},
journal = {Information Sciences},
volume = {219},
pages = {168-180},
year = {2013},
issn = {0020-0255},
doi = {https://doi.org/10.1016/j.ins.2012.07.003},
url = {https://www.sciencedirect.com/science/article/pii/S0020025512004677},
author = {André Ricardo Backes and Dalcimar Casanova and Odemir Martinez Bruno},
keywords = {Texture analysis, Texture recognition, Complex network},
abstract = {In this paper, we propose a novel texture analysis method using the complex network theory. We investigated how a texture image can be effectively represented, characterized and analyzed in terms of a complex network. The proposed approach uses degree measurements to compose a set of texture descriptors. The results show that the method is very robust, and it presents a excellent texture discrimination for all considered classes, overcoming traditional texture methods.}
}

###

@article{RIBAS2020107189,
title = {Fusion of complex networks and randomized neural networks for texture analysis},
journal = {Pattern Recognition},
volume = {103},
pages = {107189},
year = {2020},
issn = {0031-3203},
doi = {https://doi.org/10.1016/j.patcog.2019.107189},
url = {https://www.sciencedirect.com/science/article/pii/S0031320319304893},
author = {Lucas C. Ribas and Jarbas Joaci de Mesquita {Sá Junior} and Leonardo F. S. Scabini and Odemir M. Bruno},
keywords = {Randomized neural networks, Complex networks, Texture analysis, Feature extraction},
abstract = {This paper presents a high discriminative texture analysis method based on the fusion of complex networks and randomized neural networks. In this approach, the input image is modeled as a complex network and its topological properties as well as the image pixels are used to train randomized neural networks to create a signature that represents the deep characteristics of the texture. The results obtained surpassed the accuracy of many methods available in the literature. This performance demonstrates that our proposed approach opens a promising source of research, which consists of exploring the synergy of neural networks and complex networks in the texture analysis field.}
}

###



```
