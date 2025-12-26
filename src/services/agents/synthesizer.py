from src.services.agents.base import BaseAgent
class SynthesizerAgent(BaseAgent):
    name = "synthesizer"

    def run(self, state):
        product = None
        questions = None
        pages = None

        for block in state.get("completed_blocks", []):
            if "product" in block:
                product = block["product"]
            elif "questions" in block:
                questions = block["questions"]
            elif "pages" in block:
                pages = block["pages"]

        return {
            "product": product,
            "FAQ": questions,          
            "pages": pages
        }
