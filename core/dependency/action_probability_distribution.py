"""
Action Probability Distribution type.

Mapping from Actions available to a State to the percentage chance they are 
chosen by the Policy.
"""

from typing import Dict

from core.dependency.action import Action

class ActionProbabilityDistribution[A: Action](Dict[A, float]):
    """Probability that an Action is chosen.
    
    Action Probability Distributions are stored by a Policy to determine an 
    Agents Actions.
    """

    def get_action_probability(
        self,
        action: A
    ) -> float:
        """Return the probability of the given Action being chosen."""
        try:
            return self[action]
        except KeyError as e:
            raise e
    
    def set_action_probability(
        self,
        action: A,
        action_probability: float
    ) -> None:
        
        """Set the probability of the Action being chosen."""
        
        self[action] = action_probability
