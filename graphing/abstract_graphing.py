"""
Abstract base class for UmbrellaRL's graphing module.
"""

from abc import ABC, abstractmethod

class IGraphing(ABC):
    
    @abstractmethod
    def plot_graph(
        self,
        graph: str
    ) -> None:
        """Specify which graph to plot."""
        
        pass

    @abstractmethod
    def plot_state_value_function(
        self
    ) -> None:
        """Plot State Value Function on the graphing Axes from the history iteration location."""
        
        pass
    
    @abstractmethod
    def plot_rewards(
        self
    ) -> None:
        
        pass
    
    @abstractmethod
    def plot_action_annotations(
        self,
        action_type: str
    ) -> None:
        
        pass

    @abstractmethod
    def animate_history(
        self
    ) -> None:
        
        pass
    
    @abstractmethod
    def plot_history(
        self,
        graph: str
    ) -> None:
        
        pass
    
    @abstractmethod
    def show_graph(
        self
    ) -> None:
        
        pass
