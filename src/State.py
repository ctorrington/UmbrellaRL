"""
State Type.

State representation for a reinforcement learning environment.
"""

from typing import List

from src.Action import Action

class State[T: Action]:
    """
    States representation for a reinforcement learning environment.
    
    This class can be inhertited from to define more State member fields.
    
    Object defing fields for States.
    
    Injected into State Space.
    """
    
    def __init__(self):
        self.actions: List[T] = []
        self.estimated_return: float = 0.0
        self.counter: int = 0
        self.reward: float = 0
        self.is_current: bool = False
        self.is_terminal: bool = False
