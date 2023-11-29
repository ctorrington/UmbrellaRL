"""
State Probability Distribution type.

Mapping from States potentially resulting, from an Action, to the percentage 
chance of the State occuring, according to the Environment.

Used by the Environment.
"""

from abc import ABC
from typing import Dict

from StateIndex import StateIndex # type: ignore

class StateProbabilityDistribution[StateIndex](ABC, Dict[StateIndex, float]):
    pass
