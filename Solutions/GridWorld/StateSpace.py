"""State Space for the Grid World."""
import logging

from typing import List

from core.dependency.state_space import StateSpace
from Solutions.GridWorld.state import GridWorldState
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
        state_actions: List[GridWorldAction],
        state_estimated_return: float,
        state_reward: float,
        terminal_states: List[GridWorldStateIndex],
        terminal_state_reward: float,
        logger: ILogger
    ) -> None:
        self._logger: logging.Logger = logger.get_logger(self.__class__.__name__)

        super().__init__(
            state_actions=state_actions,
            state_estimated_return=state_estimated_return,
            state_reward=state_reward
        )
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.terminal_states = terminal_states
        
        self._logger.info(
            f"Initialising GridWorldStateSpace with number of rows: {number_of_rows}, number of columns: {number_of_columns}, terminal states: {terminal_states}."
        )

        self._initialise_states(
            logger=logger
        )
        self._initialise_terminal_states(
            reward=terminal_state_reward
        )

    def _initialise_states(
        self,
        logger: ILogger
    ):
        """Initialise all states."""
        self._logger.info(
            f"Initialising Grid World State's within the Grid World State Space."
        )

        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                grid_world_state: GridWorldState = GridWorldState(
                    action_list=self.state_actions,
                    estimated_return=self.state_estimated_return,
                    reward=self.state_reward,
                    logger=logger,
                    x=row,
                    y=column
                )
                self[(row, column)] = grid_world_state

        self._logger.info(
            f"Grid World State's initialised successfully."
        )

    def _initialise_terminal_states(
        self,
        reward: float
    ):
        """Initialise & set terminal state values."""
        self._logger.info(
            f"Setting Terminal State properties."
        )
        
        for state_index in self.terminal_states:
            state = self.get_state(state_index)
            state.is_terminal = True
            state.reward = reward
            self._logger.info(
                f"Terminal State {state_index} reward set to {reward}."
            )

        self._logger.info(
            f"Terminal State properties set successfully."
        )
