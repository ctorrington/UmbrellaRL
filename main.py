"""
All episodes begin in the center.
Move either left or right by one state, all with equal probability.
(in the project, states are aggregated,
 so there are 100 states to the left & 100 states to the right.)
In the case that the state is near an edge,
 then the probability of that would have gone into the missing neighbours
 goes into the probability of terminating on that side.
(thus, state 1 has a 0.5 chance of terminating on the left,
 & state 950 has a 0.25 chance of terminating on the right)

Termination on the left produces a reward of -1.
Termination on the right produces a reward of +1.
All other transitions have a reward of 0.
"""

from Agent.Agent import Agent
from Environment.Environment import Environment
from Services.EnvironmentService import EnvironmentService
from StateSpace import StateSpace
from State import State
from Policy.EquiprobablePolicy import EquiprobablePolicy

def main() -> None:
    
    number_of_states: int = 10
    number_of_aggregated_states: int = 100
    terminal_states_rewards: dict[int, int] = {0: -1, number_of_states - 1: 1}
    
    state_space: StateSpace = StateSpace(
        number_of_states,
        terminal_states_rewards,
        state_class = State
        )
    
    environment_service: EnvironmentService = EnvironmentService(
        state_space
        )
    
    environment: Environment = Environment(
        number_of_aggregated_states,
        state_space,
        environment_service
        )
    
    policy: EquiprobablePolicy = EquiprobablePolicy(
        state_space,
        )
    
    agent = Agent(
        environment,
        state_space,
        policy
        )
    agent.learn()
    
if __name__ == "__main__":
    main()
