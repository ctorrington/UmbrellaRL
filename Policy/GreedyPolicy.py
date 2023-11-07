"""Policy class used for action selection for a reinforcement learning agent."""

from ActionProbabilityDistribution import ActionProbabilityDistribution
from Policy.BasePolicy import ACTIONS, BasePolicy

class GreedyPolicy(BasePolicy):
    """Greedy policy, will always select action with the highest value."""
    
    def __init__(self, ):
        pass
    
    def choose_action(self, state: int) -> ACTIONS:
        """Choose an action for the given state."""
        
        return max(self[state], key = lambda action: self[state][action])
    
    def get_action_probability_distribution(self, state: int) -> ActionProbabilityDistribution:
        """Return the action probability distribution for the given state."""
        
        return self[state]
    