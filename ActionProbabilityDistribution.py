"""
Action Probability Distribution type.

Mapping from Actions available to a State to the percentage chance they are 
chosen by the Policy.
"""

from abc import ABC

from Action import Action

class ActionProbabilityDistribution[A: Action](ABC, dict[A, float]):
    def __getitem__(self,
                    key: A
                   ) -> float:
        return self[key]
    
    def get_action_probability(self,
                               action: A
                              ) -> float:
        """Return the probability of the given action being chosen."""
        
        return self[action]
