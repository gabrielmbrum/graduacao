"""
main.py
-------
Ponto de entrada da API FastAPI. Registra o CORS (necessário para o
frontend Vite em outra origem/porta) e inclui as rotas de /api/graph.

Rodar localmente:
    uvicorn app.main:app --reload --port 8000

Swagger automático em: http://localhost:8000/docs
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as graph_router

app = FastAPI(
    title="Menger Routing API",
    description=(
        "API de simulação de roteamento multi-caminho tolerante a falhas, "
        "baseada no Teorema de Menger (caminhos disjuntos via fluxo unitário)."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, restrinja à origem do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graph_router)


@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok", "service": "menger-routing-api"}
