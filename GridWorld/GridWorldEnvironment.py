"""Grid World Environment."""

from typing import Tuple, Dict

from Environment.Environment import Environment

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
        
        # Environment structure.
        for state in self.state_space:
            
            # Assign State Actions.
            self[state] = {action: {} for action in GridWorldAction.members()}
            
            for action in self[state]:
                
                # TODO This is going to need function to calculate the probability
                    # of each next State following the Action.
                    # The potential next States are given here, along with their
                    # probabilities - that is what needs to be calculated &
                    # applied to this reference below.
                self[state][action] = self.determine_next_states(state, action)
                
    def determine_next_states(self,
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
        row, column = state
        
        possible_next_states: Dict[Tuple[int, int], float] = {}
        
        match action:
            case GridWorldAction.UP:
                if row > 0:
                    possible_next_states[row - 1, column] = 1
                else:
                    possible_next_states[row, column] = 1
                    
            case GridWorldAction.DOWN:
                if row < self.state_space.number_of_rows - 1:
                    possible_next_states[row + 1, column] = 1
                else:
                    possible_next_states[row, column] = 1
                
            case GridWorldAction.LEFT:
                if column > 0:
                    possible_next_states[row, column - 1] = 1
                else:
                    possible_next_states[row, column] = 1
                
            case GridWorldAction.RIGHT:
                if column < self.state_space.number_of_columns - 1:
                    possible_next_states[row, column + 1] = 1
                else:
                    possible_next_states[row, column] = 1
                    
        return possible_next_states

# TODO
    # (This is the Environment itself (nested dict with nested dict))
    # Loop through Grid Worlds State Space.
    
        # (This is the StateActions dict)
        # For every State, apply its available Actions.
        # Loop through each of those available Actions (StateActions)

            # (This is the StateProbabilityDistribution dict)
            # For every available Action (StateAction), apply the possible next States from that Action.
            # Loop through each possible next State & apply its probability of occuring.