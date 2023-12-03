"""Grid World Environment."""

from typing import Tuple

from Environment.Environment import Environment

from GridWorld.StateSpace import GridWorldStateSpace
from GridWorld.Action import GridWorldAction

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
                self[state][action] = 
                
                
        

# TODO
    # (This is the Environment itself (nested dict with nested dict))
    # Loop through Grid Worlds State Space.
    
        # (This is the StateActions dict)
        # For every State, apply its available Actions.
        # Loop through each of those available Actions (StateActions)

            # (This is the StateProbabilityDistribution dict)
            # For every available Action (StateAction), apply the possible next States from that Action.
            # Loop through each possible next State & apply its probability of occuring.