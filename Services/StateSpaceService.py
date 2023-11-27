"""State Space service."""

from typing import Dict, List

from Action import Action
from State import State # TODO temp fix for ciruclar imports. 
                        # Would prefer StateSpace type to Dict[int, State]

class StateSpaceService:
    """Service class for the StateSpace."""
    
    # TODO Custom states need to be considered. ie, custom terminal properties.
    @staticmethod
    def set_terminal_states_rewards(state_space: Dict[int, State],
                                    terminal_states_rewards: Dict[int, float]
                                   ) -> None:
        """Set the rewards & properties for the terminal States."""
        
        for state in terminal_states_rewards:
            state_space[state].reward = terminal_states_rewards[state]
            state_space[state].is_terminal = True
            
    @staticmethod
    def set_state_actions(state_space: Dict[int, State],
                          state_actions: Dict[int, List[Action]]
                         ) -> None:
        """Set the actions for each State."""
        
        for state in state_actions:
            state_space[state].actions = state_actions[state]
