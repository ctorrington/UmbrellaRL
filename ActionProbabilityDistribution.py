"""
Action Probability Distribution type.

Mapping from Actions available to a State to the percentage chance they are 
chosen by the Policy.
"""

from abc import ABC

from Action import Action

class ActionProbabilityDistribution(ABC, dict[Action, float]):
    pass        
        