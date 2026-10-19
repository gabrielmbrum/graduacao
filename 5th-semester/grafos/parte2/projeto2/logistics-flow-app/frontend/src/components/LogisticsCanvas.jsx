import { useEffect, useRef } from 'react'
import cytoscape from 'cytoscape'
import dagre from 'cytoscape-dagre'

cytoscape.use(dagre)

const COLORS = {
  nodeFill: '#16223A',
  nodeBorder: '#38BDF8',
  nodeSourceSink: '#F5A524',
  text: '#E8EDF7',
  edgeIdle: '#2A3A5A',
  edgeFlow: '#38BDF8',
  edgeSaturated: '#FB7185',
  edgeAugmenting: '#F5A524',
}

/**
 * LogisticsCanvas
 * ----------------
 * Grafo visual da malha viária. Cada aresta é rotulada no formato "f(e)/c(e)".
 * Arestas do corte mínimo recebem um traço de risco (hazard stripe) e
 * arestas saturadas (f(e) = c(e)) mudam de cor — a leitura visual imediata
 * do gargalo logístico.
 *
 * `highlightPath`: lista de ids de nós do caminho aumentante da iteração
 * atual (usado pelo StepByStepPanel para "iluminar" o caminho em animação).
 */
export default function LogisticsCanvas({
  nodes,
  edges,
  source,
  sink,
  minCutEdgeKeys = new Set(),
  highlightPath = [],
}) {
  const containerRef = useRef(null)
  const cyRef = useRef(null)

  useEffect(() => {
    if (!containerRef.current) return

    const elements = [
      ...nodes.map((n) => ({
        data: { id: n, label: n, isTerminal: n === source || n === sink },
      })),
      ...edges.map((e, i) => {
        const key = `${e.source}->${e.target}`
        const isAugmenting =
          highlightPath.length > 1 &&
          highlightPath.some(
            (node, idx) =>
              idx < highlightPath.length - 1 &&
              node === e.source &&
              highlightPath[idx + 1] === e.target
          )
        return {
          data: {
            id: `e${i}-${key}`,
            source: e.source,
            target: e.target,
            label: `${e.flow ?? 0}/${e.capacity}`,
            saturated: !!e.saturated,
            isCut: minCutEdgeKeys.has(key),
            isAugmenting,
          },
        }
      }),
    ]

    const cy = cytoscape({
      container: containerRef.current,
      elements,
      layout: {
        name: 'dagre',
        rankDir: 'LR',
        nodeSep: 55,
        rankSep: 130,
        animate: true,
        animationDuration: 350,
      },
      style: [
        {
          selector: 'node',
          style: {
            'background-color': COLORS.nodeFill,
            'border-width': 2,
            'border-color': (ele) =>
              ele.data('isTerminal') ? COLORS.nodeSourceSink : COLORS.nodeBorder,
            label: 'data(label)',
            color: COLORS.text,
            'font-family': 'JetBrains Mono, monospace',
            'font-size': 12,
            'font-weight': 600,
            'text-valign': 'center',
            'text-halign': 'center',
            width: 40,
            height: 40,
            shape: 'round-rectangle',
          },
        },
        {
          selector: 'edge',
          style: {
            width: 2.5,
            'curve-style': 'bezier',
            'target-arrow-shape': 'triangle',
            'arrow-scale': 1.1,
            'line-color': (ele) =>
              ele.data('isAugmenting')
                ? COLORS.edgeAugmenting
                : ele.data('saturated')
                  ? COLORS.edgeSaturated
                  : COLORS.edgeIdle,
            'target-arrow-color': (ele) =>
              ele.data('isAugmenting')
                ? COLORS.edgeAugmenting
                : ele.data('saturated')
                  ? COLORS.edgeSaturated
                  : COLORS.edgeIdle,
            label: 'data(label)',
            'font-family': 'JetBrains Mono, monospace',
            'font-size': 10,
            color: COLORS.text,
            'text-background-color': '#0A0E1A',
            'text-background-opacity': 0.85,
            'text-background-padding': 2,
            'line-style': (ele) => (ele.data('isCut') ? 'dashed' : 'solid'),
            'line-dash-pattern': [6, 3],
          },
        },
      ],
    })

    cyRef.current = cy
    return () => cy.destroy()
  }, [nodes, edges, source, sink, minCutEdgeKeys, highlightPath])

  return (
    <div className="relative rounded-lg border border-line bg-panel/60 bp-grid">
      <div
        ref={containerRef}
        className="h-[420px] w-full sm:h-[480px]"
        role="img"
        aria-label="Grafo da malha viária com fluxo calculado"
      />
      <div className="flex flex-wrap gap-4 border-t border-line px-4 py-2 text-xs font-mono text-muted">
        <LegendDot color={COLORS.edgeIdle} label="trecho livre" />
        <LegendDot color={COLORS.edgeSaturated} label="trecho saturado" />
        <LegendDot color={COLORS.edgeAugmenting} label="caminho aumentante" />
        <span className="flex items-center gap-1.5">
          <span className="inline-block h-2 w-4 bg-hazard rounded-sm" />
          corte mínimo
        </span>
      </div>
    </div>
  )
}

function LegendDot({ color, label }) {
  return (
    <span className="flex items-center gap-1.5">
      <span className="inline-block h-2 w-2 rounded-full" style={{ backgroundColor: color }} />
      {label}
    </span>
  )
}
