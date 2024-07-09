"""State Space for the Grid World."""

from typing import List, Optional

from core.dependency.StateSpace import StateSpace

from Solutions.GridWorld.State import GridWorldState
from Solutions.GridWorld.Action import GridWorldAction
from Solutions.GridWorld.StateIndex import GridWorldStateIndex

class GridWorldStateSpace(StateSpace[GridWorldStateIndex, GridWorldAction]):
    """Grid World State Space representation."""
    
    def __init__(
        self,
        number_of_rows: int,
        number_of_columns: int,
        terminal_states: Optional[List[GridWorldStateIndex]] = None
    ) -> None:
        self.terminal_states = terminal_states
        # Set terminal states if they are not provided.
        if terminal_states is None:
            self.terminal_states = [
                (0, 0),
                (number_of_rows - 1, number_of_columns - 1)
            ]
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns

        for row in range(number_of_rows):
            for column in range(number_of_columns):

                grid_world_state: GridWorldState = GridWorldState(row, column)
                grid_world_state.actions = GridWorldAction.members()
                self[(row, column)] = grid_world_state

        for state_index in self.terminal_states:

            state = self.get_state(state_index)
            state.is_terminal = True
            state.reward = 1.0
