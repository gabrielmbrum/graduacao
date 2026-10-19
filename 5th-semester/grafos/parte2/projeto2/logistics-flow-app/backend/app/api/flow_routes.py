"""
flow_routes.py
---------------
Endpoints REST do módulo de Distribuição e Logística de Malha de Abastecimento.

    POST /api/flow/solve            -> fluxo máximo + corte mínimo (resultado final)
    POST /api/flow/trace-iterations -> histórico passo a passo (para animação no frontend)
"""
from fastapi import APIRouter, HTTPException

from app.engine.edmonds_karp import run_edmonds_karp, max_flow_value
from app.engine.min_cut import compute_min_cut
from app.engine.network import FlowNetwork
from app.schemas.flow_dto import (
    AugmentingStep,
    EdgeFlowResult,
    FlowSolveRequest,
    FlowSolveResponse,
    FlowTraceResponse,
    MinCutEdge,
)

router = APIRouter(prefix="/api/flow", tags=["flow"])


def _build_network(payload: FlowSolveRequest) -> FlowNetwork:
    if payload.source not in payload.nodes:
        raise HTTPException(status_code=422, detail=f"Nó de origem '{payload.source}' não está em `nodes`.")
    if payload.sink not in payload.nodes:
        raise HTTPException(status_code=422, detail=f"Nó de destino '{payload.sink}' não está em `nodes`.")
    if payload.source == payload.sink:
        raise HTTPException(status_code=422, detail="Origem e destino não podem ser o mesmo nó.")

    net = FlowNetwork(payload.nodes)
    for edge in payload.edges:
        if edge.source not in payload.nodes or edge.target not in payload.nodes:
            raise HTTPException(
                status_code=422,
                detail=f"Aresta ({edge.source} -> {edge.target}) referencia nó fora de `nodes`.",
            )
        net.add_edge(edge.source, edge.target, edge.capacity)
    return net


def _edge_results(net: FlowNetwork) -> list[EdgeFlowResult]:
    return [
        EdgeFlowResult(
            source=e.source,
            target=e.target,
            capacity=e.capacity,
            flow=e.flow,
            saturated=abs(e.flow - e.capacity) < 1e-9,
        )
        for e in net.original_edges()
    ]


@router.post("/solve", response_model=FlowSolveResponse)
def solve_flow(payload: FlowSolveRequest) -> FlowSolveResponse:
    """Calcula o fluxo máximo s->t e o corte mínimo (gargalo logístico) da malha."""
    net = _build_network(payload)
    run_edmonds_karp(net, payload.source, payload.sink)

    cut = compute_min_cut(net, payload.source)
    total_flow = max_flow_value(net, payload.source)

    return FlowSolveResponse(
        max_flow=total_flow,
        edges=_edge_results(net),
        partition_s=cut.partition_s,
        partition_t=cut.partition_t,
        min_cut_edges=[
            MinCutEdge(source=s, target=t, capacity=c) for (s, t, c) in cut.cut_edges
        ],
    )


@router.post("/trace-iterations", response_model=FlowTraceResponse)
def trace_iterations(payload: FlowSolveRequest) -> FlowTraceResponse:
    """
    Retorna o histórico completo de iterações do Edmonds-Karp: caminho
    aumentante, gargalo e estado da rede residual a cada passo — usado pelo
    StepByStepPanel do frontend para animar a construção do fluxo.
    """
    net = _build_network(payload)
    records = run_edmonds_karp(net, payload.source, payload.sink)

    steps = [
        AugmentingStep(
            iteration=r.iteration,
            augmenting_path=r.augmenting_path_nodes,
            bottleneck=r.bottleneck,
            flow_after_step=r.flow_after_step,
            residual_edges=[
                EdgeFlowResult(
                    source=e.source,
                    target=e.target,
                    capacity=e.capacity,
                    flow=e.flow,
                    saturated=abs(e.residual_capacity) < 1e-9,
                )
                for e in r.residual_snapshot
            ],
        )
        for r in records
    ]

    return FlowTraceResponse(steps=steps, max_flow=max_flow_value(net, payload.source))
