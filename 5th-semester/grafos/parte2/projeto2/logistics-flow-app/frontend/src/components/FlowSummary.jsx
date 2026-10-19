import { Truck } from 'lucide-react'

/**
 * FlowSummary
 * -----------
 * Card compacto exibindo o Valor Total do Fluxo F = f(D), a origem e o
 * destino da malha calculada.
 */
export default function FlowSummary({ maxFlow, source, sink, unit = 't/dia' }) {
  return (
    <div className="rounded-lg border border-line bg-panel-raised p-4">
      <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-muted">
        <Truck size={14} strokeWidth={2} />
        Escoamento ótimo — F = f(D)
      </div>
      <div className="mt-2 flex items-baseline gap-2">
        <span className="font-display text-4xl font-700 text-ink">
          {maxFlow === null || maxFlow === undefined ? '—' : maxFlow}
        </span>
        <span className="font-mono text-sm text-muted">{unit}</span>
      </div>
      <div className="mt-3 flex items-center gap-2 font-mono text-xs text-muted">
        <span className="rounded border border-signal/40 px-1.5 py-0.5 text-signal">{source}</span>
        <span aria-hidden="true">→</span>
        <span className="rounded border border-signal/40 px-1.5 py-0.5 text-signal">{sink}</span>
      </div>
    </div>
  )
}
