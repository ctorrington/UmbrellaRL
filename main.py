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

from agent import Agent

    def generate_random_walk(self) -> None:
        """Creates the random walk with the given parameters."""

        RandomWalk(self.number_of_episodes,
                   self.number_of_states,
                   self.state_space,
                   self.terminal_states,
                   self.states_per_block,
                   self.current_state,)

if __name__ == "__main__":
    
    agent = Agent()
    
    I_WILL_WALK_1K = ThousandStateRandomWalk()
    I_WILL_WALK_1K.generate_random_walk()
