"""Test State Space."""

import unittest
from unittest.mock import Mock
from typing import List, Dict

from StateSpace import StateSpace
from State import State
from Action import Action
from Services.StateSpaceService import StateSpaceService

class TestStateSpace(unittest.TestCase):
    class CustomState(State):
        def __init__(self):
            super().__init__()
            self.custom_property: str = ""
        
    def setUp(self) -> None:
        self.number_of_states = 5
        self.terminal_states_rewards = {3: 10.0, 4: 5.0}
        self.state_actions: Dict[int, List[Action]] = {0: [Mock(spec=Action) for _ in range(3)], 2: [Mock(spec=Action)]}

    def test_initialize_state_space(self):
        state_space = StateSpace(self.number_of_states, self.terminal_states_rewards, self.state_actions)
        self.assertEqual(len(state_space), self.number_of_states)

    def test_set_terminal_states_rewards(self):
        state_space = StateSpace(self.number_of_states, {}, {})
        StateSpaceService.set_terminal_states_rewards(state_space, self.terminal_states_rewards)

        for state, reward in self.terminal_states_rewards.items():
            self.assertEqual(state_space[state].reward, reward)
            self.assertTrue(state_space[state].is_terminal)

    def test_set_state_actions(self):
        state_space = StateSpace(self.number_of_states, {}, {})
        StateSpaceService.set_state_actions(state_space, self.state_actions)

        for state, actions in self.state_actions.items():
            self.assertEqual(state_space[state].actions, actions)

    def test_get_attribute(self):
        state_space = StateSpace(self.number_of_states, {}, {}, self.CustomState)
        state_space[0].custom_property = "custom_value" # type: ignore

        self.assertEqual(state_space[0].custom_property, "custom_value") # type: ignore

    def test_invalid_attribute(self):
        state_space = StateSpace(self.number_of_states, {}, {}, self.CustomState)

        with self.assertRaises(AttributeError):
            _ = state_space.invalid_attribute # type: ignore
