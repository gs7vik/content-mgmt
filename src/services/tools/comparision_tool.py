from src.services.tools.base import BaseTool


class ComparisonTool(BaseTool):
    name = "comparison-tool"

    def execute(self, product_a, product_b):
        return {
            "comparison": {
                product_a["name"]: {
                    "ingredients": product_a["ingredients"],
                    "benefits": product_a["benefits"],
                    "price": product_a["price"]
                },
                product_b["name"]: {
                    "ingredients": product_b["ingredients"],
                    "benefits": product_b["benefits"],
                    "price": product_b["price"]
                }
            }
        }
