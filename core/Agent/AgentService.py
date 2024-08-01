"""Agent Service class"""

import logging

from typing import List, Dict

from core.dependency.state_index import StateIndex
from core.dependency.action import Action
from core.dependency.state_space import StateSpace
from core.Environment.Environment import Environment
from core.Policy.BasePolicy import BasePolicy
from core.dependency.BellmanEquation import BellmanEquation
from core.dependency.StateProbabilityDistribution import StateProbabilityDistribution
from core.dependency.state import State

# TODO Service class could probably do with a Bellman Service class of its own.

class AgentService[SI: StateIndex, A: Action]():
    """Class to handle calculations for the Agent."""

    @classmethod
    def calculate_state_value(
        cls,
        state_index: SI,
        policy: BasePolicy[SI, A],
        environment: Environment[SI, A],
        gamma: float
    ) -> float:
        # TODO Doc string.
        state_value: float = BellmanEquation.calculate_state_value(
            state_index=state_index,
            policy=policy,
            environment=environment,
            gamma=gamma
        )

        return state_value

    @classmethod
    def determine_greedy_actions(
        cls,
        state_index: SI,
        environment: Environment[SI, A],
        gamma: float,
        logger: logging.Logger
    ) -> List[A]:
        """
        Determine the Actions resulting in the greatest estimated return 
        from the given State.
        """
        logger.info(f"Determining greedy Actions for State {state_index} with gamma {gamma}.")

        action_value_distribution: Dict[A, float] = cls.calculate_greedy_actions_estimated_return(
            state_index=state_index,
            environment=environment,
            gamma=gamma
            )
        greedy_actions: List[A] = cls.determine_best_actions(
            action_value_distribution
        )

        logger.info(
            f"State {state_index} greedy Actions determined successfully - greedy Actions: {greedy_actions}."
        )
        return greedy_actions

    @classmethod
    def calculate_action_value_for_action_in_state(
        cls,
        state_index: SI,
        action: A,
        environment: Environment[SI, A],
        gamma: float
    ) -> float:
        """Calculate the Action value of the State with State Index.

        Args:
            state_index (SI): _description_
            action (A): _description_
            environment (Environment[SI, A]): _description_
            gamma (float): _description_

        Returns:
            float: _description_
        """
        state_space: StateSpace[SI, A] = environment.get_state_space()
        next_state_distribution: StateProbabilityDistribution[SI] = (
            environment.get_next_states(
                current_state_index=state_index,
                action=action
            )
        )
        action_value: float = 0
        
        for state_index in next_state_distribution:
            state: State[A] = state_space.get_state(state_index)
            reward: float = state.reward
            estimated_return: float = state.estimated_return
            
            update_value: float = (
                next_state_distribution[state_index]* (reward + (gamma * estimated_return))
            )
            
            action_value += update_value

        return action_value
        

    @classmethod
    def calculate_greedy_actions_estimated_return(
        cls,
        state_index: SI,
        environment: Environment[SI, A],
        gamma: float
    ) -> Dict[A, float]:
        """
        Calculate the Actions resulting in the highest estimated return from 
        the given State.
        """
        state_space: StateSpace[SI, A] = environment.get_state_space()
        action_value_distribution: Dict[A, float] = {}

        for action in state_space[state_index].actions:

            action_value: float = BellmanEquation.calculate_update_value(
                state_index=state_index,
                action=action,
                environment=environment,
                gamma=gamma
            )
            action_value_distribution[action] = action_value

        return action_value_distribution

    @classmethod
    def determine_best_actions(
        cls,
        action_value_distribution: Dict[A, float]
    ) -> List[A]:
        """Return the Actions that result in the greatest esimated return."""

        best_value: float = max(action_value_distribution.values())
        best_actions: List[A] = []

        for action in action_value_distribution:

            if action_value_distribution[action] == best_value:
                # best_value = action_value_distribution[action]
                best_actions.append(action)

        return best_actions
