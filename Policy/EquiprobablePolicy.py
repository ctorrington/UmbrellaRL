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
        
    def choose_action(self, state: int,
                      action_probability_distribution: ActionProbabilityDistribution) -> ACTIONS:
        """Choose an action based on the Action Probability Distribution."""
        
        state_distribution: dict[ACTIONS, float] = self.action_probability_distribution[state]
        
        action_chosen: ACTIONS = random.choice(list(state_distribution.keys()))
        
        return action_chosen
        