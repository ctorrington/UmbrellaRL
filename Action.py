"""
Action Type.

Actions that can be implemented by a reinforcement learning agent.
"""

from enum import Enum
from typing import List, Type, TypeVar

# TODO the generics here need to be update to 3.12.
T = TypeVar('T', bound = Enum)

class Action(Enum):
    """
    Generic Action class.
    
    Inherit from this class to define actions that can be taken by the agent.
    Actions should be enum member fields of the class.
    """
    
    @classmethod
    def members(cls: Type[T]) -> List[T]:
        """Return all actions available."""
        
        return list(cls.__members__.values())
