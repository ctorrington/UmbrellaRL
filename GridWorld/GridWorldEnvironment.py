"""Grid World Environment."""

from typing import Tuple, Dict
from collections import defaultdict

from Environment.Environment import Environment
from StateActions import StateActions
from StateProbabilityDistribution import StateProbabilityDistribution

from GridWorld.StateSpace import GridWorldStateSpace
from GridWorld.Action import GridWorldAction


# Grid World State Space representation.

# 00 01 02 03
# 04 05 06 07
# 08 09 10 11
# 12 13 14 15

# TODO class to reprsent the Tuple[int, int] type.
class GridWorldEnvironment(Environment[Tuple[int, int]]):
    def __init__(self,
                 state_space: GridWorldStateSpace,
                 ) -> None:

        # Dependencies.
        self.state_space: GridWorldStateSpace = state_space
        
        self.initialize_environment()
        
    def initialize_environment(self) -> None:
        for state in self.state_space:
            state_actions: StateActions[Tuple[int, int]] = self.determine_state_actions(state)
            self[state] = state_actions
            
    def determine_state_actions(self,
                                state: Tuple[int, int]) -> StateActions[Tuple[int, int]]:
        """Determine the Actions available for each State."""
        
        # TODO Figure out defaultdict for this.
        state_actions: StateActions[Tuple[int, int]] = {}
        
        for action in self.state_space[state].actions:
            
            possible_next_states_distribution: Dict[Tuple[int, int], float] = self.determine_next_state_probability_distribution(state, action)
            
            state_actions[action].update(possible_next_states_distribution)
            
        return state_actions
            
            
            
    def determine_next_state_probability_distribution(self,
                                                      state: Tuple[int, int],
                                                      action: GridWorldAction
                                                     ) -> Dict[Tuple[int, int], float]:
        """
        Return a mapping of the possible next States & their probability of
        occuring.
        
        In this Grid World, Actions are deterministic.
        Up will only go up (if possible).
        
        If an Action would take the Agent off the State Space, then the next 
        state is the State the Agent is currently in.
        """
        
        # TODO error checking State is correct type for Grid World problem.
        # TODO service class.
        row, column = state
        
        # TODO defaultdict.
        possible_next_states: Dict[Tuple[int, int], float] = {}
        
        match action:
            case GridWorldAction.UP:
                if row > 0:
                    possible_next_states[row - 1, column] = 1.0
                else:
                    possible_next_states[row, column] = 1.0
                    
            case GridWorldAction.DOWN:
                if row < self.state_space.number_of_rows - 1:
                    possible_next_states[row + 1, column] = 1.0
                else:
                    possible_next_states[row, column] = 1.0
                
            case GridWorldAction.LEFT:
                if column > 0:
                    possible_next_states[row, column - 1] = 1.0
                else:
                    possible_next_states[row, column] = 1.0
                
            case GridWorldAction.RIGHT:
                if column < self.state_space.number_of_columns - 1:
                    possible_next_states[row, column + 1] = 1.0
                else:
                    possible_next_states[row, column] = 1.0
                    
        return possible_next_states
