"""
Policy class used for managing action selection for a reinforcement
learning agent.
"""

from typing import Type
import random

from ActionProbabilityDistribution import ActionProbabilityDistribution
from Policy.BasePolicy import BasePolicy
from constants import Constants

ACTIONS = Constants.ACTIONS

class EquiprobablePolicy(BasePolicy):
    def __init__(self,
                 number_of_states: int
                ) -> None:
        super().__init__(number_of_states)
        
        action_probability: float = 1/ len(ACTIONS.as_tuple())
        
        for state in range(number_of_states):
            for action in ACTIONS.as_tuple():
                self[state][action] = action_probability
            
    def choose_action(self, state: int) -> ACTIONS:
        """Choose an action based on the Action Probability Distribution."""

        return random.choice(list(self[state].keys()))

    def get_action_probability_distribution(self, state: int) -> ActionProbabilityDistribution:

        return self[state]
