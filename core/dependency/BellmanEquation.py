"""Bellman Equation service class."""

from typing import List

from core.dependency.StateIndex import StateIndex
from core.dependency.action import Action
from core.dependency.StateSpace import StateSpace
from core.dependency.State import State
from core.Environment.Environment import Environment
from core.dependency.StateProbabilityDistribution import StateProbabilityDistribution
from core.dependency.ActionProbabilityDistribution import ActionProbabilityDistribution
from core.Policy.BasePolicy import BasePolicy

class BellmanEquation[SI: StateIndex, A: Action]():
    """Bellman Equation service class."""
    
    @classmethod
    def calculate_state_value(
        cls,
        state_index: SI,
        policy: BasePolicy[SI, A],
        environment: Environment[SI,A],
        gamma: float
    ) -> float:
        """Calculate the value of the State for the provided State Index.

        Args:
            state_index (SI): State Index of the State to calcuate the value of.
            state_space (StateSpace[SI, A]): State Space that the State is in.
            policy (BasePolicy[SI, A]): Policy that the State is following.
            environment (Environment[SI,A]): Environment that the State is in.
            gamma (float): Gamma value for the State value.

        Returns:
            float: Value (estimated return) of the State.
        """
        state_space: StateSpace[SI, A] = environment.get_state_space()
        state_action_probability_distribution: ActionProbabilityDistribution[A] = (
            policy.get_action_probability_distribution(state_index)
        )
        state: State[A] = state_space.get_state(state_index)
        state_actions: List[A] = state.actions
        state_value: float = 0

        for action in state_actions:

            action_probability: float = (
                state_action_probability_distribution[action]
            )
            update_value: float = cls.calculate_update_value(
                state_index=state_index,
                action=action,
                environment=environment,
                gamma=gamma
            )
            state_value += action_probability * update_value

        return state_value
        
    @classmethod
    def calculate_update_value(
        cls,
        state_index: SI,
        action: A,
        environment: Environment[SI, A],
        gamma: float
    ) -> float:
        """Calculate the update value of the Bellman Equation.

        Args:
            state_index (SI): State Index of the State to calculate the update 
            value of.
            action (A): Action to calculate the update value 
            state_space (StateSpace[SI, A]): State Space that the State is in.
            environment (Environment[SI, A]): Environment that the State is in.
            gamma (float): Gamma value to calculate the update value with.

        Returns:
            float: Update value for the Bellman Equation.
        """
        state_space: StateSpace[SI, A] = environment.get_state_space()
        update_value: float = 0
        next_states: StateProbabilityDistribution[SI] = (
            environment.get_next_states(state_index, action)
        )

        for next_state_index in next_states:

            next_state_probability: float = (
                environment.get_state_transition_probability(
                    state_index,
                    action,
                    next_state_index
                )
            )
            next_state: State[A] = state_space.get_state(next_state_index)
            next_state_reward: float = next_state.reward
            next_state_value: float = next_state.estimated_return
            update_value += next_state_probability * (next_state_reward + (gamma * next_state_value))

        return update_value

    @classmethod
    def calculate_state_action_value(
        cls,
        state_index: SI,
        action: A,
        environment: Environment[SI, A],
        gamma: float
    ) -> float:
        """
        Calculate the state action-value.

        From my understanding, the update value to the state value function is 
        equivalent to the state-action value. When greedy policy simply chooses 
        the maximising state-action (update) value.
        """
        state_action_value: float = cls.calculate_update_value(
            state_index,
            action,
            environment,
            gamma
            )

        return state_action_value
