# src/services/agents/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):
    """
    Base class for all agents.
    Each agent:
    - reads from shared state
    - returns a partial state update
    """

    name: str = "base-agent"

    @abstractmethod
    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute agent logic.

        Args:
            state: Current LangGraph state

        Returns:
            Partial state update
        """
        pass

    def __call__(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Makes agent compatible with LangGraph nodes.
        """
        return self.run(state)
