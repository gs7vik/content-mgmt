from src.services.graph.workflow import app
from src.utils.input_product import PRODUCT_DATA


initial_state = {
    "raw_product_data": PRODUCT_DATA,
    "product": None,
    "questions": None,
    "faq_page": None,
    "product_page": None,
    "comparison_page": None
}

result = app.invoke(initial_state)
# print("\nFINAL STATE\n", result)

print(result)
print("\nFAQ PAGE\n", result["faq_page"])
print("\nPRODUCT PAGE\n", result["product_page"])
print("\nCOMPARISON PAGE\n", result["comparison_page"])
