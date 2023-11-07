"""
Class for representing the action probability distribution for reinforcement
learning agents.
"""

from constants import Constants

ACTIONS = Constants.ACTIONS

class ActionProbabilityDistribution(dict[ACTIONS, float]):
    """
    Class for representing the action probability distribution of each state.
    
    Intended to be used within the Policy class.
    """
    
    def __init__(self,
                 action_probability_distribution: dict[ACTIONS, float]
                ):
        self = action_probability_distribution
        