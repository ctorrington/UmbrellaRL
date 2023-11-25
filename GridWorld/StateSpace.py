"""State Space for the Grid World."""

from typing import Dict, List

from StateSpace import StateSpace

from GridWorld.State import GridWorldState
from GridWorld.Action import GridWorldAction

class GridWorldStateSpace(StateSpace):
    def __init__(self,
                 number_of_states: int,
                 terminal_states_rewards: Dict[int, int],
                 state_actions: Dict[int, List[GridWorldAction]]
                ):
        super().__init__(number_of_states,
                         terminal_states_rewards,
                         state_actions, # HERE
                         state_class = GridWorldState)
