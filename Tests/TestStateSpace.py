# # """Test State Space."""

# # FIXME this class needs an entire overhaul.
# import unittest
# from typing import Type, Tuple
# from src.StateSpace import StateSpace
# from src.State import State
# from src.StateIndex import StateIndex
# from src.Action import Action

# class TestStateSpace(unittest.TestCase):
    
#     def test_get_state_attributes(self):
        
#         class MyAction(Action):
            
#             FIRST = 1
            
#             SECOND = 2

#         class MyState(State[MyAction]):
            
#             pass
        
#         type MyStateIndexType = int

#         class MyStateSpace(StateSpace[MyStateIndexType, MyAction]):
            
#             pass

#         my_state_space = MyStateSpace()
        
#         state_index = 1

#         my_state_space[state_index] = MyState()

#         my_state_space[state_index].set_reward(5.0)

#         my_state_space[state_index].set_estimated_return(10.5)

#         self.assertEqual(my_state_space.get_reward(state_index), 5.0)

#         self.assertEqual(my_state_space.get_estimated_return(state_index), 10.5)

#     def test_get_nonexistent_state_attributes(self):
#         class MyAction(Action):
#             FIRST = 1
#             SECOND = 2

#         class MyState(State[MyAction]):
#             pass

#         class MyStateSpace(StateSpace[MyState, MyAction]):
#             pass

#         my_state_space = MyStateSpace()
#         state_index = 1

#         with self.assertRaises(KeyError):
#             my_state_space.get_reward(state_index)

#         with self.assertRaises(KeyError):
#             my_state_space.get_estimated_return(state_index)

#     def test_get_dimensions_abstract_method(self):
#         class MyAction(Action):
#             FIRST = 1
#             SECOND = 2

#         class MyState(State[MyAction]):
#             pass

#         class MyStateSpace(StateSpace[MyState, MyAction]):
#             pass

#         my_state_space = MyStateSpace()

#         with self.assertRaises(TypeError):
#             my_state_space.get_dimensions()

#     def test_get_state_by_index(self):
#         class MyAction(Action):
#             FIRST = 1
#             SECOND = 2

#         class MyState(State[MyAction]):
#             pass

#         class MyStateSpace(StateSpace[MyState, MyAction]):
#             pass

#         my_state_space = MyStateSpace()
#         state_index = 1

#         my_state_space[state_index] = MyState()

#         retrieved_state = my_state_space[state_index]
#         self.assertIsInstance(retrieved_state, MyState)

#     def test_get_nonexistent_state_by_index(self):
#         class MyAction(Action):
#             FIRST = 1
#             SECOND = 2

#         class MyState(State[MyAction]):
#             pass

#         class MyStateSpace(StateSpace[MyState, MyAction]):
#             pass

#         my_state_space = MyStateSpace()
#         state_index = 1

#         with self.assertRaises(KeyError):
#             retrieved_state = my_state_space[state_index]

#     def test_get_attribute_by_index(self):
#         class MyAction(Action):
#             FIRST = 1
#             SECOND = 2

#         class MyState(State[MyAction]):
#             pass

#         class MyStateSpace(StateSpace[MyState, MyAction]):
#             pass

#         my_state_space = MyStateSpace()
#         state_index = 1

#         my_state_space[state_index] = MyState()
#         my_state_space[state_index].set_reward(5.0)

#         retrieved_reward = my_state_space.get_reward(state_index)
#         self.assertEqual(retrieved_reward, 5.0)

#     def test_get_nonexistent_attribute_by_index(self):
#         class MyAction(Action):
#             FIRST = 1
#             SECOND = 2

#         class MyState(State[MyAction]):
#             pass

#         class MyStateSpace(StateSpace[MyState, MyAction]):
#             pass

#         my_state_space = MyStateSpace()
#         state_index = 1

#         with self.assertRaises(KeyError):
#             retrieved_reward = my_state_space.get_reward(state_index)

#     def test_get_dimensions_abstract_method(self):
#         class MyAction(Action):
#             FIRST = 1
#             SECOND = 2

#         class MyState(State[MyAction]):
#             pass

#         class MyStateSpace(StateSpace[MyState, MyAction]):
#             pass

#         my_state_space = MyStateSpace()

#         with self.assertRaises(TypeError):
#             my_state_space.get_dimensions()
