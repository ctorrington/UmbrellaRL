# Graphing module for UmbrellaRL ☂️

## This module enables visualising individual or all aspects of UmbrellaRL's agent interactions.

### This module is not required.

### Currently implemented & planned features can be found on UmbrellaRL's [project board](https://github.com/users/ctorrington/projects/3).

## Usage

### UmbrellaRL's ☂ graphing module's features are accessed through its object's methods. The details for these methods can be found below.

#### plot graph

This method takes a string as a parameter, specifying which graph to plot.
This method will only plot the most current version of the specified graph.

#### plot state value function

This method plots the latest version of the agent's state value function.
This method is equivalent to passing 'state value function' to the plot graph method.

#### plot action annotations

This method takes an action type as a string as a parameter, specifying which actions to plot.
This method plots arrow annotations onto the graph that has been plotted onto by the plot graph method.

Currently this method will only plot annotations for the latest iteration of the state space, not for the entire history (this will be added in a later release).

#### plot history

This method plots the history tracked by the agent as it interacts with the environment.
This methood will plot seperate graphs for each iteration of the environment experienced by the agent.

This method is useful for observing comparisons between agent-environment interactions.
