"""
Grid World representation of a State.

Each State has the same Actions, ie. Up, Down, Left, Right.
"""

from typing import Optional, List

from core.dependency.State import State
from Solutions.GridWorld.Action import GridWorldAction

class GridWorldState(State[GridWorldAction]):
    def __init__(
        self,
        action_list: List[GridWorldAction],
        x: Optional[int] = None,
        y: Optional[int] = None
    ):
        """Initialisation for a GridWorld State. Each Attribute is expected to 
        be relevant for the GridWorld Solution.

        Args:
            action_list (List[GridWorldAction]): List of GridWorld Actions. 
            The type of the list is inherited from GridWorld.Actions.
            x (Optional[int], optional): X value within the GridWorld grid. 
            Defaults to None.
            y (Optional[int], optional): Y value within the GridWorld grid. 
            Defaults to None.
        """
        super().__init__(
            action_list=action_list
        )
        
        self.reward = -1
        
        self.x: Optional[int] = x
        self.y: Optional[int] = y
