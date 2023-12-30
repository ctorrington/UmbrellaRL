"""
Agent History Class.

Currently trackable metrics:
    - Actions
"""

from typing import Dict, List

from src.Action import Action

class History[A: Action](Dict[int, Dict[str, List[A]]]):
    """
    Agent History class for recording the history of the Environment & 
    State Value Function during Action interactions.
    """
    
    def __init__(self) -> None:
        
        self.count = 0
        
        self[0] = {}
        
    def track_actions(
        self,
        actions: List[A]
    ) -> None:
        """Record the given actions."""
        
        self[self.count]["actions"] = actions
