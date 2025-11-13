### ANN - Artificial Neural Networks (Redes Neurais Artificiais)

- **O que é?**
    
    - No contexto de simulações físicas, uma ANN é um modelo de _machine learning_ usado como um **"modelo substituto" (surrogate model)**.  
        
    - Ela é treinada para substituir um passo específico, lento e computacionalmente caro da simulação física, em vez de executar todo o cálculo algorítmico.  
        
    - O objetivo principal é **acelerar drasticamente** a simulação geral, permitindo previsões em tempo real.  
        
    - Como visto na Figura 14 do artigo de pesquisa, um exemplo principal é usar a ANN para acelerar o **passo de projeção de pressão** , que é um gargalo notório em _solvers_ de fluidos incompressíveis.  
        
- **Como faz? (Duas Abordagens Principais)**
    
    - **1. Modelo Substituto Baseado em Dados (O que você descreveu):**
        
        - **Treinamento:** O processo é supervisionado e aprende com dados históricos.
            
        - **Dados de Treinamento:** Milhares de simulações físicas tradicionais de alta fidelidade são executadas para gerar um conjunto de dados gigante.  
            
        - **Extração de Características:** Para cada passo da simulação, extrai-se as `Entradas` (o estado do problema) e a `Saída` (o resultado real da simulação, ou **"Ground Truth"**).  
            
        - **Função de Perda (Loss):** A rede neural compara sua predição (ex: o campo de pressão previsto) com a `Pressão` do "Ground Truth". O erro é usado para ajustar os pesos da rede (via _backpropagation_).  
            
        - **Entradas (Feature vector):** A rede é alimentada com um vetor que descreve o estado atual _antes_ do cálculo caro. Isso inclui:
            
            - **Velocity** (O campo de velocidade atual, possivelmente divergente).
                
            - **Level set** (Uma função que descreve onde está a superfície do fluido).
                
            - **Pressure** (O campo de pressão _antes_ da projeção).
                
            - **Boundary conditions** (Condições de contorno, ex: paredes).  
                
        - **Saídas:** A rede retorna o resultado do passo que ela está substituindo. No caso da Figura 14, a saída é o campo de **Pressure** final, corrigido e fisicamente plausível.  
            
    - **2. Modelo Informado pela Física (PINNs - Physics-Informed Neural Networks):**
        
        - Esta é uma abordagem mais avançada que _não_ requer dados de "Ground Truth" da simulação.
            
        - **Treinamento (Como faz?):** A ANN não aprende com pares de entrada-saída. Em vez disso, ela aprende a _resolver_ a própria equação física.  
            
        - **Diferenciação Automática (AutoDiff):** A rede usa a diferenciação automática para calcular as derivadas de suas saídas (ex: velocidade) em relação às suas entradas (ex: posição x, y, z).  
            
        - **Função de Perda (Loss):** A "Loss" é o **"resíduo"** das Equações Diferenciais Parciais (PDEs) governantes (como as equações de Navier-Stokes). A rede é treinada para encontrar os pesos que tornam o resíduo da PDE o mais próximo de zero possível, forçando a rede a satisfazer as leis da física.  
            
        - **Estruturas (Frameworks):** Ferramentas como o **NVIDIA PhysicsNeMo** são projetadas especificamente para construir esses modelos, combinando dados de simulação com causalidade orientada pela física.  
            
- **Comparação**
    
    - **Métodos Clássicos (Solvers de Pressão):** São **iterativos** (ex: _solvers_ de Poisson) e computacionalmente caros, podendo consumir a maior parte do tempo de simulação.  
        
    - **ANN (Modelo Substituto):** Substitui o _solver_ iterativo por uma única **consulta (forward pass)** na rede neural, que é quase instantânea.  
        
    - **PINN:** É o próprio _solver_. Ele usa malhas mais grosseiras (cursor meshes) para alcançar precisão comparável, pois as derivadas são calculadas analiticamente (via AutoDiff) e não por discretização.  
        

### NeRF - Neural Radiance Fields

- **O que é / O que faz?**
    
    - NeRF é um método para **síntese de novas visualizações (novel view synthesis)**.  
        
    - Ele representa uma cena 3D estática não como uma malha ou _voxels_, mas como uma **função 5D contínua**.  
        
    - Esta função é um Perceptron Multicamadas (MLP) simples (uma rede neural) que codifica toda a cena nos pesos da rede.  
        
    - Ele consegue resultados fotorrealistas de alta fidelidade, especialmente na captura de efeitos de luz complexos que superam os métodos clássicos.  
        
