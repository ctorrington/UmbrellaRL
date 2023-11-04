"""RL Agent."""

from ActionProbability import ActionProbability
from StateSpace import StateSpace
from State import State
from Environment.Environment import Environment

class Agent:
    """RL Agent."""
    
    def __init__(self, environment: Environment):
        number_of_states = 1000
        state_rewards = {0: -1, number_of_states - 1: 1}
        
        self.environment = environment
        
        self.state_space: StateSpace = StateSpace(
            number_of_states,
            state_rewards,
            state_class = State
        )
        self.action_probability: ActionProbability = ActionProbability(
            self.state_space
        )
    
    def learn(self):
        self.interact_with_environment()
        
    def interact_with_environment(self) -> None:
        self.evaluate_policy()
        
    def evaluate_policy(self) -> None:
        pass
