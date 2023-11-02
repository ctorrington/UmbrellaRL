"""State Space service."""

from StateSpace import StateSpace

class StateSpaceService:
    """Service class for the StateSpace."""
    
    @classmethod
    def set_rewards(cls, state_space: StateSpace,
                    rewards: dict[int, int]) -> None:
        """Set the rewards for the State Space."""
        
        for state in rewards:
            state_space[state].reward = rewards[state]
            