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
    
    def __init__(self):
        for action in ACTIONS.as_tuple():
            self[action] = 1/ len(ACTIONS.as_tuple())
            