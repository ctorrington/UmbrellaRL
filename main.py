"""
The nonterminal states are S = {1, 2,..., 14}.
There are four actions possible in each state, A = {up, down, right, left}, 
    which deterministically cause the corresponding state transitions,
    except that actions that would take the agent off the grid in fact leave the state unchanged.
Thus, for instance, p(6, 1|5, right) = 1, p(7, 1|7, right) = 1,
and p(10, r|5, right) = 0 for all r 2 R. This is an undiscounted, episodic task. The
reward is 1 on all transitions until the terminal state is reached. The terminal state is
shaded in the figure (although it is shown in two places, it is formally one state).
The expected reward function is thus r(s, a, s0) = 1 for all states s, s0 and actions a.
Suppose the agent follows the equiprobable random policy (all actions equally likely).
"""

from typing import Tuple

from Agent.Agent import Agent
from Environment.Environment import Environment
from StateIndex import StateIndex
from StateSpace import StateSpace
from State import State
from Action import Action
from StateActions import StateActions

# Using an tuple to reprsent rows & columns.
index_type = Tuple[int, int]

# Grid World Actions.
class GridWorldActions(Action):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class GridWorldEnvironment(Environment[index_type]):
    def __init__(self, row: int, columns: int):
        
        



print(actions)
print(state_space)
