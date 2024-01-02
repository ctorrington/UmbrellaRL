# UmbrellaRL ☂️ GridWorld Module

The Grid World problem is often used to explain reinforcement learning concepts.
It allows for an intuitive 2D environment that can easily be graphed.

This Grid World Specifically uses a four by four grid, with a starting index of zero at the top left & one terminal index of fifteen at the bottom right. Each section on the grid represents an independent state, with the entire four by four grid representing the state space. Each state can perform four actions: up, down, left & right. The actions are fairly intuitive with up actions moving the agent to the state above, left actions moving the agent to the state to its left & so on. Actions that have no immediate next state, for example a state on the top row of the grid does not have another state above it, will result in the agent remaining in its current state. This scenario can be described as an undiscounted episodic task. The agent uses an equiprobable random policy that it later improves.
