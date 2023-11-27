"""
State index generic type.

Type used to represent the index type of the States in the State Space.
This allows for State Spaces that fit different problems.
For example, vectors for 2D & 3D State Spaces, integers for 'regular' State
Spaces, or strings for labelled State Space.
"""
# TODO Wondering if this class is even necessary.
    # Why not just a generic in State Space.
class StateIndex[T]():
    def __init__(self, value: T):
       self.value = value
       
    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        else:
            return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.value) 
