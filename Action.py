"""
Action Type.

Actions that can be implemented by a reinforcement learning agent.
"""

from enum import Enum
from typing import List, TypeVar

T = TypeVar('T', bound = 'Action')

class Action(Enum):
    """Generic Action class."""
    pass
    
    @classmethod
    def members(cls: T) -> List[T]:
        """Return all actions available."""
        
        return list(cls)
