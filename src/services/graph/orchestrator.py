# services/graph/orchestrator.py
from src.utils.state import AgentState
def orchestrator_node(state: AgentState):
    """
    Decide WHAT needs to be generated.
    This is the planner.
    """
    plan = [
        {"type": "parse_product"},
        {"type": "generate_questions"},
        {"type": "generate_pages"}
    ]
    return {"plan": plan}

from langgraph.types import Send

def assign_workers(state: AgentState):
    sends = []
    for task in state.get("plan", []):
        sends.append(
            Send(
                "worker",
                {"task": task, "raw_product_data": state["raw_product_data"]}
            )
        )
    return sends