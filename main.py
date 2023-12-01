from Agent.Agent import Agent
from Environment.Environment import Environment
from StateIndex import StateIndex
from StateSpace import StateSpace
from State import State
from Action import Action

index_type = int

# Grid World Actions.
class GridWorldActions(Action):
    UP = "up"
    DOWN = "down"
    Left = "left"
    RIGHT = "right"
    
actions = GridWorldActions

state_space = StateSpace[index_type]()

# State Space setup.
for i in range(16):
    # Grid World States.
    state_space[i] = State()
    
    # Grid World Actions.
    state_space[i].actions = actions.members()

# Grid World Terminal States
state_space[0].is_terminal = True
state_space[15].is_terminal = True
state_space[0].reward = 1
state_space[15].reward = 1

environment = Environment[index_type]()

# Environment setup.
for state in state_space:
    # Environment States.
    environment[state] = {}
    
    # State Actions.
    for action in state_space[state].actions:
        pass
        
        
    




print(actions)
print(state_space)
