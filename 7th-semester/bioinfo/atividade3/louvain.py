# Importando as bibliotecas
import networkx as nx
import community.community_louvain as community_louvain

# 1. Instanciando o Grafo com NetworkX
G = nx.Graph()

# 2. Inserindo a rede (Focada em hematologia e resposta inflamatória)
# Modelaremos proteínas envolvidas na cascata de coagulação, 
# ativação plaquetária e resposta inflamatória inicial.
interacoes = [
    # Módulo 1: Cascata de Coagulação (Fatores de coagulação)
    ('F8', 'F9'), ('F9', 'F10'), ('F8', 'F10'), 
    ('F10', 'F2'), ('F5', 'F10'), ('F5', 'F2'),
    
    # Módulo 2: Formação da Fibrina e Fibrinólise
    ('F2', 'FGA'), ('F2', 'FGB'), ('FGA', 'FGB'), 
    ('FGA', 'FGG'), ('FGB', 'FGG'), ('PLG', 'PLAT'), 
    ('PLAT', 'FGA'), ('PLG', 'F2'),

    # Módulo 3: Receptores Plaquetários (Adesão e Agregação)
    ('ITGA2B', 'ITGB3'), ('GP1BA', 'GP1BB'), ('GP1BA', 'VWF'), 
    ('VWF', 'F8'), ('ITGA2B', 'FGA'),

    # Módulo 4: Resposta Inflamatória e Citocinas
    ('IL6', 'TNF'), ('TNF', 'IL1B'), ('IL6', 'CRP'), 
    ('CRP', 'FGA'), ('IL1B', 'F2')
]

# Adicionando as arestas ao grafo
G.add_edges_from(interacoes)

# 3. Aplicando o Algoritmo de Louvain
# O método 'best_partition' avalia a topologia do grafo do NetworkX
# e retorna um dicionário mapeando cada nó (proteína) para um ID de comunidade.
particao = community_louvain.best_partition(G)

# 4. Exibição dos Resultados
print("=== Resultados da Detecção de Comunidades (Algoritmo de Louvain) ===\n")

# Reorganizando o dicionário de saída do Louvain para agrupar as proteínas por ID da comunidade
comunidades = {}
for proteina, id_comunidade in particao.items():
    if id_comunidade not in comunidades:
        comunidades[id_comunidade] = []
    comunidades[id_comunidade].append(proteina)

# Organizando e imprimindo o output
for id_comunidade, proteinas_na_comunidade in comunidades.items():
    print(f"Comunidade {id_comunidade + 1} (Tamanho: {len(proteinas_na_comunidade)} proteínas):")
    print(f" -> {', '.join(proteinas_na_comunidade)}\n")