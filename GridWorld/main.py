from typing import Tuple

from Agent.Agent import Agent

from GridWorld.StateSpace import GridWorldStateSpace
from GridWorld.Action import GridWorldAction

from GridWorld.GridWorldEnvironment import GridWorldEnvironment

from GridWorld.Policy import GridWorldEquiprobablePolicy

def main():
    
    number_of_rows: int = 4
    number_of_columns: int = 4
    
    # Agent Dependencies.
    
    state_space: GridWorldStateSpace = GridWorldStateSpace(
        number_of_rows,
        number_of_columns
    )
    
    environment: GridWorldEnvironment = GridWorldEnvironment(state_space)
    
    policy: GridWorldEquiprobablePolicy[Tuple[int, int], GridWorldAction] = GridWorldEquiprobablePolicy(state_space)
    
    agent: Agent[Tuple[int, int], GridWorldAction] = Agent(
        environment,
        state_space,
        policy
    )
    
    agent.evaluate_policy()
    
    

if __name__ == "__main__":
    main()