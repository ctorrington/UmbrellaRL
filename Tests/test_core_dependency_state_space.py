import unittest

# from core.dependency.state_index import StateIndex

# TODO Figure this out.
# Argument of type "StateIndex" cannot be assigned to parameter "cls" of type "_ClassInfo" in function "assertIsInstance"
#   Type "TypeAliasType" is incompatible with type "_ClassInfo"
#     "TypeAliasType" is incompatible with "type"
#     "TypeAliasType" is incompatible with "UnionType"
#     "TypeAliasType" is incompatible with "tuple[_ClassInfo, ...]"PylancereportArgumentType

# class TestStateIndex(unittest.TestCase):
    
#     def test_int_valid(self):
#         """Test that an integer is a valid StateIndex."""
#         self.assertIsInstance(5, StateIndex)
        
#     def test_str_valid(self):
#         """Test that a string is a valid StateIndex."""
#         self.assertIsInstance("state", StateIndex)
        
#     def test_tuple_valid(self):
#         """Test that a tuple of integers is a valid StateIndex."""
#         self.assertIsInstance((1, 2, 3), StateIndex)
        
#     def test_empty_tuple_valid(self):
#         """Test that an empty tuple is a valid StateIndex."""
#         self.assertIsInstance((), StateIndex)
        
#     def test_single_element_tuple_valid(self):
#         """Test that a single-element tuple is a valid StateIndex."""
#         self.assertIsInstance((1,), StateIndex)
        
#     def test_invalid_type_float(self):
#         """Test that a float is not a valid StateIndex."""
#         self.assertNotIsInstance(5.5, StateIndex)
        
#     def test_invalid_type_list(self):
#         """Test that a list is not a valid StateIndex."""
#         self.assertNotIsInstance([1, 2, 3], StateIndex)
        
#     def test_invalid_type_dict(self):
#         """Test that a dictionary is not a valid StateIndex."""
#         self.assertNotIsInstance({"key": "value"}, StateIndex)
        
#     def test_invalid_type_set(self):
#         """Test that a set is not a valid StateIndex."""
#         self.assertNotIsInstance({1, 2, 3}, StateIndex)
        
#     def test_invalid_type_tuple_of_str(self):
#         """Test that a tuple of strings is not a valid StateIndex."""
#         self.assertNotIsInstance(("a", "b", "c"), StateIndex)
        
#     def test_invalid_type_mixed_tuple(self):
#         """Test that a tuple with mixed types is not a valid StateIndex."""
#         self.assertNotIsInstance((1, "a", 3), StateIndex)

if __name__ == '__main__':
    unittest.main()
