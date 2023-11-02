"""State."""

from constants import Constants

ACTIONS = Constants.ACTIONS

class State:
    """States representation."""
    
    def __init__(self):
        self.actions: list[ACTIONS] = []
        self.estimated_return: float = 0
        self.counter: int = 0
        self.reward: int = 0
        self.is_current: bool = False
        self.is_terminal: bool = False
