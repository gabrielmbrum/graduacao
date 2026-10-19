/**
 * api.js
 * ------
 * Cliente fetch para os endpoints do backend (routes.py):
 *   POST /api/graph/analyze
 *   POST /api/graph/simulate-failure
 *
 * A URL base é configurável via VITE_API_URL (arquivo .env), com
 * fallback para o servidor local de desenvolvimento do FastAPI.
 */

const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function postJSON(path, payload) {
  const res = await fetch(`${BASE_URL}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    let detail = `Erro ${res.status} ao chamar ${path}`;
    try {
      const body = await res.json();
      if (body?.detail) detail = body.detail;
    } catch {
      // resposta sem corpo JSON; mantém a mensagem padrão
    }
    throw new Error(detail);
  }

  return res.json();
}

/**
 * Envia a topologia atual e o par (origem, destino) para análise:
 * caminhos disjuntos, conectividade CA/CV, pontos de articulação,
 * pontes e cortes mínimos.
 */
export function analyzeGraph({ nodes, edges, directed = false }, source, sink) {
  return postJSON("/api/graph/analyze", {
    graph: { nodes, edges, directed },
    source,
    sink,
  });
}

/**
 * Envia a topologia junto com os nós/arestas marcados como falhos e
 * recebe de volta as rotas sobreviventes e a conectividade recalculada.
 */
export function simulateFailure(
  { nodes, edges, directed = false },
  source,
  sink,
  failedNodes,
  failedEdges
) {
  return postJSON("/api/graph/simulate-failure", {
    graph: { nodes, edges, directed },
    source,
    sink,
    failed_nodes: failedNodes,
    failed_edges: failedEdges,
  });
}
