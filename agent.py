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
    
    def get_action_probability_distribution(self, state: int) -> dict[ACTIONS, int | float]:
        """Return the probability distribution for the actions of the given state."""
        
        action_probability_distribution = {}
        
        # Random policy.
        if self.policy == "random":
            action_probability = 1 / (len(self.environment.get_possible_actions(state)))
            
            for action in self.environment.get_possible_actions(state):
                action_probability_distribution[action] = action_probability
                
        return action_probability_distribution

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
        
        # state_return = self.environment.get_state_return(state)
        possible_actions = self.environment.get_possible_actions(state)
        action_probability_distribution = self.get_action_probability_distribution(state)
        
        expected_return = 0
        
        # Loop for every possible action in the state.
        for action in possible_actions:
            action_probability = action_probability_distribution[action]
            possible_next_states = self.environment.get_next_states(state, action)
            
            # Loop for every possible next state resulting from the current action.
            for next_state in possible_next_states:
                next_state_probability = self.environment.get_state_transition_probability(state, action, next_state)
                next_state_reward = self.environment.get_state_reward(state)
                next_state_return = self.environment.get_state_return(state)
                
                action_reward = next_state_probability * (next_state_reward + (self.gamma * next_state_return))
                expected_return += action_probability * action_reward
                
        # state_value = expected_return
        
        # return state_value
        return expected_return
        