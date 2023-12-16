"""
Graphing class for UmbrellaRL package.

Currently supported graph dimensions:
    - 2D

"""

from typing import List

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from matplotlib.axes import Axes
from matplotlib.image import AxesImage

from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.Agent import Agent
from src.StateSpace import StateSpace

class Graphing[A: Action]():
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
        
        # TODO add check for empty State Space.
        dimensionality: int = self.deterine_graph_dimensionality(next(iter(state_space.keys())))
        
        if dimensionality == 2:
            
            x, y = zip(*state_space.keys())
            
            values = np.zeros((max(x) + 1, max(y) + 1))
            
            for key, v in state_space.items():
                
                if isinstance(key, tuple) and len(key) == 2:
                    
                    i, j = key
                    
                    values[i, j] = v
                    
                else:
                    
                    # TODO proper handle here.
                    print(f"Ignoring invalid key: {key}.")
                    
            ax: Axes = plt.gca()
            
            img: AxesImage = ax.imshow(
                values,
                cmap = 'virdis',
                interpolation = 'nearest',
                origin = 'lower'
            )
            
            plt.colorbar(img)
            
            plt.show()
            
    def deterine_graph_dimensionality(self,
                                      key: StateIndex
                                     ) -> int:
        """Return the dimension required to plot the graph."""
        
        if isinstance(key, tuple):
            
            return len(key)
        
        else:
            
            raise ValueError("Unsupported StateIndex type.")
