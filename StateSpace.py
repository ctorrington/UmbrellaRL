"""
State Space Type.

Structure for every State in the Environment that can be interacted with by a 
reinforcement learning Agent.
"""

from typing import Dict

from State import State

class StateSpace[T](Dict[T, State]):
    """
    Collection of every State in the Environment that can be interacted with by
    a reinforcement learning Agent.
    
    Dictionary structure mapping each index to its State.
    
    Injected into Environment.
    """

    def __getattr__(self, key: int):
        if key in self:
            return self[key]
        else:
            raise AttributeError(f"'StateSpace' object has not attribute '{key}'")
 