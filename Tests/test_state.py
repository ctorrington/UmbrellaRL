import unittest

from core.dependency.action import Action
from core.dependency.state import State

# Define a dummy Action class for testing
class TestAction(Action):
    ACTION_1 = 1
    ACTION_2 = 2

class TestState(unittest.TestCase):

    def setUp(self):
        self.actions = [TestAction.ACTION_1, TestAction.ACTION_2]
        self.estimated_return = 10.0
        self.reward = 5.0
        self.state = State(self.actions, self.estimated_return, self.reward)

    def test_initialization(self):
        self.assertEqual(self.state.actions, self.actions)
        self.assertEqual(self.state.estimated_return, self.estimated_return)
        self.assertEqual(self.state.reward, self.reward)
        self.assertFalse(self.state.is_current)
        self.assertFalse(self.state.is_terminal)
        self.assertEqual(self.state.counter, 0)

    def test_actions_property(self):
        new_actions = [TestAction.ACTION_2]
        self.state.actions = new_actions
        self.assertEqual(self.state.actions, new_actions)

    def test_estimated_return_property(self):
        new_estimated_return = 15.0
        self.state.estimated_return = new_estimated_return
        self.assertEqual(self.state.estimated_return, new_estimated_return)

    def test_reward_property(self):
        new_reward = 7.0
        self.state.reward = new_reward
        self.assertEqual(self.state.reward, new_reward)

    def test_is_current_property(self):
        self.state.is_current = True
        self.assertTrue(self.state.is_current)

    def test_is_terminal_property(self):
        self.state.is_terminal = True
        self.assertTrue(self.state.is_terminal)

    def test_counter_property(self):
        self.state.increment_counter()
        self.assertEqual(self.state.counter, 1)

    def test_has_actions(self):
        self.assertTrue(self.state.has_actions())
        self.state.actions = []
        self.assertFalse(self.state.has_actions())

if __name__ == '__main__':
    unittest.main()
