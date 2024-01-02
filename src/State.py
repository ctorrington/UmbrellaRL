"""
State Type.

State representation for a reinforcement learning environment.
"""

from typing import List

from src.Action import Action

class State[A: Action]:
    """
    States representation for a reinforcement learning environment.

    Inherit from this class to define additional State member fields.
    """

    def __init__(self):
        self.actions: List[A] = []
        self.estimated_return: float = 0.0
        self.counter: int = 0
        self.reward: float = 0
        self.is_current: bool = False
        self.is_terminal: bool = False
