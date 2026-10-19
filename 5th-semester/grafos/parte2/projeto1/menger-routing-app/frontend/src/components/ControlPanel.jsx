/**
 * ControlPanel.jsx
 * ----------------
 * - Cadastro de nós (roteadores) e enlaces.
 * - Seleção de origem (v) e destino (w).
 * - Botão "Analisar" (calcula caminhos disjuntos e conectividade).
 * - Alternância para o modo "Simular Falha" (clique no canvas marca
 *   nós/arestas como falhos) + botão para rodar a simulação.
 */

export default function ControlPanel({
  nodes,
  edges,
  newNodeId,
  onNewNodeIdChange,
  onAddNode,
  edgeFrom,
  edgeTo,
  onEdgeFromChange,
  onEdgeToChange,
  onAddEdge,
  onRemoveEdge,
  source,
  sink,
  onSourceChange,
  onSinkChange,
  onAnalyze,
  analyzing,
  failureMode,
  onToggleFailureMode,
  failedCount,
  onSimulateFailure,
  simulating,
  onResetFailures,
  onLoadSample,
  errorMessage,
}) {
  return (
    <div className="flex h-full flex-col gap-4 overflow-y-auto rounded-lg border border-line bg-panel p-4 shadow-panel">
      <Section title="Topologia">
        <div className="flex gap-2">
          <input
            value={newNodeId}
            onChange={(e) => onNewNodeIdChange(e.target.value)}
            placeholder="id do nó, ex: R4"
            className="w-full rounded border border-line-soft bg-panel2 px-2 py-1.5 font-mono text-xs text-hi placeholder:text-dim focus:border-signal focus:outline-none"
            maxLength={12}
          />
          <button
            onClick={onAddNode}
            className="shrink-0 rounded border border-line-soft bg-panel2 px-3 py-1.5 font-mono text-xs text-signal hover:border-signal"
          >
            + nó
          </button>
        </div>

        <div className="mt-3 flex gap-2">
          <select
            value={edgeFrom}
            onChange={(e) => onEdgeFromChange(e.target.value)}
            className="w-full rounded border border-line-soft bg-panel2 px-2 py-1.5 font-mono text-xs text-hi focus:border-signal focus:outline-none"
          >
            <option value="">de…</option>
            {nodes.map((n) => (
              <option key={n.id} value={n.id}>
                {n.id}
              </option>
            ))}
          </select>
          <select
            value={edgeTo}
            onChange={(e) => onEdgeToChange(e.target.value)}
            className="w-full rounded border border-line-soft bg-panel2 px-2 py-1.5 font-mono text-xs text-hi focus:border-signal focus:outline-none"
          >
            <option value="">para…</option>
            {nodes.map((n) => (
              <option key={n.id} value={n.id}>
                {n.id}
              </option>
            ))}
          </select>
          <button
            onClick={onAddEdge}
            className="shrink-0 rounded border border-line-soft bg-panel2 px-3 py-1.5 font-mono text-xs text-signal hover:border-signal"
          >
            + link
          </button>
        </div>

        {edges.length > 0 && (
          <ul className="mt-3 flex max-h-28 flex-col gap-1 overflow-y-auto font-mono text-[11px] text-mid">
            {edges.map((e, i) => (
              <li
                key={`${e.source}-${e.target}-${i}`}
                className="flex items-center justify-between rounded px-1.5 py-0.5 hover:bg-panel2"
              >
                <span>
                  {e.source} <span className="text-dim">↔</span> {e.target}
                </span>
                <button
                  onClick={() => onRemoveEdge(i)}
                  className="text-dim hover:text-alert"
                  aria-label={`Remover enlace ${e.source}-${e.target}`}
                >
                  ×
                </button>
              </li>
            ))}
          </ul>
        )}

        <button
          onClick={onLoadSample}
          className="mt-3 w-full rounded border border-dashed border-line-soft py-1.5 font-mono text-[11px] text-dim hover:border-mid hover:text-mid"
        >
          carregar topologia de exemplo
        </button>
      </Section>

      <Section title="Rota">
        <div className="flex gap-2">
          <Labeled label="origem (v)">
            <select
              value={source}
              onChange={(e) => onSourceChange(e.target.value)}
              className="w-full rounded border border-line-soft bg-panel2 px-2 py-1.5 font-mono text-xs text-signal focus:border-signal focus:outline-none"
            >
              <option value="">—</option>
              {nodes.map((n) => (
                <option key={n.id} value={n.id}>
                  {n.id}
                </option>
              ))}
            </select>
          </Labeled>
          <Labeled label="destino (w)">
            <select
              value={sink}
              onChange={(e) => onSinkChange(e.target.value)}
              className="w-full rounded border border-line-soft bg-panel2 px-2 py-1.5 font-mono text-xs text-redundant focus:border-redundant focus:outline-none"
            >
              <option value="">—</option>
              {nodes.map((n) => (
                <option key={n.id} value={n.id}>
                  {n.id}
                </option>
              ))}
            </select>
          </Labeled>
        </div>

        <button
          onClick={onAnalyze}
          disabled={!source || !sink || source === sink || analyzing}
          className="mt-3 w-full rounded bg-signal py-2 font-mono text-xs font-semibold uppercase tracking-wide text-ink disabled:cursor-not-allowed disabled:bg-line-soft disabled:text-dim"
        >
          {analyzing ? "analisando…" : "analisar caminhos"}
        </button>
      </Section>

      <Section title="Simulação de falha">
        <button
          onClick={onToggleFailureMode}
          className={`w-full rounded border py-1.5 font-mono text-xs uppercase tracking-wide ${
            failureMode
              ? "border-alert bg-alert/10 text-alert"
              : "border-line-soft text-mid hover:border-mid"
          }`}
        >
          {failureMode ? "modo falha: ativo" : "ativar modo falha"}
        </button>

        {failureMode && (
          <p className="mt-2 font-mono text-[11px] text-dim">
            clique em nós/enlaces no diagrama para marcá-los como
            indisponíveis ({failedCount} marcado{failedCount === 1 ? "" : "s"})
          </p>
        )}

        <div className="mt-3 flex gap-2">
          <button
            onClick={onSimulateFailure}
            disabled={!source || !sink || failedCount === 0 || simulating}
            className="w-full rounded bg-alert py-2 font-mono text-xs font-semibold uppercase tracking-wide text-ink disabled:cursor-not-allowed disabled:bg-line-soft disabled:text-dim"
          >
            {simulating ? "simulando…" : "simular queda"}
          </button>
          <button
            onClick={onResetFailures}
            disabled={failedCount === 0}
            className="shrink-0 rounded border border-line-soft px-3 font-mono text-xs text-mid hover:border-mid disabled:opacity-40"
          >
            limpar
          </button>
        </div>
      </Section>

      {errorMessage && (
        <div className="rounded border border-alert/40 bg-alert/10 px-3 py-2 font-mono text-[11px] text-alert">
          {errorMessage}
        </div>
      )}
    </div>
  );
}

function Section({ title, children }) {
  return (
    <div>
      <h2 className="mb-2 font-mono text-[10px] uppercase tracking-[0.15em] text-dim">
        {title}
      </h2>
      {children}
    </div>
  );
}

function Labeled({ label, children }) {
  return (
    <div className="w-full">
      <span className="mb-1 block font-mono text-[10px] text-dim">{label}</span>
      {children}
    </div>
  );
}
