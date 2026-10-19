"""
schemas.py
----------
Modelos Pydantic usados para validar as requisições/respostas da API.
"""

from __future__ import annotations
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field, field_validator


class EdgeIn(BaseModel):
    source: str
    target: str


class GraphIn(BaseModel):
    """Payload de topologia enviado pelo frontend (ControlPanel / GraphCanvas)."""
    nodes: List[str] = Field(..., min_length=2, description="IDs dos roteadores/nós")
    edges: List[EdgeIn] = Field(..., min_length=1, description="Enlaces de fibra/rádio")
    directed: bool = False

    @field_validator("nodes")
    @classmethod
    def nodes_must_be_unique(cls, v: List[str]) -> List[str]:
        if len(v) != len(set(v)):
            raise ValueError("A lista de nós contém identificadores duplicados.")
        return v


class AnalyzeRequest(BaseModel):
    graph: GraphIn
    source: str
    sink: str


class SimulateFailureRequest(BaseModel):
    graph: GraphIn
    source: str
    sink: str
    failed_nodes: List[str] = Field(default_factory=list)
    failed_edges: List[EdgeIn] = Field(default_factory=list)


class AnalyzeResponse(BaseModel):
    source: str
    sink: str
    edge_connectivity: int
    vertex_connectivity: int
    edge_disjoint_paths: List[List[str]]
    vertex_disjoint_paths: List[List[str]]
    articulation_points: List[str]
    bridges: List[Tuple[str, str]]
    min_cut_edges: List[Tuple[str, str]]
    min_cut_vertices: List[str]


class SimulateFailureResponse(BaseModel):
    connected: bool
    reason: Optional[str] = None
    edge_connectivity: int
    vertex_connectivity: int
    edge_disjoint_paths: List[List[str]]
    vertex_disjoint_paths: List[List[str]]
    remaining_nodes: List[str] = Field(default_factory=list)
    remaining_edges: List[EdgeIn] = Field(default_factory=list)
