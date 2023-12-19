"""Bellman Equation service class."""

from src.StateIndex import StateIndex
from src.Action import Action
from src.StateSpace import StateSpace
from src.Environment.Environment import Environment
from src.StateProbabilityDistribution import StateProbabilityDistribution

class BellmanEquation[SI: StateIndex, A: Action]():
    """Bellman Equation service class."""
    
    @classmethod
    def calculate_state_value(cls,
                              state: SI
                             ) -> float:
        """Calculate the state value """
        
        state_value: float = 0
        
    @classmethod
    def calculate_update_value(cls,
                               state: SI,
                               action: A,
                               state_space: StateSpace[SI, A],
                               environment: Environment[SI, A],
                               gamma: float
                              ) -> float:
        """Calculate the update to the Bellman Equation."""
        
        update_value: float = 0
        
        next_states: StateProbabilityDistribution[SI] = environment.get_next_states(
            state, action
        )
        
        for next_state in next_states:
            
            next_state_probability: float = environment.get_state_transition_probability(
                state,
                action,
                next_state
            )
            
            next_state_reward: float = state_space.get_reward(next_state)
            
            next_state_value: float = state_space.get_estimated_return(next_state)
            
            update_value += next_state_probability * (next_state_reward + (gamma * next_state_value))
            
        return update_value
        