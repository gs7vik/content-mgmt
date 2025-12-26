# services/agents/worker.py
from src.services.agents.base import BaseAgent

class WorkerAgent(BaseAgent):
    name = "worker"

    def run(self, state):
        task = state["task"]["type"]
        raw = state["raw_product_data"]

        if task == "parse_product":
            result = {"product": raw["Product Name"]}

        elif task == "generate_questions":
            result = {"questions": ["Q1", "Q2"]}

        elif task == "generate_pages":
            result = {"pages": {"product_page": "..."}}

        return {
            "completed_blocks": [result]
        }
