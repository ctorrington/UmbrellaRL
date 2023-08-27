"""
Random walk configuration.
"""

import random
import math

from constants import Constants


ACTIONS = Constants.ACTIONS

class RandomWalk:
    def __init__(self, number_of_episodes: int,
                 number_of_states: int,
                 state_space: dict[int, dict],
                 terminal_states: list[int],
                 states_per_block: int,
                 current_state: int) -> None:
        
        self.number_of_episodes = number_of_episodes
        self.number_of_states = number_of_states
        self.state_space = state_space
        self.terminal_states = terminal_states
        self.states_per_block = states_per_block
        self.current_state = current_state
        # self.estimated_value = 0
        # self.alpha = 0.00002
        # self.dimensionality = 1000
        # self.weights = [0 for i in range(self.dimensionality)]

        # Generate the random walk.
        for episode_number in range(self.number_of_episodes):
            episode = self.generate_episode()
            self.display_episode(episode)

    def generate_episode(self) -> list:
        """Single episode for the random walk."""

        episode = []

        while self.current_state not in self.terminal_states:

            timestep = {}

            action = self.make_action()
            next_state = self.determine_next_state(action)
            reward = self.state_space

            timestep["state"] = self.current_state
            timestep["action"] = action
            timestep["next state"] = next_state
            timestep["reward"] = self.state_space[next_state]

            self.current_state = next_state

            episode.append(timestep)

        return episode
        
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

        # TODO ERROR: Start state 500 went to next state of 700

        current_block = self.get_current_block()

        # Left action was chosen.
        if action == ACTIONS.LEFT:
            # Check if possible to move left.
            if current_block > 0:
                # Possible to move left.

                # Move left.
                current_block -= 1
                # Choice a state within the new aggregated block.
                # All states within the new block are chosen with equal
                # probability.
                next_state = random.choice(
                    self.get_current_block_range(current_block)
                )
            else:
                # Not possible to move left. Already in the left most block.
                # The number of states less than the number of states per block
                # add to the probability of the terminal state.

                # To include the probabilities of the missing states into the
                # probability of selecting the terminal state I include all
                # states in the current block & select a next state from an
                # equally random distribution. This way any state still to the
                # left is chosen fairly, but if any state to the right is
                # chosen - it is taken as the terminal state.
                next_state = random.choice(
                    self.get_current_block_range(current_block)
                )
                if next_state > self.current_state:
                    next_state = 0
                elif next_state == self.current_state:
                    # The agent has to move
                    self.determine_next_state(action)
                    # TODO I would rather come straight be to next_state,
                    # rather than restarting the entire function

        # Right action was chosen.
        else:
            # Check if it is possible to move right.
            if current_block < math.floor(self.number_of_states /
                                          self.states_per_block) - 1:
                # Possible to move right.
                current_block += 1
                next_state = random.choice(
                    self.get_current_block_range(current_block)
                )

            else:
                # Not possible to move right.
                # Pick a state with from the states remaining in the last block
                # to the right of the current state; adding the states missing
                # to the probability of terminating in the last state (same as
                # the process for the left action).
                next_state = random.choice(
                    self.get_current_block_range(current_block)
                )
                if next_state < self.current_state:
                    next_state = self.number_of_states - 1
                elif next_state == self.current_state:
                    # The agent has to move.
                    self.determine_next_state(action)

        return next_state

    def get_current_block(self) -> int:
        """Returns the current block the agent is in.
        
        The state space is aggregated for this exercise."""

        return math.floor(self.current_state / self.states_per_block)

    def get_current_block_range(self, current_block: int) -> range:
        """Return the range of states for the given block of states.
        
        This is for the state aggregation."""

        current_block_start = current_block * self.states_per_block

        return range(current_block_start,
                     current_block_start + self.states_per_block + 1)

    def display_episode(self, episode: list[dict]) -> None:
        """Display the generated episode."""

        counter = 0
        for timestamp in episode:
            print(f"Timestep: {counter}")
            print(f"State: {timestamp['state']}")
            print(f"Action: {timestamp['action']}")
            print(f"Next State: {timestamp['next state']}\n")

            counter += 1

            input()