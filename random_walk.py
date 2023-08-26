"""
Random walk configuration.
"""

import random

from constants import Constants


ACTIONS = Constants.ACTIONS

class RandomWalk:
    def __init__(self, number_of_episodes: int,
                 number_of_states: int,
                 state_space: dict[int, dict],
                 current_state: int) -> None:
        self.number_of_episodes = number_of_episodes
        self.number_of_states = number_of_states
        self.state_space = state_space
        self.current_state = current_state
        # self.estimated_value = 0
        # self.alpha = 0.00002
        # self.dimensionality = 1000
        # self.weights = [0 for i in range(self.dimensionality)]

        # Generate the random walk.
        for episode_number in range(self.number_of_episodes):
            self.generate_episode()


    def generate_episode(self):
        """Single episode for the random walk."""

        print(self.make_action())

    
    def make_action(self) -> ACTIONS:
        """Take an action according to the policy."""

        # The way that actions are handled here is embarrassingly bad.
        # When I figure out how to do this mathematically, I will.
        # Until then:

        # Handle random actions.
        if self.state_space[self.current_state]["policy"] == "random":
           action = random.choice(ACTIONS.as_tuple())
           return action

        # This is here to pacify the linter.
        return random.choice(ACTIONS.as_tuple())