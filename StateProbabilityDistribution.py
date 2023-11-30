"""
State Probability Distribution type.

Mapping from States potentially resulting from an Action to the percentage 
chance of the State occuring, according to the Environment.

Used by the Environment.
"""

from abc import ABC
from typing import Dict

from StateIndex import StateIndex # type: ignore

# TODO this class needs to implement __getsetetcitem__ methods for classes.
    # The getsetetc methods need to check if a State exists, otherwise
    # return a custom Attribute error for that State not existing - then
    # thats handled or equated to 0.
class StateProbabilityDistribution[StateIndex](ABC, Dict[StateIndex, float]):
    def __getitem__(self,
                    key: StateIndex
                   ) -> float:
        return self[key]
    
    def __setitem__(self,
                    key: StateIndex,
                    value: float
                   ) -> None:
        self[key] = value
