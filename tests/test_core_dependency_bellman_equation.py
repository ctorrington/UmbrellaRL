
import unittest
from unittest.mock import MagicMock, create_autospec

from core.dependency.bellman_equation import BellmanEquation
from core.dependency.state_index import StateIndex
from core.dependency.action import Action
from core.Environment.Environment import Environment
from core.Policy.BasePolicy import BasePolicy
from core.dependency.state_space import StateSpace
from core.dependency.state import State
from core.dependency.action_probability_distribution import ActionProbabilityDistribution
from core.dependency.state_probability_distribution import StateProbabilityDistribution

from tests.utils import timed

class TestBellmanEquation(unittest.TestCase):
    @timed
    def setUp(self):
        # Create mock objects
        self.mock_state_index = create_autospec(StateIndex)
        self.mock_action = create_autospec(Action)
        self.mock_environment = create_autospec(Environment)
        self.mock_policy = create_autospec(BasePolicy)
        self.mock_state_space = create_autospec(StateSpace)
        self.mock_state = create_autospec(State)
        self.mock_action_prob_dist = create_autospec(ActionProbabilityDistribution)
        self.mock_state_prob_dist = create_autospec(StateProbabilityDistribution)

        # Setup environment mock
        self.mock_environment.get_state_space.return_value = self.mock_state_space
        
        # Setup policy mock
        self.mock_policy.get_action_probability_distribution.return_value = self.mock_action_prob_dist

        # Setup state space mock
        self.mock_state_space.get_state.return_value = self.mock_state

        # Setup state mock
        self.mock_state.actions = [self.mock_action]
        self.mock_state.reward = 1.0
        self.mock_state.estimated_return = 10.0

        # Setup action probability distribution mock
        self.mock_action_prob_dist.__getitem__.return_value = 1.0

        # Setup state probability distribution mock
        self.mock_environment.get_next_states.return_value = self.mock_state_prob_dist
        self.mock_state_prob_dist.__iter__.return_value = iter([self.mock_state_index])
        self.mock_environment.get_state_transition_probability.return_value = 1.0

    @timed
    def test_calculate_state_value(self):
        # Test normal case
        gamma = 0.9
        value = BellmanEquation.calculate_state_value(
            self.mock_state_index,
            self.mock_policy,
            self.mock_environment,
            gamma
        )
        self.assertAlmostEqual(value, 10)

        # Test edge case: empty state actions
        self.mock_state.actions = []
        value = BellmanEquation.calculate_state_value(
            self.mock_state_index,
            self.mock_policy,
            self.mock_environment,
            gamma
        )
        self.assertEqual(value, 0)

    @timed
    def test_calculate_update_value(self):
        # Test normal case
        gamma = 0.9
        value = BellmanEquation.calculate_update_value(
            self.mock_state_index,
            self.mock_action,
            self.mock_environment,
            gamma
        )
        self.assertAlmostEqual(value, 10)

        # Test edge case: empty next states
        self.mock_state_prob_dist.__iter__.return_value = iter([])
        value = BellmanEquation.calculate_update_value(
            self.mock_state_index,
            self.mock_action,
            self.mock_environment,
            gamma
        )
        self.assertEqual(value, 0)

    @timed
    def test_calculate_action_value_for_state(self):
        # Test normal case
        gamma = 0.9
        value = BellmanEquation.calculate_action_value_for_state(
            self.mock_state_index,
            self.mock_action,
            self.mock_environment,
            gamma
        )
        self.assertAlmostEqual(value, 10)

if __name__ == '__main__':
    unittest.main()
