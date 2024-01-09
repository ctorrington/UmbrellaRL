"""
Agent History Class.

Currently trackable metrics:
    - Actions
"""

from typing import Dict
from copy import deepcopy

from core.Action import Action
from core.StateSpace import StateSpace
from core.StateIndex import StateIndex

# TODO Allow for tracking the policy actions as well.
# TODO Class currently tracks the entire State Space.
    # Should make it more modular.

class History[SI: StateIndex, A: Action](Dict[int, StateSpace[SI, A]]):
    """
    Agent History class for recording the history of the Environment & 
    State Value Function during Action interactions.
    """
    
    def __init__(self) -> None:
        
        self.history_count = 0
        
    def track_state_space(
        self,
        state_space: StateSpace[SI, A]
    ) -> None:
        """Record the given State Space."""
        
        self[self.history_count] = deepcopy(state_space)
        
    def increment_history_count(self) -> None:
        """Increment the history count."""
        
        self.history_count += 1
