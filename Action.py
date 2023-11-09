"""
Action Type.

Actions that can be implemented by a reinforcement learning agent.
"""

from enum import Enum
from typing import List

class Action(Enum):
    """Generic Action class."""
    pass
    
    @classmethod
    def members(cls) -> List['Action']:
        """Return all actions available."""
        
        return list(cls)
