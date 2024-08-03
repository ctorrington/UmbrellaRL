import unittest

from unittest.mock import MagicMock

from core.dependency.state import State
from core.dependency.action import Action

from log.ilogger import ILogger
from tests.utils import timed

class TestState(unittest.TestCase):

    @timed
    def setUp(self):
        # Create mock actions
        self.action1 = MagicMock(spec=Action)
        self.action2 = MagicMock(spec=Action)
        
        # Create mock logger
        self.logger = MagicMock(spec=ILogger)
        self.mock_logger_instance = MagicMock()
        self.logger.get_logger.return_value = self.mock_logger_instance

    @timed
    def test_initialization(self):
        state = State(action_list=[self.action1, self.action2], estimated_return=5.0, reward=1.0, is_terminal=False, logger=self.logger)
        self.assertEqual(state.actions, [self.action1, self.action2])
        self.assertEqual(state.estimated_return, 5.0)
        self.assertEqual(state.reward, 1.0)
        self.assertFalse(state.is_terminal)
        self.assertFalse(state.is_current)
        self.assertEqual(state.counter, 0)
        self.mock_logger_instance.info.assert_called_once()

    @timed
    def test_initialization_empty_action_list(self):
        state = State(action_list=[], estimated_return=0.0, reward=0.0, is_terminal=False, logger=self.logger)
        self.assertEqual(state.actions, [])
        self.assertEqual(state.estimated_return, 0.0)
        self.assertEqual(state.reward, 0.0)
        self.assertFalse(state.is_terminal)
        self.assertFalse(state.is_current)
        self.assertEqual(state.counter, 0)

    @timed
    def test_initialization_terminal_state(self):
        state = State(action_list=[self.action1], estimated_return=10.0, reward=2.0, is_terminal=True, logger=self.logger)
        self.assertTrue(state.is_terminal)

    @timed
    def test_has_actions(self):
        state_with_actions = State(action_list=[self.action1], estimated_return=1.0, reward=0.5, is_terminal=False, logger=self.logger)
        self.assertTrue(state_with_actions.has_actions())

        state_without_actions = State(action_list=[], estimated_return=1.0, reward=0.5, is_terminal=False, logger=self.logger)
        self.assertFalse(state_without_actions.has_actions())

    @timed
    def test_increment_counter(self):
        state = State(action_list=[self.action1], estimated_return=1.0, reward=0.5, is_terminal=False, logger=self.logger)
        self.assertEqual(state.counter, 0)
        state.increment_counter()
        self.assertEqual(state.counter, 1)
        self.mock_logger_instance.info.assert_called_with(f"Incrementing State.counter from 0 to 1.")

    @timed
    def test_invalid_initialization(self):
        with self.assertRaises(TypeError):
            State(action_list=None, estimated_return=1.0, reward=0.5, is_terminal=False, logger=self.logger)

        with self.assertRaises(TypeError):
            State(action_list=[self.action1], estimated_return=None, reward=0.5, is_terminal=False, logger=self.logger)

        with self.assertRaises(TypeError):
            State(action_list=[self.action1], estimated_return=1.0, reward=None, is_terminal=False, logger=self.logger)

        with self.assertRaises(TypeError):
            State(action_list=[self.action1], estimated_return=1.0, reward=0.5, is_terminal=None, logger=self.logger)

if __name__ == '__main__':
    unittest.main()
