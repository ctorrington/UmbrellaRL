"""RL Agent."""

# Dependencies.
from ActionProbabilityDistribution import ActionProbabilityDistribution
from StateSpace import StateSpace
from Environment.Environment import Environment
from Policy.BasePolicy import BasePolicy

class Agent:
    """RL Agent."""
    
    def __init__(self, environment: Environment,
                 state_space: StateSpace,
                 policy: BasePolicy,
                 action_probability_distribution: ActionProbabilityDistribution):
        
        # Dependencies. 
        self.environment: Environment = environment
        
        self.state_space: StateSpace = state_space
        
        self.action_probability_distribution: ActionProbabilityDistribution = action_probability_distribution
        
        self.policy: BasePolicy = policy
    
    def learn(self):
        self.interact_with_environment()
        
    def interact_with_environment(self) -> None:
        self.evaluate_policy()
        
    def evaluate_policy(self) -> None:
        pass
