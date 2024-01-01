"""
Graphing module for UmbrellaRL ☂️
"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import numpy.typing as npt
from numpy import float64

from typing import List, Dict

from Graphing.abstract_graphing import Graphing
from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.Agent import Agent
from src.StateSpace import StateSpace
from src.StateSpace import StateSpace
from src.StateProbabilityDistribution import StateProbabilityDistribution
from src.Agent.History import History

class Graphing[SI: StateIndex, A: Action](Graphing):

    def __init__(
        self,
        agent: Agent[SI, A]
    ) -> None:

        self.agent: Agent[SI, A] = agent

        self.history: History[SI, A] = self.agent.history

        self.history_iteration: int = 0
        
    def plot_graph(
        self,
        graph: str
    ) -> None:
        
        match graph:
            
            case "state value function":
                
                self.plot_state_value_function()
                
            case "rewards":
                
                self.plot_rewards()
                
            case _:
                
                raise AttributeError(f"Attribute of type {graph} is not supported.")
