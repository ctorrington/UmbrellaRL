import unittest

from core.dependency.action import Action
from core.dependency.action_probability_distribution import ActionProbabilityDistribution

class TestActions(Action):
    ACTION_1 = 1
    ACTION_2 = 2

class TestActionProbabilityDistribution(unittest.TestCase):
    def setUp(self):
        self.prob_distribution = ActionProbabilityDistribution({
            TestActions.ACTION_1: 0.7,
            TestActions.ACTION_2: 0.3,
        })

    def test_initial_probabilities(self):
        self.assertEqual(self.prob_distribution.get_action_probability(TestActions.ACTION_1), 0.7)
        self.assertEqual(self.prob_distribution.get_action_probability(TestActions.ACTION_2), 0.3)

    def test_set_action_probability(self):
        self.prob_distribution.set_action_probability(TestActions.ACTION_1, 0.6)
        self.assertEqual(self.prob_distribution.get_action_probability(TestActions.ACTION_1), 0.6)
        
        self.prob_distribution.set_action_probability(TestActions.ACTION_2, 0.4)
        self.assertEqual(self.prob_distribution.get_action_probability(TestActions.ACTION_2), 0.4)

    def test_update_probabilities(self):
        self.prob_distribution[TestActions.ACTION_1] = 0.8
        self.assertEqual(self.prob_distribution.get_action_probability(TestActions.ACTION_1), 0.8)

        self.prob_distribution[TestActions.ACTION_2] = 0.2
        self.assertEqual(self.prob_distribution.get_action_probability(TestActions.ACTION_2), 0.2)

    def test_non_existent_action(self):
        with self.assertRaises(ValueError):
            self.prob_distribution.get_action_probability(TestActions(99))

if __name__ == '__main__':
    unittest.main()
