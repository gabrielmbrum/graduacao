import { AlertTriangle } from 'lucide-react'

/**
 * BottleneckCard
 * ---------------
 * Painel de destaque das arestas do Corte Mínimo — as rodovias que formam
 * o gargalo logístico, onde investimento de ampliação de capacidade traria
 * o maior retorno (Teorema do Fluxo Máximo-Corte Mínimo).
 */
export default function BottleneckCard({ cutEdges = [], partitionS = [], partitionT = [] }) {
  const totalCapacity = cutEdges.reduce((sum, e) => sum + e.capacity, 0)

  return (
    <div className="rounded-lg border border-saturated/30 bg-panel-raised">
      <div className="flex items-center gap-2 border-b border-saturated/20 bg-hazard/[0.06] px-4 py-3">
        <AlertTriangle size={16} className="text-saturated" strokeWidth={2} />
        <h3 className="font-display text-sm font-600 tracking-wide text-ink">
          Gargalo logístico — Corte Mínimo
        </h3>
      </div>

      {cutEdges.length === 0 ? (
        <p className="px-4 py-4 text-sm text-muted">
          Calcule o fluxo para identificar os trechos que limitam o escoamento.
        </p>
      ) : (
        <>
          <ul className="divide-y divide-line-soft">
            {cutEdges.map((e, i) => (
              <li key={i} className="flex items-center justify-between px-4 py-2.5">
                <span className="font-mono text-sm text-ink">
                  {e.source} <span className="text-muted">→</span> {e.target}
                </span>
                <span className="rounded bg-saturated/10 px-2 py-0.5 font-mono text-xs text-saturated">
                  c = {e.capacity}
                </span>
              </li>
            ))}
          </ul>
          <div className="flex items-center justify-between border-t border-line-soft px-4 py-3 font-mono text-xs text-muted">
            <span>capacidade do corte</span>
            <span className="text-ink">{totalCapacity}</span>
          </div>
          <div className="grid grid-cols-2 gap-px border-t border-line-soft bg-line-soft text-xs">
            <div className="bg-panel-raised px-4 py-2">
              <div className="text-muted">partição S</div>
              <div className="mt-0.5 font-mono text-ink">{partitionS.join(', ')}</div>
            </div>
            <div className="bg-panel-raised px-4 py-2">
              <div className="text-muted">partição S̄</div>
              <div className="mt-0.5 font-mono text-ink">{partitionT.join(', ')}</div>
            </div>
          </div>
        </>
      )}
    </div>
  )
}
