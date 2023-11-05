"""
Base Policy class to be inherited by Policy classes used by a reinforcement
learning agent.
"""

from abc import ABC, abstractmethod

class BasePolicy(ABC):
    @abstractmethod
    def choose_action(self):
        """
        Abstracted method to be implemented by Policy subclasses.
        
        The Policy classes will use the ActionProbabilityDistribution class
        for determining actions.
        """
        
        pass
