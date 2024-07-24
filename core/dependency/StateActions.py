"""
State Actions type.

Mapping from Actions to a list of potential States from that Action.
"""

from abc import ABC
from typing import Dict

from core.dependency.action import Action
from core.dependency.StateIndex import StateIndex
from core.dependency.StateProbabilityDistribution import StateProbabilityDistribution

class StateActions[SI: StateIndex, A: Action](ABC, Dict[A, StateProbabilityDistribution[SI]]):

    def get_state_probability_distribution(
        self,
        action: A
    ) -> StateProbabilityDistribution[SI]:
        """
        Return the State Probability Distribution for the State's accessible 
        following the given Action.
        """

        return StateProbabilityDistribution(self[action])
