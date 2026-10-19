import { useEffect, useRef } from "react";
import cytoscape from "cytoscape";

/**
 * GraphCanvas.jsx
 * ---------------
 * Renderiza a topologia da rede com Cytoscape.js.
 *
 * - Nó de origem / destino recebem estilo distinto.
 * - Em modo de simulação de falha, clicar em um nó ou aresta
 *   alterna seu estado "falho" (chamando onToggleFailedNode /
 *   onToggleFailedEdge).
 * - Os caminhos disjuntos retornados pela análise são desenhados
 *   com "pulsos de sinal" (linha tracejada animada) percorrendo as
 *   arestas de cada rota — a metáfora visual de tráfego sendo
 *   redistribuído entre enlaces de fibra redundantes.
 */

const PATH_COLORS = ["#4FD8C4", "#9B8CFF", "#E8B75E", "#FF9FB2", "#7DD3FC"];

function edgeSelector(a, b) {
  return `edge[source = "${a}"][target = "${b}"], edge[source = "${b}"][target = "${a}"]`;
}

function baseStyle() {
  return [
    {
      selector: "node",
      style: {
        "background-color": "#121820",
        "border-width": 2,
        "border-color": "#3A4B5C",
        label: "data(id)",
        color: "#E8EEF3",
        "font-family": "JetBrains Mono, monospace",
        "font-size": 12,
        "font-weight": 600,
        "text-valign": "center",
        "text-halign": "center",
        width: 42,
        height: 42,
        "transition-property": "background-color, border-color, border-width",
        "transition-duration": 120,
      },
    },
    {
      selector: "node.endpoint-source",
      style: {
        "border-color": "#4FD8C4",
        "border-width": 3,
        "background-color": "#12312C",
      },
    },
    {
      selector: "node.endpoint-sink",
      style: {
        "border-color": "#9B8CFF",
        "border-width": 3,
        "background-color": "#231C3D",
      },
    },
    {
      selector: "node.failed",
      style: {
        "background-color": "#3A1613",
        "border-color": "#FF6B5E",
        "border-style": "dashed",
        opacity: 0.55,
      },
    },
    {
      selector: "edge",
      style: {
        width: 2,
        "line-color": "#2B3948",
        "curve-style": "bezier",
        "target-arrow-shape": "none",
      },
    },
    {
      selector: "edge.failed",
      style: {
        "line-color": "#FF6B5E",
        "line-style": "dashed",
        opacity: 0.5,
      },
    },
    {
      selector: "edge.failable:active",
      style: { "line-color": "#FF6B5E" },
    },
  ];
}

