"""
Policy class used for managing action selection for a reinforcement
learning agent.
"""

# TODO This Policy will be provided eventually as a builtin.

# import random

# from ActionProbabilityDistribution import ActionProbabilityDistribution
# from Policy.BasePolicy import BasePolicy
# from StateSpace import StateSpace
# from Action import Action

# class EquiprobablePolicy(BasePolicy):
#     def __init__(self,
#                  state_space: StateSpace
#                 ) -> None:
#         super().__init__(state_space)
        
#         action_probability: float = 1/ len(Action.members())
        
#         for state in state_space:
#             for action in state_space[state].actions:
#                 self[state][action] = action_probability
            
#     def choose_action(self, state: int) -> Action:
#         """Choose an action based on the Action Probability Distribution."""

#         return random.choice(list(self[state].keys()))

#     def get_action_probability_distribution(self, state: int) -> ActionProbabilityDistribution:

#         return self[state]
