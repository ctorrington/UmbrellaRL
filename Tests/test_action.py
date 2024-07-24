import unittest

from core.dependency.action import Action

class TestAction(unittest.TestCase):
    def test_inheritance(self):
        class TestActions(Action):
            ACTION_1 = 1
            ACTION_2 = 2
        
        self.assertIsInstance(TestActions.ACTION_1, TestActions)
        self.assertIsInstance(TestActions.ACTION_2, TestActions)

    def test_members_method(self):
        class TestActions(Action):
            ACTION_1 = 1
            ACTION_2 = 2
        
        expected_members = [TestActions.ACTION_1, TestActions.ACTION_2]
        self.assertListEqual(TestActions.members(), expected_members)
    
    def test_empty_actions(self):
        class EmptyActions(Action):
            pass
        
        self.assertListEqual(EmptyActions.members(), [])

if __name__ == '__main__':
    unittest.main()