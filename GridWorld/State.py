"""Grid World representation of a State."""

from State import State

class GridWorldState(State):
    def __init__(self):
        super().__init__()
        
        self.x: int
        self.y: int