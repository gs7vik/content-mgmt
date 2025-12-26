from src.services.agents.base import BaseAgent


class QuestionGenerationAgent(BaseAgent):
    name = "question-generation-agent"

    def run(self, state):
        product = state["product"]

        questions = {
            "informational": [
                f"What is {product['name']}?",
                "What does this serum do?",
                "What is the Vitamin C concentration?"
            ],
            "usage": [
                "How should I apply this serum?",
                "When should I use this product?",
                "Should it be used before sunscreen?"
            ],
            "safety": [
                "Are there any side effects?",
                "Is mild tingling normal?",
                "Is it suitable for sensitive skin?"
            ],
            "purchase": [
                "What is the price of this product?",
                "Is this serum good for oily skin?"
            ],
            "comparison": [
                "How does this compare with other Vitamin C serums?"
            ]
        }

        return {"questions": questions}
