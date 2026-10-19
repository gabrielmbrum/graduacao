"""
routes.py
---------
Endpoints REST expostos pelo FastAPI:

- POST /api/graph/analyze          -> caminhos disjuntos + conectividade + gargalos
- POST /api/graph/simulate-failure -> recalcula rotas sobreviventes após falha
"""

from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    SimulateFailureRequest,
    SimulateFailureResponse,
)
from app.core.graph import Graph
from app.core.menger import edge_min_cut, vertex_min_cut
from app.core.resilience import (
    pairwise_connectivity,
    articulation_points_and_bridges,
    simulate_failure,
)

router = APIRouter(prefix="/api/graph", tags=["graph"])


def _build_graph(payload) -> Graph:
    g = Graph(directed=payload.directed)
    for n in payload.nodes:
        g.add_node(n)
    for e in payload.edges:
        g.add_edge(e.source, e.target, capacity=1)
    return g


def _validate_endpoints(g: Graph, source: str, sink: str) -> None:
    if source not in g.nodes:
        raise HTTPException(status_code=422, detail=f"Nó de origem '{source}' não existe no grafo.")
    if sink not in g.nodes:
        raise HTTPException(status_code=422, detail=f"Nó de destino '{sink}' não existe no grafo.")
    if source == sink:
        raise HTTPException(status_code=422, detail="Origem e destino devem ser diferentes.")


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    g = _build_graph(request.graph)
    _validate_endpoints(g, request.source, request.sink)

    result = pairwise_connectivity(g, request.source, request.sink)
    articulation, bridges = articulation_points_and_bridges(g)
    cut_edges = edge_min_cut(g, request.source, request.sink)
    cut_vertices = vertex_min_cut(g, request.source, request.sink)

    return AnalyzeResponse(
        source=result["source"],
        sink=result["sink"],
        edge_connectivity=result["edge_connectivity"],
        vertex_connectivity=result["vertex_connectivity"],
        edge_disjoint_paths=result["edge_disjoint_paths"],
        vertex_disjoint_paths=result["vertex_disjoint_paths"],
        articulation_points=sorted(articulation),
        bridges=bridges,
        min_cut_edges=cut_edges,
        min_cut_vertices=cut_vertices,
    )


@router.post("/simulate-failure", response_model=SimulateFailureResponse)
def simulate_failure_endpoint(request: SimulateFailureRequest) -> SimulateFailureResponse:
    g = _build_graph(request.graph)
    _validate_endpoints(g, request.source, request.sink)

    failed_edges = [(e.source, e.target) for e in request.failed_edges]
    result = simulate_failure(g, request.source, request.sink, request.failed_nodes, failed_edges)

    return SimulateFailureResponse(**result)
