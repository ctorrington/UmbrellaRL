"""Environment Service."""

from StateSpace import StateSpace
from constants import Constants

ACTIONS = Constants.ACTIONS

class EnvironmentService:
    """Environment Service."""
    
    def __init__(self, state_space: StateSpace) -> None:
        self.state_space = state_space
        
        
    def get_next_states(self, current_state: int,
                        action: ACTIONS) -> list[int]
        """Return the next states from the current state following an action."""
        
        match action:
            case ACTIONS.LEFT:
                return [current_state - 1]
            case ACTIONS.RIGHT:
                return [current_state + 1]
            