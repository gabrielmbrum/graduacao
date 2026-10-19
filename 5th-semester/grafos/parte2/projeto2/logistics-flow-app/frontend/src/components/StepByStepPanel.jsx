import { ChevronLeft, ChevronRight, Play, Pause, RotateCcw } from 'lucide-react'
import { useEffect, useRef, useState } from 'react'

/**
 * StepByStepPanel
 * ----------------
 * Controle para avançar as iterações da rede residual: a cada passo mostra
 * o caminho aumentante encontrado pela BFS (Edmonds-Karp) e o gargalo
 * Δ = min c0(e) daquela iteração. Suporta reprodução automática.
 */
export default function StepByStepPanel({ steps = [], currentIndex, onChangeIndex }) {
  const [playing, setPlaying] = useState(false)
  const intervalRef = useRef(null)

  const hasSteps = steps.length > 0
  const step = hasSteps ? steps[currentIndex] : null
  const atEnd = currentIndex >= steps.length - 1

  useEffect(() => {
    if (playing && hasSteps) {
      intervalRef.current = setInterval(() => {
        onChangeIndex((prev) => {
          if (prev >= steps.length - 1) {
            setPlaying(false)
            return prev
          }
          return prev + 1
        })
      }, 1100)
    }
    return () => clearInterval(intervalRef.current)
  }, [playing, hasSteps, steps.length, onChangeIndex])

  return (
    <div className="rounded-lg border border-line bg-panel-raised">
      <div className="flex items-center justify-between border-b border-line px-4 py-3">
        <h3 className="font-display text-sm font-600 tracking-wide text-ink">
          Iterações do Edmonds-Karp
        </h3>
        <span className="font-mono text-xs text-muted">
          {hasSteps ? `${currentIndex + 1} / ${steps.length}` : '0 / 0'}
        </span>
      </div>

      <div className="px-4 py-4">
        {!hasSteps ? (
          <p className="text-sm text-muted">
            Calcule o rastro (trace) para visualizar cada caminho aumentante encontrado pela busca
            em largura na rede residual.
          </p>
        ) : (
          <div className="space-y-3">
            <div>
              <div className="text-xs font-mono uppercase tracking-wider text-muted">
                Caminho aumentante
              </div>
              <div className="mt-1 flex flex-wrap items-center gap-1.5 font-mono text-sm text-flow">
                {step.augmenting_path.map((node, i) => (
                  <span key={i} className="flex items-center gap-1.5">
                    <span className="rounded border border-flow/40 bg-flow/10 px-1.5 py-0.5">
                      {node}
                    </span>
                    {i < step.augmenting_path.length - 1 && (
                      <span className="text-muted">→</span>
                    )}
                  </span>
                ))}
              </div>
            </div>

            <div className="flex gap-6 font-mono text-xs">
              <div>
                <span className="text-muted">gargalo Δ = </span>
                <span className="text-signal">{step.bottleneck}</span>
              </div>
              <div>
                <span className="text-muted">fluxo acumulado = </span>
                <span className="text-ink">{step.flow_after_step}</span>
              </div>
            </div>
          </div>
        )}
      </div>

      <div className="flex items-center justify-between border-t border-line px-4 py-3">
        <button
          type="button"
          onClick={() => onChangeIndex((prev) => Math.max(0, prev - 1))}
          disabled={!hasSteps || currentIndex === 0}
          className="flex items-center gap-1 rounded border border-line px-2.5 py-1.5 text-xs font-mono text-ink disabled:opacity-30 hover:enabled:border-flow"
        >
          <ChevronLeft size={14} />
          anterior
        </button>

        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={() => {
              if (atEnd) onChangeIndex(0)
              setPlaying((p) => !p)
            }}
            disabled={!hasSteps}
            className="flex items-center gap-1.5 rounded bg-flow/15 px-3 py-1.5 text-xs font-mono text-flow disabled:opacity-30 hover:enabled:bg-flow/25"
          >
            {playing ? <Pause size={14} /> : <Play size={14} />}
            {playing ? 'pausar' : 'reproduzir'}
          </button>
          <button
            type="button"
            onClick={() => {
              setPlaying(false)
              onChangeIndex(0)
            }}
            disabled={!hasSteps}
            className="flex items-center gap-1 rounded border border-line px-2.5 py-1.5 text-xs font-mono text-muted disabled:opacity-30 hover:enabled:border-flow hover:enabled:text-ink"
          >
            <RotateCcw size={13} />
          </button>
        </div>

        <button
          type="button"
          onClick={() => onChangeIndex((prev) => Math.min(steps.length - 1, prev + 1))}
          disabled={!hasSteps || atEnd}
          className="flex items-center gap-1 rounded border border-line px-2.5 py-1.5 text-xs font-mono text-ink disabled:opacity-30 hover:enabled:border-flow"
        >
          próximo
          <ChevronRight size={14} />
        </button>
      </div>
    </div>
  )
}
