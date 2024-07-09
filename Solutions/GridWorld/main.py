from core.Agent.Agent import Agent

from Solutions.GridWorld.StateSpace import GridWorldStateSpace
from Solutions.GridWorld.Action import GridWorldAction
from Solutions.GridWorld.GridWorldEnvironment import GridWorldEnvironment
from Solutions.GridWorld.Policy import GridWorldEquiprobablePolicy
from Solutions.GridWorld.StateIndex import GridWorldStateIndex

from Graphing.graphing import Graphing

def main():

    number_of_rows: int = 3
    number_of_columns: int = 10
    state_space: GridWorldStateSpace = GridWorldStateSpace(
        number_of_rows,
        number_of_columns,
        [(0, 0), (2, 5)]
    )
    environment: GridWorldEnvironment = GridWorldEnvironment(state_space)
    policy: GridWorldEquiprobablePolicy[GridWorldStateIndex, GridWorldAction] = GridWorldEquiprobablePolicy(state_space)
    agent: Agent[GridWorldStateIndex, GridWorldAction] = Agent(
        environment,
        policy
    )
    agent.evaluate_policy()
    agent.improve_policy()
    
    for state in state_space:

        print(f"{state} value: {state_space[state].estimated_return}. Policy: {policy.get_action_probability_distribution(state)}")

    graph = Graphing(agent)
    graph.plot_graph("state value function")
    # graph.plot_history("state value function")
    graph.plot_action_annotations("greedy")
    graph.show_graph()

if __name__ == "__main__":
    main()
