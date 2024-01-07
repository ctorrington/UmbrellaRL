"""
State Probability Distribution type.

Mapping from States potentially resulting from an Action to the percentage 
chance of the State occuring, according to the Environment.
"""

from typing import Dict

from src.StateIndex import StateIndex

class StateProbabilityDistribution[SI: StateIndex](Dict[SI, float]):

    def get_state_probability(
        self,
        state_index: SI
        ) -> float:
        """Return the probability of reaching the given State."""

        return self[state_index]
