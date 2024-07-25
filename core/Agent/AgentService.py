"""Agent Service class"""

from typing import List, Dict

from core.dependency.state_index import StateIndex
from core.dependency.action import Action
from core.dependency.StateSpace import StateSpace
from core.Environment.Environment import Environment
from core.Policy.BasePolicy import BasePolicy
from core.dependency.BellmanEquation import BellmanEquation

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
        gamma: float
    ) -> List[A]:
        """
        Determine the Actions resulting in the greatest estimated return 
        from the given State.
        """
        action_value_distribution: Dict[A, float] = cls.calculate_greedy_actions_estimated_return(
            state_index=state_index,
            environment=environment,
            gamma=gamma
            )
        best_actions: List[A] = cls.determine_best_actions(
            action_value_distribution
        )

        return best_actions

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

            if action_value_distribution[action] >= best_value:
                best_value = action_value_distribution[action]
                best_actions.append(action)

        return best_actions
