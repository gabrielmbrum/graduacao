import { useMemo, useState } from "react";
import GraphCanvas from "./components/GraphCanvas.jsx";
import ControlPanel from "./components/ControlPanel.jsx";
import PathViewer from "./components/PathViewer.jsx";
import MetricsCard from "./components/MetricsCard.jsx";
import { analyzeGraph, simulateFailure } from "./services/api.js";

const SAMPLE_GRAPH = {
  nodes: ["DC", "R1", "R2", "R3", "BR"],
  edges: [
    { source: "DC", target: "R1" },
    { source: "R1", target: "BR" },
    { source: "DC", target: "R2" },
    { source: "R2", target: "BR" },
    { source: "DC", target: "R3" },
    { source: "R3", target: "R1" },
  ],
};

export default function App() {
  const [nodeIds, setNodeIds] = useState(SAMPLE_GRAPH.nodes);
  const [edges, setEdges] = useState(SAMPLE_GRAPH.edges);

  const [newNodeId, setNewNodeId] = useState("");
  const [edgeFrom, setEdgeFrom] = useState("");
  const [edgeTo, setEdgeTo] = useState("");

  const [source, setSource] = useState("DC");
  const [sink, setSink] = useState("BR");

  const [analysis, setAnalysis] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);

  const [failureMode, setFailureMode] = useState(false);
  const [failedNodes, setFailedNodes] = useState(new Set());
  const [failedEdges, setFailedEdges] = useState([]); // [[a,b], ...]
  const [simulation, setSimulation] = useState(null);
  const [simulating, setSimulating] = useState(false);

  const [activeTab, setActiveTab] = useState("edge");
  const [errorMessage, setErrorMessage] = useState("");

  const nodes = useMemo(() => nodeIds.map((id) => ({ id })), [nodeIds]);

  const currentGraph = useMemo(
    () => ({ nodes: nodeIds, edges, directed: false }),
    [nodeIds, edges]
  );

  const highlightPaths = simulation
    ? activeTab === "edge"
      ? simulation.edge_disjoint_paths
      : simulation.vertex_disjoint_paths
    : analysis
    ? activeTab === "edge"
      ? analysis.edge_disjoint_paths
      : analysis.vertex_disjoint_paths
    : [];

  function handleAddNode() {
    const id = newNodeId.trim();
    if (!id) return;
    if (nodeIds.includes(id)) {
      setErrorMessage(`o nó "${id}" já existe.`);
      return;
    }
    setNodeIds((prev) => [...prev, id]);
    setNewNodeId("");
    setErrorMessage("");
  }

  function handleAddEdge() {
    if (!edgeFrom || !edgeTo || edgeFrom === edgeTo) {
      setErrorMessage("selecione dois nós distintos para o enlace.");
      return;
    }
    const exists = edges.some(
      (e) =>
        (e.source === edgeFrom && e.target === edgeTo) ||
        (e.source === edgeTo && e.target === edgeFrom)
    );
    if (exists) {
      setErrorMessage("esse enlace já existe.");
      return;
    }
    setEdges((prev) => [...prev, { source: edgeFrom, target: edgeTo }]);
    setEdgeFrom("");
    setEdgeTo("");
    setErrorMessage("");
  }

  function handleRemoveEdge(index) {
    setEdges((prev) => prev.filter((_, i) => i !== index));
  }

  function handleLoadSample() {
    setNodeIds(SAMPLE_GRAPH.nodes);
    setEdges(SAMPLE_GRAPH.edges);
    setSource("DC");
    setSink("BR");
    resetAnalysisState();
  }

  function resetAnalysisState() {
    setAnalysis(null);
    setSimulation(null);
    setFailedNodes(new Set());
    setFailedEdges([]);
    setFailureMode(false);
    setErrorMessage("");
  }

  async function handleAnalyze() {
    setAnalyzing(true);
    setErrorMessage("");
    setSimulation(null);
    try {
      const result = await analyzeGraph(currentGraph, source, sink);
      setAnalysis(result);
    } catch (err) {
      setErrorMessage(err.message);
      setAnalysis(null);
    } finally {
      setAnalyzing(false);
    }
  }

  function handleToggleFailedNode(nodeId) {
    if (!failureMode) return;
    setFailedNodes((prev) => {
      const next = new Set(prev);
      next.has(nodeId) ? next.delete(nodeId) : next.add(nodeId);
      return next;
    });
  }

  function handleToggleFailedEdge(a, b) {
    if (!failureMode) return;
    setFailedEdges((prev) => {
      const exists = prev.some(([x, y]) => (x === a && y === b) || (x === b && y === a));
      if (exists) {
        return prev.filter(([x, y]) => !((x === a && y === b) || (x === b && y === a)));
      }
      return [...prev, [a, b]];
    });
  }

  async function handleSimulateFailure() {
    setSimulating(true);
    setErrorMessage("");
    try {
      const result = await simulateFailure(
        currentGraph,
        source,
        sink,
        Array.from(failedNodes),
        failedEdges.map(([s, t]) => ({ source: s, target: t }))
      );
      setSimulation(result);
    } catch (err) {
      setErrorMessage(err.message);
      setSimulation(null);
    } finally {
      setSimulating(false);
    }
  }

  function handleResetFailures() {
    setFailedNodes(new Set());
    setFailedEdges([]);
    setSimulation(null);
  }

  const failedCount = failedNodes.size + failedEdges.length;
  const linkStatus = simulation
    ? simulation.connected
      ? `${activeTab === "edge" ? simulation.edge_connectivity : simulation.vertex_connectivity} ROTA(S) SOBREVIVENTE(S)`
      : "REDE DESCONECTADA"
    : analysis
    ? `${activeTab === "edge" ? analysis.edge_connectivity : analysis.vertex_connectivity} ROTA(S) DISJUNTA(S)`
    : "AGUARDANDO ANÁLISE";

  return (
    <div className="flex h-screen flex-col gap-3 bg-ink p-3 text-hi">
      <header className="flex items-center justify-between rounded-lg border border-line bg-panel px-4 py-2.5 shadow-panel">
        <div className="flex items-baseline gap-2">
          <h1 className="font-mono text-sm font-semibold tracking-tight text-hi">
            MENGER<span className="text-signal">//</span>
          </h1>
          <span className="font-mono text-[11px] text-dim">
            console de roteamento multi-caminho
          </span>
        </div>
        <div className="flex items-center gap-2 font-mono text-[11px] uppercase tracking-wide text-mid">
          <span
            className={`h-2 w-2 rounded-full ${
              simulation && !simulation.connected
                ? "bg-alert animate-blink"
                : analysis || simulation
                ? "bg-signal"
                : "bg-dim"
            }`}
          />
          {linkStatus}
        </div>
      </header>

      <div className="grid min-h-0 flex-1 grid-cols-[1fr_300px] gap-3">
        <GraphCanvas
          nodes={nodes}
          edges={edges}
          source={source}
          sink={sink}
          failureMode={failureMode}
          failedNodes={failedNodes}
          failedEdges={failedEdges}
          highlightPaths={highlightPaths}
          onToggleFailedNode={handleToggleFailedNode}
          onToggleFailedEdge={handleToggleFailedEdge}
        />

        <ControlPanel
          nodes={nodes}
          edges={edges}
          newNodeId={newNodeId}
          onNewNodeIdChange={setNewNodeId}
          onAddNode={handleAddNode}
          edgeFrom={edgeFrom}
          edgeTo={edgeTo}
          onEdgeFromChange={setEdgeFrom}
          onEdgeToChange={setEdgeTo}
          onAddEdge={handleAddEdge}
          onRemoveEdge={handleRemoveEdge}
          source={source}
          sink={sink}
          onSourceChange={setSource}
          onSinkChange={setSink}
          onAnalyze={handleAnalyze}
          analyzing={analyzing}
          failureMode={failureMode}
          onToggleFailureMode={() => setFailureMode((v) => !v)}
          failedCount={failedCount}
          onSimulateFailure={handleSimulateFailure}
          simulating={simulating}
          onResetFailures={handleResetFailures}
          onLoadSample={handleLoadSample}
          errorMessage={errorMessage}
        />
      </div>

      <div className="grid h-64 grid-cols-[1fr_300px] gap-3">
        <PathViewer
          activeTab={activeTab}
          onTabChange={setActiveTab}
          edgePaths={(simulation || analysis)?.edge_disjoint_paths || []}
          vertexPaths={(simulation || analysis)?.vertex_disjoint_paths || []}
          connected={simulation ? simulation.connected : null}
        />
        <MetricsCard metrics={analysis} simulation={simulation} />
      </div>
    </div>
  );
}
