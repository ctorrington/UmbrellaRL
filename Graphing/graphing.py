"""
Graphing class for UmbrellaRL package.

Currently supported graph dimensions:
    - 2D

"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import numpy.typing as npt
from numpy import float64

from typing import List, Dict

from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.Agent import Agent
from src.StateSpace import StateSpace
from src.StateProbabilityDistribution import StateProbabilityDistribution

class Graphing[SI: StateIndex, A: Action]():
    """Graphing class for UmbrellaRL package."""
   # TODO Remove need for multiple ax variables. just assign it to the class.
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
        
        state_value_function: npt.NDArray[float64] = state_space.get_state_value_function()
        
        fig, ax = plt.subplots(1, 1)
        
        self.plot_graph(
            state_value_function,
            ax,
            plot_action_annotations,
            plot_greedy_actions,
        )
        
        plt.show()
        
    def plot_graph(self,
                   graph: npt.NDArray[float64],
                   ax: Axes,
                   plot_action_annotations: bool | None = None,
                   plot_greedy_actions: bool | None = None,
                   state_space: StateSpace[SI, A] | None = None
                  ) -> None:
        """Plot the given graph, along with the given options."""
        
        # fig, ax = plt.subplots()    # type: ignore
        
        img = ax.imshow(
            graph,
            cmap = 'viridis',
            interpolation = 'nearest'
        )
        
        if plot_action_annotations:
            
            if plot_greedy_actions:
                
                self.plot_policy_greedy_actions(
                    ax,
                    state_space
                )
            
            else:
                
                self.plot_available_actions(ax)
     
        # TODO make all plots share a color bar.   
        # plt.colorbar(img)   # type: ignore
        
    def plot_policy_greedy_actions(self,
                            ax: Axes,
                            state_space: None | StateSpace[SI, A] = None
                           ) -> None:
        """Plot Actions chosen by the Policy for each State."""
        
        if state_space is None:
        
            state_space = self.agent.environment.get_state_space()
        
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
                
    def plot_history(
        self,
        history: Dict[int, StateSpace[SI, A]]
    ) -> None:
        """Plot graphs for each stage of evaluation-improvement process."""
        
        fig, axs = plt.subplots(1, len(history))
        
        if len(history) == 1:
            
            self.plot_graph(
                history[0].get_state_value_function(),
                axs,
                True,
                True
            )
            
        else:
            
            for timestep in history:
                
                self.plot_graph(
                    history[timestep].get_state_value_function(),
                    axs[timestep],
                    True,
                    True,
                    history[timestep]
                )
        
        plt.show()
        
    def animate_history(
        self,
        history: Dict[int, StateSpace[SI, A]]
    ) -> None:
        """Animate the stages of the evaluation-improvement process."""
 
        fig, ax = plt.subplots()
        
        for timestep in history:
            
            ax.clear()
            
            self.plot_graph(
                history[timestep].get_state_value_function(),
                ax,
                True,
                True
            )
            
            ax.set_title(f"frame: {timestep}")
            
            plt.pause(3)
        
        
