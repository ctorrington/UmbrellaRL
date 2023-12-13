"""Graphing class for UmbrellaRL package."""

import matplotlib as mlp

from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.Agent import Agent

class Graphing[StateIndex, A: Action]():
    """Graphing class for UmbrellaRL package."""
    
    def __init__(self,
                 agent: Agent[StateIndex, A]
                ) -> None:
        
        # Dependencies.
        self.agent = agent

    # TODO overarching method that prints some dashboard with lots of lots.
