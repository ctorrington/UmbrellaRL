import unittest

from core.dependency.action import Action
from tests.utils import timed

class TestActions(Action):
    ACTION_1 = 1
    ACTION_2 = 2

class TestCoreDependencyAction(unittest.TestCase):
    
    @timed
    def test_inheritance(self):
        self.assertIsInstance(TestActions.ACTION_1, TestActions)
        self.assertIsInstance(TestActions.ACTION_2, TestActions)

    @timed
    def test_members_method(self):
        expected_members = [TestActions.ACTION_1, TestActions.ACTION_2]
        self.assertListEqual(TestActions.members(), expected_members)

    @timed
    def test_empty_actions(self):
        class EmptyActions(Action):
            pass
        
        self.assertListEqual(EmptyActions.members(), [])

if __name__ == '__main__':
    unittest.main()