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
    
    def __init__(self,
                 environment: Environment,
                 state_space: StateSpace,
                 policy: BasePolicy,
                ):
        
        self.theta: float = 0.01
        self.gamma: float = 0.9999
        
        # Dependencies. 
        self.environment: Environment = environment
        
        self.state_space: StateSpace = state_space
        
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
                
                old_state_value: float = self.state_space[state].estimated_return
                
                updated_state_value: float = self.calculate_state_value(state)
                
                self.assign_new_state_estimated_return(state, updated_state_value)
                
                delta = max(delta, (abs(old_state_value - updated_state_value)))
                
            if delta < self.theta:
                break
                
    def calculate_state_value(self,
                              state: int
                             ) -> float:
        """
        Calcualte the value of the given state following the given policy
        in the given environment.
        """
        
        new_state_value: float = 0
        
        state_action_probability_distribution: ActionProbabilityDistribution = self.policy.get_action_probability_distribution(state)
        
        for action in state_action_probability_distribution:
            
            action_probability: float = state_action_probability_distribution[action]
            
            next_states: list[int] = self.environment.get_next_states(
                state,
                action
            )
            
            for next_state in next_states:
                
                next_state_probability = self.environment.get_state_transition_probability(
                    state,
                    action,
                    next_state
                )
                
                next_state_reward = self.state_space[next_state].reward
                
                next_state_value: float = self.state_space[next_state].estimated_return
                
                new_state_value += action_probability * next_state_probability * (next_state_reward + (self.gamma * next_state_value))
                
        return new_state_value
    
    def assign_new_state_estimated_return(self,
                               state: int,
                               value: float
                              ) -> None:
        """Assign the new estimated return (value) to the given state."""
        
        self.state_space[state].estimated_return = value
