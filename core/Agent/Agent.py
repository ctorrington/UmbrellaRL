"""RL Agent."""

from typing import List
from copy import deepcopy

from core.dependency.ActionProbabilityDistribution import ActionProbabilityDistribution
from core.dependency.StateSpace import StateSpace
from core.Environment.Environment import Environment
from core.Policy.BasePolicy import BasePolicy
from core.dependency.StateIndex import StateIndex
from core.dependency.State import State
from core.dependency.Action import Action
from core.Agent.AgentService import AgentService
from core.Agent.History import History

# TODO Need option to improve Policy without changing the current State Space. (in place)
    # Need copy of old State Value function, improve according to those values - set State Value Function to those updated values all at once (optional, include with current implementation)

class Agent[SI: StateIndex, A: Action]:
    """RL Agent."""

    # TODO add method for optinally tracking the history.

    def __init__(
        self,
        environment: Environment[SI, A],
        policy: BasePolicy[SI, A],
        theta: float = 0.01,
        gamma: float = 0.9
    ) -> None:
        # TODO Doc String.

        self.history = History[SI, A]()
        self.theta: float = theta
        self.gamma: float = gamma
        self.environment: Environment[SI, A] = environment
        self.policy: BasePolicy[SI, A] = policy

    def evaluate_policy(self) -> None:
        """
        Evaluate the policy.

        Determine the state-value function for the policy.
        """

        state_space: StateSpace[SI, A] = self.environment.get_state_space()

        while True:
            delta = 0
            for state_index in state_space:

                state: State[A] = state_space.get_state(state_index)
                if state.is_terminal:
                    continue

                old_state_value: float = state.estimated_return
                updated_state_value: float = AgentService.calculate_state_value(
                    state_index,
                    state_space,
                    self.policy,
                    self.environment,
                    self.gamma
                )
                state.estimated_return = updated_state_value
                delta = max(delta, (abs(old_state_value - updated_state_value)))

            if delta < self.theta:
                self.history.track_state_space(state_space)
                self.history.increment_history_count()
                break

    def improve_policy(self) -> None:
        """
        Improve the Policy.

        Determine optimal actions for each State in the State Space.
        """

        state_space: StateSpace[SI, A] = self.environment.get_state_space()

        while True:

            policy_stable: bool = True
            for state_index in state_space:
                
                state: State[A] = state_space.get_state(state_index)
                if not state.has_actions():
                    continue

                old_state_policy: ActionProbabilityDistribution[A] = deepcopy(self.policy.get_action_probability_distribution(state_index))
                new_greedy_actions: List[A] = AgentService.determine_greedy_actions(
                    state_index,
                    state_space,
                    self.environment,
                    self.gamma
                )
                self.policy.set_new_state_policy(
                    state_index,
                    new_greedy_actions
                )
                new_state_policy: ActionProbabilityDistribution[A] = self.policy.get_action_probability_distribution(state_index)
                if old_state_policy != new_state_policy:
                    policy_stable = False

            if policy_stable:
                break
            else:
                self.evaluate_policy()
