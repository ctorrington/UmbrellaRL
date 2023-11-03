"""State Space service."""

# TODO Actually do this Service class.

from StateSpace import StateSpace

class StateSpaceService:
    """Service class for the StateSpace."""
    
    def set_rewards(self, state_space: StateSpace,
                    rewards: dict[int, int]) -> None:
        """Set the rewards for the State Space."""
        
        for state in rewards:
            state_space[state].reward = rewards[state]
            