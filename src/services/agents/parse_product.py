from src.services.agents.base import BaseAgent


class ParseProductAgent(BaseAgent):
    name = "parse-product-agent"

    def run(self, state):
        raw = state["raw_product_data"]

        product = {
            "name": raw["Product Name"],
            "concentration": raw["Concentration"],
            "skin_type": raw["Skin Type"].split(", "),
            "ingredients": raw["Key Ingredients"].split(", "),
            "benefits": raw["Benefits"].split(", "),
            "usage": raw["How to Use"],
            "side_effects": raw["Side Effects"].split(", "),
            "price": raw["Price"],
        }

        return {"product": product}
