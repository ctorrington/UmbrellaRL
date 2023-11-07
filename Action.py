"""
Action Type.

Actions that can be implemented by a reinforcement learning agent.
"""

from enum import Enum

class Action(Enum):
    left = "left"
    right = "right"
    
    @classmethod
    def members(cls) -> list[str]:
        """Return all actions available."""
        
        return list(cls.__members__)
