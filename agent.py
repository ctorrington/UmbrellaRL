"""RL Agent to interact with a given environment."""

from environment import Environment
from constants import Constants

ACTIONS = Constants.ACTIONS

class Agent:
    """RL Agent."""
    
    def __init__(self) -> None:
        self.environment = Environment
        self.policy = "random"
        self.gamma = 0.9
        self.theta = 0.001
        self.history: list[Environment] = []