"""
Class for representing the action probability distribution for reinforcement
learning agents.
"""

from constants import Constants
from StateSpace import StateSpace

ACTIONS = Constants.ACTIONS

class ActionProbabilityDistribution(dict[int, dict[ACTIONS, float]]):
    """
    Class for representing the action probability distribution for reinforcement
    learning agents.
    """
    
    def __init__(self, state_space: StateSpace) -> None:
        """Action probability is initialised to equiprobable."""
        
        for state in state_space:
            self[state] = {action: 1/ len(ACTIONS.as_tuple()) for action in ACTIONS.as_tuple()}


class ActionProbabilityDistribution2(dict[ACTIONS, float]):
    """
    Class for representing the action probability distribution of each state.
    
    Intended to be used within the Policy class.
    """
    
    def __init__(self):
        for action in ACTIONS.as_tuple():
            self[action] = 1/ len(ACTIONS.as_tuple())
    