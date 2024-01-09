"""Bellman Equation service class."""

from typing import List

from core.StateIndex import StateIndex
from core.Action import Action
from core.StateSpace import StateSpace
from core.State import State
from core.Environment.Environment import Environment
from core.StateProbabilityDistribution import StateProbabilityDistribution
from core.ActionProbabilityDistribution import ActionProbabilityDistribution
from core.Policy.BasePolicy import BasePolicy

class BellmanEquation[SI: StateIndex, A: Action]():
    """Bellman Equation service class."""
    
    @classmethod
    def calculate_state_value(cls,
                              state_index: SI,
                              state_space: StateSpace[SI, A],
                              policy: BasePolicy[SI, A],
                              environment: Environment[SI,A],
                              gamma: float
                             ) -> float:
        """Calculate the state value """

        state_value: float = 0

        state_action_probability_distribution: ActionProbabilityDistribution[A] = policy.get_action_probability_distribution(state_index)

        state: State[A] = state_space.get_state(state_index)

        state_actions: List[A] = state.actions
        
        for action in state_actions:
            
            # TODO get method for below
            action_probability: float = state_action_probability_distribution[action]
            
            update_value: float = cls.calculate_update_value(
                state_index,
                action,
                state_space,
                environment,
                gamma
            )
            
            state_value += action_probability * update_value
            
        return state_value
        
    @classmethod
    def calculate_update_value(cls,
                               state: SI,
                               action: A,
                               state_space: StateSpace[SI, A],
                               environment: Environment[SI, A],
                               gamma: float
                              ) -> float:
        """Calculate the update to the Bellman Equation."""

        update_value: float = 0

        next_states: StateProbabilityDistribution[SI] = environment.get_next_states(
            state,
            action
        )

        for next_state_index in next_states:

            next_state_probability: float = environment.get_state_transition_probability(
                state,
                action,
                next_state_index
            )

            next_state: State[A] = state_space.get_state(next_state_index)

            next_state_reward: float = next_state.reward

            next_state_value: float = next_state.estimated_return

            update_value += next_state_probability * (next_state_reward + (gamma * next_state_value))

        return update_value

    @classmethod
    def calculate_state_action_value(cls,
                                     state: SI,
                                     action: A,
                                     state_space: StateSpace[SI,A],
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
            state,
            action,
            state_space,
            environment,
            gamma
            )

        return state_action_value
