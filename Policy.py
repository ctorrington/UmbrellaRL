"""
Policy class used for managing action selection for a reinforcement
learning agent.
"""

from ActionProbabilityDistribution import ActionProbabilityDistribution

class Policy:
    def __init__(self, action_probability_distribution: ActionProbabilityDistribution):
        self.action_probability_distribution = action_probability_distribution
        