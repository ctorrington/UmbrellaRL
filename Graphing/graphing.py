"""Graphing class for UmbrellaRL package."""

import matplotlib.pyplot as plt
from typing import List

from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.Agent import Agent
from src.StateSpace import StateSpace

class Graphing[StateIndex, A: Action]():
    """Graphing class for UmbrellaRL package."""
    
   # TODO overarching method that prints some dashboard with lots of lots.
    
    def __init__(self,
                 agent: Agent[StateIndex, A]
                ) -> None:
        
        # Dependencies.
        self.agent = agent
        
    def plot_state_value_function(self):
        """Plot the State Value Function of the State Space."""
        
        state_space: StateSpace[StateIndex, A] = self.agent.environment.get_state_space()
        
    def get_z_axis_data(self,
                        # TODO data for z-axis supports more types.
                        state_space: StateSpace[StateIndex, A],
                       ) -> List[float]:
        # TODO data for z-axis supports more types.
        # TODO variable attribute retrieved from data.
        """
        Return the z-axis from the given data collection to be displayed by 
        a graph.
        """
        
        z_axis_data: List[float] = []
        
        for state in state_space:
            z_axis_data.append(state_space[state].estimated_return)
            
        return z_axis_data
