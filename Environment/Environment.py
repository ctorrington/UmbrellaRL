"""
Environment type for a reinforcement learning problem.

Environment type is a mapping from a State Index to the State's possible Actions.

"""

# TODO Make the dictionary indexing perperties rather.
    # I think that it will be easer to read.
    # eg self.state_actions => StateActions. so id use:
    # self.state_actions[current_state].state_probability_distribution(action)
    # idk maybe thats dumb.

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
                                         current_state_index: StateIndex,
                                         action: Action,
                                         next_state_index: StateIndex
                                        ) -> float:
        """
        Return the probability of transitioning from one state to another
        given an action.
        """
 
        return self[current_state_index][action][next_state_index]       
