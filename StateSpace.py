"""
State Space Type.

Structure for every State in the Environment that can be interacted with by a 
reinforcement learning Agent.
"""

from typing import Type, List, Dict

from State import State
from Action import Action

from Services.StateSpaceService import StateSpaceService

# TODO CHATGPT SUCKS & TYPEVAR IS NOT NEEDED FOR GENERICS
# TODO state indices should allow for any type, not just integer types.
class StateSpace(Dict[int, State]):
    """
    Collection of every State in the Environment that can be interacted with by
    a reinforcement learning Agent.
    
    Dictionary structure mapping each index to its State.
    
    Injected into Environment.
    """

    def __init__(self,
                 number_of_states: int,
                 terminal_states_rewards: Dict[int, float],
                 state_actions: Dict[int, List[Action]], # Classes derived from Action.
                 state_class: Type[State] = State
                ) -> None:
        for state in range(number_of_states):
            self[state] = state_class()
            
        StateSpaceService.set_terminal_states_rewards(self,
                                                      terminal_states_rewards)
        
        StateSpaceService.set_state_actions(self, state_actions)

    def __getattr__(self, key: int):
        if key in self:
            return self[key]
        else:
            raise AttributeError(f"'StateSpace' object has not attribute '{key}'")
 