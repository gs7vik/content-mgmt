from src.services.tools.base import BaseTool
from typing import List


class BenefitsTool(BaseTool):
    name = "benefits-tool"

    def execute(self, benefits: List[str]) -> List[str]:
        return benefits
