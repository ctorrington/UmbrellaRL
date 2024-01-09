"""Grid World representation of a State."""

from typing import Optional

from core.State import State
from Solutions.GridWorld.Action import GridWorldAction

class GridWorldState(State[GridWorldAction]):
    def __init__(self, x: Optional[int] = None, y: Optional[int] = None):
        super().__init__()
        
        self.x: Optional[int] = x
        self.y: Optional[int] = y
