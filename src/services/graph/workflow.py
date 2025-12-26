from typing import List
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send

from src.utils.state import AgentState

from src.services.graph.orchestrator import orchestrator_node, assign_workers
from src.services.agents.parse_product import ParseProductAgent
from src.services.agents.question_generator import QuestionGenerationAgent
from src.services.agents.page_generation import PageGenerationAgent
from src.services.agents.synthesizer import SynthesizerAgent


builder = StateGraph(AgentState)

builder.add_node("orchestrator", orchestrator_node)
builder.add_node("parse_product_worker", ParseProductAgent())
builder.add_node("question_gen_worker", QuestionGenerationAgent())
builder.add_node("page_gen_worker", PageGenerationAgent())
builder.add_node("synthesizer", SynthesizerAgent())

# Kick off orchestrator
builder.add_edge(START, "orchestrator")

# Orchestrator sends workers
builder.add_conditional_edges(
    "orchestrator",
    assign_workers,
    ["parse_product_worker", "question_gen_worker", "page_gen_worker"],
)

# After workers complete, go to synthesizer
builder.add_edge("parse_product_worker", "synthesizer")
builder.add_edge("question_gen_worker", "synthesizer")
builder.add_edge("page_gen_worker", "synthesizer")

builder.add_edge("synthesizer", END)

app = builder.compile()

