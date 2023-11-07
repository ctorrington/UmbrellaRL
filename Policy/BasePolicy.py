"""
Base Policy class to be inherited by Policy classes used by a reinforcement
learning agent.
"""

from abc import ABC, abstractmethod
from typing import Type

from ActionProbabilityDistribution import ActionProbabilityDistribution
from StateSpace import StateSpace
from Action import Action

class BasePolicy(ABC, dict[int, ActionProbabilityDistribution]):
    def __init__(self,
                 state_space: StateSpace,
                 action_probability_distribution_class: Type[ActionProbabilityDistribution] = ActionProbabilityDistribution
                ) -> None:
        for state in state_space:
            self[state] = action_probability_distribution_class({})
    
    @abstractmethod
    def choose_action(self, state: int) -> Action:
        """
        Abstracted method to be implemented by Policy subclasses.

        The Policy classes will use the ActionProbabilityDistribution class
        for determining actions.
        """
 
        pass

    @abstractmethod
    def get_action_probability_distribution(self, state: int) -> ActionProbabilityDistribution:
        """Get the action probability distribution for the given state."""

        pass
