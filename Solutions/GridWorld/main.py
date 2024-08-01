from typing import List

from core.Agent.Agent import Agent

from Solutions.GridWorld.StateSpace import GridWorldStateSpace
from Solutions.GridWorld.Action import GridWorldAction
from Solutions.GridWorld.GridWorldEnvironment import GridWorldEnvironment
from Solutions.GridWorld.Policy import GridWorldEquiprobablePolicy
from Solutions.GridWorld.StateIndex import GridWorldStateIndex

from graphing.graphing import Graphing

from log.logger_manager import LoggerManager

def main():
    logger_manager: LoggerManager = LoggerManager()
    number_of_rows: int = 4
    number_of_columns: int = 4
    state_actions: List[GridWorldAction] = GridWorldAction.members()
    state_estimated_return: float = 0
    state_reward: float = -1
    terminal_state_reward: float = 0
    state_space: GridWorldStateSpace = GridWorldStateSpace(
        number_of_rows=number_of_rows,
        number_of_columns=number_of_columns,
        state_actions=state_actions,
        state_estimated_return=state_estimated_return,
        state_reward=state_reward,
        # terminal_states=[
        #     (number_of_rows - 1, number_of_columns - 1)
        # ]
        terminal_states=[
            (0, 0),
            (number_of_rows - 1, number_of_columns - 1),
            (1, 2),
            (2, 1),
            (2, 0)
        ],
        terminal_state_reward=terminal_state_reward,
        logger=logger_manager
    )
    environment: GridWorldEnvironment = GridWorldEnvironment(state_space)
    policy: GridWorldEquiprobablePolicy[GridWorldStateIndex, GridWorldAction] = (
        GridWorldEquiprobablePolicy(
            state_space=state_space,
            logger=logger_manager
        )
    )
    agent: Agent[GridWorldStateIndex, GridWorldAction] = Agent(
        environment=environment,
        policy=policy,
        logger=logger_manager,
        theta=0.001,
        gamma=0.9
    )
    # agent.evaluate_policy()
    # agent.evaluate_policy_synchronous()
    # agent.improve_policy()
    agent.iterate_policy(evaluation_synchronous=True)

    # for state_index in state_space:
    #     print(f"State ({state_index})")
    #     print(f"Value: {state_space[state_index].estimated_return}")
    #     for action in policy.get_action_probability_distribution(state_index):
    #         print(f"    {action.value}: {policy.get_action_probability_distribution(state_index)[action]}")                


    graph = Graphing(
        agent=agent,
        environment=environment,
        logger=logger_manager
    )
    graph.plot_graph("state value function")
    # graph.plot_history("state value function")
    graph.plot_action_annotations("greedy")
    graph.show_graph()

if __name__ == "__main__":
    main()
