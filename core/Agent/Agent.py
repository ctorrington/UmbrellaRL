"""RL Agent."""

from typing import List, Dict
from copy import deepcopy

from core.dependency.StateSpace import StateSpace
from core.Environment.Environment import Environment
from core.Policy.BasePolicy import BasePolicy
from core.dependency.state_index import StateIndex
from core.dependency.state import State
from core.dependency.action import Action
from core.Agent.AgentService import AgentService
from core.Agent.History import History

from log.ilogger import ILogger

class Agent[SI: StateIndex, A: Action]:
    """RL Agent."""

    # TODO add method for optinally tracking the history.

    def __init__(
        self,
        environment: Environment[SI, A],
        policy: BasePolicy[SI, A],
        logger: ILogger,
        theta: float,
        gamma: float,
    ) -> None:
        """Agent Initialisation.
        
        The Agent is capable of interacting with the provided Environment. It 
        does so in accordance with it's provided Policy.

        Args:
            environment (Environment[SI, A]): Environment the Agent shall 
            interact with.
            policy (BasePolicy[SI, A]): Policy the Agent follows.
            logger (ILogger): Logger class for logging processes.
            theta (float): Theta value used as threshold value for Policy 
            Evaluation.
            gamma (float): Gamma value used for determining State value 
            function.
        """
        # TODO Doc String.

        self.history = History[SI, A]()
        self.theta: float = theta
        self.gamma: float = gamma
        self.environment: Environment[SI, A] = environment
        self.policy: BasePolicy[SI, A] = policy
        self._logger = logger.get_logger(self.__class__.__name__)

    def evaluate_policy_synchronous(self) -> None:
        """Evaluate the Agent's Policy.
        
        Method uses Iterative Policy Evalution for estimating the value of each 
        State within the Environment.
        This method evaluates the Agent's Policy synchronously - each State's 
        estimated return is only updated after the entire State Space has been 
        iterated.
        """
        self._logger.info("Beginning synchronous Policy Evaluation process.")
        # Dictionary to store State values for updating after iterating through the State Space.
        state_value_history: dict[SI, float] = {}
        state_space: StateSpace[SI, A] = self.environment.get_state_space()
        while True:
            delta = 0
            # Determine State values.
            for state_index in state_space:
                # Value of terminal states are not evaluated.
                state: State[A] = state_space.get_state(state_index)
                if state.is_terminal:
                    continue

                old_state_value: float = state.estimated_return
                updated_state_value: float = AgentService.calculate_state_value(
                    state_index=state_index,
                    policy=self.policy,
                    environment=self.environment,
                    gamma=self.gamma
                )
                state_value_history[state_index] = updated_state_value
                delta = max(delta, (abs(old_state_value - updated_state_value)))

            # Update estimated returns for State's in the State Space.
            for state_index in state_space:
                state: State[A] = state_space.get_state(state_index)
                if state.is_terminal:
                    continue
                state.estimated_return = state_value_history[state_index]
            
            # Check whether State values have converged with parameter value.
            if delta < self.theta:
                self._logger.info(f"State value delta converged at value: {delta}. Ending synchronous Policy Evaluation process.")
                # self.history.track_state_space(state_space)
                # self.history.increment_history_count()
                break

    def evaluate_policy(self) -> None:
        """
        Evaluate the policy.

        Determine the state-value function for the policy.
        """
        self._logger.info("Beginning Policy Evaluation process.")
        state_space: StateSpace[SI, A] = self.environment.get_state_space()
        while True:
            delta = 0
            for state_index in state_space:
                state: State[A] = state_space.get_state(state_index)
                # Value of terminal states are not evaluated.
                if state.is_terminal:
                    continue

                old_state_value: float = state.estimated_return
                # Determine updated State's value.
                updated_state_value: float = AgentService.calculate_state_value(
                    state_index=state_index,
                    policy=self.policy,
                    environment=self.environment,
                    gamma=self.gamma
                )
                self._logger.debug(f"State {state_index} updated State Value: {updated_state_value}.")
                delta = max(delta, (abs(old_state_value - updated_state_value)))
                # Update the State's value.
                state.estimated_return = updated_state_value

            if delta < self.theta:
                # self.history.track_state_space(state_space)
                # self.history.increment_history_count()
                self._logger.info(f"State value delta converged at value: {delta}. Ending Policy Evaluation process.")
                break

            self._logger.info(
                f"State value delta {delta} still greater than break value theta {self.theta} - running Policy Evaluation again."
            )

    def improve_policy(self) -> None:
        """
        Improve the Policy.

        Determine optimal actions for each State in the State Space.
        """
        self._logger.info("Beginning Policy Improvement process.")
        state_space: StateSpace[SI, A] = self.environment.get_state_space()

        for state_index in state_space:
            state: State[A] = state_space.get_state(state_index)

            # Skip states that have no Actions.
            if not state.has_actions():
                self._logger.info(
                    f"State {state_index} has no Actions - skipping State. State Actions: {state.actions}."
                )
                continue

            # Get Action value function for State.
            action_value: Dict[A, float] = {}
            for action in state.actions:
                value: float = (
                    AgentService.calculate_action_value_for_action_in_state(
                        state_index=state_index,
                        action=action,
                        environment=self.environment,
                        gamma=self.gamma
                    )
                )
                action_value[action] = value

            # Determine greedy Actions.
            # TODO error here when calculating state value for improved policy.
            greedy_action_value: float = max(action_value.values())
            greedy_actions: List[A] = []
            for action in action_value:
                if action_value[action] == greedy_action_value:
                    greedy_actions.append(action)
            # greedy_actions: List[A] = (
            #     AgentService.determine_greedy_actions(
            #         state_index=state_index,
            #         environment=self.environment,
            #         gamma=self.gamma,
            #         logger=self._logger
            #     )
            # )

            # Set the Policy for the State to be greedy.
            self.policy.set_new_state_policy(
                state_index=state_index,
                new_actions=greedy_actions
            )

        self._logger.info("Ending Policy Improvement process.")

    def iterate_policy(
        self,
        evaluation_synchronous: bool
    ) -> None:
        """Iterate the Agent's Policy using iterative policy evaluation to 
        estimate an optimal Policy.

        Args:
            evaluation_synchronous (bool): Boolean value determining if Policy 
            Evaluation is performed synchronously or asynchrnously.
        """
        
        policy_evaluation_method = (
            self.evaluate_policy_synchronous if evaluation_synchronous else self.evaluate_policy
        )
        evaluation_method_string: str = (
            "synchronous" if evaluation_synchronous else "asynchronous"
        )
        self._logger.info(f"Beginning Policy Iteration process with {evaluation_method_string} Policy Evaluation.")

        while True:
            policy_evaluation_method()
            old_policy = deepcopy(self.policy)
            self.improve_policy()

            # Check if the new improved policy equals the old policy.
            if self.policy == old_policy:
                self._logger.info("Policy stable. Ending Policy Iteration.")
                break
            self._logger.info("Policies not equal - continuing Policy Iteration.")
