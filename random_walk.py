"""
Random walk configuration.
"""

class RandomWalk:
    def __init__(self, number_of_episodes: int) -> None:
        self.number_of_episodes = number_of_episodes
        # self.estimated_value = 0
        # self.alpha = 0.00002
        # self.dimensionality = 1000
        # self.weights = [0 for i in range(self.dimensionality)]

        # Generate the random walk.
        for episode_number in range(self.number_of_episodes):
            self.generate_episode()


    def generate_episode(self):
        """Single episode for the random walk."""

