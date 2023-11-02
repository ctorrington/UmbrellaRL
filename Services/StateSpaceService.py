"""State Space service."""

from StateSpace import StateSpace

class StateSpaceService:
    """Service class for the StateSpace."""
    
    def __init__(self, state_space: StateSpace) -> None:
       self.state_space = state_space
       
    def set_rewards(self, rewards: dict[int, int]) -> None:
        """Set the rewards for the State Space."""
        
        for state in rewards:
            self.state_space[state].reward = rewards[state]