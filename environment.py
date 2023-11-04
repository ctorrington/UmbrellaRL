# """Environment to be interacted with by an RL Agent."""

# from constants import Constants

# import math

# ACTIONS = Constants.ACTIONS

# class Environment:
#     """Environment."""
    
#     def __init__(self, number_of_episodes: int) -> None:
#         """Initialise the environment."""
        
#         self.number_of_episodes = number_of_episodes
        
#         # State space properties.
#         self.number_of_states = 1000
#         self.number_of_aggregated_states = 10
#         self.states_per_block = math.floor(
#             self.number_of_states / self.number_of_aggregated_states
#         )
#         self.starting_state = math.floor(self.number_of_states / 2)
#         self.current_state = self.starting_state
#         self.current_block = math.floor(
#             self.current_state / self.states_per_block
#         )
        
#         # State space set up.
#         self.state_space = {}
#         for state in range(self.number_of_states):
#             # State properties.
#             self.state_space[state] = {
#                 "actions": [],
#                 "estimated return": 0,
#                 "state entries": 0,
#                 "reward": 0,
#             }
            
#             # State actions.
#             for action in ACTIONS.as_tuple():
#                 self.state_space[state]["actions"].append(action)
                
#         # Terminal states.
#         self.terminal_states = [0, self.number_of_states - 1]
        
#         # Terminal states rewards.
#         self.state_space[0]["reward"] = -1
#         self.state_space[self.number_of_states - 1]["reward"] = 1
        
#     def set_current_block(self) -> None:
#         """Update the current block that the agent is in."""
#         self.current_block = math.floor(
#             self.current_block / self.states_per_block
#         )
        
#     def set_state_return(self, state: int, value: int | float) -> None:
#         """Set the expected return for a state."""
        
#         self.state_space[state]["estimated return"] = value
        
#     def get_terminal_states(self) -> list[int]:
#         """Return the terminal states of the state space."""
        
#         return self.terminal_states
    
#     def get_state_space(self) -> dict[int, dict]:
#         """Return the state space."""
        
#         return self.state_space
    
#     def get_possible_actions(self, state: int) -> list[ACTIONS]:
#         """Return a list of the actions possible from the given state."""
        
#         return self.state_space[state]["actions"]
    
#     def get_next_states(self, state: int, action: ACTIONS) -> list[int]:
#         """
#         Return the next states from the from the current state by following
#         the given action.
        
#         This returns a list for some future proofing (trying to get some best
#         practises in). There is a chance for multiple states from a single
#         action.
#         """

#         match action:
#             # Left action.
#             case ACTIONS.LEFT:
#                 return [state - 1]
#             case ACTIONS.RIGHT:
#                 return [state + 1]
            
#     def get_state_transition_probability(self, state: int,
#                                          action: ACTIONS,
#                                          next_state: int) -> float | int:
#         """Return the probability of transitioning from a given state to another
#         state with a given action."""
        
#         return 1
    
#     def get_state_reward(self, state: int) -> int | float:
#         """Return the reward for the given state."""
        
#         return self.state_space[state]["reward"]
    
#     def get_state_return(self, state: int) -> int | float:
#         """Return the expected return for the given state."""
        
#         return self.state_space[state]["estimated return"]