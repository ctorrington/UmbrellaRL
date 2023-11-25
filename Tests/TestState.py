"""Test State."""

import unittest
from unittest.mock import Mock
from typing import List

from State import State
from Action import Action

class TestState(unittest.TestCase):
    def test_default_values(self):
        state = State()

        self.assertEqual(state.actions, [])
        self.assertEqual(state.estimated_return, 0.0)
        self.assertEqual(state.counter, 0)
        self.assertEqual(state.reward, 0)
        self.assertFalse(state.is_current)
        self.assertFalse(state.is_terminal)

    def test_custom_values(self):
        actions: List[Action] = [Mock(spec=Action) for _ in range(3)]
        state = State()
        state.actions = actions
        state.estimated_return = 10.5
        state.counter = 42
        state.reward = 100
        state.is_current = True
        state.is_terminal = True

        self.assertEqual(state.actions, actions)
        self.assertEqual(state.estimated_return, 10.5)
        self.assertEqual(state.counter, 42)
        self.assertEqual(state.reward, 100)
        self.assertTrue(state.is_current)
        self.assertTrue(state.is_terminal)

    def test_inheritance(self):
        class CustomState(State):
            def __init__(self, custom_field: str):
                super().__init__()
                self.custom_field = custom_field

        custom_state = CustomState(custom_field="custom_value")

        self.assertEqual(custom_state.actions, [])
        self.assertEqual(custom_state.estimated_return, 0.0)
        self.assertEqual(custom_state.counter, 0)
        self.assertEqual(custom_state.reward, 0)
        self.assertFalse(custom_state.is_current)
        self.assertFalse(custom_state.is_terminal)
        self.assertEqual(custom_state.custom_field, "custom_value")
