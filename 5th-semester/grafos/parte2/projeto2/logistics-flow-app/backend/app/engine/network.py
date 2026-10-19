"""
network.py
----------
Estrutura de dados que representa o digrafo ponderado D = (V, E, c) e o
estado de fluxo f(e) associado a cada aresta.

Cada aresta original é armazenada junto de sua "aresta reversa" (capacidade 0
inicialmente), pois é essa reversa que torna a Rede Residual D0(f) possível:
    - aresta direta:  capacidade residual = c(e) - f(e)
    - aresta reversa: capacidade residual = f(e)
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Edge:
    """Uma aresta dirigida dentro da rede (pode ser original ou reversa)."""
    source: str
    target: str
    capacity: float
    flow: float = 0.0
    is_reverse: bool = False
    # índice, na lista de adjacência de `target`, da aresta irmã (reversa/direta)
    reverse_index: int = -1

    @property
    def residual_capacity(self) -> float:
        return self.capacity - self.flow


class FlowNetwork:
    """
    Rede de fluxo representada por lista de adjacência.
    adjacency[v] -> lista de Edge que partem de v (incluindo reversas).
    """

    def __init__(self, nodes: List[str]):
        self.nodes: List[str] = list(dict.fromkeys(nodes))  # preserva ordem, remove duplicatas
        self.adjacency: Dict[str, List[Edge]] = {n: [] for n in self.nodes}

    def add_node(self, node: str) -> None:
        if node not in self.adjacency:
            self.nodes.append(node)
            self.adjacency[node] = []

    def add_edge(self, source: str, target: str, capacity: float) -> None:
        """
        Adiciona uma aresta original (source -> target, capacidade c) e sua
        aresta reversa correspondente (target -> source, capacidade 0),
        já vinculando os índices de reverse_index entre as duas.
        """
        self.add_node(source)
        self.add_node(target)

        forward = Edge(source=source, target=target, capacity=capacity, is_reverse=False)
        backward = Edge(source=target, target=source, capacity=0.0, is_reverse=True)

        self.adjacency[source].append(forward)
        self.adjacency[target].append(backward)

        forward.reverse_index = len(self.adjacency[target]) - 1
        backward.reverse_index = len(self.adjacency[source]) - 1

    def get_edges(self, node: str) -> List[Edge]:
        return self.adjacency.get(node, [])

    def get_reverse_edge(self, edge: Edge) -> Edge:
        return self.adjacency[edge.target][edge.reverse_index]

    def original_edges(self) -> List[Edge]:
        """Retorna somente as arestas originais (não as reversas artificiais)."""
        result: List[Edge] = []
        for node in self.nodes:
            for e in self.adjacency[node]:
                if not e.is_reverse:
                    result.append(e)
        return result

    def total_flow_out_of_source(self, source: str) -> float:
        return sum(e.flow for e in self.get_edges(source) if not e.is_reverse) - sum(
            e.flow for e in self.get_edges(source) if e.is_reverse
        )

    def reset_flow(self) -> None:
        for node in self.nodes:
            for e in self.adjacency[node]:
                e.flow = 0.0
