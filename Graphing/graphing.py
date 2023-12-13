"""Graphing class for UmbrellaRL package."""

import matplotlib.pyplot as plt
from typing import List, Tuple

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
        
        z_axis_data: List[float] = self.get_z_axis_data(state_space)
        
        fig, ax = plt.subplots()
        
        ax.imshow(z_axis_data)
        
        plt.show()
        
    def get_z_axis_data(self,
                        state_space: StateSpace[StateIndex, A],
                       ) -> List[float]:
        # TODO data for z-axis supports more types.
        # TODO variable attribute retrieved from data.
        # TODO I am not sure how to make this applicable to any type or range of State Spaces.
        """
        Return the z-axis from the given data collection to be displayed by 
        a graph.
        """
        
        (x_range, y_range) = self.agent.environment.get_state_space().get_dimensions()
        
        z_axis_data: List[float] = []
        
        for state in state_space:
            z_axis_data.append(state_space[state].estimated_return)
            
        return z_axis_data
