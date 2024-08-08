# TODO These tests are not being discover 🕵️ _discover_ why 💥.

import unittest

from typing import Dict

from tests.utils import timed

# Mocking the dependencies
class MockStateIndex:
    pass

class MockAction:
    pass

class MockStateProbabilityDistribution(Dict[MockStateIndex, float]):
    def __init__(self, distribution):
        super().__init__(distribution)

    def get_state_probability(self, state_index: MockStateIndex) -> float:
        return self[state_index]

# The StateActions class as described in the provided code.
class StateActions(Dict[MockAction, MockStateProbabilityDistribution]):
    def get_state_probability_distribution(self, action: MockAction) -> MockStateProbabilityDistribution:
        return self[action]

# Unit test cases for StateActions
class TestStateActions(unittest.TestCase):

    def setUp(self):
        # Create mock actions and state indices
        self.action1 = MockAction()
        self.action2 = MockAction()
        self.state1 = MockStateIndex()
        self.state2 = MockStateIndex()

        # Create mock state probability distributions
        self.spd1 = MockStateProbabilityDistribution({self.state1: 0.7, self.state2: 0.3})
        self.spd2 = MockStateProbabilityDistribution({self.state1: 1.0})

        # Initialize StateActions with these mock distributions
        self.state_actions = StateActions({self.action1: self.spd1, self.action2: self.spd2})

    @timed
    def test_get_state_probability_distribution_valid_action(self):
        """Test that the correct state probability distribution is returned for a valid action."""
        result = self.state_actions.get_state_probability_distribution(self.action1)
        self.assertEqual(result, self.spd1)

    @timed
    def test_get_state_probability_distribution_invalid_action(self):
        """Test that an error is raised when an invalid action is provided."""
        with self.assertRaises(KeyError):
            self.state_actions.get_state_probability_distribution(MockAction())

    @timed
    def test_empty_state_actions(self):
        """Test behavior when StateActions is empty."""
        empty_state_actions = StateActions()
        with self.assertRaises(KeyError):
            empty_state_actions.get_state_probability_distribution(self.action1)

    @timed
    def test_state_probability_distribution_edge_case(self):
        """Test behavior with an edge case where the state probability distribution has zero states."""
        spd_empty = MockStateProbabilityDistribution({})
        empty_action = MockAction()
        state_actions = StateActions({empty_action: spd_empty})

        result = state_actions.get_state_probability_distribution(empty_action)
        self.assertEqual(len(result), 0)

    @timed
    def test_state_probability_retrieval(self):
        """Test retrieval of state probability from the distribution."""
        spd = self.state_actions.get_state_probability_distribution(self.action1)
        self.assertAlmostEqual(spd.get_state_probability(self.state1), 0.7)
        self.assertAlmostEqual(spd.get_state_probability(self.state2), 0.3)


if __name__ == '__main__':
    unittest.main()
