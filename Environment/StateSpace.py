"""
CURRENT THINKING

The environemnt is dependent on the state space.
then the state space should be injected into the environment.
"""

from State import State

class StateSpace:
    """Environment State Space Dependency."""
    
    def __init__(self, number_of_states: int,
                 terminal_state_rewards: dict[int, int]) -> None:
        self.state_space: dict[int, State] = {}
        for state in range(number_of_states):
            self.state_space[state] = State()
            
        # Terminal states.
        for state in terminal_state_rewards:
            self.state_space[state].is_terminal = True
        
        # Terminal state rewards.
        self.state_space[0].reward = -1
        self.state_space[number_of_states - 1].reward = 1
        