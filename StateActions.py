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
    pass