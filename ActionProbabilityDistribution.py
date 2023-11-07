"""
Class for representing the action probability distribution for reinforcement
learning agents.
"""

from Action import Action

class ActionProbabilityDistribution(dict[Action, float]):
    """
    Class for representing the action probability distribution of each state.
    
    Intended to be used within the Policy class.
    """
    
    def __init__(self,
                 action_probability_distribution: dict[Action, float]
                ):
        self = action_probability_distribution
        