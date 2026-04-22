import numpy as np

def demonstrar_grafo_desconexo():
    print("=== 1. GRAFO DESCONEXO (Matriz em Blocos) ===")
    # Imagine um componente G1 (um triângulo: 3 vértices, 3 arestas)
    A_G1 = np.array([
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1]
    ])
    
    # Imagine um componente G2 (uma linha simples: 2 vértices, 1 aresta)
    A_G2 = np.array([
        [1],
        [1]
    ])
    
    # Para juntá-los em um único grafo desconexo G, preenchemos o resto com zeros
    zeros_superior_direito = np.zeros((3, 1), dtype=int)
    zeros_inferior_esquerdo = np.zeros((2, 3), dtype=int)
    
    # Montando a matriz de incidência A(G) em formato de blocos
    A_G = np.block([
        [A_G1, zeros_superior_direito],
        [zeros_inferior_esquerdo, A_G2]
    ])
    
    print("Matriz A(G1):\n", A_G1)
    print("\nMatriz A(G2):\n", A_G2)
    print("\nMatriz do Grafo Completo Desconexo A(G):")
    print(A_G)
    print("-" * 50)


def demonstrar_isomorfismo():
    print("\n=== 2. ISOMORFISMO (Permutação de Linhas e Colunas) ===")
    # Matriz de incidência de um grafo G (Grafo Estrela com 4 vértices e 3 arestas)
    # v0 é o centro, ligado a v1, v2 e v3.
    A = np.array([
        [1, 1, 1],  # v0 (centro)
        [1, 0, 0],  # v1
        [0, 1, 0],  # v2
        [0, 0, 1]   # v3
    ])
    
    print("Matriz Original (Grafo A):\n", A)
    
    # Ordem original: 0, 1, 2, 3. Nova ordem: 2, 0, 3, 1
    permutacao_linhas = [2, 0, 3, 1]
    
    # Ordem original: 0, 1, 2. Nova ordem: 2, 0, 1
    permutacao_colunas = [2, 0, 1]
    
    # Aplicando as permutações
    B = A[permutacao_linhas, :]  # Permuta as linhas
    B = B[:, permutacao_colunas] # Permuta as colunas
    
    print("\nMatriz Permutada (Grafo B - Isomorfo a A):")
    print(B)
    
    print("\nConclusão: Embora as matrizes A e B pareçam diferentes numericamente,")
    print("elas representam EXATAMENTE a mesma estrutura (isomorfismo).")
    print("Basta reordenar vértices e arestas para B voltar a ser A.")

# Executando as demonstrações
demonstrar_grafo_desconexo()
demonstrar_isomorfismo()