"""
Class for representing the action probability distribution for reinforcement
learning agents.
"""

from abc import ABC

from Action import Action

class ActionProbabilityDistribution(ABC, dict[Action, float]):
    """
    Class for representing the action probability distribution for a State.
    
    Intended to be used within the Policy class to map each state to an Action 
    with a probability.
    """
    
    def __init__(self,
                 action_probability_distribution: dict[Action, float]
                ):
        self = action_probability_distribution
        