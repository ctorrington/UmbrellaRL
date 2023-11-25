"""Grid World Environment Transitions.

Dictionary representing the next states following an action in a state."""

class GridWorldEnvironmentTransitions(dict[int, dict[int, float]]):
    """
    Mapping data structure for the probabilities for getting from one state
    to another.
    
    0    1   2   3
    4    5   6   7
    8    9  10  11
    12  13  14  15
    
    """
    
    def __init__(self,
                 number_of_states:int
                ) -> None:
        
        
