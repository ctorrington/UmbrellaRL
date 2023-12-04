"""State Space for the Grid World."""

from typing import Tuple

from GridWorld.State import GridWorldState

from StateSpace import StateSpace

class GridWorldStateSpace(StateSpace[Tuple[int, int]]):
    """Grid World State Space representation."""
    
    def __init__(self,
                 number_of_rows: int,
                 number_of_columns: int
                ) -> None:
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        
        for row in range(number_of_columns):
            for column in range(number_of_columns):
                self[(row, column)] = GridWorldState(row, column)
