"""
Environment type for a reinforcement learning problem.

Environment type is a mapping from a State Index to the State's possible Actions.

"""

from abc import ABC
from typing import Dict

from StateIndex import StateIndex # type: ignore
from StateProbabilityDistribution import StateProbabilityDistribution # type: ignore
from StateActions import StateActions
from Action import Action

class Environment[StateIndex](ABC, Dict[StateIndex, StateActions[StateIndex]]):
    def __init__(self):
        # Environment properties.
        self.number_of_states: int = len(self)

    def get_next_states(self,
                        current_state: StateIndex,
                        action: Action
                       ) -> StateProbabilityDistribution[StateIndex]:
        return self[current_state][action]

    # TODO Potentially redundant given the get-next-states method returning 
        # the distribution.
    def get_state_transition_probability(self,
                                         current_state: StateIndex,
                                         action: Action,
                                         next_state: StateIndex
                                        ) -> float:
        """
        Return the probability of transitioning from one state to another
        given an action.
        """
 
        return self[current_state][action][next_state]
