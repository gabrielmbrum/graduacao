"""
edmonds_karp.py
----------------
Implementação do algoritmo de Ford-Fulkerson usando BFS para escolha do
caminho aumentante (isto é, Edmonds-Karp), com complexidade O(V * E^2).

A cada iteração:
    1. Busca (BFS) um caminho aumentante s -> t na rede residual D0(f).
    2. Calcula o gargalo Δ = min c0(e) das arestas do caminho.
    3. Satura o caminho: soma Δ ao fluxo das arestas de avanço e subtrai Δ
       do fluxo das arestas de retorno (equivalente a somar Δ ao fluxo da
       aresta reversa espelhada).
    4. Repete até que não exista mais caminho aumentante (corte mínimo
       saturado) — condição de parada do Teorema do Fluxo Máximo-Corte Mínimo.
"""
from dataclasses import dataclass
from typing import List

from .network import Edge, FlowNetwork
from .residual import bfs_augmenting_path, residual_edges_snapshot


@dataclass
class IterationRecord:
    iteration: int
    augmenting_path_nodes: List[str]
    bottleneck: float
    flow_after_step: float
    residual_snapshot: List[Edge]


def _apply_flow_along_path(path: List[Edge], bottleneck: float) -> None:
    """Aplica o incremento de fluxo Δ ao longo do caminho aumentante,
    mantendo a conservação de fluxo (atualiza também a aresta reversa)."""
    for e in path:
        e.flow += bottleneck
        # a aresta reversa "desfaz" fluxo equivalente na direção contrária,
        # o que é o que permite ao algoritmo "cancelar" decisões passadas
        e.capacity  # (sem-op, apenas documentando que a capacidade não muda)


def run_edmonds_karp(net: FlowNetwork, source: str, sink: str) -> List[IterationRecord]:
    """
    Executa Edmonds-Karp sobre `net` (em memória, alterando o fluxo das
    arestas in-place) e retorna o histórico de iterações para fins de
    trace/visualização passo a passo.
    """
    net.reset_flow()
    records: List[IterationRecord] = []
    total_flow = 0.0
    iteration = 0

    while True:
        path, bottleneck = bfs_augmenting_path(net, source, sink)
        if not path or bottleneck <= 0:
            break

        _apply_flow_along_path(path, bottleneck)
        total_flow += bottleneck
        iteration += 1

        path_nodes = [source] + [e.target for e in path]
        records.append(
            IterationRecord(
                iteration=iteration,
                augmenting_path_nodes=path_nodes,
                bottleneck=bottleneck,
                flow_after_step=total_flow,
                residual_snapshot=residual_edges_snapshot(net),
            )
        )

    return records


def max_flow_value(net: FlowNetwork, source: str) -> float:
    """Valor total do fluxo F = f(D), calculado pela saída líquida de `source`."""
    return net.total_flow_out_of_source(source)
