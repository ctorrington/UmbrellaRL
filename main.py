from Agent.Agent import Agent
from Environment.Environment import Environment
from StateIndex import StateIndex
from StateSpace import StateSpace
from State import State
from Action import Action

index_type = StateIndex[int]

state_space = StateSpace[index_type]()

class Actions(Action):
    UP = "up"
    DOWN = "down"
    Left = "left"
    RIGHT = "right"

# Grid World State Space init.
for i in range(16):
    state_space[i] = State()
    
    # State Actions.
    for action in A
    
# Terminal States.
state_space[0].is_terminal = True
state_space[-1].is_terminal = True
state_space[0].reward = 1
state_space[-1].reward = 1

print(state_space)