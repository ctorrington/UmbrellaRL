"""
State Space Type.

Structure containing every State in the Environment that can be interacted with 
by a reinforcement learning Agent.
"""

from typing import Dict, Tuple, Any, cast
from abc import ABC, abstractmethod

import numpy as np
import numpy.typing as npt
from numpy import float64

from src.State import State
from src.StateIndex import StateIndex
from src.Action import Action

class StateSpace[SI: StateIndex, A: Action](ABC, Dict[SI, State[A]]):
    """
    Structure containing every State in the Environment that can be interacted 
    with by a reinforcement learning Agent.
    
    Dictionary structure mapping each index to its State.
    """

    def get_reward(
        self,
        key: SI
        ) -> float:
        """Return the reward of the given State."""
        
        return self[key].reward
    
    def get_estimated_return(
        self,
        key: SI
        ) -> float:
        """Return the estimated return (value) of the given State."""
        
        return self[key].estimated_return
    
    def get_dimensionality(
        self
        ) -> int:
        """Return the dimensionality of the State Space."""
        
        first_index_key = next(iter(self.keys()))
        
        if isinstance(first_index_key, tuple):
            
            # Queting the type checker.
            return len(cast(Tuple[int, ...], first_index_key))
        
        else:
            
            raise TypeError("Type for State Index not currently supported.")
    
    def get_state_value_function(
        self
        ) -> npt.NDArray[float64]:
        
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

    # TODO Any type here, & any reference to StateIndex, needs to change to be bound to a type (similar to Action).
    @abstractmethod
    def get_dimensions(self) -> Tuple[Any, ...]:
        """Return the dimensions of the State Space."""

        pass
