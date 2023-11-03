"""Environment."""

import math
from constants import Constants
from StateSpace import StateSpace
# from Services.StateSpaceService import StateSpaceService

ACTIONS = Constants.ACTIONS

class Environment:
    def __init__(self, number_of_states: int) -> None:
        """Environment."""
        
        # Environment properties.
        self.number_of_states: int = 1000
        self.number_of_aggregated_states: int = 10
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
        
        # Environment state space.
        self.state_space: StateSpace = StateSpace(number_of_states,
                                                  terminal_state_rewards,
                                                #   StateSpaceService()
                                                )
    