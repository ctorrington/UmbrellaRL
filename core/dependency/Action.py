"""
Action Type.

Actions that can be implemented by a reinforcement learning agent.
"""

from enum import Enum
from typing import List, Self

class Action(Enum):
    """
    Inherit from this class to define actions that can be taken by the agent.
    Actions should be enum member fields of the class.

    Generic type for each action available to the Agent.
    """

    @classmethod
    def members(cls) -> List[Self]:
        """Return all actions available."""

        return list(cls.__members__.values())
