"""Test State Space."""

from StateSpace import StateSpace
from State import State

import unittest

class TestStateSpace(unittest.TestCase):
    def test_initialization(self):
        number_of_states: int = 5
        terminal_states_rewards: dict[int, int] = {0: -1, number_of_states - 1: 1}
        
        state_space = StateSpace(number_of_states,
                                 terminal_states_rewards)
        
        # Check correct amountof states are created.
        self.assertEqual(len(state_space), number_of_states)
        
        # Check States are correct type.
        # Check state terminal properties are correct.
        for state in state_space:
            self.assertIsInstance(state_space[state], State)
            
            if state not in terminal_states_rewards:
                self.assertFalse(state_space[state].is_terminal)
                self.assertEqual(state_space[state].reward, 0)
            else:
                self.assertTrue(state_space[state].is_terminal)
                self.assertEqual(state_space[state].reward, terminal_states_rewards[state])
                
        