"""
State Index type.

Generic type for index States.

Currently allowed types:
    - int
    - str
    - Tuple
"""

from typing import Tuple, Any

# TODO probably want to use something like this: https://docs.python.org/3/library/typing.html#user-defined-generic-types:~:text=type%20Response%5BS%5D%20%3D%20Iterable%5BS%5D%20%7C%20int

class StateIndex[T: int | str | Tuple[Any, ...]]:
    pass