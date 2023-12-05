"""
State Index type.

Generic type for index States.

Currently allowed types:
    - int
    - str
    - Tuple
"""

from typing import Tuple, Any

class StateIndex[T: int | str | Tuple[*Any]]:
    pass