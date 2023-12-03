"""Grid World Environment."""

from typing import Tuple

from Environment.Environment import Environment

from GridWorld.StateSpace import GridWorldStateSpace

# TODO class to reprsent the Tuple[int, int] type.
class GridWorldEnvironment(Environment[Tuple[int, int]]):
    def __init__(self,
                 state_space: GridWorldStateSpace,
                 ) -> None:
        
        # Dependencies.
        self.state_space: GridWorldStateSpace = state_space
        

# TODO
    # (This is the Environment itself (nested dict with nested dict))
    # Loop through Grid Worlds State Space.
    
        # (This is the StateActions dict)
        # For every State, apply its available Actions.
        # Loop through each of those available Actions (StateActions)

            # (This is the StateProbabilityDistribution dict)
            # For every available Action (StateAction), apply the possible next States from that Action.
            # Loop through each possible next State & apply its probability of occuring.