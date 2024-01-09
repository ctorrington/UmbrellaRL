"""Test State Index Type Class."""

import unittest

from core.StateIndex import StateIndex

# TODO Find a better way to do this.
# TODO Currently do not know how to test Tuples.
def assert_index_type(value: StateIndex):
    
    assert isinstance(value, (int, str))

class TestStateIndex(unittest.TestCase):
    
    def test_int_type(self):
        
        state_index: StateIndex = 42
        
        assert_index_type(state_index)

    def test_str_type(self):
        
        state_index: StateIndex = "some_state"
        
        assert_index_type(state_index)

    # def test_tuple_type(self):
    #     state_index: StateIndex = (1, 2, 3)
    #     assert_index_type(state_index)

    def test_invalid_type(self):
        
        with self.assertRaises(AssertionError):
            
            state_index: grid_world_index = 3.14    # type: ignore
            
            assert_index_type(state_index)  # type: ignore
