"""Agent Service class"""

class AgentService():
    """Class to handle calculations for the Agent."""
    
    @classmethod
    def calculate_bellman_optimality_value(cls,
                                           action_probability: float,
                                           next_state_probability: float,
                                           next_state_reward: float,
                                           gamma: float,
                                           next_state_value: float) -> float:
        """Return the optimal State value."""
        
        return action_probability * next_state_probability * (next_state_reward + (gamma * next_state_value))
        
        