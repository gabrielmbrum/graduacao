/**
 * flowApi.js
 * ----------
 * Camada de acesso à API REST do backend (Ford-Fulkerson / Edmonds-Karp).
 */
const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

async function postJson(path, body) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })

  if (!res.ok) {
    let detail = res.statusText
    try {
      const err = await res.json()
      detail = err.detail || detail
    } catch {
      /* corpo não era JSON */
    }
    throw new Error(detail)
  }

  return res.json()
}

/**
 * Envia a malha viária (nós, arestas com capacidade, origem e destino) e
 * recebe o fluxo máximo final + a partição do corte mínimo.
 */
export function solveFlow({ nodes, edges, source, sink }) {
  return postJson('/api/flow/solve', { nodes, edges, source, sink })
}

/**
 * Recebe o histórico passo a passo de cada iteração do Edmonds-Karp
 * (caminho aumentante, gargalo, rede residual) para animação.
 */
export function traceIterations({ nodes, edges, source, sink }) {
  return postJson('/api/flow/trace-iterations', { nodes, edges, source, sink })
}
