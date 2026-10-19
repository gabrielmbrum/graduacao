"""
Estruturas (Pydantic) de entrada e saída para a API de Fluxo Máximo.
"""
from typing import List, Dict, Optional
from pydantic import BaseModel, Field, field_validator


class EdgeInput(BaseModel):
    """Aresta da malha viária (trecho de rodovia)."""
    source: str = Field(..., description="Vértice de origem do trecho")
    target: str = Field(..., description="Vértice de destino do trecho")
    capacity: float = Field(..., gt=0, description="Capacidade de transporte c(e)")

    @field_validator("source", "target")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Identificador de vértice não pode ser vazio")
        return v.strip()


class FlowSolveRequest(BaseModel):
    """Requisição para POST /api/flow/solve"""
    nodes: List[str] = Field(..., description="Lista de vértices (cidades/armazéns)")
    edges: List[EdgeInput] = Field(..., description="Lista de trechos com capacidade")
    source: str = Field(..., description="Nó de origem (centro de distribuição) s")
    sink: str = Field(..., description="Nó de destino (polo de entrega) t")


class EdgeFlowResult(BaseModel):
    """Estado final de uma aresta após o cálculo do fluxo máximo."""
    source: str
    target: str
    capacity: float
    flow: float
    saturated: bool


class MinCutEdge(BaseModel):
    """Aresta que compõe o corte mínimo (gargalo logístico)."""
    source: str
    target: str
    capacity: float


class FlowSolveResponse(BaseModel):
    """Resposta de POST /api/flow/solve"""
    max_flow: float
    edges: List[EdgeFlowResult]
    partition_s: List[str] = Field(..., description="Vértices alcançáveis a partir de s na rede residual final")
    partition_t: List[str] = Field(..., description="Complemento: vértices não alcançáveis (lado de t)")
    min_cut_edges: List[MinCutEdge]


class AugmentingStep(BaseModel):
    """Uma iteração do algoritmo de Edmonds-Karp."""
    iteration: int
    augmenting_path: List[str]
    bottleneck: float
    flow_after_step: float
    residual_edges: List[EdgeFlowResult] = Field(
        ..., description="Estado da rede residual D0(f) logo após esta iteração"
    )


class FlowTraceResponse(BaseModel):
    """Resposta de POST /api/flow/trace-iterations"""
    steps: List[AugmentingStep]
    max_flow: float
