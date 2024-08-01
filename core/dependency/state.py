"""
State Type.

State representation for a reinforcement learning environment.
A State's estimated return is synonymous a State's value.
"""
import logging

from typing import List

from core.dependency.action import Action
from log.ilogger import ILogger

class State[A: Action]:
    """
    State representation for a reinforcement learning environment.

    Inherit from this class to define additional State member fields.
    """

    def __init__(
        self,
        action_list: List[A],
        estimated_return: float,
        reward: float,
        logger: ILogger
    ):
        """Initialisation for an individual State.

        Args:
            state_action_list (List[A]): Agent Actions available within the 
            State. The type of the list is inherited from the 
            core.dependency.action class.
            estimated_return (float): Float value for the estimated return of 
            the State.
            reward (float): Float value for the reward of the Agent reaching 
            the State.
        """
        self._logger: logging.Logger = logger.get_logger(self.__class__.__name__)
        self._actions: List[A] = action_list
        self._estimated_return: float = estimated_return
        self._reward: float = reward
        self._is_current: bool = False
        self._is_terminal: bool = False
        self._counter: int = 0

        self._logger.info(
            f"State initialised with actions: {action_list}, estimated return: {estimated_return}, reward: {reward}, current state: {self._is_current}, terminal state: {self._is_terminal}, counter: {self._counter}."
        )

    @property
    def actions(self) -> List[A]:
        return self._actions

    @actions.setter
    def actions(
        self,
        actions: List[A]
    ) -> None:
        self._actions = actions

    def has_actions(self) -> bool:
        return bool(self._actions)

    @property
    def estimated_return(self) -> float:
        return self._estimated_return

    @estimated_return.setter
    def estimated_return(
        self,
        estimated_return: float
    ) -> None:
        self._estimated_return = estimated_return

    @property
    def counter(self) -> int:
        return self._counter
    
    def increment_counter(self) -> None:
        self._counter += 1

    @property
    def reward(self) -> float:
        return self._reward

    @reward.setter
    def reward(
        self,
        reward: float
    ) -> None:
        self._reward = reward

    @property
    def is_current(self) -> bool:
        return self._is_current

    @is_current.setter
    def is_current(
        self,
        is_current: bool
    ) -> None:
        self._is_current = is_current

    @property
    def is_terminal(self) -> bool:
        return self._is_terminal

    @is_terminal.setter
    def is_terminal(
        self,
        is_terminal: bool
    ) -> None:
        self._is_terminal = is_terminal
