"""Environment."""

from constants import Constants
from StateSpace import StateSpace
from Services.EnvironmentService import EnvironmentService

ACTIONS = Constants.ACTIONS

class Environment:
    def __init__(self,
                 state_space: StateSpace,
                 environment_service: EnvironmentService
                ) -> None:
        """Environment."""
        
        # Environment properties.
        self.number_of_states: int = len(state_space)
        
        # Dependencies.
        self.state_space: StateSpace = state_space
        
        self.environment_service: EnvironmentService = environment_service
        
    def get_next_states(self,
                        current_state: int,
                        action: ACTIONS
                       ) -> list[int]:
        return self.environment_service.get_next_states(current_state, action)
    
    def get_state_transition_probability(self,
                                         current_state_index: int,
                                         action: ACTIONS,
                                         next_state_index: int
                                        ) -> float:
        """
        Return the probability of transitioning from one state to another
        given an action.
        """
        
        return self.environment_service.get_state_transition_probability(
            current_state_index,
            action,
            next_state_index
        )
