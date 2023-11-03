"""
CURRENT THINKING

The environemnt is dependent on the state space.
then the state space should be injected into the environment.
"""

from State import State
# from Services.StateSpaceService import StateSpaceService

class StateSpace(dict[int, State]):
    """Environmnet State Space dependency."""
    
    def __init__(self, number_of_states: int,
                 terminal_states_rewards: dict[int, int],
                #  state_space_service: StateSpaceService
                ) -> None:
        for state in range(number_of_states):
            self[state] = State()
            
        # Terminal states.
        for state in terminal_states_rewards:
            self[state].is_terminal = True
            
        # Terminal state rewards.
        # state_space_service.set_rewards(self, terminal_states_rewards)
        self.set_rewards(terminal_states_rewards)
        
    def __getattr__(self, key: int):
        if key in self:
            return self[key]
        else:
            raise AttributeError(f"'StateSpace' object has not attribute '{key}'")
 
    # def __setattr__(self, key: str, value: State):
    #     self[key] = value
    
    # TODO StateSpaceService.
    def set_rewards(self, rewards: dict[int, int]) -> None:
        """Set the rewards fro the State Space."""
        
        for state in rewards:
            self[state].reward = rewards[state]
            
    # TODO StateSpaceService.
    def set_next_states(self)
