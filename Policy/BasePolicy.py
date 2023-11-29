"""
Base Policy class to be inherited by Policy classes used by a reinforcement
learning agent.
"""

from abc import ABC, abstractmethod
from typing import Dict

from ActionProbabilityDistribution import ActionProbabilityDistribution
from StateIndex import StateIndex # type: ignore
from Action import Action

# Policy type is a mapping from a State Index to its Action Probability Distribution.
# A State's Action Probability Distribution is a mapping of available actions
    # to their probability of being taken.

class BasePolicy[StateIndex](ABC, Dict[StateIndex, ActionProbabilityDistribution]):
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

        # TODO this method can be implemented & inherited. will be the same.
        pass
