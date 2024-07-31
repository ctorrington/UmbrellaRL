"""
State Probability Distribution type.

Mapping from States potentially resulting from an Action to the percentage 
chance of the State occuring, according to the Environment.
"""

from typing import Dict

from core.dependency.state_index import StateIndex

class StateProbabilityDistribution[SI: StateIndex](Dict[SI, float]):
    """Probability that a State is achieved.
    Dictionary mapping State Index type to float.

    State Probability Distribution is a distribution of States following an 
    Action from a State within the Environment.
    """

    def get_state_probability(
        self,
        state_index: SI
    ) -> float:
        """Return the probability of reaching the given State."""
        return self[state_index]
