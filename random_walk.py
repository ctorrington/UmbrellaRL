"""
Random walk configuration.
"""

class RandomWalk:
    def __init__(self) -> None:
        self.number_of_episodes = 100000
        self.estimated_value = 0
        self.alpha = 0.00002
        self.dimensionality = 1000
        self.weights = [0 for i in range(self.dimensionality)]

        for episode_number in range(self.number_of_episodes):
            self.generate_episode()


    def generate_episode(self):
        """Single episode for the random walk."""

