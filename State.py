"""State."""

from Action import Action

from typing import List, TypeVar

T = TypeVar('T', bound = Action)

class State:
    """States representation."""
    
    def __init__(self):
        self.actions: List[T] = []
        self.estimated_return: float = 0
        self.counter: int = 0
        self.reward: int = 0
        self.is_current: bool = False
        self.is_terminal: bool = False
