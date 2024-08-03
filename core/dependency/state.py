"""
State Type.

State representation for a reinforcement learning environment.
A State's estimated return is synonymous a State's value.
"""
import logging

from typing import List, Any

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
        is_terminal: bool,
        logger: ILogger
    ):
        """Initialisation for an individual State.

        Args:
            action_list (List[A]): Agent Actions available within the 
            State. The type of the list is inherited from the 
            core.dependency.action class.
            estimated_return (float): Float value for the estimated return of 
            the State.
            reward (float): Float value for the reward of the Agent reaching 
            the State.
            is_terminal (bool): Boolean value for if the State is a Terminal 
            State
        """
        self._validate_parameters(action_list=action_list, estimated_return=estimated_return, reward=reward, is_terminal=is_terminal, logger=logger)
        # Assigned properties.
        self._logger: logging.Logger = logger.get_logger(self.__class__.__name__)
        self.actions: List[A] = action_list
        self.estimated_return: float = estimated_return
        self.reward: float = reward
        self.is_terminal: bool = is_terminal

        self.is_current: bool = False
        self.counter: int = 0

        self._logger.info(
            f"State initialised with actions: {self.actions}, estimated return: {self.estimated_return}, reward: {self.reward}, current state: {self.is_current}, terminal state: {self.is_terminal}, counter: {self.counter}."
        )

    def _validate_parameters(
        self,
        action_list: Any,
        estimated_return: Any,
        reward: Any,
        is_terminal: Any,
        logger: Any
    ) -> None:
        if not isinstance(action_list, list) or not all(isinstance(action, Action) for action in action_list):
            raise TypeError(f"action_list must be list of type Action instances.")
        if not isinstance(estimated_return, float):
            raise TypeError(f"estimated_return must be of type float.")
        if not isinstance(reward, float):
            raise TypeError(f"reward must be of type float.")
        if not isinstance(is_terminal, bool):
            raise TypeError(f"is_terminal must be of type bool.")
        if not isinstance(logger, ILogger):
            raise TypeError(f"logger must be of type ILogger.")

    def has_actions(self) -> bool:
        return bool(self.actions)

    def increment_counter(self) -> None:
        self._logger.info(f"Incrementing State.counter from {self.counter} to {self.counter + 1}.")
        self.counter += 1
