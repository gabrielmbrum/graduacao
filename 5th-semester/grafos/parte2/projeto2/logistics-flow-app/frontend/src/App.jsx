import { useMemo, useState } from 'react'
import { Route, Plus, Trash2, Play, Loader2 } from 'lucide-react'
import LogisticsCanvas from './components/LogisticsCanvas.jsx'
import StepByStepPanel from './components/StepByStepPanel.jsx'
import BottleneckCard from './components/BottleneckCard.jsx'
import FlowSummary from './components/FlowSummary.jsx'
import { solveFlow, traceIterations } from './services/flowApi.js'

const DEFAULT_EDGES = [
  { source: 'CD-Campinas', target: 'Hub-Jundiaí', capacity: 10 },
  { source: 'CD-Campinas', target: 'Hub-Sorocaba', capacity: 10 },
  { source: 'Hub-Jundiaí', target: 'Polo-SP-Norte', capacity: 4 },
  { source: 'Hub-Jundiaí', target: 'Hub-Sorocaba', capacity: 2 },
  { source: 'Hub-Jundiaí', target: 'Terminal-ABC', capacity: 8 },
  { source: 'Hub-Sorocaba', target: 'Terminal-ABC', capacity: 9 },
  { source: 'Polo-SP-Norte', target: 'Polo-SP-Capital', capacity: 10 },
  { source: 'Terminal-ABC', target: 'Polo-SP-Norte', capacity: 6 },
  { source: 'Terminal-ABC', target: 'Polo-SP-Capital', capacity: 10 },
]

const DEFAULT_SOURCE = 'CD-Campinas'
const DEFAULT_SINK = 'Polo-SP-Capital'

function nodesFromEdges(edges) {
  const set = new Set()
  edges.forEach((e) => {
    if (e.source) set.add(e.source)
    if (e.target) set.add(e.target)
  })
  return Array.from(set)
}

