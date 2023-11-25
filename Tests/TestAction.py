"""Test Action generic type."""

from Action import Action

import unittest

class TestAction(unittest.TestCase):
    def test_empty_members_enum(self):
        class EmptyActionEnum(Action):
            pass
        
        self.assertEqual(EmptyActionEnum.members(), [])
        
    def test_non_empty_members_enum(self):
        class NonEmptyActionEnum(Action):
            ACTION1 = "action1"
            ACTION2 = "action2"
            
        self.assertEqual(NonEmptyActionEnum.members(),
                         [NonEmptyActionEnum.ACTION1, NonEmptyActionEnum.ACTION2])