"""
Graphing module for UmbrellaRL ☂️
"""

import logging

import matplotlib.pyplot as plt

from graphing.abstract_graphing import IGraphing

from core.dependency.state_index import StateIndex
from core.dependency.action import Action
from core.dependency.state import State
from core.Agent.Agent import Agent
from core.Agent.History import History
from core.Environment.Environment import Environment

from log.ilogger import ILogger

class Graphing[SI: StateIndex, A: Action](IGraphing):
    def __init__(
        self,
        agent: Agent[SI, A],
        environment: Environment[SI, A],
        logger: ILogger
    ) -> None:
        self.agent: Agent[SI, A] = agent
        self.environment: Environment[SI, A] = environment
        self.history: History[SI, A] = self.agent.history
        self.history_iteration: int = -1
        self.fig, self.axes = plt.subplots()
        self._logger: logging.Logger = (
            logger.get_logger(self.__class__.__name__)
        )

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
            self._logger.info("Plotting State Value Function graph.")
            self.axes[self.history_iteration].imshow(
                self.history[self.history_iteration].get_state_value_function(),
                cmap = "viridis",
                interpolation = "nearest"
            )
            self._logger.info("State Value Function graph plotted successfully.")

    def plot_rewards(
        self
    ) -> None:
        raise NotImplementedError
        # TODO add plotting rewards feature.

    def plot_action_annotations(
        self,
        action_type: str
    ) -> None:
        self._logger.info("Plotting Action annotations.")
        self._logger.debug(f"Action type: {action_type}.")
        # TODO below logic needs to be a method.
        if self.history_iteration == -1:
            state_space = self.agent.environment.get_state_space()
        else:
            state_space = self.agent.history[self.history_iteration]
        for state_index in state_space:
            self._logger.debug(f"Current State Index: {state_index}.")
            state: State[A] = state_space.get_state(state_index)
            # Do not annotate Actions from terminal States.
            if state.is_terminal:
                self._logger.debug(f"State {state_index} is Terminal, continueing. State is_terminal property: {state.is_terminal}.")
                continue
            
            # Get Actions for the State.
            match action_type:
                case "greedy":
                    self._logger.info(f"Getting greedy Actions for State: {state_index}.")
                    actions = self.agent.policy.get_greedy_actions(
                        state_index=state_index,
                        environment=self.environment
                    )
                    self._logger.info(f"Retrieved greedy Actions for State {state_index} successfully.")
                    self._logger.debug(f"State {state_index} greedy Actions: {actions}.")
                case "all":
                    self._logger.info(f"Getting all Actions for State: {state_index}.")
                    actions = state_space[state_index].actions
                    self._logger.info(f"Retrieved all Actions for State {state_index} successfully.")
                    self._logger.debug(f"State {state_index} reedy Actions: {actions}.")
                case _:
                    raise AttributeError(f"Attribute of type {action_type} is not supported.")

            # Plot the Actions as annotations.
            for action in actions:
                self._logger.debug(f"Current action for State {state_index}: {action}.")
                
                # Get the possible next States for the Action from the current State.
                self._logger.info(f"Getting possible next States for State {state_index} following Action {action}.")
                next_states = self.agent.environment.get_next_states(
                    state_index,
                    action
                )
                self._logger.info(f"Retrieved next States for State {state_index} following Action {action} successfully.")
                self._logger.debug(f"Next Actions for State {state_index} follow Action {action}: {next_states}.")
                for next_state_index in next_states:
                    self._logger.debug(f"Current next State: {next_state_index}.")
                    # Don't annotate to the current State.
                    if next_state_index == state_index:
                        self._logger.debug(f"Next State is current State - continueing. Current State Index: {state_index}, next State Index: {next_state_index}.")
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
                    
                    self._logger.debug(f"Annotating Action {action} for State {state_index} to State {next_state_index}.")
                    self._logger.debug(f"xytext argument: {xytext}. xy argument: {xy}.")
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
        