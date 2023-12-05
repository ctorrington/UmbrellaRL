"""State Space for the Grid World."""

from typing import Tuple


from StateSpace import StateSpace

from GridWorld.State import GridWorldState
from GridWorld.Action import GridWorldAction


class GridWorldStateSpace(StateSpace[Tuple[int, int], GridWorldAction]):
    """Grid World State Space representation."""
    
    def __init__(self,
                 number_of_rows: int,
                 number_of_columns: int
                ) -> None:
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        
        for row in range(number_of_rows):
            for column in range(number_of_columns):
                self[(row, column)] = GridWorldState(row, column)
