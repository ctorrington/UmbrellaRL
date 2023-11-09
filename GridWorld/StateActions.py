"""
Grid World Actions for each State.

Mapping from each State to each action available to them.
"""

from typing import Dict, List

from Action import Action

class GridWorldStateActions(Dict[int, List[Action]]):
    """Dictionary object representing the Actions available to each State."""
    
    def __init__(self,
                 number_of_actions: int
                ):
        for state in range(number_of_actions):
            self[state] = Action.members()
