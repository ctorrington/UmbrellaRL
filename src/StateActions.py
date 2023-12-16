"""
State Actions type.

Mapping from Actions to a list of potential States from that Action.

Used by the Environment.
"""

from abc import ABC
from typing import Dict

from src.Action import Action
from src.StateIndex import StateIndex
from src.StateProbabilityDistribution import StateProbabilityDistribution

# TODO There is potential for this needing to be calculated dynamically, rather than programmed.
class StateActions[SI: StateIndex, A: Action](ABC, Dict[A, StateProbabilityDistribution[SI]]):
    def __getitem__(self,
                    key: A
                   ) -> StateProbabilityDistribution[SI]:
        """
        Return the State Probability Distribution for the State's accessible 
        following the given Action.
        """
        
        return self[key]
    
    def get_state_probability_distribution(self,
                                           action: A
                                          ) -> StateProbabilityDistribution[SI]:
        """Return the Action Probability Distribution for the given Action."""
        return self[action]
