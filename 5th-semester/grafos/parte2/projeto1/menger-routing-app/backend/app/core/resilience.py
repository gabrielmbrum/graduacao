"""
resilience.py
-------------
Métricas globais de resiliência da rede:

- Conectividade de vértices (CV) e de arestas (CA) entre um par (v, w)
  e, opcionalmente, a conectividade global do grafo (mínimo sobre
  todos os pares, aproximado via um vértice fixo contra todos os
  demais, que é suficiente para grafos não completos).
- Identificação de pontos de articulação (cut vertices) e pontes
  (bridges), que são os gargalos estruturais de grau 1 de resiliência
  (k=1): sua queda desconecta a rede.
- Simulação de falha: recalcula a conectividade após a remoção de
  nós/arestas informados pelo usuário.
"""

from __future__ import annotations
from typing import Dict, List, Set, Tuple
from app.core.graph import Graph
from app.core.menger import edge_disjoint_paths, vertex_disjoint_paths


def articulation_points_and_bridges(graph: Graph) -> Tuple[Set[str], List[Tuple[str, str]]]:
    """
    Algoritmo clássico de Tarjan (DFS com low-link) para encontrar,
    em uma única passada O(V+E), os pontos de articulação e as pontes
    do grafo. Um nó de grau 1 de conectividade de vértices (CV=1)
    sempre possui ao menos um ponto de articulação em algum caminho
    entre a origem e o destino; o mesmo vale para pontes quando CA=1.
    """
    disc: Dict[str, int] = {}
    low: Dict[str, int] = {}
    parent: Dict[str, str] = {}
    articulation: Set[str] = set()
    bridges: List[Tuple[str, str]] = []
    timer = {"t": 0}

    def dfs(u: str):
        disc[u] = low[u] = timer["t"]
        timer["t"] += 1
        children = 0
        for v in graph.neighbors(u):
            if v not in disc:
                children += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])

                if parent.get(u) is not None and low[v] >= disc[u]:
                    articulation.add(u)
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent.get(u):
                low[u] = min(low[u], disc[v])

        if parent.get(u) is None and children > 1:
            articulation.add(u)

    for node in graph.nodes:
        if node not in disc:
            dfs(node)

    return articulation, bridges


def pairwise_connectivity(graph: Graph, source: str, sink: str) -> Dict[str, object]:
    """Calcula CA (conectividade de arestas) e CV (conectividade de vértices)
    entre 'source' e 'sink', junto com os caminhos disjuntos correspondentes."""
    edge_paths, edge_k = edge_disjoint_paths(graph, source, sink)
    vertex_paths, vertex_k = vertex_disjoint_paths(graph, source, sink)

    return {
        "source": source,
        "sink": sink,
        "edge_connectivity": edge_k,
        "vertex_connectivity": vertex_k,
        "edge_disjoint_paths": edge_paths,
        "vertex_disjoint_paths": vertex_paths,
    }


def simulate_failure(
    graph: Graph,
    source: str,
    sink: str,
    failed_nodes: List[str],
    failed_edges: List[Tuple[str, str]],
) -> Dict[str, object]:
    """
    Remove os nós/arestas indicados e recalcula:
    - se source/sink ainda estão conectados
    - os caminhos disjuntos sobreviventes
    - a nova conectividade CA/CV
    """
    working = graph
    if failed_nodes:
        for n in failed_nodes:
            working = working.remove_node(n)
    if failed_edges:
        working = working.remove_edges(set(failed_edges))

    if source not in working.nodes or sink not in working.nodes:
        return {
            "connected": False,
            "reason": "Origem ou destino removido da rede.",
            "edge_connectivity": 0,
            "vertex_connectivity": 0,
            "edge_disjoint_paths": [],
            "vertex_disjoint_paths": [],
        }

    reachable = working.bfs_reachable(source)
    connected = sink in reachable

    result = {
        "connected": connected,
        "edge_connectivity": 0,
        "vertex_connectivity": 0,
        "edge_disjoint_paths": [],
        "vertex_disjoint_paths": [],
        "remaining_nodes": sorted(working.nodes),
        "remaining_edges": [{"source": u, "target": v} for u, v in working.edges],
    }

    if connected:
        edge_paths, edge_k = edge_disjoint_paths(working, source, sink)
        vertex_paths, vertex_k = vertex_disjoint_paths(working, source, sink)
        result["edge_connectivity"] = edge_k
        result["vertex_connectivity"] = vertex_k
        result["edge_disjoint_paths"] = edge_paths
        result["vertex_disjoint_paths"] = vertex_paths

    return result
