"""
State Space Type.

Structure containing every State in the Environment that can be interacted with 
by a reinforcement learning Agent.
"""

from typing import Dict, Tuple, cast
from abc import ABC

import numpy as np
import numpy.typing as npt
from numpy import float64

from core.dependency.State import State
from core.dependency.StateIndex import StateIndex
from core.dependency.Action import Action

class StateSpace[SI: StateIndex, A: Action](ABC, Dict[SI, State[A]]):
    """
    Structure containing every State in the Environment that can be interacted 
    with by a reinforcement learning Agent.
    
    Dictionary structure mapping each index to its State.
    """
    def __init__(
        self,
        state_actions: list[A],
        state_estimated_return: float,
        state_reward: float
    ) -> None:
        self.state_actions: list[A] = state_actions
        self.state_estimated_return: float = state_estimated_return
        self.state_reward: float = state_reward

    def get_state(
        self,
        state: SI
    ) -> State[A]:
        """Return the State object of the given State Index."""
        return self[state]

    def get_dimensionality(self) -> int:
        """Return the dimensionality of the State Space."""
        
        first_index_key = next(iter(self.keys()))
        
        if isinstance(first_index_key, tuple):
            # Queting the type checker.
            return len(cast(Tuple[int, ...], first_index_key))
        else:
            raise TypeError("Type for State Index not currently supported.")
    
    def get_state_value_function(self) -> npt.NDArray[float64]:
        
        dimensionality: int = self.get_dimensionality()
        
        if dimensionality == 2:
            x, y = zip(*self.keys())
            values = np.zeros((max(x) + 1, max(y) + 1))
            for state_index, state in self.items():
                
                if isinstance(state_index, tuple):
                    # Quieting the type checker.
                    i, j = cast(Tuple[int, ...], state_index)
                    values[i, j] = state.estimated_return
                else:
                    raise TypeError("Type for State Index not currently supported.")

            return values
        else:
            raise ValueError("Dimensionality currently unsupported.")
