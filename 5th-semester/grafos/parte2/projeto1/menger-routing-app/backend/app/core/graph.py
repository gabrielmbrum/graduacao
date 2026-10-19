"""
graph.py
--------
Estrutura de grafo baseada em lista de adjacência, com suporte a
grafos direcionados e não-direcionados, usada como base para os
algoritmos de Menger (menger.py) e de resiliência (resilience.py).
"""

from __future__ import annotations
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional


class Graph:
    """
    Grafo representado por lista de adjacência.

    Cada aresta é guardada como (destino, capacidade, id_da_aresta_original)
    para permitir a modelagem de rede de fluxo unitário (capacidade = 1)
    exigida pela redução do Teorema de Menger a fluxo máximo.
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        self.nodes: Set[str] = set()
        self.edges: List[Tuple[str, str]] = []

    # ------------------------------------------------------------------
    # Construção do grafo
    # ------------------------------------------------------------------
    def add_node(self, node_id: str) -> None:
        self.nodes.add(node_id)
        if node_id not in self.adj:
            self.adj[node_id] = []

    def add_edge(self, u: str, v: str, capacity: int = 1) -> None:
        """Adiciona uma aresta u -> v (e v -> u se não-direcionado)."""
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, capacity))
        self.edges.append((u, v))
        if not self.directed:
            self.adj[v].append((u, capacity))

    def neighbors(self, node_id: str) -> List[str]:
        return [v for v, _ in self.adj.get(node_id, [])]

    def degree(self, node_id: str) -> int:
        return len(self.adj.get(node_id, []))

    def node_count(self) -> int:
        return len(self.nodes)

    def edge_count(self) -> int:
        return len(self.edges)

    def remove_node(self, node_id: str) -> "Graph":
        """Retorna uma cópia do grafo sem o nó informado (e suas arestas)."""
        g = Graph(directed=self.directed)
        for n in self.nodes:
            if n != node_id:
                g.add_node(n)
        for u, v in self.edges:
            if u != node_id and v != node_id and u in g.nodes and v in g.nodes:
                if not g.directed and (v, u) in [(a, b) for a, b in g.edges]:
                    continue
                g.adj[u].append((v, 1))
                g.edges.append((u, v))
                if not g.directed:
                    g.adj[v].append((u, 1))
        return g

    def remove_edges(self, removed: Set[Tuple[str, str]]) -> "Graph":
        """Retorna uma cópia do grafo sem as arestas informadas (em qualquer sentido)."""
        norm = set()
        for a, b in removed:
            norm.add((a, b))
            norm.add((b, a))
        g = Graph(directed=self.directed)
        for n in self.nodes:
            g.add_node(n)
        seen = set()
        for u, v in self.edges:
            if (u, v) in norm:
                continue
            key = (u, v) if self.directed else tuple(sorted((u, v)))
            if key in seen:
                continue
            seen.add(key)
            g.add_edge(u, v, 1)
        return g

    def to_dict(self) -> dict:
        return {
            "directed": self.directed,
            "nodes": sorted(self.nodes),
            "edges": [{"source": u, "target": v} for u, v in self.edges],
        }

    @classmethod
    def from_payload(cls, nodes: List[str], edges: List[Tuple[str, str]], directed: bool = False) -> "Graph":
        g = cls(directed=directed)
        for n in nodes:
            g.add_node(n)
        for u, v in edges:
            g.add_edge(u, v, capacity=1)
        return g

    def bfs_reachable(self, start: str, blocked_nodes: Optional[Set[str]] = None) -> Set[str]:
        """Conjunto de nós alcançáveis a partir de start, ignorando nós bloqueados."""
        blocked_nodes = blocked_nodes or set()
        visited = {start}
        queue = [start]
        while queue:
            cur = queue.pop(0)
            for nxt in self.neighbors(cur):
                if nxt in blocked_nodes or nxt in visited:
                    continue
                visited.add(nxt)
                queue.append(nxt)
        return visited
