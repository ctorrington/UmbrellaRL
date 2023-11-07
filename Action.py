"""
Action Type.

Actions that can be implemented by a reinforcement learning agent.
"""

from enum import Enum
from typing import Type, TypeVar

T = TypeVar("T", bound = Enum)

class Action(Enum):
    """Generic Action class."""
    pass
    
    @classmethod
    def members(cls: Type[T]) -> list[str]:
        """Return all actions available."""
        
        return list(cls.__members__)
