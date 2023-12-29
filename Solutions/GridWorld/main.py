from typing import Tuple

from src.Agent.Agent import Agent

from Solutions.GridWorld.StateSpace import GridWorldStateSpace
from Solutions.GridWorld.Action import GridWorldAction
from Solutions.GridWorld.GridWorldEnvironment import GridWorldEnvironment
from Solutions.GridWorld.Policy import GridWorldEquiprobablePolicy

from Graphing.graphing import Graphing

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
        policy
    )
    
    agent.evaluate_policy()
    agent.improve_policy()
    
    for state in state_space:
        print(f"{state} value: {state_space[state].estimated_return}. Policy: {policy.get_action_probability_distribution(state)}")
    
    graph = Graphing(agent)
    
    # graph.plot_state_value_function(True, True)
    graph.plot_history(agent.history)

if __name__ == "__main__":
    main()
