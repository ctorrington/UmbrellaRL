"""Agent Service class"""

from typing import List, Dict

from src.StateIndex import StateIndex
from src.Action import Action
from src.StateSpace import StateSpace
from src.StateProbabilityDistribution import StateProbabilityDistribution
from src.Environment.Environment import Environment
from src.Policy.BasePolicy import BasePolicy
from src.ActionProbabilityDistribution import ActionProbabilityDistribution

# TODO Service class could probably do with a Bellman Service class of its own.

class AgentService[SI: StateIndex, A: Action]():
    """Class to handle calculations for the Agent."""
    
    @classmethod
    def calculate_bellman_equation(cls,
                                   state: SI,
                                   state_space: StateSpace[SI, A],
                                   policy: BasePolicy[SI, A],
                                   environment: Environment[SI, A],
                                   gamma: float
                                  ) -> float:
        
        bellman_equation_value = cls.calculate_bellman_equation_value(
            state,
            state_space,
            policy,
            environment,
            gamma)
        
        return bellman_equation_value
    
    @classmethod
    def determine_greedy_actions(cls,
                                 state: SI,
                                 state_space: StateSpace[SI, A],
                                 environment: Environment[SI, A],
                                 gamma: float
                                ) -> List[A]:
        """
        Determine the Actions resulting in the greatest estimated return 
        from the given State.
        """
        
        action_value_distribution: Dict[A, float] = cls.calculate_greedy_actions_estimated_return(
            state,
            state_space,
            environment,
            gamma
            )
        
        best_actions: List[A] = cls.determine_best_actions(
            action_value_distribution
        )
        
        return best_actions

    @classmethod
    def calculate_greedy_actions_estimated_return(cls,
                                                  state: SI,
                                                  state_space: StateSpace[SI, A],
                                                  environment: Environment[SI, A],
                                                  gamma: float
                                                 ) -> Dict[A, float]:
        """
        Calculate the Actions resulting in the highest estimated return from 
        the given State.
        """
        
        action_value_distribution: Dict[A, float] = {}
        
        for action in state_space[state].actions:
            
            action_value: float = cls.calculate_bellman_update(
                state,
                action,
                state_space,
                environment,
                gamma
            )
                
            action_value_distribution[action] = action_value
            
        return action_value_distribution

    @classmethod
    def determine_best_actions(cls,
                               action_value_distribution: Dict[A, float]
                              ) -> List[A]:
        """Return the Actions that result in the greatest esimated return."""
        
        best_value: float = 0
        
        best_actions: List[A] = []
        
        for action in action_value_distribution:
            
            if action_value_distribution[action] > best_value:
                
                best_value = action_value_distribution[action]
                
                best_actions.append(action)
                
        return best_actions
    
    @classmethod
    def calculate_bellman_equation_value(cls,
                                         state: SI,
                                         state_space: StateSpace[SI, A],
                                         policy: BasePolicy[SI, A],
                                         environment: Environment[SI, A],
                                         gamma: float
                                         ) -> float:
        
        state_action_probability_distribution: ActionProbabilityDistribution[A] = policy.get_action_probability_distribution(state)
        
        bellman_equation_value: float = 0
        
        for action in state_space[state].actions:
            
            # TODO get method for below.
            action_probability: float = state_action_probability_distribution[action]
            
            bellman_update_value: float = cls.calculate_bellman_update(
                state,
                action,
                state_space,
                environment,
                gamma
                )
            
            bellman_equation_value += action_probability * bellman_update_value
            
        return bellman_equation_value
    
    @classmethod
    def calculate_bellman_update(cls,
                                 state: SI,
                                 action: A,
                                 state_space: StateSpace[SI, A],
                                 environment: Environment[SI, A],
                                 gamma: float
                                ) -> float:
        """Calculate the bellman update."""
        
        action_value: float = 0
        
        next_states: StateProbabilityDistribution[SI] = environment.get_next_states(
            state,
            action
        )
        
        for next_state in next_states:
            
            next_state_probability: float = environment.get_state_transition_probability(
                state,
                action,
                next_state
            )
            
            next_state_reward: float = state_space.get_reward(next_state)
            
            next_state_value: float = state_space.get_estimated_return(next_state)
            
            action_value += next_state_probability * (next_state_reward + (gamma * next_state_value))
            
        return action_value
