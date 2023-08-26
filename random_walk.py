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
                 terminal_states: list[int],
                 current_state: int) -> None:
        
        self.number_of_episodes = number_of_episodes
        self.number_of_states = number_of_states
        self.state_space = state_space
        self.terminal_states = terminal_states
        self.current_state = current_state
        # self.estimated_value = 0
        # self.alpha = 0.00002
        # self.dimensionality = 1000
        # self.weights = [0 for i in range(self.dimensionality)]

        # Generate the random walk.
        for episode_number in range(self.number_of_episodes):
            episode = self.generate_episode()
            print(episode)

            input()


    def generate_episode(self):
        """Single episode for the random walk."""

        episode = []
        
        while self.current_state not in self.terminal_states:

            timestep = {}

            action = self.make_action()
            next_state = self.determine_next_state(action)
            reward = self.state_space
            self.current_state = next_state

            timestep["state"] = self.current_state
            timestep["action"] = action
            timestep["next state"] = next_state
            timestep["reward"] = self.state_space[next_state]

            episode.append(timestep)
        
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
    
    def determine_next_state(self, action: ACTIONS) -> int:
        """Determine which state is next based on the action chosen."""

        # Left action was chosen.
        if action == ACTIONS.LEFT:
            next_state = random.choice(range(0, self.current_state - 1))
        # Right action was chosen.
        else:
            next_state = random.choice(range(self.current_state + 1,
                                             self.number_of_states))

        return next_state
