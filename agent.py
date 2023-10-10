"""RL Agent to interact with a given environment."""

from environment import Environment
from constants import Constants

ACTIONS = Constants.ACTIONS

class Agent:
    """RL Agent."""
    
    def __init__(self, environment) -> None:
        self.environment: Environment = environment
        self.policy = "random"
        self.gamma = 0.9
        self.theta = 0.001
        self.history: list[Environment] = []
        
    def get_terminal_states(self) -> list[int]:
        """Get the terminal states of the state space"""
        
        return self.environment.get_terminal_states()

    def determine_value_function_over_state_space(self) -> None:
        """Determine the value of all states across the state space."""
        
        terminal_states = self.get_terminal_states()
        
        # Update the estimated returns for all states in the state space until
        # a theta is reached (theta is the value used for accuracy).
        while True:
            delta = 0
            
            # Update the expected return for each state.
            for state in self.environment.get_state_space():
                if state not in self.environment.get_terminal_states():
                    previous_state_return = self.environment.get_state_return(state)
                    self.environment.set_state_return(state, self.determine_state_value(state))
            
    def determine_state_value(self, state: int) -> int | float:
        """
        Determine the estimated return for the given state.
        This method uses the state value function.
        """
        
        
        