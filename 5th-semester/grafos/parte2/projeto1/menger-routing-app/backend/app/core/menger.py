"""
menger.py
---------
Implementação do Teorema de Menger via redução a Fluxo Máximo em
rede de capacidade unitária (Edmonds-Karp / BFS de aumento).

Dois modos são suportados:

1. Caminhos ARESTA-disjuntos:
   - Cada aresta original (u, v) vira um arco de capacidade 1 no grafo
     residual (bidirecional, pois a rede de telecom não é orientada).

2. Caminhos VÉRTICE-disjuntos:
   - Técnica de "node splitting": cada vértice v (exceto origem e
     destino) é dividido em v_in -> v_out com capacidade 1. Isso força
     o fluxo máximo a nunca reutilizar o mesmo vértice intermediário
     em dois caminhos diferentes.

O número máximo de caminhos disjuntos encontrado equivale, pelo
Teorema de Menger, ao tamanho do corte mínimo (de arestas ou de
vértices, respectivamente) entre a origem e o destino.
"""

from __future__ import annotations
from collections import deque, defaultdict
from typing import Dict, List, Tuple, Set
from app.core.graph import Graph


class FlowNetwork:
    """Rede de fluxo residual simples, usada internamente pelo Edmonds-Karp."""

    def __init__(self):
        self.capacity: Dict[Tuple[str, str], int] = defaultdict(int)
        self.adj: Dict[str, Set[str]] = defaultdict(set)

    def add_edge(self, u: str, v: str, cap: int = 1) -> None:
        self.capacity[(u, v)] += cap
        self.capacity.setdefault((v, u), 0)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def bfs_augmenting_path(self, source: str, sink: str) -> List[str]:
        parent: Dict[str, str] = {}
        visited = {source}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            if u == sink:
                break
            for v in self.adj[u]:
                if v not in visited and self.capacity[(u, v)] > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
        if sink not in visited:
            return []
        path = [sink]
        while path[-1] != source:
            path.append(parent[path[-1]])
        path.reverse()
        return path

    def max_flow_paths(self, source: str, sink: str) -> List[List[str]]:
        """Executa Edmonds-Karp e devolve a lista de caminhos aumentantes
        (cada um com capacidade unitária) que compõem o fluxo máximo."""
        paths: List[List[str]] = []
        while True:
            path = self.bfs_augmenting_path(source, sink)
            if not path:
                break
            # capacidade unitária garante bottleneck = 1 em cada caminho
            bottleneck = min(self.capacity[(path[i], path[i + 1])] for i in range(len(path) - 1))
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                self.capacity[(u, v)] -= bottleneck
                self.capacity[(v, u)] += bottleneck
            paths.append(path)
        return paths

    def min_cut_reachable(self, source: str) -> Set[str]:
        """Após rodar max_flow_paths, retorna o conjunto de nós ainda
        alcançáveis a partir da origem no grafo residual (lado S do corte)."""
        visited = {source}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if v not in visited and self.capacity[(u, v)] > 0:
                    visited.add(v)
                    queue.append(v)
        return visited


def edge_disjoint_paths(graph: Graph, source: str, sink: str) -> Tuple[List[List[str]], int]:
    """
    Retorna (lista_de_caminhos_aresta_disjuntos, conectividade_de_arestas).
    """
    net = FlowNetwork()
    for u, v in graph.edges:
        net.add_edge(u, v, 1)
        if not graph.directed:
            net.add_edge(v, u, 1)

    paths = net.max_flow_paths(source, sink)
    return paths, len(paths)


def edge_min_cut(graph: Graph, source: str, sink: str) -> List[Tuple[str, str]]:
    """Retorna as arestas do corte mínimo desconectador (aresta-corte)."""
    net = FlowNetwork()
    for u, v in graph.edges:
        net.add_edge(u, v, 1)
        if not graph.directed:
            net.add_edge(v, u, 1)
    net.max_flow_paths(source, sink)
    s_side = net.min_cut_reachable(source)

    cut_edges = []
    for u, v in graph.edges:
        u_in_s, v_in_s = u in s_side, v in s_side
        if u_in_s != v_in_s:
            cut_edges.append((u, v))
    return cut_edges


def vertex_disjoint_paths(graph: Graph, source: str, sink: str) -> Tuple[List[List[str]], int]:
    """
    Retorna (lista_de_caminhos_vertice_disjuntos, conectividade_de_vertices),
    usando a técnica de node-splitting (v -> v_in, v_out).
    """
    net = FlowNetwork()

    def in_node(n: str) -> str:
        return f"{n}__in"

    def out_node(n: str) -> str:
        return f"{n}__out"

    for n in graph.nodes:
        if n in (source, sink):
            continue
        net.add_edge(in_node(n), out_node(n), 1)

    # Arestas originais recebem capacidade "infinita": o gargalo de
    # capacidade 1 deve vir exclusivamente dos arcos de split (v_in->v_out),
    # garantindo que o corte mínimo resultante seja um corte de VÉRTICES puro.
    INF = graph.node_count() + 1
    for u, v in graph.edges:
        u_out = source if u == source else (sink if u == sink else out_node(u))
        v_in = sink if v == sink else (source if v == source else in_node(v))
        net.add_edge(u_out, v_in, INF)
        if not graph.directed:
            v_out = source if v == source else (sink if v == sink else out_node(v))
            u_in = sink if u == sink else (source if u == source else in_node(u))
            net.add_edge(v_out, u_in, INF)

    raw_paths = net.max_flow_paths(source, sink)

    # limpa os sufixos __in/__out para exibição amigável
    clean_paths = []
    for p in raw_paths:
        clean = []
        for node in p:
            base = node.replace("__in", "").replace("__out", "")
            if not clean or clean[-1] != base:
                clean.append(base)
        clean_paths.append(clean)

    return clean_paths, len(raw_paths)


def vertex_min_cut(graph: Graph, source: str, sink: str) -> List[str]:
    """Retorna os vértices do corte mínimo (vértice-corte), via node-splitting."""
    net = FlowNetwork()

    def in_node(n: str) -> str:
        return f"{n}__in"

    def out_node(n: str) -> str:
        return f"{n}__out"

    for n in graph.nodes:
        if n in (source, sink):
            continue
        net.add_edge(in_node(n), out_node(n), 1)

    INF = graph.node_count() + 1
    for u, v in graph.edges:
        u_out = source if u == source else (sink if u == sink else out_node(u))
        v_in = sink if v == sink else (source if v == source else in_node(v))
        net.add_edge(u_out, v_in, INF)
        if not graph.directed:
            v_out = source if v == source else (sink if v == sink else out_node(v))
            u_in = sink if u == sink else (source if u == source else in_node(u))
            net.add_edge(v_out, u_in, INF)

    net.max_flow_paths(source, sink)
    s_side = net.min_cut_reachable(source)

    cut_nodes = []
    for n in graph.nodes:
        if n in (source, sink):
            continue
        if in_node(n) in s_side and out_node(n) not in s_side:
            cut_nodes.append(n)
    return cut_nodes
