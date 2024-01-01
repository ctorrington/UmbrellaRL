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

        self.history_iteration: int = -1

        self.fig, self.axes = plt.subplots()

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

    def plot_state_value_function(
        self
    ) -> None:
        
        if self.history == -1:
            
            img = plt.imshow(
                self.agent.environment.get_state_space().get_state_value_function(),
                cmap = "viridis",
                interpolation = "nearest"
            )
            
        else:
            
            img = plt.show(
                self.history[self.history_iteration].get_state_value_function(),
                cmap = "viridis",
                interpolation = "nearest"
            )
            
    def plot_rewards(
        self
    ) -> None:
        
        # TODO add plotting rewards feature.
        
        pass
    
    def plot_actions(
        self,
        actions: str
    ) -> None:
        
        match actions:
            
            case "greedy":
                
                self.plot_greedy_actions()
                
            case "all":
                
                self.plot_all_actions()
                
            case _:
                
                raise AttributeError(f"Attribute of type {actions} is not supported.")
