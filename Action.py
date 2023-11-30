"""
Action Type.

Actions that can be implemented by a reinforcement learning agent.
"""

from enum import Enum
from typing import List, Type

class Action(Enum):
    """
    Generic Action class.
    
    Inherit from this class to define actions that can be taken by the agent.
    Actions should be enum member fields of the class.
    
    Generic type for each action available to the Agent.
    
    Injected into State.
    """
    
    @classmethod
    def members(cls: Type['Action']) -> List['Action']:
        """Return all actions available."""
        
        return list(cls.__members__.values())
