"""State Space for the Grid World."""
import logging

from core.dependency.state_space import StateSpace
from Solutions.GridWorld.Action import GridWorldAction
from Solutions.GridWorld.StateIndex import GridWorldStateIndex
from log.ilogger import ILogger

class GridWorldStateSpace(StateSpace[GridWorldStateIndex, GridWorldAction]):
    """
    Grid World State Space representation.
    
    Every State is initialised the same.
    Terminal State values are then set afterwards.
    """
    
    def __init__(
        self,
        number_of_rows: int,
        number_of_columns: int,
        logger: ILogger
    ) -> None:
        self._logger: logging.Logger = logger.get_logger(self.__class__.__name__)
        self._logger.info(f"Initialising {self.__class__.__name__}...")

        super().__init__(logger=logger)
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        
        self._logger.info(
            f"Initialised {self.__class__.__name__} with number of rows: {number_of_rows}, number of columns: {number_of_columns}."
        )
