"""
All episodes begin in the center.
Move either left or right by one state, all with equal probability.
(in the project, states are aggregated,
 so there are 100 states to the left & 100 states to the right.)
In the case that the state is near an edge,
 then the probability of that would have gone into the missing neighbours
 goes into the probability of terminating on that side.
(thus, state 1 has a 0.5 chance of terminating on the left,
 & state 950 has a 0.25 chance of terminating on the right)

Termination on the left produces a reward of -1.
Termination on the right produces a reward of +1.
All other transitions have a reward of 0.
"""

import math

from constants import Constants
from random_walk import RandomWalk

# Constants
ACTIONS = Constants.ACTIONS

class ThousandStateRandomWalk:
    """Random walk environment."""

    def __init__(self) -> None:
        """Initialse the environment."""

        # self.number_of_episodes = 1000
        self.number_of_episodes = 1

        # State space values.
        self.number_of_states = 1000
        self.number_of_aggregated_states = 10
        self.states_per_block = math.floor(
            self.number_of_states / self.number_of_aggregated_states
        )
        self.starting_state = math.floor(self.number_of_states / 2)
        self.current_state = self.starting_state

        self.current_block = math.floor(self.current_state /
                                         self.states_per_block)
        
        # State space set up.
        self.state_space = {}
        for state in range(0, self.number_of_states - 1):
            # Properties for each state.
            self.state_space[state] = {
                "actions": {},
                "policy": {},
                "estimated return": 0,
                "state entries": 0,
                "reward": 0
            }

            # Actions for each state.
            for action in ACTIONS.as_tuple():
                self.state_space[state]["actions"][action] = {
                    "value": 0,
                    "cumulative weight": 0,
                }

            # Policy.
            # Random policy.
            self.state_space[state]["policy"] = "random"

        # Terminal states.
        self.terminal_states = [0, self.number_of_states - 1]

        # Terminal rewards.
        self.state_space[0]["reward"] = -1
        self.state_space[self.number_of_states - 1] = 1

    def set_current_block(self) -> None:
        """Updates the current block that the agent is currently in."""
        self.current_block = math.floor(self.current_state /
                                        self.states_per_block)
        
    def generate_random_walk(self) -> None:
        """Creates the random walk with the given parameters."""

        RandomWalk(self.number_of_episodes,
                   self.number_of_states,
                   self.state_space,
                   self.terminal_states,
                   self.states_per_block,
                   self.current_state,)

if __name__ == "__main__":
    I_WILL_WALK_1K = ThousandStateRandomWalk()
    I_WILL_WALK_1K.generate_random_walk()
