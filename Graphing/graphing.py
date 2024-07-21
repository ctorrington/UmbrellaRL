"""
Graphing module for UmbrellaRL ☂️
"""

import matplotlib.pyplot as plt

from Graphing.abstract_graphing import Graphing

from core.dependency.StateIndex import StateIndex
from core.dependency.Action import Action
from core.dependency.State import State
from core.Agent.Agent import Agent
from core.Agent.History import History
from core.Environment.Environment import Environment

class Graphing[SI: StateIndex, A: Action](Graphing):

    def __init__(
        self,
        agent: Agent[SI, A],
        environment: Environment[SI, A]
    ) -> None:

        self.agent: Agent[SI, A] = agent
        self.environment: Environment[SI, A] = environment
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
        
        if self.history_iteration == -1:
            img = self.axes.imshow(
                self.agent.environment.get_state_space().get_state_value_function(),
                cmap = "viridis",
                interpolation = "nearest"
            )
        else:
            self.axes[self.history_iteration].imshow(
                self.history[self.history_iteration].get_state_value_function(),
                cmap = "viridis",
                interpolation = "nearest"
            )
            
    def plot_rewards(
        self
    ) -> None:
        raise NotImplementedError
        # TODO add plotting rewards feature.

    def plot_action_annotations(
        self,
        action_type: str
    ) -> None:
        
        # TODO below logic needs to be a method.
        if self.history_iteration == -1:
            state_space = self.agent.environment.get_state_space()
        else:
            state_space = self.agent.history[self.history_iteration]
        for state_index in state_space:
            state: State[A] = state_space.get_state(state_index)
            # Do not annotate Actions from terminal States.
            if state.is_terminal:
                continue
            
            # Get Actions for the State.
            match action_type:
                case "greedy":
                    actions = self.agent.policy.get_greedy_actions(
                        state_index=state_index,
                        environment=self.environment
                    )
                case "all":
                    actions = state_space[state_index].actions
                case _:
                    raise AttributeError(f"Attribute of type {action_type} is not supported.")

            # Plot the Actions as annotations.
            for action in actions:
                # Get the possible next States for the Action from the current State.
                next_states = self.agent.environment.get_next_states(
                    state_index,
                    action
                )
                # Don't annotate to the current State.
                for next_state_index in next_states:
                    if next_state_index == state_index:
                        continue
                    
                    current_center_y, current_center_x = state_index
                    next_center_y, next_center_x = next_state_index
                    direction_vector = (next_center_x - current_center_x,
                                        next_center_y - current_center_y)
                    scaled_direction = (direction_vector[0] * 0.5,
                                      direction_vector[1] * 0.5)
                    xytext = (current_center_x, current_center_y)
                    xy = (next_center_x - scaled_direction[0],
                          next_center_y - scaled_direction[1])
                    
                    if self.history_iteration == -1:
                        self.axes.annotate(
                            "",
                            xytext = xytext,
                            xy = xy,
                            arrowprops = dict(arrowstyle = "->"),
                            annotation_clip = False
                        )
                    else:
                        self.axes[self.history_iteration].annotate(
                            "",
                            xytext = xytext,
                            xy = xy,
                            arrowprops = dict(arrowstyle = "->"),
                            annotation_clip = False
                        )

    def plot_history(
        self,
        graph: str
    ) -> None:
        if len(self.history) == 1:
            self.plot_graph(
                graph
            )
            return

        self.fig, self.axes = plt.subplots(
            nrows = 1,
            ncols = len(self.history)
        )
        self.history_iteration = -1
        
        for timestep in range(len(self.history)):
            self.history_iteration += 1
            self.plot_graph(graph)
            self.axes[timestep].set_title(f"iteration {timestep}")
            
    def animate_history(self) -> None:
        # TODO future release.
        raise NotImplementedError

    def show_graph(
        self
    ) -> None:
        plt.show()
        