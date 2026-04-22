import itertools

def caixeiro_viajante_forca_bruta(matriz_distancias, nomes_cidades):
    n = len(matriz_distancias)
    cidades = list(range(n))
    melhor_rota = None
    menor_custo = float('inf')
    total_iterations = 0

    # Fixamos a cidade 0 como início/fim para não repetir rotas circulares
    # itertools.permutations gera todas as rotas possíveis (ex: (1,2,3), (1,3,2)...)
    for permutacao in itertools.permutations(cidades[1:]):
        rota_atual = (0,) + permutacao + (0,) # Inicia em 0, visita as outras, volta pro 0
        custo_atual = 0
        
        # Calcula o custo total desta rota
        for i in range(len(rota_atual) - 1):
            origem = rota_atual[i]
            destino = rota_atual[i+1]
            custo_atual += matriz_distancias[origem][destino]

        # Atualiza se encontrou uma rota mais barata
        if custo_atual < menor_custo:
            menor_custo = custo_atual
            melhor_rota = rota_atual

        total_iterations += 1

    # Traduz os índices (0, 1, 2) para os nomes reais das cidades
    rota_nomeada = " -> ".join([nomes_cidades[i] for i in melhor_rota])
    return rota_nomeada, menor_custo, total_iterations


print("=== PROBLEMA DO CAIXEIRO VIAJANTE ===")

# Exemplo Simples: 3 cidades (um triângulo)
cidades_simples = ['A', 'B', 'C']
matriz_simples = [
    [0, 10, 15],  # Distâncias saindo de A
    [10, 0, 20],  # Distâncias saindo de B
    [15, 20, 0]   # Distâncias saindo de C
]
rota_s, custo_s, total_it_s = caixeiro_viajante_forca_bruta(matriz_simples, cidades_simples)
print("Matriz de Adjacência (Simples):")
aux = 0
for linha in matriz_simples:
    print(f"{cidades_simples[aux]}: {linha}")
    aux += 1
print(f"(3 cidades): Rota: {rota_s} | Custo: {custo_s} | Total de Iterações: {total_it_s}")

print("\n" + "="*50 + "\n")

# Exemplo Complexo: 5 cidades (Grafo Completo K5)
cidades_complexas = ['SP', 'RJ', 'MG', 'PR', 'SC']
matriz_complexa = [
    [0,  400, 580, 400, 700], # SP
    [400, 0,  430, 800, 1100],# RJ
    [580, 430, 0,  980, 1200],# MG
    [400, 800, 980, 0,  300], # PR
    [700, 1100,1200,300, 0]   # SC
]
rota_c, custo_c, total_it_c = caixeiro_viajante_forca_bruta(matriz_complexa, cidades_complexas)
print("Matriz de Adjacência (Complexo):")
aux = 0
for linha in matriz_complexa:
    print(f"{cidades_complexas[aux]}: {linha}")
    aux += 1
print(f"(5 cidades): Rota: {rota_c} | Custo: {custo_c} | Total de Iterações: {total_it_c}")