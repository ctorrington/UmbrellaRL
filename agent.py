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
        
        pass
    
    def set_state_value(self, state) -> None:
        """
        Update the estimated return for the given state.
        This method uses the state value function.
        """
        pass
        