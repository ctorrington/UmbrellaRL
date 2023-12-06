"""
Policy class used for managing action selection for a reinforcement
learning agent.
"""

# TODO This Policy will be provided eventually as a builtin.

import random
from typing import List

from ActionProbabilityDistribution import ActionProbabilityDistribution
from Policy.BasePolicy import BasePolicy
from StateSpace import StateSpace
from StateIndex import StateIndex # type: ignore
from Action import Action

class EquiprobablePolicy[StateIndex, A: Action](BasePolicy[StateIndex, A]):
    def __init__(self,
                 state_space: StateSpace[StateIndex, A]
                ) -> None:
        
        self.state_space: StateSpace[StateIndex, A] = state_space
        
        for state in self.state_space:
            
            # TODO division by zero risk.
            action_probability: float = 1/ len(self.state_space[state].actions)
            
            for action in state_space[state].actions:
                
                self[state][action] = action_probability
            
    def choose_action(self,
                      state: StateIndex
                     ) -> A:
        """Choose an action based on the Action Probability Distribution."""

        actions: List[A] = list(self[state].keys())
        
        return random.choice(actions)

    def get_action_probability_distribution(self,
                                            state: StateIndex
                                           ) -> ActionProbabilityDistribution[A]:

        return self[state]
