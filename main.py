"""
The nonterminal states are S = {1, 2,..., 14}. There are four actions possible in each
state, A = {up, down, right, left}, which deterministically cause the corresponding
state transitions, except that actions that would take the agent o↵ the grid in fact leave
the state unchanged. Thus, for instance, p(6, 1|5, right) = 1, p(7, 1|7, right) = 1,
and p(10, r|5, right) = 0 for all r 2 R. This is an undiscounted, episodic task. The
reward is 1 on all transitions until the terminal state is reached. The terminal state is
shaded in the figure (although it is shown in two places, it is formally one state).
The expected reward function is thus r(s, a, s0) = 1 for all states s, s0 and actions a.
Suppose the agent follows the equiprobable random policy (all actions equally likely).
"""

from Agent.Agent import Agent
from Environment.Environment import Environment
from StateIndex import StateIndex
from StateSpace import StateSpace
from State import State
from Action import Action
from StateActions import StateActions

index_type = int

# Grid World Actions.
class GridWorldActions(Action):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    
actions = GridWorldActions

state_space = StateSpace[index_type]()

# State Space setup.
for i in range(16):
    # Grid World States.
    state_space[i] = State()
    
    # Grid World Actions.
    state_space[i].actions = actions.members()

# Grid World Terminal States.
state_space[0].is_terminal = True
state_space[15].is_terminal = True
state_space[0].reward = 1
state_space[15].reward = 1

# State Actions.
state_actions = StateActions[index_type]()


environment = Environment[index_type]()

# Environment setup.
for state in state_space:
    # Environment States.
    # TODO needs State Actions
    
    # State Actions.
    
    
    # State Actions.
    for action in state_space[state].actions:
        pass







print(actions)
print(state_space)
