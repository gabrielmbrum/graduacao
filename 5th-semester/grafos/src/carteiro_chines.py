import networkx as nx

def carteiro_chines_didatico(G):
    # Passo 1: O grafo já é Euleriano? (Todos os vértices têm grau par)
    if nx.is_eulerian(G):
        print(" -> O grafo já é Euleriano! Nenhuma aresta extra é necessária.")
        # Retorna o circuito usando o algoritmo interno de Hierholzer
        return list(nx.eulerian_circuit(G))

    # Passo 2: Se não é, encontramos os vértices problemáticos (grau ímpar)
    impares = [v for v, grau in G.degree() if grau % 2 != 0]
    print(f" -> Grafo semi-Euleriano. Vértices de grau ímpar encontrados: {impares}")

    # Passo 3: O caso mais comum na prática é ter exatamente 2 vértices ímpares.
    if len(impares) == 2:
        origem, destino = impares
        
        # Encontra o caminho mais curto entre eles usando algoritmo de Dijkstra
        caminho_minimo = nx.shortest_path(G, origem, destino, weight='weight')
        print(f" -> Duplicando as arestas do caminho mínimo: {caminho_minimo}")
        
        # Passo 4: Transforma em um Multigrafo (permite arestas paralelas) e duplica o caminho
        G_euleriano = nx.MultiGraph(G)
        for i in range(len(caminho_minimo) - 1):
            u = caminho_minimo[i]
            v = caminho_minimo[i+1]
            peso_aresta = G[u][v]['weight']
            G_euleriano.add_edge(u, v, weight=peso_aresta) # Adiciona aresta paralela
            
        return list(nx.eulerian_circuit(G_euleriano))
    else:
        return "Para mais de 2 nós ímpares, é necessário o Emparelhamento Perfeito de Peso Mínimo."

print("\n=== PROBLEMA CHINÊS DO CARTEIRO ===")

# Exemplo Simples: Grafo que já é Euleriano (Um quadrado cruzado - Graus: 2 e 4)
G_simples = nx.Graph()
G_simples.add_weighted_edges_from([
    ('A', 'B', 5), ('B', 'C', 5), ('C', 'A', 5), # Triângulo da esquerda
    ('C', 'D', 6), ('D', 'E', 6), ('E', 'C', 6)  # Triângulo da direita
])
print("\nTeste Simples (Grafo Euleriano):")
circuito_s = carteiro_chines_didatico(G_simples)
for edges in G_simples.edges(data=True):
    print(f"Aresta: {edges[0]} <-> {edges[1]} | Peso: {edges[2]['weight']}")
print("Circuito do Carteiro:", circuito_s)

# Exemplo Complexo: Grafo Semi-Euleriano (Um retângulo com apenas UMA diagonal)
# A e C terão grau 3 (Ímpares). B e D terão grau 2 (Pares).
G_complexo = nx.Graph()
G_complexo.add_weighted_edges_from([
    ('A', 'B', 10), ('B', 'C', 20), 
    ('C', 'D', 10), ('D', 'A', 20),
    ('A', 'C', 15) # Apenas uma diagonal
])
print("\nTeste Complexo (Grafo Semi-Euleriano):")
circuito_c = carteiro_chines_didatico(G_complexo)
for edges in G_complexo.edges(data=True):
    print(f"Aresta: {edges[0]} <-> {edges[1]} | Peso: {edges[2]['weight']}")
print("Circuito do Carteiro:", circuito_c)