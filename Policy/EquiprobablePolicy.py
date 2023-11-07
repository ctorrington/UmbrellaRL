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
                 number_of_states: int,
                 action_probability_class: Type[ActionProbabilityDistribution] = ActionProbabilityDistribution
                 ) -> None:
        
        action_probability_distribution: dict[ACTIONS, float] = {}
        action_probability: float = 1/ len(ACTIONS.as_tuple())
        
        for action in ACTIONS.as_tuple():
            action_probability_distribution[action] = action_probability
            
        for state in range(number_of_states):
            self[state] = action_probability_class(action_probability_distribution)
        
    def choose_action(self, state: int) -> ACTIONS:
        """Choose an action based on the Action Probability Distribution."""
        
        return random.choice(list(self[state].keys()))
    
    def get_action_probability_distribution(self, state: int) -> ActionProbabilityDistribution:
        
        return self[state]
        