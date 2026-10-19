/**
 * PathViewer.jsx
 * --------------
 * Mostra as rotas redundantes encontradas pelo Teorema de Menger,
 * com um ponto colorido por rota que corresponde exatamente à cor
 * do pulso de sinal desenhado em GraphCanvas (mesmo índice → mesma
 * cor), para que o usuário associe visualmente lista ↔ diagrama.
 */

const PATH_COLORS = ["#4FD8C4", "#9B8CFF", "#E8B75E", "#FF9FB2", "#7DD3FC"];

export default function PathViewer({ activeTab, onTabChange, edgePaths, vertexPaths, connected }) {
  const hasResult = edgePaths.length > 0 || vertexPaths.length > 0;
  const paths = activeTab === "edge" ? edgePaths : vertexPaths;

  return (
    <div className="flex h-full flex-col rounded-lg border border-line bg-panel p-4 shadow-panel">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="font-mono text-[10px] uppercase tracking-[0.15em] text-dim">
          Rotas redundantes
        </h2>
        {connected === false && (
          <span className="rounded bg-alert/10 px-2 py-0.5 font-mono text-[10px] uppercase text-alert">
            desconectado
          </span>
        )}
      </div>

      <div className="mb-3 flex gap-1 rounded border border-line-soft bg-panel2 p-1">
        <TabButton active={activeTab === "edge"} onClick={() => onTabChange("edge")}>
          aresta-disjuntos
        </TabButton>
        <TabButton active={activeTab === "vertex"} onClick={() => onTabChange("vertex")}>
          vértice-disjuntos
        </TabButton>
      </div>

      {!hasResult && (
        <p className="font-mono text-[11px] text-dim">
          rode uma análise para ver as rotas redundantes entre origem e destino.
        </p>
      )}

      {hasResult && paths.length === 0 && (
        <p className="font-mono text-[11px] text-alert">
          nenhuma rota sobrevivente entre origem e destino.
        </p>
      )}

      <ul className="flex flex-col gap-1.5 overflow-y-auto">
        {paths.map((path, idx) => (
          <li
            key={idx}
            className="flex items-center gap-2 rounded border border-line-soft bg-panel2 px-2.5 py-1.5 font-mono text-xs text-hi"
          >
            <span
              className="h-2.5 w-2.5 shrink-0 rounded-full"
              style={{ backgroundColor: PATH_COLORS[idx % PATH_COLORS.length] }}
            />
            <span className="truncate">{path.join(" → ")}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function TabButton({ active, onClick, children }) {
  return (
    <button
      onClick={onClick}
      className={`w-full rounded py-1 font-mono text-[11px] uppercase tracking-wide transition-colors ${
        active ? "bg-signal text-ink" : "text-mid hover:text-hi"
      }`}
    >
      {children}
    </button>
  );
}