export default function App() {
  const [edges, setEdges] = useState(DEFAULT_EDGES)
  const [source, setSource] = useState(DEFAULT_SOURCE)
  const [sink, setSink] = useState(DEFAULT_SINK)

  const [result, setResult] = useState(null)
  const [steps, setSteps] = useState([])
  const [stepIndex, setStepIndex] = useState(0)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const nodes = useMemo(() => nodesFromEdges(edges), [edges])

  const minCutEdgeKeys = useMemo(() => {
    if (!result) return new Set()
    return new Set(result.min_cut_edges.map((e) => `${e.source}->${e.target}`))
  }, [result])

  const displayEdges = useMemo(() => {
    if (result) return result.edges
    return edges.map((e) => ({ ...e, flow: 0, saturated: false }))
  }, [result, edges])

  const currentHighlightPath = steps.length ? steps[stepIndex]?.augmenting_path ?? [] : []

  function updateEdge(index, patch) {
    setEdges((prev) => prev.map((e, i) => (i === index ? { ...e, ...patch } : e)))
  }

  function addEdge() {
    setEdges((prev) => [...prev, { source: '', target: '', capacity: 1 }])
  }

  function removeEdge(index) {
    setEdges((prev) => prev.filter((_, i) => i !== index))
  }

  async function handleSolve() {
    setError(null)
    setLoading(true)
    setSteps([])
    setStepIndex(0)
    try {
      const payload = { nodes, edges, source, sink }
      const [solveRes, traceRes] = await Promise.all([
        solveFlow(payload),
        traceIterations(payload),
      ])
      setResult(solveRes)
      setSteps(traceRes.steps)
    } catch (err) {
      setError(err.message || 'Falha ao calcular o fluxo. Verifique se a API está no ar.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-void">
      <header className="border-b border-line bg-panel/60">
        <div className="mx-auto flex max-w-6xl items-center gap-3 px-6 py-5">
          <div className="flex h-9 w-9 items-center justify-center rounded border border-signal/50 bg-signal/10">
            <Route size={18} className="text-signal" strokeWidth={2} />
          </div>
          <div>
            <h1 className="font-display text-lg font-700 leading-tight text-ink">
              Malha de Abastecimento
            </h1>
            <p className="font-mono text-xs text-muted">
              fluxo máximo · rede residual · corte mínimo — Ford-Fulkerson / Edmonds-Karp
            </p>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-6xl px-6 py-8">
        <div className="grid grid-cols-1 gap-6 lg:grid-cols-[1fr_320px]">
          {/* Coluna principal: editor da malha + canvas + passo a passo */}
          <div className="space-y-6">
            <EdgeEditor
              edges={edges}
              source={source}
              sink={sink}
              nodes={nodes}
              onUpdateEdge={updateEdge}
              onAddEdge={addEdge}
              onRemoveEdge={removeEdge}
              onChangeSource={setSource}
              onChangeSink={setSink}
              onSolve={handleSolve}
              loading={loading}
            />

            {error && (
              <div className="rounded-lg border border-saturated/40 bg-saturated/10 px-4 py-3 text-sm text-saturated">
                {error}
              </div>
            )}

            <LogisticsCanvas
              nodes={nodes}
              edges={displayEdges}
              source={source}
              sink={sink}
              minCutEdgeKeys={minCutEdgeKeys}
              highlightPath={currentHighlightPath}
            />

            <StepByStepPanel steps={steps} currentIndex={stepIndex} onChangeIndex={setStepIndex} />
          </div>

          {/* Coluna lateral: métricas */}
          <div className="space-y-6">
            <FlowSummary maxFlow={result?.max_flow ?? null} source={source} sink={sink} />
            <BottleneckCard
              cutEdges={result?.min_cut_edges ?? []}
              partitionS={result?.partition_s ?? []}
              partitionT={result?.partition_t ?? []}
            />
          </div>
        </div>
      </main>
    </div>
  )
}

function EdgeEditor({
  edges,
  source,
  sink,
  nodes,
  onUpdateEdge,
  onAddEdge,
  onRemoveEdge,
  onChangeSource,
  onChangeSink,
  onSolve,
  loading,
}) {
  return (
    <div className="rounded-lg border border-line bg-panel-raised">
      <div className="flex flex-wrap items-center justify-between gap-3 border-b border-line px-4 py-3">
        <h2 className="font-display text-sm font-600 tracking-wide text-ink">
          Trechos da malha viária
        </h2>
        <div className="flex items-center gap-3 font-mono text-xs">
          <label className="flex items-center gap-1.5 text-muted">
            origem (s)
            <input
              value={source}
              onChange={(e) => onChangeSource(e.target.value)}
              list="node-options"
              className="w-32 rounded border border-line bg-void px-2 py-1 text-signal"
            />
          </label>
          <label className="flex items-center gap-1.5 text-muted">
            destino (t)
            <input
              value={sink}
              onChange={(e) => onChangeSink(e.target.value)}
              list="node-options"
              className="w-32 rounded border border-line bg-void px-2 py-1 text-signal"
            />
          </label>
          <datalist id="node-options">
            {nodes.map((n) => (
              <option key={n} value={n} />
            ))}
          </datalist>
        </div>
      </div>

      <div className="divide-y divide-line-soft">
        {edges.map((edge, i) => (
          <div key={i} className="flex items-center gap-2 px-4 py-2">
            <input
              value={edge.source}
              onChange={(e) => onUpdateEdge(i, { source: e.target.value })}
              placeholder="origem"
              className="w-full min-w-0 flex-1 rounded border border-line bg-void px-2 py-1.5 font-mono text-sm text-ink placeholder:text-muted/60"
            />
            <span className="text-muted">→</span>
            <input
              value={edge.target}
              onChange={(e) => onUpdateEdge(i, { target: e.target.value })}
              placeholder="destino"
              className="w-full min-w-0 flex-1 rounded border border-line bg-void px-2 py-1.5 font-mono text-sm text-ink placeholder:text-muted/60"
            />
            <input
              type="number"
              min="1"
              value={edge.capacity}
              onChange={(e) => onUpdateEdge(i, { capacity: Number(e.target.value) })}
              className="w-20 rounded border border-line bg-void px-2 py-1.5 text-right font-mono text-sm text-signal"
            />
            <button
              type="button"
              onClick={() => onRemoveEdge(i)}
              aria-label={`Remover trecho ${edge.source} para ${edge.target}`}
              className="rounded p-1.5 text-muted hover:bg-saturated/10 hover:text-saturated"
            >
              <Trash2 size={14} />
            </button>
          </div>
        ))}
      </div>

      <div className="flex items-center justify-between gap-3 px-4 py-3">
        <button
          type="button"
          onClick={onAddEdge}
          className="flex items-center gap-1.5 rounded border border-line px-3 py-1.5 font-mono text-xs text-ink hover:border-flow"
        >
          <Plus size={14} />
          adicionar trecho
        </button>

        <button
          type="button"
          onClick={onSolve}
          disabled={loading}
          className="flex items-center gap-2 rounded bg-signal px-4 py-2 font-mono text-xs font-600 text-void disabled:opacity-50 hover:enabled:brightness-110"
        >
          {loading ? <Loader2 size={14} className="animate-spin" /> : <Play size={14} />}
          {loading ? 'calculando…' : 'calcular fluxo máximo'}
        </button>
      </div>
    </div>
  )
}
