/**
 * MetricsCard.jsx
 * ---------------
 * Exibe a "leitura de instrumentos" da rede: conectividade de
 * arestas (CA) e de vértices (CV) — o k do Teorema de Menger —,
 * além dos gargalos estruturais (pontos de articulação, pontes) e
 * do corte mínimo desconectador associado ao par origem/destino.
 */

export default function MetricsCard({ metrics, simulation }) {
  const hasMetrics = !!metrics;

  return (
    <div className="flex flex-col gap-3 rounded-lg border border-line bg-panel p-4 shadow-panel">
      <h2 className="font-mono text-[10px] uppercase tracking-[0.15em] text-dim">
        Métricas de resiliência
      </h2>

      {!hasMetrics && (
        <p className="font-mono text-[11px] text-dim">
          aguardando análise…
        </p>
      )}

      {hasMetrics && (
        <>
          <div className="grid grid-cols-2 gap-2">
            <Gauge label="k (arestas)" value={metrics.edge_connectivity} accent="#4FD8C4" />
            <Gauge label="k (vértices)" value={metrics.vertex_connectivity} accent="#9B8CFF" />
          </div>

          <Row label="pontos de articulação">
            {metrics.articulation_points.length > 0
              ? metrics.articulation_points.join(", ")
              : "nenhum"}
          </Row>

          <Row label="pontes">
            {metrics.bridges.length > 0
              ? metrics.bridges.map((b) => `${b[0]}–${b[1]}`).join(", ")
              : "nenhuma"}
          </Row>

          <Row label="corte mínimo (arestas)">
            {metrics.min_cut_edges.length > 0
              ? metrics.min_cut_edges.map((e) => `${e[0]}–${e[1]}`).join(", ")
              : "—"}
          </Row>

          <Row label="corte mínimo (vértices)">
            {metrics.min_cut_vertices.length > 0 ? metrics.min_cut_vertices.join(", ") : "—"}
          </Row>
        </>
      )}

      {simulation && (
        <div
          className={`mt-1 rounded border px-3 py-2 font-mono text-[11px] ${
            simulation.connected
              ? "border-signal/40 bg-signal/10 text-signal"
              : "border-alert/40 bg-alert/10 text-alert"
          }`}
        >
          {simulation.connected
            ? `sobrevive à falha — CA=${simulation.edge_connectivity} CV=${simulation.vertex_connectivity}`
            : simulation.reason || "rede desconectada após a falha simulada"}
        </div>
      )}
    </div>
  );
}

function Gauge({ label, value, accent }) {
  return (
    <div className="rounded border border-line-soft bg-panel2 px-3 py-2">
      <div className="font-mono text-2xl font-semibold" style={{ color: accent }}>
        {value}
      </div>
      <div className="font-mono text-[10px] uppercase tracking-wide text-dim">{label}</div>
    </div>
  );
}

function Row({ label, children }) {
  return (
    <div className="border-t border-line-soft pt-2 first:border-t-0 first:pt-0">
      <div className="font-mono text-[10px] uppercase tracking-wide text-dim">{label}</div>
      <div className="font-mono text-xs text-hi">{children}</div>
    </div>
  );
}
