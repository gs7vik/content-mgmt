
from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for all tools.
    Tools are stateless, reusable logic blocks.
    """

    name: str = "base-tool"

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass

    def __call__(self, *args, **kwargs) -> Any:
        return self.execute(*args, **kwargs)
