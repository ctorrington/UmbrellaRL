"""
Base Policy type for a reinforcement learning agent.

Policy type is a mapping from a State Index to the State's
Action Probability Distribution.
A State's Action Probability Distribution is a mapping of available Actions to 
their probability of being taken by the Policy.
"""

import math
import warnings

from abc import ABC, abstractmethod
from typing import Dict, List

from core.dependency.action_probability_distribution import ActionProbabilityDistribution
from core.dependency.state_index import StateIndex
from core.dependency.action import Action
from core.Environment.Environment import Environment
from core.dependency.StateSpace import StateSpace
from core.dependency.StateProbabilityDistribution import StateProbabilityDistribution
from core.dependency.state import State

from log.ilogger import ILogger

# TODO Relook at the Policies, they need to be tidied up.

class BasePolicy[SI: StateIndex, A: Action](ABC, Dict[SI, ActionProbabilityDistribution[A]]):
    
    def __init__(
        self,
        logger: ILogger
    ):
        self._logger = logger.get_logger(self.__class__.__name__)        

    @abstractmethod
    def choose_action(
        self,
        state_index: SI
    ) -> A:
        """
        Policy selects an action for the given State according to the State's
        Action Probability Distribution & the goal of the Policy.
        """
        raise NotImplementedError

    def get_action_probability_distribution(
        self,
        state_index: SI
    ) -> ActionProbabilityDistribution[A]:
        """Return the Action Probability Distribution for the given state."""
        return ActionProbabilityDistribution(self[state_index])

    def set_action_probability_distribution(
        self,
        state_index: SI,
        distribution: ActionProbabilityDistribution[A]
    ) -> None:
        """Set the new Action Probability Distribution for the State at the given 
        State Index.

        Args:
            state_index (SI): State Index of the State to update the 
            Action Probability Distribution of.
            distribution (ActionProbabilityDistribution[A]): 
            ActionProbabilityDistribution type containing new Action 
            Probability Distribution values.
        """
        self._logger.info(f"Updating State {state_index} Action Probability Distribution with distribution: {distribution}.")

        # Ensure distribution values are not greater than 1.
        if sum(distribution.values()) > 1:
            raise ValueError(f"Action Probability Distribution values are greater than 1. A State cannot have Actions with a probability of being chosen being greater than 100%.")
        elif sum(distribution.values()) < 1:
            warnings.warn(f"Sum of Action Probability Distribution is less than 1.")

        self[state_index] = distribution

    def get_greedy_actions_for_state(
        self,
        state_index: SI,
        environment: Environment[SI, A]
    ) -> List[A]:
        """Return a list of Actions that result in States with the greatest 
        estimated value.

        Args:
            state_index (SI): State Index of the State to return the greedy 
            actions from.

        Returns:
            List[A]: List of type Action. Each Action results in a State with 
            the greatest value from the provided State.
        """
        self._logger.debug(f"Getting greedy Actions for State: {state_index}.")

        state_space: StateSpace[SI, A] = environment.get_state_space()
        action_max_value: Dict[A, float] = {}

        # Get the Actions for the State.
        state_actions: List[A] = state_space.get_state(state_index).actions

        for action in state_actions:
            # Get the possible next States following current Action.
            next_states: StateProbabilityDistribution[SI] = (
                environment.get_next_states(
                    current_state_index=state_index,
                    action=action
                )
            )
            self._logger.debug(f"State {state_index} next States with Action {action}: {next_states}.")

            # Get the estimated return of the possible next States.
            next_state_values: List[float] = []
            for next_state_index in next_states:

                state: State[A] = state_space.get_state(next_state_index)
                state_value: float = state.estimated_return
                self._logger.debug(f"State {next_state_index} estimated return: {state_value}.")

                # Record next State values for current Action.
                next_state_values.append(state_value)

            # Get the maximum value of the possible next States.
            next_state_max_value: float = max(next_state_values)            
            action_max_value[action] = next_state_max_value
            
        max_value: float = max(action_max_value.values())
        
        greedy_actions: List[A] = (
            [action for action, value in action_max_value.items() if math.isclose(value, max_value, rel_tol=1e-9)]
        )

        self._logger.debug(f"Retrieved greedy Actions for State: {state_index} successfully. Greedy Actions: {greedy_actions}.")
        return greedy_actions

    def get_greedy_actions_old(
        self,
        state_index: SI
    ) -> List[A]:
        raise DeprecationWarning()
        # TODO This should not be correct?
        """Return the Actions with the highest probability of being chosen."""

        greedy_actions: List[A] = []
        greedy_value = max(self.get_action_probability_distribution(state_index).values())

        # TODO type of self.get_action_probability_distribution is not correct type (ActionProbabilityDistribution).
        action_prob_dist: ActionProbabilityDistribution[A] = ActionProbabilityDistribution(self.get_action_probability_distribution(state_index))
        
        for action in action_prob_dist:

            if action_prob_dist.get_action_probability(action) >= greedy_value:
                greedy_actions.append(action)

        return greedy_actions

    # TODO should not be a list (this is equiprobable)
    def set_new_state_policy(
        self,
        state_index: SI,
        new_actions: List[A]
    ) -> None:
        raise DeprecationWarning(f"Method {self.__class__.__name__} depracated. Use core.policy.base_policy.set_new_state_policy instead.")
        """Set a new Policy for given State."""
        self._logger.info(
            f"Setting new Policy for State {state_index} - new greedy Actions: {new_actions}."
        )

        state_action_probability_distribution: ActionProbabilityDistribution[A] = (
            self.get_action_probability_distribution(state_index)
        )
        new_action_probability: float = 1 / len(new_actions)

        for action in state_action_probability_distribution:

            if action in new_actions:
                self[state_index][action] = new_action_probability
                self._logger.debug(
                    f"State {state_index} Action {action} has a new Policy probability of {new_action_probability}."
                )
            else:
                self[state_index][action] = 0
        
        self._logger.info(
            f"Setting new Policy for State {state_index} completed successfuly."
        )
