"""
State Probability Distribution type.

Mapping from States potentially resulting from an Action to the percentage 
chance of the State occuring, according to the Environment.

Used by the Environment.
"""

from abc import ABC
from typing import Dict

from StateIndex import StateIndex # type: ignore

class StateProbabilityDistribution[StateIndex](ABC, Dict[StateIndex, float]):
    def __getitem__(self,
                    key: StateIndex
                   ) -> float:
        return self[key]
    
    def __setitem__(self,
                    key: StateIndex,
                    value: float
                   ) -> None:
        self[key] = value
        
    def get_state_probability(self,
                              state: StateIndex
                             ) -> float:
        """Return the probability of reaching the given State."""
        
        return self[state]
