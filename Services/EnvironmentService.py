"""Environment Service."""

from StateSpace import StateSpace
from Action import Action

class EnvironmentService:
    """Environment Service."""
    
    def __init__(self, state_space: StateSpace) -> None:
        self.state_space = state_space
        
    def get_next_states(self,
                        current_state: int,
                        action: Action
                       ) -> list[int]:
        """Return the next states from the current state following an action."""
        
        match action:
            case Action.left:
                return [current_state - 1]
            case Action.right:
                return [current_state + 1]
            
    def get_state_transition_probability(self,
                                         current_state_index: int,
                                         action: Action,
                                         next_state_index: int
                                        ) -> float:
        """
        Return the probability of transitioning from one state to another
        given an action.
        """
       
        # Catch states transitioning outside of the state space.
        if next_state_index < 0 or next_state_index > len(self.state_space):
            raise ValueError("Invalid index for next state. The index must be within the range of the State Space.")
 
        return 1
            