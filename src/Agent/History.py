"""
Agent History Class.

Currently trackable metrics:
    - Actions
"""

from typing import Dict, List
from copy import deepcopy
from numpy import float64

import numpy.typing as npt

from src.Action import Action

class History[A: Action](Dict[int, Dict[str, List[A] | npt.NDArray[float64]]]):
    """
    Agent History class for recording the history of the Environment & 
    State Value Function during Action interactions.
    """
    
    def __init__(self) -> None:
        
        self.count = 0
        
        self[0] = {}
        
    def track_actions(
        self,
        actions: List[A]
    ) -> None:
        """Record the given Actions."""
        
        self[self.count]["actions"] = deepcopy(actions)
        
    def track_state_value_function(
        self,
        state_value_function: npt.NDArray[float64]
    ) -> None:
        """Record the given State Value Function."""
        
        self[self.count]["state value function"] = deepcopy(state_value_function)
