"""
State Space Type.

Structure containing every State in the Environment that can be interacted with 
by a reinforcement learning Agent.
"""

from typing import Dict, Tuple, cast
from abc import ABC
from logging import Logger

import numpy as np
import numpy.typing as npt
from numpy import float64

from core.dependency.state import State
from core.dependency.state_index import StateIndex
from core.dependency.action import Action
from log.ilogger import ILogger

class StateSpace[SI: StateIndex, A: Action](ABC, Dict[SI, State[A]]):
    """
    Structure containing every State in the Environment that can be interacted 
    with by a reinforcement learning Agent.
    
    Dictionary structure mapping each State Index to its State object.
    """
    def __init__(
        self,
        logger: ILogger
    ) -> None:
        self._logger: Logger = logger.get_logger(self.__class__.__name__)
        self._logger.info(f"Initialised {self.__class__.__name__}.")

    def get_state(
        self,
        state: SI
    ) -> State[A]:
        """Return the State object of the given State Index."""
        return self[state]

    def set_state_for_state_index(
        self,
        state_index: SI,
        state: State[A]
    ) -> None:
        """Set the State for the State Index within the State Space.

        Args:
            state_index (SI): State Index for the State.
            state (State[A]): State object of the State within the State Space.
        """
        self[state_index] = state

    def get_dimensionality(self) -> int:
        """Return the dimensionality of the State Space."""
        
        first_index_key = next(iter(self.keys()))
        
        if isinstance(first_index_key, tuple):
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
                    i, j = cast(Tuple[int, ...], state_index)
                    values[i, j] = state.estimated_return
                else:
                    raise TypeError("Type for State Index not currently supported.")

            return values
        else:
            raise ValueError("Dimensionality currently unsupported.")
