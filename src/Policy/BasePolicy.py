"""
Base Policy type for a reinforcement learning agent.

Policy type is a mapping from a State Index to the State's
Action Probability Distribution.
A State's Action Probability Distribution is a mapping of available Actions to 
their probability of being taken by the Policy.
"""

from abc import ABC, abstractmethod
from typing import Dict, List

from src.ActionProbabilityDistribution import ActionProbabilityDistribution
from src.StateIndex import StateIndex
from src.Action import Action

# TODO Relook at the Policies, they need to be tidied up.

class BasePolicy[SI: StateIndex, A: Action](ABC, Dict[SI, ActionProbabilityDistribution[A]]):

    @abstractmethod
    def choose_action(
        self,
        state_index: SI
    ) -> A:

        """
        Policy selects an action for the given State according to the State's
        Action Probability Distribution & the goal of the Policy.
        """
 
        pass

    def get_action_probability_distribution(
        self,
        state_index: SI
    ) -> ActionProbabilityDistribution[A]:

        """Return the Action Probability Distribution for the given state."""
        
        return ActionProbabilityDistribution(self[state_index])

    def get_greedy_actions(
        self,
        state_index: SI
    ) -> List[A]:

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
        state: SI,
        new_actions: List[A]
    ) -> None:
        """Set a new Policy for given State."""

        state_action_probability_distribution: ActionProbabilityDistribution[A] = self.get_action_probability_distribution(state)

        new_action_probability: float = 1 / len(new_actions)

        for action in state_action_probability_distribution:

            if action in new_actions:

                self[state][action] = new_action_probability

            else:

                self[state][action] = 0
