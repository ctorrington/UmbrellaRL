"""
Base Policy type for a reinforcement learning agent.

Policy type is a mapping from a State Index to the State's
Action Probability Distribution.
A State's Action Probability Distribution is a mapping of available Actions to 
their probability of being taken by the Policy.
"""

from abc import ABC, abstractmethod
from typing import Dict, List

from src.ActionProbabilityDistribution import ActionProbabilityDistribution
from src.StateIndex import StateIndex
from src.Action import Action


class BasePolicy[SI: StateIndex, A: Action](ABC, Dict[SI, ActionProbabilityDistribution[A]]):
    @abstractmethod
    def choose_action(self,
                      state: SI
                     ) -> A:
        """
        Policy selects an action for the given State according to the State's
        Action Probability Distribution & the goal of the Policy.
        """
 
        pass

    @abstractmethod
    def get_action_probability_distribution(self,
                                            state: SI
                                           ) -> ActionProbabilityDistribution[A]:
        """Return the Action Probability Distribution for the given state."""
        
        return ActionProbabilityDistribution(self[state])
   
    # TODO should not be a list (this is equiprobable)
    def set_new_state_policy(self,
                             state: SI,
                             new_actions: List[A]
                            ) -> None:
        """Set a new Policy for given State."""
        
        state_action_probability_distribution: ActionProbabilityDistribution[A] = self.get_action_probability_distribution(state)
        
        new_action_probability: float = 1 / len(new_actions)
        
        for action in state_action_probability_distribution:
            if action in new_actions:
                self[state][action] = new_action_probability
            else:
                self[state][action] = 0
