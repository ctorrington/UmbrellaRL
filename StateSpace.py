"""
State Space Type.

Structure containing every State in the Environment that can be interacted with 
by a reinforcement learning Agent.
"""

from typing import Dict

from State import State
# I don't think that this is a problem.
# But is also potentially a problem if the generic type isn't being used.
from StateIndex import StateIndex

class StateSpace[StateIndex](Dict[StateIndex, State]):
    """
    Structure containing every State in the Environment that can be interacted 
    with by a reinforcement learning Agent.
    
    Dictionary structure mapping each index to its State.
    
    Injected into Environment.
    """

    def __getattr__(self, key: StateIndex):
        if key in self:
            return self[key]
        else:
            raise AttributeError(f"'StateSpace' object has not attribute '{key}'")
 