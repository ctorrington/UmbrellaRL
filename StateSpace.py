"""
CURRENT THINKING

The environemnt is dependent on the state space.
then the state space should be injected into the environment.
"""

from State import State
from Action import Action

from typing import Type, List, Dict, TypeVar

T = TypeVar('T', bound = 'Action')

class StateSpace(dict[int, State]):
    """
    Collection of States.
    
    Environmnet State Space dependency.
    """

    def __init__(self,
                 number_of_states: int,
                 terminal_states_rewards: Dict[int, int],
                 state_actions: Dict[int, List[T]], # Classes derived from Action.
                 state_class: Type[State] = State
                ) -> None:
        # for state in range(number_of_states):
        #     self[state] = state_class()
            
        # Terminal states & their rewards.
        # TODO StateSpaceService.
        self.set_terminal_states_rewards(terminal_states_rewards)
        
        # TODO StateSpaceService.
        self.set_actions(state_actions)

    def __getattr__(self, key: int):
        if key in self:
            return self[key]
        else:
            raise AttributeError(f"'StateSpace' object has not attribute '{key}'")
 
    # TODO StateSpaceService.
    def set_terminal_states_rewards(self, terminal_state_rewards: dict[int, int]) -> None:
        """Set the rewards & terminal properties for the terminal States."""
        
        for state in terminal_state_rewards:
            self[state].reward = terminal_state_rewards[state]
            self[state].is_terminal = True

    # TODO StateSpaceService.
    def set_actions(self,
                    state_actions: dict[int, list[T]]) -> None:
        """Set the possible actions for each State in the State Space."""
        
        # Check all states have been provided actions.
        if len(self) != len(state_actions):
            raise TypeError("Provide actions for all states. The number of key within 'state_actions' is not equal to the length of the State Space.")
        
        for state in state_actions:
            self[state].actions = state_actions[state]
        