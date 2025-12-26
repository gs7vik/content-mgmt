from src.services.agents.base import BaseAgent
from src.services.tools.benefits_tool import BenefitsTool
from src.services.tools.usage_tool import UsageTool
from src.services.tools.comparision_tool import ComparisonTool


class PageGenerationAgent(BaseAgent):
    name = "page-generation-agent"

    def __init__(self):
        self.benefits_tool = BenefitsTool()
        self.usage_tool = UsageTool()
        self.comparison_tool = ComparisonTool()

    def run(self, state):
        product = state["product"]

        fictional_product = {
            "name": "RadiantFix Vitamin C Serum",
            "ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": ["Brightening", "Oil control"],
            "price": 899
        }

        faq_page = {
            "page": "FAQ",
            "items": [
                {
                    "question": "Is this suitable for oily skin?",
                    "answer": "Yes, it is designed for oily and combination skin types."
                },
                {
                    "question": "Are there side effects?",
                    "answer": "Some users may experience mild tingling."
                },
                {
                    "question": "When should I apply it?",
                    "answer": "Apply in the morning before sunscreen."
                },
                {
                    "question": "What are the main benefits?",
                    "answer": ", ".join(product["benefits"])
                },
                {
                    "question": "What is the price?",
                    "answer": f"₹{product['price']}"
                }
            ]
        }

        product_page = {
            "product_name": product["name"],
            "ingredients": product["ingredients"],
            "benefits": self.benefits_tool(product["benefits"]),
            "usage": self.usage_tool(product["usage"]),
            "price": product["price"]
        }

        comparison_page = self.comparison_tool(product, fictional_product)

        return {
            "faq_page": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page
        }
