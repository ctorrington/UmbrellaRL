import unittest

from core.Action import Action

class TestAction(unittest.TestCase):
    def test_members_return_type(self):
        class MyAction(Action):
            FIRST = 1
            SECOND = 2

        members = MyAction.members()
        self.assertIsInstance(members, list)

    def test_members_contains_enum_values(self):
        class MyAction(Action):
            FIRST = 1
            SECOND = 2

        members = MyAction.members()
        expected_values = [MyAction.FIRST, MyAction.SECOND]

        for value in expected_values:
            self.assertIn(value, members)

    def test_members_empty_for_empty_enum(self):
        class EmptyAction(Action):
            pass

        members = EmptyAction.members()
        self.assertEqual(members, [])
