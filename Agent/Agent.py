"""RL Agent."""

# Dependencies.
from ActionProbabilityDistribution import ActionProbabilityDistribution
from StateSpace import StateSpace
from Environment.Environment import Environment
from Policy.BasePolicy import BasePolicy
from constants import Constants

ACTIONS = Constants.ACTIONS

class Agent:
    """RL Agent."""
    
    def __init__(self, environment: Environment,
                 state_space: StateSpace,
                 policy: BasePolicy,
                 action_probability_distribution: ActionProbabilityDistribution):
        
        self.theta: float = 0.01
        
        # Dependencies. 
        self.environment: Environment = environment
        
        self.state_space: StateSpace = state_space
        
        self.action_probability_distribution: ActionProbabilityDistribution = action_probability_distribution
        
        self.policy: BasePolicy = policy
    
    def learn(self):
        self.evaluate_policy()
        
    def evaluate_policy(self) -> None:
        """
        Evaluate the policy.
        
        Determine the state-value function for the policy.
        """
        
        while True:
            delta = 0
            
            for state in self.state_space:
                
                current_state_value: float = self.state_space[state].estimated_return
                
                updated_state_value: float = self.calculate_state_value()
                
    def calcualte_state_value(self) -> float:
        """
        Calcualte the value of the given state following the given policy
        in the given environment.
        """
        
        for action in ACTIONS.as_tuple():
            
            action_probability: float = self.policy
