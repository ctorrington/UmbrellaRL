"""Test State."""

from State import State

import unittest

class TestState(unittest.TestCase):
    def test_initialization(self):
        state = State()
        
        self.assertIsInstance(state, State)
        self.assertEqual(len(state.actions), 0)
        self.assertEqual(state.estimated_return, 0)
        self.assertEqual(state.counter, 0)
        self.assertEqual(state.reward, 0)
        self.assertFalse(state.is_current)
        self.assertFalse(state.is_terminal)
        