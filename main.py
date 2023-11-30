from Agent.Agent import Agent
from Environment.Environment import Environment
from StateIndex import StateIndex
from StateSpace import StateSpace
from State import State
from Action import Action

index_type = StateIndex[int]

# Grid World Actions.
class GridWorldActions(Action):
    UP = "up"
    DOWN = "down"
    Left = "left"
    RIGHT = "right"
    
actions = GridWorldActions

# Grid World State Space init.
class GridWorldStateSpace(StateSpace[index_type]):
    def __init__(self):
        for i in range(16):
            # Grid World States.
            self[i] = State()
            
            # Grid World Actions.
            self[i].actions = actions.members()


state_space = GridWorldStateSpace()

# Grid World Terminal States
state_space[0].is_terminal = True
state_space[-1].is_terminal = True
state_space[0].reward = 1
state_space[-1].reward = 1




print(actions)
print(state_space)
