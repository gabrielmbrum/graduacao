"""
main.py
-------
Ponto de entrada da API FastAPI para a plataforma de Distribuição e
Logística de Malha de Abastecimento (Fluxo Máximo / Ford-Fulkerson).

Rodar localmente:
    uvicorn app.main:app --reload --port 8000

Docs interativas:
    http://localhost:8000/docs
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.flow_routes import router as flow_router

app = FastAPI(
    title="Logistics Flow API",
    description=(
        "API para cálculo de fluxo máximo (Edmonds-Karp), construção da "
        "rede residual e identificação do corte mínimo em malhas de "
        "distribuição logística."
    ),
    version="1.0.0",
)

# CORS liberado para o frontend (Vite dev server / produção) consumir a API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flow_router)


@app.get("/", tags=["health"])
def health_check() -> dict:
    return {"status": "ok", "service": "logistics-flow-api"}
