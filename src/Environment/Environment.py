"""
Environment type for a reinforcement learning problem.

Environment type is a mapping from a State Index to the State's possible Actions.

"""

from abc import ABC
from typing import Dict

from src.StateIndex import StateIndex # type: ignore
from src.StateSpace import StateSpace
from src.StateProbabilityDistribution import StateProbabilityDistribution # type: ignore
from src.StateActions import StateActions
from src.Action import Action

class Environment[StateIndex, A: Action](ABC, Dict[StateIndex, StateActions[StateIndex]]):
    def __init__(self,
                 state_space: StateSpace[StateIndex, A]
                ) -> None:
        
        # Dependencies.
        self.state_space: StateSpace[StateIndex, A] = state_space
        
    def get_next_states(self,
                        current_state: StateIndex,
                        action: Action
                       ) -> StateProbabilityDistribution[StateIndex]:
        return self[current_state][action]

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
    
    def number_of_states(self):
        """Return the number of State's in the State Space."""
        
        return len(self)
    
    def get_state_space(self) -> StateSpace[StateIndex, A]:
        """Return the State Space."""
        
        return self.state_space
