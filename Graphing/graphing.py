"""
Graphing class for UmbrellaRL package.

Currently supported graph dimensions:
    - 2D

"""

import matplotlib.pyplot as plt
import numpy as np

from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.Agent import Agent
from src.StateSpace import StateSpace

class Graphing[SI: StateIndex, A: Action]():
    """Graphing class for UmbrellaRL package."""
    
   # TODO overarching method that prints some dashboard with lots of lots.
   
    def __init__(self,
                 agent: Agent[SI, A]
                ) -> None:
        
        # Dependencies.
        self.agent = agent
        
    def plot_state_value_function(self):
        """Plot the State Value Function of the State Space."""
        
        state_space: StateSpace[SI, A] = self.agent.environment.get_state_space()
        
        # TODO add check for empty State Space.
        dimensionality: int = self.deterine_graph_dimensionality(next(iter(state_space.keys())))
        
        if dimensionality == 2:
            
            x, y = zip(*state_space.keys())
            
            values = np.zeros((max(x) + 1, max(y) + 1))
            
            for state_index, state in state_space.items():
                
                if isinstance(state_index, tuple) and len(state_index) == 2:
                    
                    i, j = state_index
                    
                    values[i, j] = state.estimated_return
                    
                else:
                    
                    # TODO proper handle here.
                    print(f"Ignoring invalid key: {key}.")
                    
            # ax: Axes = plt.gca()
            
            fig, ax = plt.subplots()
            
            img = ax.imshow(
                values,
                cmap = 'viridis',
                interpolation = 'nearest',
                origin = 'lower'
            )
            
            plt.colorbar(img)
            
            plt.show()
            
    def deterine_graph_dimensionality(self,
                                      key: SI
                                     ) -> int:
        """Return the dimension required to plot the graph."""
        
        if isinstance(key, tuple):
            
            return len(key)
        
        else:
            
            raise ValueError("Unsupported StateIndex type.")