export default function GraphCanvas({
  nodes,
  edges,
  source,
  sink,
  failureMode,
  failedNodes,
  failedEdges,
  highlightPaths,
  onToggleFailedNode,
  onToggleFailedEdge,
}) {
  const containerRef = useRef(null);
  const cyRef = useRef(null);
  const animFrameRef = useRef(null);
  const callbacksRef = useRef({ onToggleFailedNode, onToggleFailedEdge });

  callbacksRef.current = { onToggleFailedNode, onToggleFailedEdge };

  // Inicializa o Cytoscape uma única vez.
  useEffect(() => {
    const cy = cytoscape({
      container: containerRef.current,
      style: baseStyle(),
      layout: { name: "preset" },
      wheelSensitivity: 0.25,
      minZoom: 0.4,
      maxZoom: 2.5,
    });

    cy.on("tap", "node", (evt) => {
      callbacksRef.current.onToggleFailedNode?.(evt.target.id());
    });
    cy.on("tap", "edge", (evt) => {
      const d = evt.target.data();
      callbacksRef.current.onToggleFailedEdge?.(d.source, d.target);
    });

    cyRef.current = cy;
    return () => {
      cy.destroy();
      cyRef.current = null;
    };
  }, []);

  // Sincroniza os elementos (nós/arestas) sempre que a topologia muda.
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy) return;

    const existingIds = new Set(cy.nodes().map((n) => n.id()));
    const nextIds = new Set(nodes.map((n) => n.id));

    // remove nós que não existem mais
    cy.nodes().forEach((n) => {
      if (!nextIds.has(n.id())) n.remove();
    });
    // adiciona novos nós em posição circular determinística
    const angleStep = (2 * Math.PI) / Math.max(nodes.length, 1);
    const radius = 160;
    nodes.forEach((n, i) => {
      if (!existingIds.has(n.id)) {
        cy.add({
          group: "nodes",
          data: { id: n.id },
          position: {
            x: 260 + radius * Math.cos(i * angleStep),
            y: 220 + radius * Math.sin(i * angleStep),
          },
        });
      }
    });

    // sincroniza arestas por (source,target) não-direcionado
    const nextEdgeKeys = new Set(edges.map((e) => [e.source, e.target].sort().join("|")));
    cy.edges().forEach((e) => {
      const key = [e.data("source"), e.data("target")].sort().join("|");
      if (!nextEdgeKeys.has(key)) e.remove();
    });
    const existingEdgeKeys = new Set(
      cy.edges().map((e) => [e.data("source"), e.data("target")].sort().join("|"))
    );
    edges.forEach((e, i) => {
      const key = [e.source, e.target].sort().join("|");
      if (!existingEdgeKeys.has(key)) {
        cy.add({
          group: "edges",
          data: { id: `e-${key}-${i}`, source: e.source, target: e.target },
          classes: "failable",
        });
      }
    });

    if (nodes.length > 0) {
      cy.layout({ name: "cose", animate: false, fit: true, padding: 40 }).run();
    }
  }, [nodes, edges]);

  // Estilo de origem / destino / falhas.
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy) return;

    cy.nodes().removeClass("endpoint-source endpoint-sink failed");
    cy.edges().removeClass("failed");

    if (source) cy.getElementById(source).addClass("endpoint-source");
    if (sink) cy.getElementById(sink).addClass("endpoint-sink");

    failedNodes.forEach((n) => cy.getElementById(n).addClass("failed"));
    failedEdges.forEach(([a, b]) => {
      cy.$(edgeSelector(a, b)).addClass("failed");
    });

    cy.nodes().toggleClass("failable", failureMode);
    cy.edges().toggleClass("failable", failureMode);
  }, [source, sink, failedNodes, failedEdges, failureMode]);

  // Desenha (e anima) os caminhos disjuntos destacados.
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy) return;

    cy.edges().forEach((e) => {
      e.data("flowColor", null);
      e.removeClass("flow");
      e.style({ "line-color": "", "line-style": "solid", width: 2, "z-index": 0 });
    });

    (highlightPaths || []).forEach((path, idx) => {
      const color = PATH_COLORS[idx % PATH_COLORS.length];
      for (let i = 0; i < path.length - 1; i++) {
        const els = cy.$(edgeSelector(path[i], path[i + 1]));
        els.addClass("flow");
        els.data("flowColor", color);
        els.style({
          "line-color": color,
          "line-style": "dashed",
          "line-dash-pattern": [7, 4],
          width: 3.5,
          "z-index": 10,
        });
      }
    });

    if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
    let offset = 0;
    const tick = () => {
      offset -= 1;
      cy.edges(".flow").forEach((e) => e.style("line-dash-offset", offset));
      animFrameRef.current = requestAnimationFrame(tick);
    };
    if ((highlightPaths || []).length > 0) {
      animFrameRef.current = requestAnimationFrame(tick);
    }

    return () => {
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
    };
  }, [highlightPaths]);

  return (
    <div className="relative h-full w-full overflow-hidden rounded-lg border border-line bg-panel2">
      <div
        ref={containerRef}
        className="h-full w-full"
        role="img"
        aria-label="Diagrama interativo da topologia de rede"
      />
      <div className="pointer-events-none absolute bottom-3 left-3 flex gap-3 rounded border border-line-soft bg-panel/80 px-2.5 py-1.5 font-mono text-[10px] uppercase tracking-wide text-mid backdrop-blur">
        <span className="flex items-center gap-1">
          <span className="h-2 w-2 rounded-full border border-signal" /> origem
        </span>
        <span className="flex items-center gap-1">
          <span className="h-2 w-2 rounded-full border border-redundant" /> destino
        </span>
        {failureMode && (
          <span className="flex items-center gap-1 text-alert">
            <span className="h-2 w-2 rounded-full bg-alert" /> clique para marcar falha
          </span>
        )}
      </div>
    </div>
  );
}
