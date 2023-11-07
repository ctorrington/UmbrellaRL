"""
Policy class used for managing action selection for a reinforcement
learning agent.
"""

import random

from ActionProbabilityDistribution import ActionProbabilityDistribution
from Policy.BasePolicy import BasePolicy
from constants import Constants

ACTIONS = Constants.ACTIONS

class EquiprobablePolicy(BasePolicy):
    def __init__(self, action_probability_distribution: ActionProbabilityDistribution):
        self.action_probability_distribution = action_probability_distribution
        
    def choose_action(self, state: int) -> ACTIONS:
        """Choose an action based on the Action Probability Distribution."""
        
        return random.choice(list(self[state].keys()))
    
    def get_action_probability_distribution(self, state: int) -> ActionProbabilityDistribution:
        
        return self[state]
        