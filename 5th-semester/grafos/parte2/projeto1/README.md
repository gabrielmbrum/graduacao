# Projeto 1: Roteamento Multi-Caminho Tolerante a Falhas

Simulador interativo de resiliência de redes baseado no **Teorema de Menger**: calcula rotas redundantes (aresta- e vértice-disjuntas) entre dois nós de uma topologia e permite simular a queda de roteadores/enlaces em tempo real.

```
menger-routing-app/
├── backend/     FastAPI + algoritmos de grafos (Python)
└── frontend/    React + Vite + Cytoscape.js (JavaScript)
```

Este guia assume **Python 3.11+** e **Node.js 18+** instalados. Os dois serviços rodam em paralelo: o backend expõe a API na porta `8000`, o frontend consome essa API na porta `5173`.

---

## 1. Backend (FastAPI)

```bash
cd backend

# cria e ativa um ambiente virtual (recomendado)
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# instala as dependências
pip install -r requirements.txt

# sobe o servidor com reload automático
uvicorn app.main:app --reload --port 8000
```

Se tudo deu certo:
- API em `http://localhost:8000`
- Documentação Swagger automática em `http://localhost:8000/docs`
- Health check: `curl http://localhost:8000/` → `{"status":"ok","service":"menger-routing-api"}`

### Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/api/graph/analyze` | Recebe a topologia + origem/destino; retorna caminhos disjuntos, conectividade CA/CV, pontos de articulação, pontes e cortes mínimos. |
| `POST` | `/api/graph/simulate-failure` | Recebe a topologia + nós/arestas falhos; recalcula as rotas sobreviventes. |

Teste rápido via `curl`:

```bash
curl -X POST http://localhost:8000/api/graph/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "graph": {
      "nodes": ["DC","R1","R2","BR"],
      "edges": [
        {"source":"DC","target":"R1"},
        {"source":"R1","target":"BR"},
        {"source":"DC","target":"R2"},
        {"source":"R2","target":"BR"}
      ],
      "directed": false
    },
    "source": "DC",
    "sink": "BR"
  }'
```

---

## 2. Frontend (React + Vite)

Em um **novo terminal** (deixe o backend rodando):

```bash
cd frontend

# copie o arquivo de ambiente de exemplo
cp .env.example .env
# .env já aponta para http://localhost:8000 — ajuste VITE_API_URL se o backend rodar em outro endereço

# instala as dependências
npm install

# sobe o servidor de desenvolvimento
npm run dev
```

Acesse `http://localhost:5173`. O console carrega com uma topologia de exemplo (`DC → R1/R2/R3 → BR`) já pronta para análise.

### Fluxo de uso

1. **Topologia**: adicione nós e enlaces pelo painel de controle (ou use o exemplo pré-carregado).
2. **Rota**: escolha origem (v) e destino (w), clique em **Analisar caminhos**.
3. O canvas destaca os caminhos disjuntos com pulsos de sinal animados; o painel de métricas mostra CA, CV, pontos de articulação, pontes e cortes mínimos.
4. **Simulação de falha**: ative o modo falha, clique em nós/enlaces no diagrama para marcá-los como indisponíveis, depois clique em **Simular queda** para ver as rotas sobreviventes recalculadas.

### Build de produção

```bash
npm run build      # gera frontend/dist
npm run preview    # serve o build localmente para conferência
```

---

## 3. Rodando os dois juntos (resumo)

```bash
# terminal 1
cd backend && source .venv/bin/activate && uvicorn app.main:app --reload --port 8000

# terminal 2
cd frontend && npm run dev
```

Depois é só abrir `http://localhost:5173` com a API já no ar em `http://localhost:8000`.

---

## 4. Solução de problemas

- **CORS / "failed to fetch" no navegador**: confirme que o backend está rodando e que `VITE_API_URL` no `.env` do frontend aponta para a porta correta. O backend já libera CORS de qualquer origem (`allow_origins=["*"]`) para desenvolvimento.
- **`422 Unprocessable Entity` no `/analyze`**: origem ou destino não existe no grafo enviado, ou origem == destino.
- **Porta 8000 ou 5173 ocupada**: rode com `--port <outra_porta>` (backend) ou ajuste `server.port` em `frontend/vite.config.js` (e o `VITE_API_URL` correspondente).