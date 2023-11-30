"""
State Actions type.

Mapping from Actions to a list of potential States from that Action.

Used by the Environment.
"""

from abc import ABC
from typing import Dict

from Action import Action
from StateIndex import StateIndex # type: ignore
from StateProbabilityDistribution import StateProbabilityDistribution

class StateActions[StateIndex](ABC, Dict[Action, StateProbabilityDistribution[StateIndex]]):
    def __getitem__(self,
                    key: Action
                   ) -> StateProbabilityDistribution[StateIndex]:
        """
        Return the State Probability Distribution for the State's accessible 
        following the given Action.
        """
        
        return self[key]
    
    def __setitem__(self,
                    key: Action,
                    value: StateProbabilityDistribution[StateIndex]
                   ) -> None:
        self[key] = value
    