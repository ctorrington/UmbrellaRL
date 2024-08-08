"""
Grid World representation of a State.

Each State has the same Actions, ie. Up, Down, Left, Right.
"""
import logging

from typing import List

from core.dependency.state import State
from Solutions.GridWorld.Action import GridWorldAction
from log.ilogger import ILogger

class GridWorldState(State[GridWorldAction]):
    def __init__(
        self,
        action_list: List[GridWorldAction],
        estimated_return: float,
        reward: float,
        is_terminal: bool,
        logger: ILogger,
        x: int,
        y: int
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
        self._logger: logging.Logger = logger.get_logger(self.__class__.__name__)
        self._logger.info(f"Initialising {self.__class__.__name__}...")
        
        # Core State properties properties.
        super().__init__(
            action_list=action_list,
            estimated_return=estimated_return,
            reward=reward,
            is_terminal=is_terminal,
            logger=logger
        )
        
        # Grid World State instance properties.
        self.x: int = x
        self.y: int = y

        self._logger.info(f"Initialised {self.__class__.__name__} with x: {self.x}, y: {self.y}.")
