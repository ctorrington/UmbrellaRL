"""
State Actions type.

Mapping from Actions to a list of potential States from that Action.
"""

from abc import ABC
from typing import Dict
from warnings import warn

from src.Action import Action
from src.StateIndex import StateIndex
from src.StateProbabilityDistribution import StateProbabilityDistribution

class StateActions[SI: StateIndex, A: Action](ABC, Dict[A, StateProbabilityDistribution[SI]]):
    def __getitem__(
        self,
        key: A
        ) -> StateProbabilityDistribution[SI]:
        """
        Return the State Probability Distribution for the State's accessible 
        following the given Action.
        """

        warn("Using square bracket notation for accessing the StateProbabilityDistribution class is not the preferred method. Consider explicitly using get_state_probability_distribution method available to the StateActions class.")

        return self[key]

    def get_state_probability_distribution(
        self,
        action: A
        ) -> StateProbabilityDistribution[SI]:
        """
        Return the State Probability Distribution for the State's accessible 
        following the given Action.
        """

        return self[action]
