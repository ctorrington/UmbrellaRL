"""
Policy class used for managing action selection for a reinforcement
learning agent.
"""

import random

from ActionProbabilityDistribution import ActionProbabilityDistribution
from constants import Constants

ACTIONS = Constants.ACTIONS

class Policy:
    def __init__(self, action_probability_distribution: ActionProbabilityDistribution):
        self.action_probability_distribution = action_probability_distribution
        
    def choose_action(self, state: int) -> ACTIONS:
        """Choose an action based on the Action Probability Distribution."""
        
        state_distribution: dict[ACTIONS, float] = self.action_probability_distribution[state]
        
        action_chosen: ACTIONS = random.choice(list(state_distribution.keys()))
        
        return action_chosen
        