- **Como faz?**
    
    - **Entradas (5D):** A rede recebe duas entradas:
        
        1. **Posição espacial 3D:** (x,y,z)
            
        2. **Direção de visualização 2D:** (θ,ϕ).  
            
    - **Saídas (4D):** A rede produz duas saídas para aquele ponto no espaço:
        
        1. **Cor (RGB):** A cor emitida (r,g,b).
            
        2. **Densidade Volumétrica (σ):** A opacidade ou probabilidade de um raio parar naquele ponto.  
            
    - **A Inovação (Separação 5D):** Para capturar reflexos realistas, a arquitetura é projetada de forma que:
        
        - A **Densidade (σ)** depende _apenas_ da localização (x,y,z).
            
        - A **Cor (RGB)** depende _tanto_ da localização (x,y,z) _quanto_ da direção de visualização (θ,ϕ).  
            
        - Isso permite que o NeRF aprenda reflexos especulares (brilhos) que mudam dependendo do ângulo de visão.  
            
    - **Treinamento (Loss Function):**
        
        - O processo é "naturalmente diferenciável".  
            
        - A função de perda é simplesmente o erro quadrático (squared error) entre a cor do pixel renderizado pela rede e a cor do pixel da imagem original de treinamento.  
            
        - Isso é feito para todos os pixels em um _batch_ de raios de várias imagens de diferentes perspectivas.  
            
    - **Codificação Posicional (Positional Encoding):** Para capturar detalhes finos e de alta frequência (como texturas e geometria complexa), as entradas (x,y,z,θ,ϕ) são mapeadas para um espaço de dimensão superior usando funções de seno e cosseno. Sem isso, a rede produziria resultados borrados.  
        
- **Renderização**
    
    - O NeRF usa **Renderização Volumétrica Clássica**.  
        
    - Para cada pixel, um raio é lançado da câmera. O NeRF consulta a rede neural em múltiplos pontos (amostras) ao longo desse raio (o que você chamou de _Ray Marching_).  
        
    - As cores (RGB) e densidades (σ) de todas as amostras ao longo do raio são então compostas (acumuladas) para produzir a cor final do pixel.  
        
- **Comparação (com Fotogrametria)**
    
    - **Fotogrametria Clássica:** Gera representações discretas (malhas de triângulos e texturas). Ela falha com superfícies transparentes, reflexivas (vidro, água) ou brilhantes.  
        
    - **NeRF:** Gera uma representação de campo de radiação contínua. Ele é excelente em capturar **reflexos e efeitos de luz com precisão** , lidando com materiais que a fotogrametria não consegue.  
        

### GAN - Generative Adversarial Network (TempoGAN)

- **O que é?**
    
    - Uma arquitetura GAN (Rede Adversarial Generativa) projetada especificamente para **super-resolução de fluxos de fluidos** (como fumaça ou líquidos).  
        
    - Ela resolve o problema da **"dissipação numérica"** , onde simulações de baixa resolução perdem detalhes finos e parecem "borradas".  
        
    - Ela pega uma simulação de baixa resolução e gera (sintetiza) uma versão de alta resolução com detalhes complexos, garantindo que esses detalhes se movam de forma fisicamente correta ao longo do tempo.  
        
- **Como faz?**
    
    - **Arquitetura:** Um **Gerador (G)** e **dois Discriminadores**.  
        
        - O Gerador (G) tenta criar um quadro de alta resolução a partir de um quadro de baixa resolução.  
            
    - **O Truque Temporal (Os Dois Discriminadores):**
        
        1. **Discriminador Espacial (Ds​):** Este é um discriminador GAN padrão. Ele olha para quadros _individuais_ e decide se o quadro parece um fluido "real" de alta resolução ou um "falso" gerado. Isso garante que os detalhes _espaciais_ (vórtices, texturas) sejam realistas.  
            
        2. **Discriminador Temporal (Dt​):** Esta é a inovação. Ele não olha para quadros individuais. Ele olha para uma **sequência de quadros** (ex: 3-5 quadros consecutivos).  
            
    - **Função de Perda (Loss):** O Gerador é treinado para enganar _ambos_ os discriminadores.  
        
        - Ds​ o força a criar detalhes bonitos.
            
        - Dt​ o força a criar detalhes que são **temporalmente coerentes** — ou seja, um vórtice no quadro 1 deve fluir para uma posição fisicamente correta no quadro 2, em vez de "piscar" aleatoriamente.  
            
- **Input e Output**
    
    - **Entrada (Input):** Um único quadro de dados de fluido de baixa resolução.  
        
        - Isso pode incluir não apenas a densidade (fumaça), mas também outras quantidades físicas como **velocidades ou vorticidades** de baixa resolução. Usar essas quantidades extras também permite **"controle artístico"** sobre o resultado.  
            
    - **Saída (Output):** Um volume de alta resolução com características detalhadas, realistas e temporalmente coerentes.  
        
- **Comparação**
    
    - **Métodos Clássicos:** Para obter alta resolução, é necessário executar uma simulação de alta resolução, que tem um custo computacional e de memória exponencialmente maior.  
        
    - **TempoGAN:** Permite rodar uma simulação de baixa resolução (rápida e barata). Em seguida, usa a rede neural treinada (que é um único _forward pass_ muito rápido) para **sintetizar** os detalhes de alta frequência que foram perdidos pela dissipação numérica.