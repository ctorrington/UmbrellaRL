import unittest

from core.Action import Action
from core.State import State

class TestState(unittest.TestCase):
    def test_state_attributes_initialization(self):
        class MyAction(Action):
            FIRST = 1
            SECOND = 2

        class MyState(State[MyAction]):
            pass

        my_state = MyState()

        self.assertEqual(my_state.actions, [])
        self.assertEqual(my_state.estimated_return, 0.0)
        self.assertEqual(my_state.counter, 0)
        self.assertEqual(my_state.reward, 0.0)
        self.assertFalse(my_state.is_current)
        self.assertFalse(my_state.is_terminal)

    # TODO Implement later.
    # def test_set_estimated_return(self):
    #     class MyAction(Action):
    #         FIRST = 1
    #         SECOND = 2

    #     class MyState(State[MyAction]):
    #         pass

    #     my_state = MyState()
    #     my_state.set_estimated_return(10.5)

    #     self.assertEqual(my_state.estimated_return, 10.5)

    # TODO Implement Later.
    # def test_increment_counter(self):
    #     class MyAction(Action):
    #         FIRST = 1
    #         SECOND = 2

    #     class MyState(State[MyAction]):
    #         pass

    #     my_state = MyState()
    #     my_state.increment_counter()

    #     self.assertEqual(my_state.counter, 1)

    # TODO Implement later.
    # def test_set_reward(self):
    #     class MyAction(Action):
    #         FIRST = 1
    #         SECOND = 2

    #     class MyState(State[MyAction]):
    #         pass

    #     my_state = MyState()
    #     my_state.set_reward(5.0)

    #     self.assertEqual(my_state.reward, 5.0)

    # TODO Implement later.
    # def test_set_is_current(self):
    #     class MyAction(Action):
    #         FIRST = 1
    #         SECOND = 2

    #     class MyState(State[MyAction]):
    #         pass

    #     my_state = MyState()
    #     my_state.set_is_current(True)

    #     self.assertTrue(my_state.is_current)

    # TODO Implement later.
    # def test_set_is_terminal(self):
    #     class MyAction(Action):
    #         FIRST = 1
    #         SECOND = 2

    #     class MyState(State[MyAction]):
    #         pass

    #     my_state = MyState()
    #     my_state.set_is_terminal(True)

    #     self.assertTrue(my_state.is_terminal)
