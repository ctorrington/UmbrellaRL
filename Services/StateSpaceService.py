"""State Space service."""

import StateSpace

class StateSpaceService:
    """Service class for the StateSpace."""
    
    def set_rewards(self, state_space: StateSpace.StateSpace,
                    rewards: dict[int, int]) -> None:
        """Set the rewards for the State Space."""
        
        for state in rewards:
            state_space[state].reward = rewards[state]
            