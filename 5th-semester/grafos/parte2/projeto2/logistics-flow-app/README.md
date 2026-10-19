# Malha de Abastecimento — Fluxo Máximo (Ford-Fulkerson / Edmonds-Karp)

## A. Resumo da Aplicação

Plataforma web de gestão logística voltada para o transporte de cargas de
centros de distribuição (origem *s*) até polos de entrega (destino *t*)
através de uma malha viária com capacidades limitadas por trecho.

A ferramenta modela a malha como uma rede de fluxo, calcula o escoamento
ótimo de carga com o algoritmo de Edmonds-Karp (Ford-Fulkerson via BFS),
constrói a rede residual a cada iteração e identifica automaticamente o
**Corte Mínimo** — as rodovias que formam o gargalo logístico, onde
investimentos de ampliação de capacidade trariam o maior retorno.

O usuário edita os trechos da malha (origem, destino e capacidade de cada
aresta) em uma interface web, define os vértices de origem e destino, e
recebe: o valor do fluxo máximo, o fluxo final de cada trecho, a partição
(S, S̄) e as arestas que compõem o gargalo — tudo visualizado em um grafo
interativo, com um modo passo a passo que anima cada caminho aumentante
encontrado pelo algoritmo.

## B. Conceitos de Teoria dos Grafos Utilizados

* **Digrafo Ponderado D = (V, E, c):** vértices como cidades/armazéns e
  arestas direcionadas com capacidade de transporte c(e).
* **Fluxo em rede:** função f(e) que respeita 0 ≤ f(e) ≤ c(e) em cada
  aresta.
* **Conservação de Fluxo:** ∑ f(vⱼ, v) = ∑ f(v, vⱼ) para todo vértice
  intermediário v ∈ V \ {s, t}.
* **Aresta e Vértice Saturado:** uma aresta é saturada quando f(e) = c(e).
* **Rede Residual D'(f):** construída a cada iteração com arestas diretas
  (capacidade residual c(e) − f(e)) e arestas contrárias (capacidade
  residual f(e)).
* **Caminho Aumentante:** caminho de s a t na rede residual; seu gargalo é
  Δ = min{c'(e) : e no caminho}.
* **Algoritmo de Ford-Fulkerson / Edmonds-Karp:** busca em largura (BFS)
  para encontrar caminhos aumentantes e saturação sucessiva de capacidade,
  repetido até não existir mais caminho aumentante na rede residual.
* **Corte (S, S̄):** partição dos vértices com s ∈ S e t ∈ S̄; capacidade do
  corte c(S, S̄) = soma das capacidades das arestas que saem de S para S̄.
* **Teorema do Fluxo Máximo – Corte Mínimo (Szwarcfiter):** o valor do
  fluxo máximo é igual à capacidade do corte mínimo; na condição de
  parada, toda aresta de avanço de S para S̄ está saturada e toda aresta
  de retorno de S̄ para S tem fluxo nulo.

## C. Estruturação Completa do Projeto

```text
logistics-flow-app/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── flow_routes.py      # Endpoints REST (POST /flow/solve, POST /flow/trace-iterations)
│   │   ├── engine/
│   │   │   ├── network.py          # Estrutura da Rede de Fluxo (Capacidade e Fluxo)
│   │   │   ├── residual.py         # Gerador da Rede Residual D0(f) + BFS de caminho aumentante
│   │   │   ├── edmonds_karp.py     # Algoritmo de Ford-Fulkerson via BFS
│   │   │   └── min_cut.py          # Identificador da partição de corte mínimo (S, S_bar)
│   │   ├── schemas/
│   │   │   └── flow_dto.py         # Estruturas de entrada/saída JSON (Pydantic)
│   │   └── main.py                 # Ponto de entrada FastAPI
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── LogisticsCanvas.jsx # Grafo visual (Cytoscape.js) com arestas "f(e) / c(e)"
    │   │   ├── StepByStepPanel.jsx # Controle para avançar iterações da rede residual
    │   │   ├── BottleneckCard.jsx  # Painel de destaque das arestas do Corte Mínimo
    │   │   └── FlowSummary.jsx     # Card do Valor Total do Fluxo F = f(D)
    │   ├── services/
    │   │   └── flowApi.js          # Cliente HTTP para a API de fluxo
    │   ├── App.jsx                 # Editor da malha + orquestração dos componentes
    │   ├── main.jsx
    │   └── index.css
    ├── index.html
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    └── postcss.config.js
```

### Principais Endpoints do Backend
- `POST /api/flow/solve` — recebe a malha viária, capacidades e nós s, t;
  retorna o fluxo máximo F, o fluxo final em cada aresta e a partição do
  corte mínimo.
- `POST /api/flow/trace-iterations` — retorna o histórico passo a passo
  (caminho aumentante e estado da rede residual de cada iteração) para
  visualização educacional animada.

## D. Stacks Utilizadas

**Backend**
- Linguagem: Python 3.11+
- Framework: FastAPI + Pydantic (validação e serialização de grafos)
- Servidor ASGI: Uvicorn
- Estruturas de dados: `collections.deque` para a fila BFS do Edmonds-Karp

**Frontend**
- Framework: React 18 + Vite
- Visualização de Grafos: Cytoscape.js com layout `dagre` (organiza o
  fluxo da esquerda para a direita, de s a t)
- Estilização: TailwindCSS (design system próprio, tema "planta técnica
  rodoviária")
- Ícones: lucide-react
