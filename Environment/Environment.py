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
                       ) -> StateActions[StateIndex]:
        return self.environment_service.get_next_states(current_state, action)
    
    def get_state_transition_probability(self,
                                         current_state_index: int,
                                         action: Action,
                                         next_state_index: int
                                        ) -> float:
        """
        Return the probability of transitioning from one state to another
        given an action.
        """
        
        return self.environment_service.get_state_transition_probability(
            current_state_index,
            action,
            next_state_index
        )
