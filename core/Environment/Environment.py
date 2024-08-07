"""
Environment type for a reinforcement learning problem.

Environment type is a mapping from a State Index to the State's possible Actions.
"""

from abc import ABC
from typing import Dict

from core.dependency.state_index import StateIndex
from core.dependency.StateSpace import StateSpace
from core.dependency.StateProbabilityDistribution import StateProbabilityDistribution
from core.dependency.StateActions import StateActions
from core.dependency.action import Action

class Environment[SI: StateIndex, A: Action](ABC, Dict[SI, StateActions[SI, A]]):
    
    def __init__(
        self,
        state_space: StateSpace[SI, A]
    ) -> None:
        self.state_space: StateSpace[SI, A] = state_space

    def get_next_states(
        self,
        current_state_index: SI,
        action: A
    ) -> StateProbabilityDistribution[SI]:
        return self.get_state_actions(current_state_index) \
            .get_state_probability_distribution(action)

    def get_state_actions(
        self,
        state_index: SI
    ) -> StateActions[SI, A]:
        return StateActions(self[state_index])

    def get_state_transition_probability(
        self,
        current_state_index: SI,
        action: A,
        next_state_index: SI
    ) -> float:
        """
        Return the probability of transitioning from one state to another
        given an action.
        """
        return self.get_state_actions(current_state_index) \
            .get_state_probability_distribution(action) \
                .get_state_probability(next_state_index)

    def number_of_states(self) -> int:
        """Return the number of State's in the State Space."""
        return len(self)

    def get_state_space(self) -> StateSpace[SI, A]:
        """Return the State Space."""
        return self.state_space
