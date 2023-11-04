"""Environment."""

import math
from constants import Constants
from StateSpace import StateSpace
from Services.EnvironmentService import EnvironmentService
# from Services.StateSpaceService import StateSpaceService

ACTIONS = Constants.ACTIONS

class Environment:
    def __init__(self, number_of_states: int,
                 number_of_aggregated_states: int,
                 environment_service: EnvironmentService) -> None:
        """Environment."""
        
        # Environment properties.
        self.number_of_states: int = number_of_states
        self.number_of_aggregated_states: int = number_of_aggregated_states
        self.states_per_block: int = math.floor(
            self.number_of_states / self.number_of_aggregated_states
        )
        self.starting_state: int = math.floor(self.number_of_states / 2)
        self.current_state: int = self.starting_state
        self.current_block: int = math.floor(
            self.current_state / self.states_per_block
        )
        
       # Terminal states & rewards.
        terminal_state_rewards: dict[int, int] = {
           0: -1,
           number_of_states: 1,
       } 
        
        # Dependencies.
        
        # Environment state space.
        self.state_space: StateSpace = StateSpace(number_of_states,
                                                  terminal_state_rewards,
                                                #   StateSpaceService()
                                                )
        
        self.environment_service: EnvironmentService = environment_service
        
    def get_next_states(self, current_state: int,
                        action: ACTIONS) -> list[int]:
        return self.environment_service.get_next_states(current_state, action)
    
    def get_state_transition_probability(self, current_state_index: int,
                                         action: ACTIONS,
                                         next_state_index: int) -> float:
        """
        Return the probability of transitioning from one state to another
        given an action.
        """
        
        return self.environment_service.get_state_transition_probability(
            current_state_index,
            action,
            next_state_index
        )