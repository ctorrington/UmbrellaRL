"""
Action Probability Distribution type.

Mapping from Actions available to a State to the percentage chance they are 
chosen by the Policy.
"""

from typing import Dict

from src.Action import Action

class ActionProbabilityDistribution[A: Action](Dict[A, float]):

    def get_action_probability(
        self,
        action: A
    ) -> float:

        """Return the probability of the given Action being chosen."""

        return self[action]
    
    def set_action_probability(
        self,
        action: A,
        action_probability: float
    ) -> None:
        
        """Set the probability of the Action being chosen."""
        
        self[action] = action_probability
