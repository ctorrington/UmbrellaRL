# Gradient-MC-1000-State-Random-Walk

## Structure

- ### Policy

The policy object determines the actions taken by the agent.
The policy object must inherit from the Base Policy class.

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
