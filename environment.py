"""Environment to be interacted with by an RL Agent."""

from constants import Constants

import math

ACTIONS = Constants.ACTIONS

class Environment:
    """Environment."""
    
    def __init__(self, number_of_episodes: int) -> None:
        """Initialise the environment."""
        
        self.number_of_episodes = number_of_episodes
        
        # State space properties.
        self.number_of_states = 1000
        self.number_of_aggregated_states = 10
        self.states_per_block = math.floor(
            self.number_of_states / self.number_of_aggregated_states
        )
        self.starting_state = math.floor(self.number_of_states / 2)
        self.current_state = self.starting_state
        self.current_block = math.floor(
            self.current_state / self.states_per_block
        )
        
        # State space set up.
        self.state_space = {}
        for state in range(self.number_of_states):
            # State properties.
            self.state_space[state] = {
                "actions": {},
                "policy": {},
                "estimated return": 0,
                "state entries": 0,
                "reward": 0,
            }
            