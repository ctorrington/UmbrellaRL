import unittest

from Solutions.GridWorld.Action import GridWorldAction

# TODO Redo

class TestGridWorldAction(unittest.TestCase):
    def test_attributes(self):
        """Test that GridWorldAction has the correct attributes."""
        self.assertEqual(GridWorldAction.UP.value, "up")
        self.assertEqual(GridWorldAction.DOWN.value, "down")
        self.assertEqual(GridWorldAction.LEFT.value, "left")
        self.assertEqual(GridWorldAction.RIGHT.value, "right")

    def test_members(self):
        """Test that the members method returns all actions."""
        expected_members = ["up", "down", "left", "right"]
        actual_members = [member.value for member in GridWorldAction.members()]
        self.assertListEqual(sorted(expected_members), sorted(actual_members))

if __name__ == "__main__":
    unittest.main()
