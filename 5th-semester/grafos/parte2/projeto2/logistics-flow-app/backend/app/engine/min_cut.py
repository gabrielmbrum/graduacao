"""
min_cut.py
----------
Extrai o Corte Mínimo (S, S̄) a partir de uma rede cujo fluxo já atingiu o
máximo (pós Edmonds-Karp), aplicando o Teorema do Fluxo Máximo-Corte Mínimo:

    F_max = c(S, S̄) = soma das capacidades das arestas que saem de S e
    chegam em S̄, sendo S o conjunto de vértices alcançáveis a partir de s
    na rede residual final.

Toda aresta de avanço (u em S, v em S̄) está necessariamente saturada
(f(e) = c(e)), e toda aresta de retorno (u em S̄, v em S) tem fluxo zero —
essa é justamente a condição de parada do algoritmo (nenhum caminho
aumentante remanescente).
"""
from dataclasses import dataclass
from typing import List, Set, Tuple

from .network import FlowNetwork
from .residual import reachable_from_source


@dataclass
class MinCutResult:
    partition_s: List[str]
    partition_t: List[str]
    cut_edges: List[Tuple[str, str, float]]  # (source, target, capacity)


def compute_min_cut(net: FlowNetwork, source: str) -> MinCutResult:
    s_set: Set[str] = reachable_from_source(net, source)
    t_set: Set[str] = set(net.nodes) - s_set

    cut_edges: List[Tuple[str, str, float]] = []
    for edge in net.original_edges():
        if edge.source in s_set and edge.target in t_set:
            cut_edges.append((edge.source, edge.target, edge.capacity))

    return MinCutResult(
        partition_s=sorted(s_set),
        partition_t=sorted(t_set),
        cut_edges=cut_edges,
    )
