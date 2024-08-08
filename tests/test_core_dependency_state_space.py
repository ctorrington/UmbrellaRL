import unittest
from unittest.mock import MagicMock, patch
import numpy as np
from core.dependency.state_space import StateSpace
from core.dependency.state import State
from core.dependency.state_index import StateIndex
from core.dependency.action import Action
from tests.utils import timed

class DummyAction(Action):
    ACTION_1 = 1
    ACTION_2 = 2

class DummyState(State[DummyAction]):
    pass

class TestStateSpace(unittest.TestCase):

    @patch('core.dependency.state_space.ILogger')
    def setUp(self, MockLogger):
        self.mock_logger = MockLogger()
        self.state_space = StateSpace(self.mock_logger)

    @timed
    def test_initialization(self):
        self.mock_logger.get_logger.assert_called_with('StateSpace')
        self.mock_logger.get_logger().info.assert_called_with('Initialised StateSpace.')

    @timed
    def test_get_state(self):
        state_index = (0, 0)
        state = DummyState(
            action_list=[DummyAction.ACTION_1, DummyAction.ACTION_2],
            estimated_return=1.0,
            reward=0.0,
            is_terminal=False,
            logger=self.mock_logger
        )
        self.state_space[state_index] = state
        self.assertEqual(self.state_space.get_state(state_index), state)

    def test_set_state_for_state_index(self):
        state_index = (0, 0)
        state = DummyState(
            action_list=[DummyAction.ACTION_1, DummyAction.ACTION_2],
            estimated_return=1.0,
            reward=0.0,
            is_terminal=False,
            logger=self.mock_logger
        )
        self.state_space.set_state_for_state_index(state_index, state)
        self.assertEqual(self.state_space[state_index], state)

    def test_get_dimensionality(self):
        state_index = (0, 0)
        state = DummyState(
            action_list=[DummyAction.ACTION_1, DummyAction.ACTION_2],
            estimated_return=1.0,
            reward=0.0,
            is_terminal=False,
            logger=self.mock_logger
        )
        self.state_space[state_index] = state
        self.assertEqual(self.state_space.get_dimensionality(), 2)

    # TODO Understand why this doesn't work.
    # def test_get_dimensionality_unsupported_type(self):
    #     with self.assertRaises(TypeError):
    #         self.state_space.get_dimensionality()

    def test_get_state_value_function(self):
        state_index_1 = (0, 0)
        state_index_2 = (1, 1)
        state_1 = DummyState(
            action_list=[DummyAction.ACTION_1, DummyAction.ACTION_2],
            estimated_return=1.0,
            reward=0.0,
            is_terminal=False,
            logger=self.mock_logger
        )
        state_2 = DummyState(
            action_list=[DummyAction.ACTION_1, DummyAction.ACTION_2],
            estimated_return=2.0,
            reward=0.0,
            is_terminal=False,
            logger=self.mock_logger
        )
        self.state_space[state_index_1] = state_1
        self.state_space[state_index_2] = state_2
        expected_values = np.zeros((2, 2))
        expected_values[0, 0] = 1.0
        expected_values[1, 1] = 2.0
        np.testing.assert_array_equal(self.state_space.get_state_value_function(), expected_values)

    def test_get_state_value_function_unsupported_dimensionality(self):
        state_index = (0, 0, 0)
        state = DummyState(
            action_list=[DummyAction.ACTION_1, DummyAction.ACTION_2],
            estimated_return=1.0,
            reward=0.0,
            is_terminal=False,
            logger=self.mock_logger
        )
        self.state_space[state_index] = state
        with self.assertRaises(ValueError):
            self.state_space.get_state_value_function()

if __name__ == '__main__':
    unittest.main()
