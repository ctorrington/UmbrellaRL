"""
Random walk configuration.
"""

from constants import Constants

ACTIONS = Constants.ACTIONS

class RandomWalk:
    def __init__(self, number_of_episodes: int,
                 number_of_states: int,
                 state_space: dict[int, dict]) -> None:
        self.number_of_episodes = number_of_episodes
        self.number_of_states = number_of_states
        self.state_space = state_space
        # self.estimated_value = 0
        # self.alpha = 0.00002
        # self.dimensionality = 1000
        # self.weights = [0 for i in range(self.dimensionality)]

        # Generate the random walk.
        for episode_number in range(self.number_of_episodes):
            self.generate_episode()


    def generate_episode(self):
        """Single episode for the random walk."""

    
    def make_action(self) -> ACTIONS:
        """Take an action according to the policy."""

        return ACTIONS.LEFT