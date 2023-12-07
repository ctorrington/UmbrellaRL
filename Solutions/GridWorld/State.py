"""Grid World representation of a State."""

from typing import Optional

from State import State
from GridWorld.Action import GridWorldAction

class GridWorldState(State[GridWorldAction]):
    def __init__(self, x: Optional[int] = None, y: Optional[int] = None):
        super().__init__()
        
        self.x: Optional[int] = x
        self.y: Optional[int] = y
