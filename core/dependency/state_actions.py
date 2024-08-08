"""
State Actions type.

Mapping from Actions to a list of potential States from that Action.
"""

from abc import ABC
from typing import Dict

from core.dependency.action import Action
from core.dependency.state_index import StateIndex
from core.dependency.state_probability_distribution import StateProbabilityDistribution

class StateActions[SI: StateIndex, A: Action](ABC, Dict[A, StateProbabilityDistribution[SI]]):
    """Mapping of an Action to it's State Probability Distribution. Actions can 
    result in multiple States. StateActions connects an Action within a State 
    to its StateProbabilityDistribution - the probability of next States 
    occuring.
    
    State Actions are used by an Environment to connect an Action taken in a 
    State to a distribution of possible next States.
    """

    def get_state_probability_distribution(
        self,
        action: A
    ) -> StateProbabilityDistribution[SI]:
        """
        Return the State Probability Distribution for the State's accessible 
        following the given Action.
        """

        return StateProbabilityDistribution(self[action])
