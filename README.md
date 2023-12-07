# UmbrellaRL

## This package is nowhere near complete.

## Structure

- ### Agent

The Agent represents the logic for reinforcement learning.
It contains functions for policy evaluation & calculating a State's value.

- ### Policy

The Policy object determines the actions taken by the agent.
The Policy object must inherit from the Base Policy class.

- ### Environment

The Environment represents the State that the Agent is in. It describes which
states are accessible following actions & what their probabilities are.

The Environment depends on the State Space.

- #### State Space

The State Space describes the states that the agent can be in.
Each State is of type State.

The State Space depends on the State.

- ##### State

The State represents a singular State that the agent can be in.
The State contains the information that describes each State.
