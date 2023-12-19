"""
Graphing class for UmbrellaRL package.

Currently supported graph dimensions:
    - 2D

"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import numpy as np
import numpy.typing as npt
from numpy import float64

from typing import List, cast, Tuple

from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.Agent import Agent
from src.StateSpace import StateSpace
from src.StateProbabilityDistribution import StateProbabilityDistribution

class Graphing[SI: StateIndex, A: Action]():
    """Graphing class for UmbrellaRL package."""
    
   # TODO Service class.
   
    def __init__(self,
                 agent: Agent[SI, A]
                ) -> None:
        
        # Dependencies.
        self.agent = agent
        
    def plot_state_value_function(self,
                                  plot_action_annotations: bool = True,
                                  plot_greedy_actions: bool = True
                                 ) -> None:
        """Plot the State Value Function of the State Space."""
        
        state_space: StateSpace[SI, A] = self.agent.environment.get_state_space()
        
        # TODO add check for empty State Space.
        dimensionality: int = self.determine_graph_dimensionality(
            next(iter(state_space.keys()))
            )
        
        state_value_function: npt.NDArray[float64] = self.get_state_value_function(
            dimensionality
        )
        
        self.plot_graph(
            state_value_function,
            plot_action_annotations,
            plot_greedy_actions
        )
        
    def plot_graph(self,
                   graph: npt.NDArray[float64],
                   plot_action_annotations: bool,
                   plot_greedy_actions: bool
                  ) -> None:
        """Plot the given graph, along with the given options."""
        
        fig, ax = plt.subplots()    # type: ignore
        
        img = ax.imshow(
            graph,
            cmap = 'viridis',
            interpolation = 'nearest'
        )
        
        if plot_action_annotations:
            
            if plot_greedy_actions:
                
                self.plot_policy_greedy_actions(ax)
            
            else:
                
                self.plot_available_actions(ax)
                
        plt.colorbar(img)   # type: ignore
        
        plt.show()  # type: ignore
            
    # TODO could be done in the StateSpace.
    def get_state_value_function(self,
                                 dimensionality: int
                                ) -> npt.NDArray[float64]:
        """Plot the State Value Function of the State Space."""
        
        state_space: StateSpace[SI, A] = self.agent.environment.get_state_space()
        
        if dimensionality == 2:
            
            x, y = zip(*state_space.keys())
            
            values = np.zeros((max(x) + 1, max(y) + 1))
            
            for state_index, state in state_space.items():
                
                if isinstance(state_index, tuple):
                    
                    # Quieting the type checker.
                    i, j = cast(Tuple[int, ...], state_index)
                    
                    values[i, j] = state.estimated_return
                    
                else:
                    
                    # TODO add a proper handle case.
                    print(f"Ignoring invalid key: {state_index}")
                    
            return values
        
        else:
            
            raise(ValueError(f"Untested dimensionality: {dimensionality}"))
            
    def determine_graph_dimensionality(self,
                                      key: SI
                                     ) -> int:
        """Return the dimension required to plot the graph."""
        
        if isinstance(key, tuple):
            
            # Quieting the type checker.
            return len(cast(Tuple[int, ...], key))
        
        else:
            
            raise ValueError("Unsupported StateIndex type.")
        
    def plot_policy_greedy_actions(self,
                            ax: Axes
                           ) -> None:
        """Plot Actions chosen by the Policy for each State."""
        
        state_space: StateSpace[SI, A] = self.agent.environment.get_state_space()
        
        for state in state_space:
            
            policy_greedy_actions = self.agent.policy.get_greedy_actions(state)
            
            self.plot_action_annotations(
                state,
                policy_greedy_actions,
                ax
            )
            
    def plot_available_actions(self,
                               ax: Axes
                              ) -> None:
        """Plot Actions available to each State."""
        
        state_space: StateSpace[SI, A] = self.agent.environment.get_state_space()
        
        for state in state_space:
            
            available_actions = state_space[state].actions
            
            self.plot_action_annotations(
                state,
                available_actions,
                ax
            )
            
    def plot_action_annotations(self,
                     state: SI,
                     actions: List[A],
                     ax: Axes
                    ) -> None:
        """Plot the provided Actions as annotations on the given axes."""
        
        for action in actions:
            
            next_states: StateProbabilityDistribution[SI] = self.agent.environment.get_next_states(
                state,
                action
            )
            
            for next_state in next_states:
                
                if next_state == state:
                    continue
                
                current_state_index: SI = state
                
                next_state_index: SI = next_state
                
                current_center_y, current_center_x = current_state_index
                
                next_center_y, next_center_x = next_state_index
                
                direction_vector = (next_center_x - current_center_x, 
                                    next_center_y - current_center_y)
                
                scaled_direction = (direction_vector[0] * 0.5,
                                    direction_vector[1] * 0.5)
                
                xytext = (current_center_x, current_center_y)
                
                xy = (next_center_x - scaled_direction[0],
                      next_center_y - scaled_direction[1])
                
                ax.annotate(
                    "",
                    xytext = xytext,
                    xy = xy,
                    arrowprops = dict(arrowstyle = "->"),
                    annotation_clip=False
                )
