from src.services.tools.base import BaseTool


class UsageTool(BaseTool):
    name = "usage-tool"

    def execute(self, usage: str):
        return [usage]
