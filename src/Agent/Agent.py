"""RL Agent."""

from typing import Dict, List

# Dependencies.
from src.ActionProbabilityDistribution import ActionProbabilityDistribution
from src.StateProbabilityDistribution import StateProbabilityDistribution
from src.StateSpace import StateSpace
from src.Environment.Environment import Environment
from src.Policy.BasePolicy import BasePolicy
from src.StateIndex import StateIndex
from src.Action import Action
from src.Agent.AgentService import AgentService

# TODO Desperately need a service class.
# TODO Look into publishing to twine on release.
# TODO Need option to improve Policy without changing the current State Space. (in place)
    # Need copy of old State Value function, improve according to those values - set State Value Function to those updated values all at once (optional, include with current implementation)

class Agent[SI: StateIndex, A: Action]:
    """RL Agent."""
    
    def __init__(self,
                 environment: Environment[SI, A],
                 policy: BasePolicy[SI, A],
                ):
        
        # Value function parameters.
        self.theta: float = 0.01
        
        self.gamma: float = 0.9
        
        # Dependencies. 
        self.environment: Environment[SI, A] = environment
        
        self.policy: BasePolicy[SI, A] = policy
    
    def evaluate_policy(self) -> None:
        """
        Evaluate the policy.
        
        Determine the state-value function for the policy.
        """
        
        state_space: StateSpace[SI, A] = self.environment.get_state_space()
        
        while True:
            
            delta = 0
            
            for state in state_space:
                
                if state_space[state].is_terminal:
                    continue
                
                old_state_value: float = state_space[state].estimated_return
                
                updated_state_value: float = self.calculate_state_value(state)
                
                self.assign_new_state_estimated_return(state, updated_state_value)
                
                delta = max(delta, (abs(old_state_value - updated_state_value)))
                
            if delta < self.theta:
                break
            
    def improve_policy(self) -> None:
        """
        Improve the Policy.
        
        Determine optimal actions for each State in the State Space.
        """
        
        state_space: StateSpace[SI, A] = self.environment.get_state_space()
        
        policy_stable: bool = True
        
        while True:
        
            for state in state_space:
                
                # TODO create has_actions method
                if len(state_space[state].actions) == 0:
                    continue
                
                old_state_policy: ActionProbabilityDistribution[A] = self.policy.get_action_probability_distribution(state)
                
                new_greedy_actions: List[A] = AgentService.determine_greedy_actions(
                    state,
                    state_space,
                    self.environment,
                    self.gamma
                )
                
                self.policy.set_new_state_policy(
                    state,
                    new_greedy_actions
                )
                
                new_state_policy: ActionProbabilityDistribution[A] = self.policy.get_action_probability_distribution(state)
                    
                if old_state_policy != new_state_policy:
                    policy_stable = False
                    
            if policy_stable:
                break

    def calculate_state_value(self,
                              state: SI
                             ) -> float:
        """
        Calcualte the value of the given state following the given policy
        in the given environment.
        """
        
        state_space: StateSpace[SI, A] = self.environment.get_state_space()
        
        new_state_value: float = 0
        
        state_action_probability_distribution: ActionProbabilityDistribution[A] = self.policy.get_action_probability_distribution(state)
        
        for action in state_action_probability_distribution:
            
            action_probability: float = state_action_probability_distribution[action]
            
            # TODO I dont understand why the line below does not work.
            # action_probability: float = state_action_probability_distribution.get_action_probability(action)
            
            next_states: StateProbabilityDistribution[SI] = self.environment.get_next_states(
                state,
                action
            )

            for next_state in next_states:
                
                next_state_probability = self.environment.get_state_transition_probability(
                    state,
                    action,
                    next_state
                )
                
                next_state_reward: float = state_space.get_reward(next_state)
                
                next_state_value: float = state_space.get_estimated_return(next_state)
                
                new_state_value += AgentService.calculate_bellman_optimality_value(
                    action_probability,
                    next_state_probability,
                    next_state_reward,
                    self.gamma,
                    next_state_value
                )
                
        return new_state_value
    
    def assign_new_state_estimated_return(self,
                               state: SI,
                               value: float
                              ) -> None:
        """Assign the new estimated return (value) to the given State."""
        
        state_space: StateSpace[SI, A] = self.environment.get_state_space()
        
        state_space[state].estimated_return = value
