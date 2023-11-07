"""
Policy class used for managing action selection for a reinforcement
learning agent.
"""

import random

from ActionProbabilityDistribution import ActionProbabilityDistribution
from Policy.BasePolicy import BasePolicy
from constants import Constants
from StateSpace import StateSpace

ACTIONS = Constants.ACTIONS

class EquiprobablePolicy(BasePolicy):
    def __init__(self,
                 state_space: StateSpace
                ) -> None:
        super().__init__(state_space)
        
        action_probability: float = 1/ len(ACTIONS.as_tuple())
        
        for state in state_space:
            for action in state_space[state].actions:
                self[state][action] = action_probability
            
    def choose_action(self, state: int) -> ACTIONS:
        """Choose an action based on the Action Probability Distribution."""

        return random.choice(list(self[state].keys()))

    def get_action_probability_distribution(self, state: int) -> ActionProbabilityDistribution:

        return self[state]
