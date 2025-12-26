from langgraph.graph import StateGraph, START, END
from utils.state import AgentState

from src.services.graph.orchestrator import orchestrator_node, assign_workers
from src.services.agents.worker import WorkerAgent
from src.services.agents.synthesizer import SynthesizerAgent

builder = StateGraph(AgentState)

builder.add_node("orchestrator", orchestrator_node)
builder.add_node("worker", WorkerAgent())
builder.add_node("synthesizer", SynthesizerAgent())

builder.add_edge(START, "orchestrator")

builder.add_conditional_edges(
    "orchestrator",
    assign_workers,
    ["worker"],
)

builder.add_edge("worker", "synthesizer")
builder.add_edge("synthesizer", END)

app = builder.compile()
