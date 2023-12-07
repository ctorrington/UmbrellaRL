"""
State Probability Distribution type.

Mapping from States potentially resulting from an Action to the percentage 
chance of the State occuring, according to the Environment.

Used by the Environment.
"""

from typing import Dict

from src.StateIndex import StateIndex # type: ignore

class StateProbabilityDistribution[StateIndex](Dict[StateIndex, float]):
    def __getitem__(self,
                    key: StateIndex
                   ) -> float:
        return self[key]
    
    def get_state_probability(self,
                              state: StateIndex
                             ) -> float:
        """Return the probability of reaching the given State."""
        
        return self[state]
