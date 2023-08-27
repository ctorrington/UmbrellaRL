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
            # self.display_episode(episode)
            self.display_episode_stats(episode)

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
    
    def get_block_for_state(self, state: int) -> int:
        """Return the block for a given state.
        
        This is necessary for different aggregation sizes."""
        # I don't know if it is better to just set an optional parameter for
        # get_current_block().

        return math.floor(state / self.states_per_block)

    def get_current_block_range(self, current_block: int) -> range:
        """Return the range of states for the given block of states.
        
        This is for the state aggregation."""

        current_block_start = current_block * self.states_per_block

        return range(current_block_start,
                     current_block_start + self.states_per_block - 1)

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

    def display_episode_stats(self, episode: list[dict]) -> None:
        """Display the stats for the generated episode."""

        action_taken_tracker = {}
        states_visited_tracker = {}
        blocks_visited_tracker = {}
        episode_length_tracker = {}
        episode_length_counter = 0
        terminal_state = None

        for timestep in episode:
            # Actions taken tracker.
            if timestep["action"] not in action_taken_tracker:
                action_taken_tracker[timestep["action"]] = 1
            else:
                action_taken_tracker[timestep["action"]] += 1

            # States visited tracker.
            if timestep["state"] not in states_visited_tracker:
                states_visited_tracker[timestep["state"]] = 1
            else:
                states_visited_tracker[timestep["state"]] += 1

            # Blocks visited tracker.
            block = self.get_block_for_state(timestep["state"])
            if block not in blocks_visited_tracker:
                blocks_visited_tracker[block] = 1
            else:
                blocks_visited_tracker[block] += 1

            # Terminal state.
            if timestep["next state"] in self.terminal_states:
                terminal_state = timestep["next state"]


            episode_length_counter += 1

        # Episode length tracker.
        if episode_length_counter not in episode_length_tracker:
            episode_length_tracker[episode_length_counter] = 1
        else:
            episode_length_tracker[episode_length_counter] += 1

        print(f"Number of episodes generated: {self.number_of_episodes}.")
        print(f"Maximum episode length: ")
        print(f"Minimum episode length: ")
        print(f"Average episode length: ")
        print(f"Number of {ACTIONS.LEFT} actions taken: {action_taken_tracker[ACTIONS.LEFT]}.")
        print(f"Number of {ACTIONS.RIGHT} actions taken: {action_taken_tracker[ACTIONS.RIGHT]}.")
        # print(f"State visited | Number of times visted.")
        # for state in states_visited_tracker:
            # print(f"{state} | {states_visited_tracker[state]}")
        print(f"Block visited | Number of times visted.")
        for block in blocks_visited_tracker:
            print(f"{block} | {blocks_visited_tracker[block]}")
        print(f"Episode terminated in state: {terminal_state}.")
