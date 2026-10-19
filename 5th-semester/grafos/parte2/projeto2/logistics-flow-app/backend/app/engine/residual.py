"""
residual.py
-----------
Utilitários sobre a Rede Residual D0(f):

    D0(f) contém, para cada aresta original (u, v) com capacidade c e fluxo f:
        - uma aresta de avanço (u, v) com capacidade residual c - f, se c - f > 0
        - uma aresta de retorno (v, u) com capacidade residual f,     se f > 0

Como `network.FlowNetwork` já mantém as arestas reversas fisicamente (com
capacidade 0 e fluxo espelhado), a rede residual em qualquer instante é
simplesmente: "toda Edge cuja residual_capacity > 0".
"""
from collections import deque
from typing import Dict, List, Set, Tuple

from .network import Edge, FlowNetwork


def residual_edges_snapshot(net: FlowNetwork) -> List[Edge]:
    """Retorna todas as arestas (diretas e reversas) com capacidade residual > 0."""
    snapshot: List[Edge] = []
    for node in net.nodes:
        for e in net.adjacency[node]:
            if e.residual_capacity > 1e-9:
                snapshot.append(e)
    return snapshot


def bfs_augmenting_path(net: FlowNetwork, source: str, sink: str) -> Tuple[List[Edge], float]:
    """
    Busca em Largura (BFS) por um caminho aumentante de `source` até `sink`
    na rede residual atual — núcleo do algoritmo de Edmonds-Karp.

    Retorna (lista_de_arestas_do_caminho, gargalo). Se não houver caminho,
    retorna ([], 0.0).
    """
    if source not in net.adjacency or sink not in net.adjacency:
        return [], 0.0

    predecessor_edge: Dict[str, Edge] = {}
    visited: Set[str] = {source}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        if u == sink:
            break
        for e in net.get_edges(u):
            if e.residual_capacity > 1e-9 and e.target not in visited:
                visited.add(e.target)
                predecessor_edge[e.target] = e
                queue.append(e.target)

    if sink not in visited:
        return [], 0.0

    # Reconstrói o caminho de trás para frente e calcula o gargalo Δ = min c0(e)
    path: List[Edge] = []
    node = sink
    bottleneck = float("inf")
    while node != source:
        e = predecessor_edge[node]
        path.append(e)
        bottleneck = min(bottleneck, e.residual_capacity)
        node = e.source

    path.reverse()
    return path, bottleneck


def reachable_from_source(net: FlowNetwork, source: str) -> Set[str]:
    """
    Conjunto S de vértices alcançáveis a partir de `source` na rede residual
    final (após o fluxo máximo já ter sido calculado). Usado para extrair a
    partição do Corte Mínimo (S, S̄) pelo Teorema do Fluxo Máximo–Corte Mínimo.
    """
    visited: Set[str] = {source}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for e in net.get_edges(u):
            if e.residual_capacity > 1e-9 and e.target not in visited:
                visited.add(e.target)
                queue.append(e.target)
    return visited
