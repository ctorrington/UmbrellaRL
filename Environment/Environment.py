"""Environment."""

import math
import constants

ACTIONS = constants.Constants.ACTIONS

class Environment:
    def __init__(self, number_of_states: int) -> None:
        """Environment."""
        
        self.number_of_episodes: int = number_of_states
        
        # Environment properties.
        self.number_of_states: int = 1000
        self.number_of_aggregated_states: int = 10
        self.states_per_block: int = math.floor(
            self.number_of_states / self.number_of_aggregated_states
        )
        self.starting_state: int = math.floor(self.number_of_states / 2)
        self.current_state: int = self.current_state
        self.current_block: int = math.floor(
            self.current_state / self.states_per_block
        )
        
        # Environment state space.
        self.state_space = {}
        for state in range(self.number_of_states):
            # State properties.
            self.state_space[state] = {
                "actions": [],
                "estimated return": 0,
                "state entries": 0,
                "reward": 0
            }
            
            # State actions.
            for action in ACTIONS.as_tuple():
                self.state_space[state]["actions"].append(action)
                
        # Terminal states.
        self.state_space[0]["reward"] = -1
        self.state_space[self.number_of_states - 1]["reward"] = 1