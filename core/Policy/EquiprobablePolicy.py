"""
Policy class used for managing action selection for a reinforcement
learning agent.
"""

# TODO This Policy will be provided eventually as a builtin.

import random
from typing import List

from core.ActionProbabilityDistribution import ActionProbabilityDistribution
from core.Policy.BasePolicy import BasePolicy
from core.StateSpace import StateSpace
from core.StateIndex import StateIndex
from core.Action import Action

class EquiprobablePolicy[SI: StateIndex, A: Action](BasePolicy[SI, A]):
    def __init__(
        self,
        state_space: StateSpace[SI, A]
    ) -> None:
        
        self.state_space: StateSpace[SI, A] = state_space
        
        for state in self.state_space:
            
            # TODO Below needed for assigning action probability in next loop.
                # Figure out how to assign a type here. figure out default dic
            self[state] = {}
            
            # TODO division by zero risk.
            action_probability: float = 1/ len(self.state_space[state].actions)
            
            for action in state_space[state].actions:
                
                self[state][action] = action_probability
            
    def choose_action(
        self,
        state_index: SI
    ) -> A:
        """Choose an action based on the Action Probability Distribution."""

        actions: List[A] = list(self[state_index].keys())
        
        return random.choice(actions)

    def get_action_probability_distribution(
        self,
        state_index: SI
    ) -> ActionProbabilityDistribution[A]:

        return self[state_index]
